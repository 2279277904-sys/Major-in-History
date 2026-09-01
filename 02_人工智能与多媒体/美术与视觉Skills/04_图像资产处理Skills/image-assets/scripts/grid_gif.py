#!/usr/bin/env python3
"""把 N 宫格精灵表切帧、抠图并编码为透明 GIF。"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def log(message: str) -> None:
    print(f"[图片素材] {message}", file=sys.stderr, flush=True)


def parse_grid(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"\s*(\d+)\s*[xX×]\s*(\d+)\s*", value)
    if not match:
        raise argparse.ArgumentTypeError("--grid 必须使用 列数x行数 格式，例如 4x4。")
    columns, rows = (int(match.group(1)), int(match.group(2)))
    if columns <= 0 or rows <= 0:
        raise argparse.ArgumentTypeError("宫格的列数和行数必须大于 0。")
    return columns, rows


def parse_color(value: str | None) -> tuple[int, int, int] | None:
    if value is None:
        return None
    match = re.fullmatch(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value.strip())
    if not match:
        raise ValueError("--background-color 必须是 #RGB 或 #RRGGBB 格式。")
    hex_value = match.group(1)
    if len(hex_value) == 3:
        hex_value = "".join(character * 2 for character in hex_value)
    return tuple(int(hex_value[index : index + 2], 16) for index in (0, 2, 4))


def infer_grid(frame_count: int) -> tuple[int, int]:
    if frame_count <= 0:
        raise ValueError("--frames 必须大于 0。")
    rows = math.isqrt(frame_count)
    while rows > 1 and frame_count % rows != 0:
        rows -= 1
    columns = frame_count // rows
    return columns, rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="把 N 宫格素材切帧、抠图并生成透明 GIF。")
    parser.add_argument("--input", required=True, help="输入的单张 N 宫格图片。")
    parser.add_argument("--output", required=True, help="输出 GIF 文件路径。")
    grid_group = parser.add_mutually_exclusive_group(required=True)
    grid_group.add_argument("--grid", type=parse_grid, help="列数x行数，例如 4x4。")
    grid_group.add_argument("--frames", type=int, help="总帧数；自动推断最接近方形的行列数。")
    parser.add_argument(
        "--cutout-mode",
        choices=["color", "none", "rmbg2", "birefnet"],
        default="color",
        help="抠图方式。默认 color，适合纯色背景像素素材。",
    )
    parser.add_argument(
        "--separator-mode",
        choices=["auto", "none"],
        default="auto",
        help="是否自动识别并剔除宫格分隔线。默认 auto。",
    )
    parser.add_argument("--separator-tolerance", type=float, default=8.0, help="分隔线均匀度容差。默认 8。")
    parser.add_argument("--separator-contrast", type=float, default=20.0, help="分隔线与邻域的最小色差。默认 20。")
    parser.add_argument("--background-color", help="显式背景色，例如 #00152F。默认从每帧四角估算。")
    parser.add_argument("--background-tolerance", type=float, default=12.0, help="纯色背景保守换底容差。默认 12。")
    parser.add_argument("--alpha-feather", type=float, default=0.0, help="纯色抠图边缘羽化宽度。像素画默认 0。")
    parser.add_argument("--duration", type=int, default=120, help="每帧持续毫秒数。默认 120。")
    parser.add_argument("--loop", type=int, default=0, help="循环次数；0 表示无限循环。默认 0。")
    parser.add_argument(
        "--playback",
        choices=["forward", "ping-pong"],
        default="forward",
        help="播放序列。forward 为 12341234，ping-pong 为 1234321。默认 forward。",
    )
    parser.add_argument("--scale", type=int, default=1, help="输出整数放大倍数，使用最近邻缩放。默认 1。")
    parser.add_argument(
        "--anchor",
        choices=["feet", "bottom-center", "center", "cell"],
        default="feet",
        help="逐帧对齐锚点。默认 feet，以脚部中心和最低接地点对齐。",
    )
    parser.add_argument("--anchor-alpha", type=int, default=32, help="锚点检测的最小 alpha。默认 32。")
    parser.add_argument("--feet-ratio", type=float, default=0.08, help="脚部检测占前景高度的底部比例。默认 0.08。")
    parser.add_argument(
        "--order",
        choices=["row-major", "column-major"],
        default="row-major",
        help="帧读取顺序。默认按行从左到右。",
    )
    parser.add_argument("--keep-frames", action="store_true", help="在 GIF 旁保留抠图后的逐帧 PNG。")
    parser.add_argument("--device", choices=["auto", "cpu", "mps", "cuda"], default="auto", help="模型抠图设备。")
    parser.add_argument("--image-size", type=int, default=1024, help="模型抠图推理边长。默认 1024。")
    parser.add_argument("--local-files-only", action="store_true", help="模型抠图只使用本机缓存。")
    parser.add_argument(
        "--background-mode",
        choices=["auto", "white", "off"],
        default="auto",
        help="模型抠图的背景色处理方式。",
    )
    parser.add_argument(
        "--shadow-mode",
        choices=["auto", "on", "off"],
        default="off",
        help="模型抠图是否保留背景投影。像素动画默认关闭。",
    )
    parser.add_argument("--no-decontaminate", action="store_true", help="模型抠图时不反推主体边缘颜色。")
    return parser.parse_args()


def line_statistics(rgb: np.ndarray, axis: int) -> tuple[np.ndarray, np.ndarray]:
    lines = np.moveaxis(rgb, axis, 0).astype(np.float32)
    medians = np.median(lines, axis=1, keepdims=True)
    distances = np.sqrt(np.mean((lines - medians) ** 2, axis=2))
    return np.percentile(distances, 90, axis=1), medians[:, 0, :]


def group_consecutive(values: np.ndarray) -> list[tuple[int, int]]:
    if values.size == 0:
        return []
    groups: list[tuple[int, int]] = []
    start = previous = int(values[0])
    for raw_value in values[1:]:
        value = int(raw_value)
        if value != previous + 1:
            groups.append((start, previous))
            start = value
        previous = value
    groups.append((start, previous))
    return groups


def detect_separator_band(
    scores: np.ndarray,
    medians: np.ndarray,
    expected: float,
    search_radius: int,
    tolerance: float,
    contrast_threshold: float,
) -> tuple[int, int] | None:
    lower = max(0, int(round(expected)) - search_radius)
    upper = min(len(scores) - 1, int(round(expected)) + search_radius)
    local_contrasts = np.zeros(len(scores), dtype=np.float32)
    contrast_radius = max(4, min(12, search_radius // 2))
    for index in range(lower, upper + 1):
        reference_lower = max(0, index - contrast_radius)
        reference_upper = min(len(scores), index + contrast_radius + 1)
        reference = np.median(medians[reference_lower:reference_upper], axis=0)
        local_contrasts[index] = float(np.sqrt(np.mean((medians[index] - reference) ** 2)))
    candidate_mask = (scores <= tolerance) & (local_contrasts >= contrast_threshold)
    candidates = np.flatnonzero(candidate_mask[lower : upper + 1]) + lower
    groups = group_consecutive(candidates)
    if not groups:
        return None
    return min(
        groups,
        key=lambda group: (
            abs((group[0] + group[1]) / 2 - expected),
            float(np.mean(scores[group[0] : group[1] + 1])),
        ),
    )


def calculate_axis_cells(
    length: int,
    count: int,
    scores: np.ndarray | None,
    medians: np.ndarray | None,
    tolerance: float,
    contrast_threshold: float,
) -> tuple[list[tuple[int, int]], list[tuple[int, int] | None]]:
    search_radius = max(2, int(length / count * 0.15))
    bands: list[tuple[int, int] | None] = []
    for index in range(count + 1):
        expected = 0.0 if index == 0 else (length - 1.0 if index == count else length * index / count)
        band = (
            None
            if scores is None or medians is None
            else detect_separator_band(
                scores,
                medians,
                expected,
                search_radius,
                tolerance,
                contrast_threshold,
            )
        )
        bands.append(band)

    cells: list[tuple[int, int]] = []
    for index in range(count):
        start = bands[index][1] + 1 if bands[index] is not None else int(round(length * index / count))
        end = bands[index + 1][0] if bands[index + 1] is not None else int(round(length * (index + 1) / count))
        if end <= start:
            raise RuntimeError(f"第 {index + 1} 个切片范围无效，请使用 --separator-mode none 重试。")
        cells.append((start, end))
    return cells, bands


def split_grid(
    image: Image.Image,
    columns: int,
    rows: int,
    separator_mode: str,
    separator_tolerance: float,
    separator_contrast: float,
    order: str,
) -> tuple[list[Image.Image], dict[str, object]]:
    rgb = np.asarray(image.convert("RGB"), dtype=np.uint8)
    if separator_mode == "auto":
        vertical_scores, vertical_medians = line_statistics(rgb, 1)
        horizontal_scores, horizontal_medians = line_statistics(rgb, 0)
    else:
        vertical_scores = vertical_medians = None
        horizontal_scores = horizontal_medians = None
    x_cells, vertical_bands = calculate_axis_cells(
        image.width,
        columns,
        vertical_scores,
        vertical_medians,
        separator_tolerance,
        separator_contrast,
    )
    y_cells, horizontal_bands = calculate_axis_cells(
        image.height,
        rows,
        horizontal_scores,
        horizontal_medians,
        separator_tolerance,
        separator_contrast,
    )

    coordinates = (
        [(row, column) for row in range(rows) for column in range(columns)]
        if order == "row-major"
        else [(row, column) for column in range(columns) for row in range(rows)]
    )
    frames = []
    for row, column in coordinates:
        left, right = x_cells[column]
        top, bottom = y_cells[row]
        frames.append(image.crop((left, top, right, bottom)).convert("RGBA"))
    metadata = {
        "x_cells": x_cells,
        "y_cells": y_cells,
        "vertical_separator_bands": vertical_bands,
        "horizontal_separator_bands": horizontal_bands,
    }
    return frames, metadata


def estimate_background_color(image: Image.Image) -> tuple[int, int, int]:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    height, width = rgb.shape[:2]
    sample = max(2, int(min(width, height) * 0.06))
    blocks = [
        rgb[:sample, :sample],
        rgb[:sample, -sample:],
        rgb[-sample:, :sample],
        rgb[-sample:, -sample:],
    ]
    medians = np.asarray([np.median(block.reshape(-1, 3), axis=0) for block in blocks])
    background = np.median(medians, axis=0)
    return tuple(int(round(value)) for value in background)


def edge_connected_mask(candidate: np.ndarray) -> np.ndarray:
    height, width = candidate.shape
    connected = np.zeros_like(candidate, dtype=bool)
    queue: deque[tuple[int, int]] = deque()

    def enqueue(y: int, x: int) -> None:
        if candidate[y, x] and not connected[y, x]:
            connected[y, x] = True
            queue.append((y, x))

    for x in range(width):
        enqueue(0, x)
        enqueue(height - 1, x)
    for y in range(height):
        enqueue(y, 0)
        enqueue(y, width - 1)

    while queue:
        y, x = queue.popleft()
        if y > 0:
            enqueue(y - 1, x)
        if y + 1 < height:
            enqueue(y + 1, x)
        if x > 0:
            enqueue(y, x - 1)
        if x + 1 < width:
            enqueue(y, x + 1)
    return connected


def foreground_components(foreground: np.ndarray) -> list[list[tuple[int, int]]]:
    height, width = foreground.shape
    visited = np.zeros_like(foreground, dtype=bool)
    components: list[list[tuple[int, int]]] = []
    for raw_y, raw_x in np.argwhere(foreground):
        start_y, start_x = int(raw_y), int(raw_x)
        if visited[start_y, start_x]:
            continue
        visited[start_y, start_x] = True
        stack = [(start_y, start_x)]
        component: list[tuple[int, int]] = []
        while stack:
            y, x = stack.pop()
            component.append((y, x))
            for neighbor_y in range(max(0, y - 1), min(height, y + 2)):
                for neighbor_x in range(max(0, x - 1), min(width, x + 2)):
                    if foreground[neighbor_y, neighbor_x] and not visited[neighbor_y, neighbor_x]:
                        visited[neighbor_y, neighbor_x] = True
                        stack.append((neighbor_y, neighbor_x))
        components.append(component)
    return components


def remove_edge_artifacts(rgba: np.ndarray) -> None:
    foreground = rgba[..., 3] > 0
    components = foreground_components(foreground)
    if not components:
        return
    height, width = foreground.shape
    largest_area = max(len(component) for component in components)
    for component in components:
        component_y, component_x = zip(*component)
        top, bottom = min(component_y), max(component_y)
        left, right = min(component_x), max(component_x)
        touches_edge = top == 0 or left == 0 or bottom == height - 1 or right == width - 1
        if not touches_edge:
            continue
        box_width = right - left + 1
        box_height = bottom - top + 1
        aspect_ratio = max(box_width, box_height) / max(1, min(box_width, box_height))
        fill_ratio = len(component) / (box_width * box_height)
        is_small = len(component) <= max(8, int(round(largest_area * 0.01)))
        is_thin_line = aspect_ratio >= 8
        is_hollow_border = box_width > width * 0.35 and box_height > height * 0.5 and fill_ratio < 0.12
        if not (is_small or is_thin_line or is_hollow_border):
            continue
        rgba[component_y, component_x, :3] = (255, 0, 255)
        rgba[component_y, component_x, 3] = 0


def color_cutout(
    image: Image.Image,
    background_color: tuple[int, int, int],
    tolerance: float,
    feather: float,
) -> Image.Image:
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    rgb = rgba[..., :3].astype(np.float32)
    background = np.asarray(background_color, dtype=np.float32)
    distances = np.sqrt(np.mean((rgb - background) ** 2, axis=2))
    connected = edge_connected_mask(distances <= tolerance + max(0.0, feather))
    generated_alpha = np.full(distances.shape, 255.0, dtype=np.float32)
    if feather > 0:
        generated_alpha[connected] = np.clip(
            (distances[connected] - tolerance) / feather * 255.0,
            0.0,
            255.0,
        )
    else:
        generated_alpha[connected] = 0.0
    transparent_background = connected & (generated_alpha <= 0)
    rgba[transparent_background, :3] = (255, 0, 255)
    rgba[..., 3] = np.minimum(rgba[..., 3], generated_alpha.astype(np.uint8))
    remove_edge_artifacts(rgba)
    return Image.fromarray(rgba)


def model_cutout_frames(frames: list[Image.Image], args: argparse.Namespace) -> tuple[list[Image.Image], list[str | None]]:
    from cutout_images import (  # 延迟导入，纯色抠图无需加载模型依赖
        build_transform,
        choose_device,
        decontaminate_background,
        infer_mask,
        load_model,
        parse_background_color,
        preserve_background_shadow,
        refine_alpha,
        resolve_background_color,
    )

    device = choose_device(args.device)
    log(f"加载 {args.cutout_mode} 模型，设备: {device}")
    model = load_model(args.cutout_mode, device, args.local_files_only)
    transform_image = build_transform(args.image_size)
    explicit_color = parse_background_color(args.background_color)
    processed: list[Image.Image] = []
    background_labels: list[str | None] = []
    for index, frame in enumerate(frames, 1):
        log(f"模型抠图: {index}/{len(frames)}")
        rgb_frame = frame.convert("RGB")
        background_color = resolve_background_color(rgb_frame, args.background_mode, explicit_color)
        mask = infer_mask(model, transform_image, rgb_frame, device)
        alpha = refine_alpha(rgb_frame, mask, background_color)
        alpha, _ = preserve_background_shadow(rgb_frame, alpha, background_color, args.shadow_mode)
        if not args.no_decontaminate and background_color is not None:
            cutout = decontaminate_background(rgb_frame, alpha, background_color)
        else:
            cutout = rgb_frame.convert("RGBA")
            cutout.putalpha(alpha)
        processed.append(cutout)
        background_labels.append(
            "#{:02X}{:02X}{:02X}".format(*background_color) if background_color is not None else None
        )
    return processed, background_labels


def significant_foreground_mask(foreground: np.ndarray) -> np.ndarray:
    components = foreground_components(foreground)

    if not components:
        return foreground
    largest_area = max(len(component) for component in components)
    minimum_area = max(8, int(round(largest_area * 0.01)))
    significant = np.zeros_like(foreground, dtype=bool)
    for component in components:
        if len(component) < minimum_area:
            continue
        component_y, component_x = zip(*component)
        significant[component_y, component_x] = True
    return significant


def detect_anchor(
    frame: Image.Image,
    anchor_mode: str,
    alpha_threshold: int,
    feet_ratio: float,
) -> tuple[int, int]:
    if anchor_mode == "cell":
        return ((frame.width - 1) // 2, (frame.height - 1) // 2)

    alpha = np.asarray(frame.getchannel("A"), dtype=np.uint8)
    foreground = significant_foreground_mask(alpha >= alpha_threshold)
    ys, xs = np.nonzero(foreground)
    if xs.size == 0:
        return ((frame.width - 1) // 2, (frame.height - 1) // 2)

    left, right = int(xs.min()), int(xs.max())
    top, bottom = int(ys.min()), int(ys.max())
    if anchor_mode == "center":
        return ((left + right) // 2, (top + bottom) // 2)
    if anchor_mode == "bottom-center":
        return ((left + right) // 2, bottom)

    foot_height = max(1, int(round((bottom - top + 1) * feet_ratio)))
    foot_region = foreground[max(top, bottom - foot_height + 1) : bottom + 1]
    _, foot_xs = np.nonzero(foot_region)
    if foot_xs.size == 0:
        return ((left + right) // 2, bottom)
    return ((int(foot_xs.min()) + int(foot_xs.max())) // 2, bottom)


def normalize_frames(
    frames: list[Image.Image],
    scale: int,
    anchor_mode: str,
    alpha_threshold: int,
    feet_ratio: float,
) -> tuple[list[Image.Image], dict[str, object]]:
    anchors = [detect_anchor(frame, anchor_mode, alpha_threshold, feet_ratio) for frame in frames]
    left_extent = max(anchor[0] for anchor in anchors)
    right_extent = max(frame.width - 1 - anchor[0] for frame, anchor in zip(frames, anchors))
    top_extent = max(anchor[1] for anchor in anchors)
    bottom_extent = max(frame.height - 1 - anchor[1] for frame, anchor in zip(frames, anchors))
    target_width = left_extent + 1 + right_extent
    target_height = top_extent + 1 + bottom_extent
    target_anchor = (left_extent, top_extent)

    normalized = []
    offsets = []
    for frame, anchor in zip(frames, anchors):
        offset = (target_anchor[0] - anchor[0], target_anchor[1] - anchor[1])
        canvas = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
        canvas.alpha_composite(frame, offset)
        if scale != 1:
            canvas = canvas.resize((target_width * scale, target_height * scale), Image.Resampling.NEAREST)
        normalized.append(canvas)
        offsets.append(offset)
    metadata = {
        "mode": anchor_mode,
        "alpha_threshold": alpha_threshold,
        "feet_ratio": feet_ratio,
        "source_anchors": anchors,
        "target_anchor": (target_anchor[0] * scale, target_anchor[1] * scale),
        "offsets": offsets,
    }
    return normalized, metadata


def build_shared_palette(frames: list[Image.Image]) -> Image.Image:
    columns = min(4, len(frames))
    rows = math.ceil(len(frames) / columns)
    width, height = frames[0].size
    atlas = Image.new("RGB", (width * columns, height * rows), (0, 0, 0))
    for index, frame in enumerate(frames):
        rgb = Image.new("RGB", frame.size, (0, 0, 0))
        rgb.paste(frame.convert("RGB"), mask=frame.getchannel("A"))
        atlas.paste(rgb, ((index % columns) * width, (index // columns) * height))
    return atlas.quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)


def convert_gif_frames(frames: list[Image.Image]) -> list[Image.Image]:
    palette = build_shared_palette(frames)
    palette_data = list(palette.getpalette() or [])
    palette_data = (palette_data + [0] * 768)[:768]
    palette_data[255 * 3 : 255 * 3 + 3] = [0, 0, 0]
    converted = []
    for frame in frames:
        rgb = Image.new("RGB", frame.size, (0, 0, 0))
        rgb.paste(frame.convert("RGB"), mask=frame.getchannel("A"))
        indexed = rgb.quantize(palette=palette, dither=Image.Dither.NONE)
        indices = np.asarray(indexed, dtype=np.uint8).copy()
        indices[np.asarray(frame.getchannel("A"), dtype=np.uint8) < 128] = 255
        gif_frame = Image.fromarray(indices).convert("P")
        gif_frame.putpalette(palette_data)
        gif_frame.info["transparency"] = 255
        gif_frame.info["disposal"] = 2
        converted.append(gif_frame)
    return converted


def checker_background(size: tuple[int, int], block: int = 16) -> Image.Image:
    width, height = size
    yy, xx = np.indices((height, width))
    pattern = ((xx // block + yy // block) % 2 == 0)
    array = np.empty((height, width, 3), dtype=np.uint8)
    array[pattern] = (235, 235, 235)
    array[~pattern] = (180, 180, 180)
    return Image.fromarray(array)


def make_alignment_preview(
    frames: list[Image.Image],
    target_anchor: tuple[int, int],
    output_path: Path,
) -> None:
    columns = min(4, len(frames))
    rows = math.ceil(len(frames) / columns)
    thumb = 240
    label_height = 28
    sheet = Image.new("RGB", (columns * thumb, rows * (thumb + label_height)), (28, 32, 42))
    for index, frame in enumerate(frames):
        scale = min((thumb - 16) / frame.width, (thumb - 16) / frame.height)
        display_size = (max(1, round(frame.width * scale)), max(1, round(frame.height * scale)))
        display = frame.resize(display_size, Image.Resampling.NEAREST)
        cell = Image.new("RGBA", (thumb, thumb + label_height), (28, 32, 42, 255))
        cell.paste(checker_background((thumb, thumb)).convert("RGBA"), (0, 0))
        offset_x = (thumb - display.width) // 2
        offset_y = (thumb - display.height) // 2
        cell.alpha_composite(display, (offset_x, offset_y))
        draw = ImageDraw.Draw(cell)
        guide_x = offset_x + round(target_anchor[0] * scale)
        guide_y = offset_y + round(target_anchor[1] * scale)
        draw.line((guide_x, 0, guide_x, thumb - 1), fill=(255, 60, 60, 190), width=1)
        draw.line((0, guide_y, thumb - 1, guide_y), fill=(60, 255, 130, 190), width=1)
        draw.text((8, thumb + 5), f"帧 {index + 1:02d}", fill=(255, 255, 255, 255))
        sheet.paste(cell.convert("RGB"), ((index % columns) * thumb, (index // columns) * (thumb + label_height)))
    sheet.save(output_path)


def make_gif_checker_preview(gif_path: Path, output_path: Path) -> None:
    preview_frames: list[Image.Image] = []
    durations: list[int] = []
    with Image.open(gif_path) as gif:
        loop = int(gif.info.get("loop", 0))
        for index in range(gif.n_frames):
            gif.seek(index)
            rgba = gif.convert("RGBA")
            checker = checker_background(rgba.size)
            checker.paste(rgba, (0, 0), rgba)
            preview_frames.append(checker)
            durations.append(int(gif.info.get("duration", 100)))
    preview_frames[0].save(
        output_path,
        save_all=True,
        append_images=preview_frames[1:],
        duration=durations,
        loop=loop,
        disposal=2,
        optimize=False,
    )


def save_gif(frames: list[Image.Image], output_path: Path, duration: int, loop: int) -> None:
    gif_frames = convert_gif_frames(frames)
    gif_frames[0].save(
        output_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=duration,
        loop=loop,
        transparency=255,
        disposal=2,
        optimize=False,
    )


def build_playback_frames(
    frames: list[Image.Image],
    playback: str,
) -> tuple[list[Image.Image], list[int]]:
    forward_order = list(range(len(frames)))
    if playback == "ping-pong" and len(frames) > 2:
        playback_order = forward_order + list(range(len(frames) - 2, 0, -1))
    else:
        playback_order = forward_order
    return [frames[index] for index in playback_order], [index + 1 for index in playback_order]


def validate_args(args: argparse.Namespace) -> tuple[int, int]:
    if args.frames is not None:
        columns, rows = infer_grid(args.frames)
    else:
        columns, rows = args.grid
    if args.duration <= 0:
        raise ValueError("--duration 必须大于 0。")
    if args.loop < 0:
        raise ValueError("--loop 不能小于 0。")
    if args.scale <= 0:
        raise ValueError("--scale 必须大于 0。")
    if not 0 <= args.anchor_alpha <= 255:
        raise ValueError("--anchor-alpha 必须在 0 到 255 之间。")
    if not 0 < args.feet_ratio <= 1:
        raise ValueError("--feet-ratio 必须大于 0 且不超过 1。")
    if (
        args.separator_tolerance < 0
        or args.separator_contrast < 0
        or args.background_tolerance < 0
        or args.alpha_feather < 0
    ):
        raise ValueError("所有容差与羽化参数都不能小于 0。")
    return columns, rows


def main() -> int:
    args = parse_args()
    columns, rows = validate_args(args)
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"输入图片不存在: {input_path}")
    if output_path.suffix.lower() != ".gif":
        raise ValueError("--output 必须指向 .gif 文件。")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    source = Image.open(input_path).convert("RGBA")
    frames, split_metadata = split_grid(
        source,
        columns,
        rows,
        args.separator_mode,
        args.separator_tolerance,
        args.separator_contrast,
        args.order,
    )
    log(f"切分完成: {columns} 列 × {rows} 行，共 {len(frames)} 帧")

    background_labels: list[str | None]
    if args.cutout_mode == "color":
        explicit_color = parse_color(args.background_color)
        background_colors = [explicit_color or estimate_background_color(frame) for frame in frames]
        frames = [
            color_cutout(frame, color, args.background_tolerance, args.alpha_feather)
            for frame, color in zip(frames, background_colors)
        ]
        background_labels = ["#{:02X}{:02X}{:02X}".format(*color) for color in background_colors]
        log("纯色背景抠图完成")
    elif args.cutout_mode in {"rmbg2", "birefnet"}:
        frames, background_labels = model_cutout_frames(frames, args)
    else:
        background_labels = [None] * len(frames)
        log("已跳过抠图")

    frames, anchor_metadata = normalize_frames(
        frames,
        args.scale,
        args.anchor,
        args.anchor_alpha,
        args.feet_ratio,
    )
    log(f"锚点对齐完成: {args.anchor}")
    alignment_preview_path = output_path.with_name(f"{output_path.stem}_alignment.png")
    make_alignment_preview(frames, tuple(anchor_metadata["target_anchor"]), alignment_preview_path)
    log(f"逐帧对齐检查板: {alignment_preview_path}")
    playback_frames, playback_order = build_playback_frames(frames, args.playback)
    save_gif(playback_frames, output_path, args.duration, args.loop)
    log(f"播放序列: {args.playback}，编码 {len(playback_frames)} 帧")
    checker_preview_path = output_path.with_name(f"{output_path.stem}_checker.gif")
    make_gif_checker_preview(output_path, checker_preview_path)
    log(f"最终 GIF 棋盘格预览: {checker_preview_path}")

    frame_paths: list[str] = []
    if args.keep_frames:
        frames_dir = output_path.with_name(f"{output_path.stem}_frames")
        frames_dir.mkdir(parents=True, exist_ok=True)
        for index, frame in enumerate(frames, 1):
            frame_path = frames_dir / f"frame_{index:03d}.png"
            frame.save(frame_path)
            frame_paths.append(str(frame_path))
        log(f"逐帧 PNG: {frames_dir}")

    manifest_path = output_path.with_suffix(".manifest.json")
    manifest = {
        "tool": "image-assets grid-gif",
        "started_at": started_at,
        "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": str(input_path),
        "output": str(output_path),
        "source_width": source.width,
        "source_height": source.height,
        "columns": columns,
        "rows": rows,
        "source_frame_count": len(frames),
        "frame_count": len(playback_frames),
        "frame_width": frames[0].width,
        "frame_height": frames[0].height,
        "duration_ms": args.duration,
        "loop": args.loop,
        "playback": args.playback,
        "playback_order": playback_order,
        "scale": args.scale,
        "anchor": anchor_metadata,
        "alignment_preview": str(alignment_preview_path),
        "checker_preview": str(checker_preview_path),
        "order": args.order,
        "cutout_mode": args.cutout_mode,
        "background_strategy": "conservative-chroma-key" if args.cutout_mode == "color" else None,
        "background_tolerance": args.background_tolerance,
        "chroma_key": "#FF00FF" if args.cutout_mode == "color" else None,
        "background_colors": background_labels,
        "separator_mode": args.separator_mode,
        "separator_tolerance": args.separator_tolerance,
        "separator_contrast": args.separator_contrast,
        "split": split_metadata,
        "frames": frame_paths,
        "output_bytes": output_path.stat().st_size,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"透明 GIF: {output_path}")
    log(f"处理清单: {manifest_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        log("用户中断。")
        raise SystemExit(130)
    except Exception as exc:  # 顶层入口需要把失败转成可读中文日志
        log(f"失败: {exc}")
        raise SystemExit(1)
