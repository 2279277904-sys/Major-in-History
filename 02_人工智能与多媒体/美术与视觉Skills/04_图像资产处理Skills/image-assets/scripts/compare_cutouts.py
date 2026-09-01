#!/usr/bin/env python3
import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成两个抠图输出目录的深色背景并排对比图。")
    parser.add_argument("--left", required=True, help="左侧输出目录。")
    parser.add_argument("--right", required=True, help="右侧输出目录。")
    parser.add_argument("--output", required=True, help="对比图输出路径。")
    parser.add_argument("--left-label", default="Left", help="左侧模型标签。")
    parser.add_argument("--right-label", default="Right", help="右侧模型标签。")
    return parser.parse_args()


def cutout_key(path: Path) -> str:
    stem = path.stem
    marker = "_cutout"
    if marker not in stem:
        return stem
    return stem.split(marker, 1)[0]


def collect_cutouts(directory: Path) -> dict[str, Path]:
    files = sorted(directory.glob("*_cutout*.png"))
    return {cutout_key(path): path for path in files}


def main() -> int:
    args = parse_args()
    left_dir = Path(args.left).expanduser().resolve()
    right_dir = Path(args.right).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    left_files = collect_cutouts(left_dir)
    right_files = collect_cutouts(right_dir)
    if not left_files:
        raise SystemExit("左侧目录没有 *_cutout*.png")
    if not right_files:
        raise SystemExit("右侧目录没有 *_cutout*.png")

    keys = sorted(set(left_files) & set(right_files))
    if not keys:
        raise SystemExit("左右目录没有可按原图名称配对的 cutout PNG")

    thumb = 180
    label_h = 42
    pair_gap = 18
    cell_w = thumb * 2 + pair_gap
    cols = 2
    rows = (len(keys) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, rows * (thumb + label_h)), (18, 22, 34))
    draw = ImageDraw.Draw(sheet)

    for index, key in enumerate(keys):
        left_path = left_files[key]
        right_path = right_files[key]
        x0 = (index % cols) * cell_w
        y0 = (index // cols) * (thumb + label_h)
        for side, (path, title) in enumerate(((left_path, args.left_label), (right_path, args.right_label))):
            bg = Image.new("RGB", (thumb, thumb), (18, 22, 34))
            image = Image.open(path).convert("RGBA")
            image.thumbnail((thumb, thumb), Image.Resampling.LANCZOS)
            bg.paste(image, ((thumb - image.width) // 2, (thumb - image.height) // 2), image)
            x = x0 + side * (thumb + pair_gap)
            sheet.paste(bg, (x, y0))
            draw.text((x + 6, y0 + thumb + 4), title, fill=(235, 240, 255))
        short = key if len(key) < 28 else key[:10] + "..." + key[-8:]
        draw.text((x0 + 6, y0 + thumb + 22), short, fill=(180, 188, 205))

    sheet.save(output)
    print(f"[图片素材] 对比图: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
