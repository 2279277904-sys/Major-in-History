#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFilter
from torchvision import transforms
from transformers import AutoModelForImageSegmentation


MODEL_REPOS = {
    "rmbg2": "briaai/RMBG-2.0",
    "birefnet": "ZhengPeng7/BiRefNet",
}

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}


def log(message: str) -> None:
    print(f"[图片素材] {message}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="批量背景移除，导出透明 PNG 和预览图。")
    parser.add_argument("--input", required=True, help="输入图片目录或单张图片路径。")
    parser.add_argument("--output", required=True, help="输出目录。")
    parser.add_argument("--model", choices=sorted(MODEL_REPOS), default="rmbg2", help="抠图模型。默认 rmbg2。")
    parser.add_argument("--device", choices=["auto", "cpu", "mps", "cuda"], default="auto", help="推理设备。默认自动选择。")
    parser.add_argument("--image-size", type=int, default=1024, help="模型推理边长。默认 1024。")
    parser.add_argument("--limit", type=int, default=0, help="只处理前 N 张，用于冒烟测试。0 表示全量。")
    parser.add_argument("--local-files-only", action="store_true", help="只使用本机已缓存模型，不访问网络。")
    parser.add_argument("--no-decontaminate", action="store_true", help="不根据背景色反推主体边缘颜色。")
    parser.add_argument("--no-alpha", action="store_true", help="不保存 *_alpha.png。")
    parser.add_argument(
        "--background-mode",
        choices=["auto", "white", "off"],
        default="auto",
        help="背景色处理方式。auto 自动识别均匀纯色背景，white 强制白底，off 关闭背景色后处理。",
    )
    parser.add_argument(
        "--background-color",
        help="显式背景色，支持 #RGB 或 #RRGGBB；设置后优先于 --background-mode。",
    )
    parser.add_argument(
        "--shadow-mode",
        choices=["auto", "on", "off"],
        default="auto",
        help="保留均匀纯色背景上的半透明投影。默认 auto，仅识别到背景色时启用。",
    )
    parser.add_argument(
        "--name-style",
        choices=["descriptive", "legacy"],
        default="descriptive",
        help="输出命名方式。默认 descriptive，会把模型写入文件名。",
    )
    return parser.parse_args()


def choose_device(requested: str) -> str:
    if requested != "auto":
        return requested
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def collect_images(input_path: Path, limit: int) -> list[Path]:
    if input_path.is_file():
        files = [input_path]
    else:
        files = sorted(p for p in input_path.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)
    if limit > 0:
        files = files[:limit]
    return files


def load_model(model_key: str, device: str, local_files_only: bool):
    repo = MODEL_REPOS[model_key]
    token = None
    if model_key == "rmbg2":
        # RMBG-2.0 是 gated 模型；优先用 HF_TOKEN，其次用 huggingface-cli login 的本地 token。
        token = os.environ.get("HF_TOKEN") or True
    log(f"加载模型: {repo}")
    try:
        model = AutoModelForImageSegmentation.from_pretrained(
            repo,
            trust_remote_code=True,
            token=token,
            local_files_only=local_files_only,
        )
    except Exception as exc:
        if model_key == "rmbg2":
            raise RuntimeError(
                "RMBG-2.0 加载失败。请确认已经在 Hugging Face 模型页申请并获批访问，"
                "然后设置 HF_TOKEN 或先运行 huggingface-cli login。"
            ) from exc
        raise
    # Apple MPS 上部分权重会以 half 加载，统一转 float32 避免输入/偏置 dtype 不一致。
    return model.float().eval().to(device)


def build_transform(image_size: int):
    return transforms.Compose(
        [
            transforms.Resize((image_size, image_size)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )


def infer_mask(model, transform_image, image: Image.Image, device: str) -> Image.Image:
    tensor = transform_image(image).unsqueeze(0).float().to(device)
    with torch.no_grad():
        output = model(tensor)
        pred = output[-1] if isinstance(output, (list, tuple)) else output
        if isinstance(pred, (list, tuple)):
            pred = pred[-1]
        pred = pred.sigmoid().cpu()[0].squeeze()
    return transforms.ToPILImage()(pred).resize(image.size, Image.Resampling.LANCZOS).convert("L")


def parse_background_color(value: str | None) -> tuple[int, int, int] | None:
    if value is None:
        return None
    match = re.fullmatch(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value.strip())
    if not match:
        raise ValueError("--background-color 必须是 #RGB 或 #RRGGBB 格式。")
    hex_value = match.group(1)
    if len(hex_value) == 3:
        hex_value = "".join(character * 2 for character in hex_value)
    return tuple(int(hex_value[index : index + 2], 16) for index in (0, 2, 4))


def estimate_uniform_background(image: Image.Image) -> tuple[int, int, int] | None:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    height, width = rgb.shape[:2]
    sample_h = max(8, int(height * 0.08))
    sample_w = max(8, int(width * 0.08))
    corner_blocks = [
        rgb[:sample_h, :sample_w],
        rgb[:sample_h, -sample_w:],
        rgb[-sample_h:, :sample_w],
        rgb[-sample_h:, -sample_w:],
    ]
    corner_medians = np.asarray([np.median(block.reshape(-1, 3), axis=0) for block in corner_blocks])
    background = np.median(corner_medians, axis=0)
    corner_distances = np.linalg.norm(corner_medians - background, axis=1)
    samples = np.concatenate([block.reshape(-1, 3) for block in corner_blocks], axis=0)
    sample_distances = np.linalg.norm(samples - background, axis=1)
    if float(np.max(corner_distances)) > 24 or float(np.percentile(sample_distances, 90)) > 18:
        return None
    return tuple(int(round(value)) for value in background)


def resolve_background_color(
    image: Image.Image, background_mode: str, explicit_color: tuple[int, int, int] | None
) -> tuple[int, int, int] | None:
    if explicit_color is not None:
        return explicit_color
    if background_mode == "off":
        return None
    if background_mode == "white":
        return (255, 255, 255)
    return estimate_uniform_background(image)


def refine_alpha(
    image: Image.Image, mask: Image.Image, background_color: tuple[int, int, int] | None
) -> Image.Image:
    alpha = np.asarray(mask, dtype=np.float32) / 255.0
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)

    if background_color is not None:
        # 对接近已识别背景色的低置信度区域做轻量抑制，减少白雾和彩色残边。
        background = np.asarray(background_color, dtype=np.float32)
        color_delta = np.sqrt(np.mean((rgb - background) ** 2, axis=2)) / 255.0
        near_background = color_delta < 0.035
        alpha[near_background & (alpha < 0.42)] *= 0.2

    alpha_img = Image.fromarray(np.clip(alpha * 255, 0, 255).astype(np.uint8), "L")
    alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(0.45))
    alpha = np.asarray(alpha_img, dtype=np.float32) / 255.0
    alpha = np.where(alpha < 0.012, 0, alpha)
    alpha = np.where(alpha > 0.988, 1, alpha)
    return Image.fromarray((np.clip(alpha, 0, 1) * 255).astype(np.uint8), "L")


def build_foreground_proximity(alpha: np.ndarray) -> np.ndarray:
    height, width = alpha.shape
    scale = min(1.0, 320.0 / max(height, width))
    small_size = (max(1, int(width * scale)), max(1, int(height * scale)))
    foreground = Image.fromarray(((alpha > 0.08) * 255).astype(np.uint8), "L").resize(
        small_size, Image.Resampling.NEAREST
    )
    radius = max(5, int(max(small_size) * 0.09))
    kernel = radius * 2 + 1
    proximity = foreground.filter(ImageFilter.MaxFilter(kernel))
    proximity = proximity.filter(ImageFilter.GaussianBlur(max(2, radius * 0.35)))
    proximity = proximity.resize((width, height), Image.Resampling.BILINEAR)
    return np.asarray(proximity, dtype=np.float32) / 255.0


def preserve_background_shadow(
    image: Image.Image,
    alpha_img: Image.Image,
    background_color: tuple[int, int, int] | None,
    shadow_mode: str,
) -> tuple[Image.Image, bool]:
    if shadow_mode == "off":
        return alpha_img, False
    if background_color is None:
        return alpha_img, False

    rgb = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0
    background = np.asarray(background_color, dtype=np.float32) / 255.0
    alpha = np.asarray(alpha_img, dtype=np.float32) / 255.0
    proximity = build_foreground_proximity(alpha)

    # 半透明投影会表现为偏离均匀背景色；按最大通道偏差估算 alpha，
    # 再限制在模型主体附近，避免把整张背景的轻微噪点一并保留下来。
    background_deviation = np.max(np.abs(rgb - background), axis=2)
    shadow_alpha = np.clip((background_deviation - 0.008) / 0.992, 0.0, 0.72)
    shadow_alpha *= proximity
    shadow_alpha = np.where(shadow_alpha < 0.01, 0.0, shadow_alpha)
    combined = np.maximum(alpha, shadow_alpha)

    combined_img = Image.fromarray((np.clip(combined, 0, 1) * 255).astype(np.uint8), "L")
    return combined_img.filter(ImageFilter.GaussianBlur(0.35)), True


def decontaminate_background(
    image: Image.Image, alpha_img: Image.Image, background_color: tuple[int, int, int]
) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    background = np.asarray(background_color, dtype=np.float32)
    alpha = np.asarray(alpha_img, dtype=np.float32) / 255.0
    safe_alpha = np.maximum(alpha[..., None], 0.08)
    foreground = (rgb - (1.0 - safe_alpha) * background) / safe_alpha
    foreground = np.where(alpha[..., None] < 0.98, foreground, rgb)
    rgba = np.dstack([np.clip(foreground, 0, 255).astype(np.uint8), np.asarray(alpha_img, dtype=np.uint8)])
    return Image.fromarray(rgba, "RGBA")


def checker(size: tuple[int, int], block: int = 24) -> Image.Image:
    width, height = size
    yy, xx = np.indices((height, width))
    pattern = ((xx // block + yy // block) % 2 == 0)
    arr = np.empty((height, width, 3), dtype=np.uint8)
    arr[pattern] = (226, 226, 226)
    arr[~pattern] = (178, 178, 178)
    return Image.fromarray(arr, "RGB")


def make_contact_sheet(paths: list[Path], mode: str, output: Path) -> None:
    thumb = 220
    label_h = 34
    cols = 4
    rows = (len(paths) + cols - 1) // cols
    background = (18, 22, 34) if mode == "dark" else (255, 255, 255)
    sheet = Image.new("RGB", (cols * thumb, rows * (thumb + label_h)), background)
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(paths):
        image = Image.open(path).convert("RGBA")
        image.thumbnail((thumb, thumb), Image.Resampling.LANCZOS)
        cell_x = (index % cols) * thumb
        cell_y = (index // cols) * (thumb + label_h)
        bg = Image.new("RGB", (thumb, thumb), (18, 22, 34)) if mode == "dark" else checker((thumb, thumb))
        bg.paste(image, ((thumb - image.width) // 2, (thumb - image.height) // 2), image)
        sheet.paste(bg, (cell_x, cell_y))
        label = path.name if len(path.name) <= 28 else path.name[:12] + "..." + path.name[-10:]
        fill = (235, 240, 255) if mode == "dark" else (20, 20, 20)
        draw.text((cell_x + 6, cell_y + thumb + 6), label, fill=fill)
    sheet.save(output)


def validate_outputs(paths: list[Path]) -> None:
    problems = []
    for path in paths:
        image = Image.open(path)
        if image.mode != "RGBA":
            problems.append(f"{path.name}: 不是 RGBA")
            continue
        alpha = image.getchannel("A")
        width, height = image.size
        corners = [
            alpha.getpixel((0, 0)),
            alpha.getpixel((width - 1, 0)),
            alpha.getpixel((0, height - 1)),
            alpha.getpixel((width - 1, height - 1)),
        ]
        if any(value != 0 for value in corners):
            problems.append(f"{path.name}: 四角不是全透明 {corners}")
    if problems:
        raise RuntimeError("输出校验失败: " + "; ".join(problems))


def cutout_name(path: Path, model_key: str, name_style: str, shadow_preserved: bool) -> str:
    if name_style == "legacy":
        return f"{path.stem}_cutout.png"
    shadow_suffix = "-shadow" if shadow_preserved else ""
    return f"{path.stem}_cutout-{model_key}{shadow_suffix}.png"


def alpha_name(path: Path, model_key: str, name_style: str, shadow_preserved: bool) -> str:
    if name_style == "legacy":
        return f"{path.stem}_alpha.png"
    shadow_suffix = "-shadow" if shadow_preserved else ""
    return f"{path.stem}_alpha-{model_key}{shadow_suffix}.png"


def main() -> int:
    args = parse_args()
    explicit_background_color = parse_background_color(args.background_color)
    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    files = collect_images(input_path, args.limit)
    if not files:
        log("没有找到可处理图片。")
        return 2

    device = choose_device(args.device)
    log(f"输入图片: {len(files)}")
    log(f"输出目录: {output_dir}")
    log(f"设备: {device}")

    model = load_model(args.model, device, args.local_files_only)
    transform_image = build_transform(args.image_size)

    processed = []
    manifest_items = []
    started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    for index, path in enumerate(files, 1):
        log(f"[{index}/{len(files)}] {path.name}")
        image = Image.open(path).convert("RGB")
        original_size = image.size
        background_color = resolve_background_color(image, args.background_mode, explicit_background_color)
        background_label = (
            "#{:02X}{:02X}{:02X}".format(*background_color) if background_color is not None else "未识别"
        )
        log(f"背景色: {background_label}")
        mask = infer_mask(model, transform_image, image, device)
        alpha = refine_alpha(image, mask, background_color)
        alpha, shadow_preserved = preserve_background_shadow(image, alpha, background_color, args.shadow_mode)
        should_decontaminate = not args.no_decontaminate and background_color is not None
        cutout = decontaminate_background(image, alpha, background_color) if should_decontaminate else image.convert("RGBA")
        if not should_decontaminate:
            cutout.putalpha(alpha)
        out_path = output_dir / cutout_name(path, args.model, args.name_style, shadow_preserved)
        cutout.save(out_path)
        alpha_path = None
        if not args.no_alpha:
            alpha_path = output_dir / alpha_name(path, args.model, args.name_style, shadow_preserved)
            alpha.save(alpha_path)
        processed.append(out_path)
        manifest_items.append(
            {
                "source": str(path),
                "output": str(out_path),
                "alpha": str(alpha_path) if alpha_path else None,
                "operation": "cutout",
                "model": args.model,
                "model_repo": MODEL_REPOS[args.model],
                "image_size": args.image_size,
                "background_mode": args.background_mode,
                "background_color": background_label if background_color is not None else None,
                "background_detected": background_color is not None,
                "decontaminate_background": should_decontaminate,
                "decontaminate_white": should_decontaminate and background_color == (255, 255, 255),
                "shadow_mode": args.shadow_mode,
                "shadow_preserved": shadow_preserved,
                "source_width": original_size[0],
                "source_height": original_size[1],
                "output_width": cutout.width,
                "output_height": cutout.height,
                "source_bytes": path.stat().st_size,
                "output_bytes": out_path.stat().st_size,
            }
        )

    make_contact_sheet(processed, "checker", output_dir / "preview_checker.png")
    make_contact_sheet(processed, "dark", output_dir / "preview_dark.png")
    validate_outputs(processed)
    manifest = {
        "tool": "image-assets cutout",
        "started_at": started_at,
        "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "input": str(input_path),
        "output": str(output_dir),
        "count": len(processed),
        "items": manifest_items,
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"透明 PNG: {len(processed)}")
    log(f"棋盘格预览: {output_dir / 'preview_checker.png'}")
    log(f"深色预览: {output_dir / 'preview_dark.png'}")
    log(f"处理清单: {output_dir / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        log("用户中断。")
        raise SystemExit(130)
    except Exception as exc:
        log(f"失败: {exc}")
        raise
