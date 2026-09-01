"""Pure image layout functions independent of the inference backend."""

from __future__ import annotations

import math
from dataclasses import dataclass
from math import gcd

from PIL import Image

from .errors import ValidationFailure

BBox = tuple[int, int, int, int]


@dataclass(frozen=True)
class LayoutResult:
    image: Image.Image
    source_bbox: BBox
    subject_bbox: BBox
    subject_size: tuple[int, int]
    scale_factor: float
    upscaled: bool


def parse_aspect_ratio(value: str) -> tuple[int, int]:
    try:
        left, right = value.split(":", 1)
        width_ratio, height_ratio = int(left), int(right)
    except (AttributeError, TypeError, ValueError) as exc:
        raise ValidationFailure("Aspect ratio must use positive integers in A:B form") from exc
    if width_ratio <= 0 or height_ratio <= 0:
        raise ValidationFailure("Aspect ratio values must be positive")
    divisor = gcd(width_ratio, height_ratio)
    return width_ratio // divisor, height_ratio // divisor


def validate_layout_options(subject_scale: float, alpha_threshold: int) -> None:
    if not 0 < subject_scale <= 1:
        raise ValidationFailure("subject-scale must be greater than 0 and at most 1")
    if not 1 <= alpha_threshold <= 255:
        raise ValidationFailure("alpha-threshold must be between 1 and 255")


def subject_bbox(
    image: Image.Image, alpha_threshold: int = 8, expansion: float = 0.02
) -> BBox:
    validate_layout_options(1.0, alpha_threshold)
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    mask = alpha.point(lambda value: 255 if value >= alpha_threshold else 0)
    bbox = mask.getbbox()
    if bbox is None:
        raise ValidationFailure(f"No subject pixels found at alpha threshold {alpha_threshold}")
    left, top, right, bottom = bbox
    width, height = right - left, bottom - top
    pad_x = math.ceil(width * expansion)
    pad_y = math.ceil(height * expansion)
    return (
        max(0, left - pad_x),
        max(0, top - pad_y),
        min(rgba.width, right + pad_x),
        min(rgba.height, bottom + pad_y),
    )


def _final_bbox(image: Image.Image, threshold: int) -> BBox:
    alpha = image.getchannel("A")
    mask = alpha.point(lambda value: 255 if value >= threshold else 0)
    bbox = mask.getbbox()
    if bbox is None:
        raise ValidationFailure("The laid-out image has no visible subject")
    return bbox


def _center(canvas: Image.Image, subject: Image.Image) -> None:
    left = (canvas.width - subject.width) // 2
    top = (canvas.height - subject.height) // 2
    canvas.alpha_composite(subject, (left, top))


def layout_exact_size(
    cutout: Image.Image,
    width: int,
    height: int,
    subject_scale: float = 0.8,
    alpha_threshold: int = 8,
) -> LayoutResult:
    validate_layout_options(subject_scale, alpha_threshold)
    if width <= 0 or height <= 0:
        raise ValidationFailure("width and height must be positive integers")
    rgba = cutout.convert("RGBA")
    source_bbox = subject_bbox(rgba, alpha_threshold)
    cropped = rgba.crop(source_bbox)
    scale = min(
        (width * subject_scale) / cropped.width,
        (height * subject_scale) / cropped.height,
    )
    resized_width = max(1, min(width, math.floor(cropped.width * scale)))
    resized_height = max(1, min(height, math.floor(cropped.height * scale)))
    resized = cropped.resize((resized_width, resized_height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    _center(canvas, resized)
    return LayoutResult(
        image=canvas,
        source_bbox=source_bbox,
        subject_bbox=_final_bbox(canvas, alpha_threshold),
        subject_size=resized.size,
        scale_factor=scale,
        upscaled=scale > 1.0 + 1e-9,
    )


def layout_aspect_ratio(
    cutout: Image.Image,
    ratio: tuple[int, int],
    subject_scale: float = 0.8,
    alpha_threshold: int = 8,
) -> LayoutResult:
    validate_layout_options(subject_scale, alpha_threshold)
    ratio_width, ratio_height = ratio
    if ratio_width <= 0 or ratio_height <= 0:
        raise ValidationFailure("aspect ratio values must be positive")
    rgba = cutout.convert("RGBA")
    source_bbox = subject_bbox(rgba, alpha_threshold)
    cropped = rgba.crop(source_bbox)
    multiplier = math.ceil(
        max(
            cropped.width / (subject_scale * ratio_width),
            cropped.height / (subject_scale * ratio_height),
        )
    )
    canvas = Image.new(
        "RGBA", (ratio_width * multiplier, ratio_height * multiplier), (0, 0, 0, 0)
    )
    _center(canvas, cropped)
    return LayoutResult(
        image=canvas,
        source_bbox=source_bbox,
        subject_bbox=_final_bbox(canvas, alpha_threshold),
        subject_size=cropped.size,
        scale_factor=1.0,
        upscaled=False,
    )
