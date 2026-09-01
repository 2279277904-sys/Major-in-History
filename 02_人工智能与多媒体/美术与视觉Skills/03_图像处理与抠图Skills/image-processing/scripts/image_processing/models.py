"""Explicit rembg model adapter with per-process session reuse."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import numpy as np
from PIL import Image
from scipy.ndimage import distance_transform_edt

from .errors import DependencyFailure, InferenceFailure, ValidationFailure

DEFAULT_MODEL = "birefnet-general"
ALLOWED_MODELS = frozenset({"birefnet-general", "birefnet-general-lite", "u2net"})


def decontaminate_edges(image: Image.Image, opaque_threshold: int = 248) -> Image.Image:
    """Replace background-tinted soft-edge colors with nearby foreground colors."""

    rgba = np.array(image.convert("RGBA"), dtype=np.uint8, copy=True)
    alpha = rgba[..., 3]
    soft = (alpha > 0) & (alpha < opaque_threshold)
    opaque = alpha >= opaque_threshold
    rgba[alpha == 0, :3] = 0
    if not np.any(soft) or not np.any(opaque):
        return Image.fromarray(rgba, mode="RGBA")

    _, nearest_indices = distance_transform_edt(~opaque, return_indices=True)
    nearest_rgb = rgba[nearest_indices[0], nearest_indices[1], :3].astype(np.float32)
    rgb = rgba[..., :3].astype(np.float32)
    strength = ((255.0 - alpha.astype(np.float32)) / 255.0)[..., None]
    corrected = np.rint(rgb * (1.0 - strength) + nearest_rgb * strength)
    rgba[..., :3][soft] = np.clip(corrected[soft], 0, 255).astype(np.uint8)
    return Image.fromarray(rgba, mode="RGBA")


def validate_model(model_name: str) -> str:
    if model_name not in ALLOWED_MODELS:
        allowed = ", ".join(sorted(ALLOWED_MODELS))
        raise ValidationFailure(f"Unsupported model '{model_name}'. Allowed models: {allowed}")
    return model_name


def _load_rembg() -> tuple[Callable[..., Any], Callable[..., Any]]:
    try:
        from rembg import new_session, remove
    except (ImportError, OSError) as exc:
        raise DependencyFailure(
            "rembg or ONNX Runtime is unavailable. Run scripts/setup.ps1 first."
        ) from exc
    return new_session, remove


class RembgBackend:
    """Remove backgrounds while always passing an explicitly allowlisted session."""

    def __init__(
        self,
        loader: Callable[[], tuple[Callable[..., Any], Callable[..., Any]]] | None = None,
    ) -> None:
        self._loader = loader or _load_rembg
        self._api: tuple[Callable[..., Any], Callable[..., Any]] | None = None
        self._sessions: dict[str, Any] = {}

    def _functions(self) -> tuple[Callable[..., Any], Callable[..., Any]]:
        if self._api is None:
            self._api = self._loader()
        return self._api

    def _session(self, model_name: str) -> Any:
        validate_model(model_name)
        if model_name not in self._sessions:
            new_session, _ = self._functions()
            try:
                self._sessions[model_name] = new_session(model_name)
            except FileNotFoundError as exc:
                raise DependencyFailure(
                    f"Model '{model_name}' is missing from REMBG_HOME. Run scripts/setup.ps1."
                ) from exc
            except (OSError, RuntimeError) as exc:
                raise DependencyFailure(f"Unable to load model '{model_name}': {exc}") from exc
        return self._sessions[model_name]

    def remove_background(self, image: Image.Image, model_name: str) -> Image.Image:
        session = self._session(model_name)
        _, remove = self._functions()
        try:
            # PyMatting's closed-form solver preallocates several GiB. BiRefNet
            # already returns a soft alpha mask, so use rembg's low-memory cutout
            # and correct soft-edge colors deterministically afterward.
            result = remove(image, session=session, alpha_matting=False)
        except Exception as exc:
            raise InferenceFailure(f"Background removal failed: {exc}") from exc
        if not isinstance(result, Image.Image):
            raise InferenceFailure("rembg returned an unsupported result type")
        return decontaminate_edges(result)
