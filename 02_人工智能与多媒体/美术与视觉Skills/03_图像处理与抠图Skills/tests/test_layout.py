from __future__ import annotations

import pytest
from PIL import Image, ImageDraw

from image_processing.errors import ValidationFailure
from image_processing.layout import (
    layout_aspect_ratio,
    layout_exact_size,
    parse_aspect_ratio,
    subject_bbox,
)


def cutout(size=(100, 100), rectangle=(20, 30, 80, 70), alpha=255):
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(image).rectangle(rectangle, fill=(200, 20, 30, alpha))
    return image


def test_empty_alpha_is_rejected():
    with pytest.raises(ValidationFailure, match="No subject"):
        subject_bbox(Image.new("RGBA", (20, 20), (0, 0, 0, 0)))


def test_soft_alpha_uses_threshold():
    image = Image.new("RGBA", (20, 20), (0, 0, 0, 0))
    image.putpixel((2, 2), (255, 0, 0, 7))
    image.putpixel((10, 11), (255, 0, 0, 8))
    assert subject_bbox(image, alpha_threshold=8) == (9, 10, 12, 13)


def test_bbox_expands_two_percent_and_clamps():
    image = cutout((200, 200), (50, 60, 149, 159))
    assert subject_bbox(image) == (48, 58, 152, 162)


@pytest.mark.parametrize("rectangle", [(10, 40, 89, 59), (40, 10, 59, 89)])
def test_exact_layout_centers_and_stays_within_target(rectangle):
    result = layout_exact_size(cutout(rectangle=rectangle), 500, 400)
    left, top, right, bottom = result.subject_bbox
    assert (right - left) / 500 <= 0.8
    assert (bottom - top) / 400 <= 0.8
    assert abs((left + right) - 500) <= 2
    assert abs((top + bottom) - 400) <= 2


def test_exact_layout_warns_when_upscaled():
    result = layout_exact_size(cutout((20, 20), (8, 8, 11, 11)), 1000, 1000)
    assert result.upscaled is True
    assert result.scale_factor > 1


def test_ratio_only_never_upscales_and_has_exact_reduced_ratio():
    source = cutout((120, 80), (10, 10, 109, 69))
    result = layout_aspect_ratio(source, parse_aspect_ratio("1080:1440"))
    assert result.scale_factor == 1
    assert result.subject_size == (104, 64)
    assert result.image.width * 4 == result.image.height * 3
    assert result.image.width == 132
    assert result.image.height == 176


def test_parse_aspect_ratio_reduces_values():
    assert parse_aspect_ratio("1080:1440") == (3, 4)
    with pytest.raises(ValidationFailure):
        parse_aspect_ratio("3x4")
