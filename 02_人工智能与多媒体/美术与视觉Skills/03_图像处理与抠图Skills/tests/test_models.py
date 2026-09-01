from __future__ import annotations

from PIL import Image

from image_processing.models import RembgBackend, decontaminate_edges


def test_backend_passes_explicit_model_reuses_session_and_avoids_large_alpha_matting():
    sessions = []
    calls = []

    def new_session(model_name):
        sessions.append(model_name)
        return object()

    def remove(image, **kwargs):
        calls.append(kwargs)
        return image.convert("RGBA")

    backend = RembgBackend(loader=lambda: (new_session, remove))
    image = Image.new("RGB", (10, 10), "white")
    backend.remove_background(image, "birefnet-general")
    backend.remove_background(image, "birefnet-general")

    assert sessions == ["birefnet-general"]
    assert all(call["session"] is calls[0]["session"] for call in calls)
    assert all(call["alpha_matting"] is False for call in calls)
    assert "bria-rmbg" not in sessions


def test_soft_edge_color_decontamination_uses_nearby_foreground():
    image = Image.new("RGBA", (5, 1), (255, 255, 255, 0))
    image.putpixel((2, 0), (220, 20, 10, 255))
    image.putpixel((1, 0), (240, 160, 150, 128))
    image.putpixel((3, 0), (240, 160, 150, 128))

    result = decontaminate_edges(image)

    assert result.getpixel((0, 0)) == (0, 0, 0, 0)
    left = result.getpixel((1, 0))
    assert left[0] >= 220
    assert left[1] < 160
    assert left[2] < 150
    assert left[3] == 128
