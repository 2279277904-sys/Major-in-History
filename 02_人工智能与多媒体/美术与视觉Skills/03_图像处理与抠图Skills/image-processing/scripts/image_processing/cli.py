"""JSON-only command-line contract for image processing."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Protocol, Sequence

from PIL import Image, ImageOps, UnidentifiedImageError

from .errors import FileFailure, InferenceFailure, ProcessingError, ValidationFailure
from .layout import LayoutResult, layout_aspect_ratio, layout_exact_size, parse_aspect_ratio
from .models import DEFAULT_MODEL, RembgBackend, validate_model


class Backend(Protocol):
    def remove_background(self, image: Image.Image, model_name: str) -> Image.Image: ...


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValidationFailure(message)


def build_parser() -> argparse.ArgumentParser:
    parser = JsonArgumentParser(prog="process-image", add_help=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--aspect-ratio")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--subject-scale", type=float, default=0.8)
    parser.add_argument("--alpha-threshold", type=int, default=8)
    parser.add_argument("--overwrite", action="store_true")
    return parser


def _validate_modes(args: argparse.Namespace) -> None:
    has_width = args.width is not None
    has_height = args.height is not None
    has_ratio = args.aspect_ratio is not None
    if has_width != has_height:
        raise ValidationFailure("width and height must be provided together")
    if has_ratio == has_width:
        raise ValidationFailure(
            "Provide either width and height, or aspect-ratio, but not both"
        )
    validate_model(args.model)


def _output_path(input_path: Path, supplied: str | None) -> Path:
    output = Path(supplied).expanduser() if supplied else input_path.with_name(
        f"{input_path.stem}.processed.png"
    )
    if output.suffix.lower() != ".png":
        raise ValidationFailure("MVP output path must end in .png")
    return output.resolve(strict=False)


def _bbox_json(bbox: tuple[int, int, int, int]) -> dict[str, int]:
    left, top, right, bottom = bbox
    return {
        "left": left,
        "top": top,
        "right": right,
        "bottom": bottom,
        "width": right - left,
        "height": bottom - top,
    }


def _atomic_save_png(image: Image.Image, output: Path, overwrite: bool) -> None:
    temporary: Path | None = None
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.exists() and not overwrite:
            raise ValidationFailure(f"Output already exists: {output}")
        with tempfile.NamedTemporaryFile(
            prefix=f".{output.stem}.", suffix=".tmp", dir=output.parent, delete=False
        ) as handle:
            temporary = Path(handle.name)
        image.save(temporary, format="PNG")
        if overwrite:
            os.replace(temporary, output)
        else:
            # The temporary file lives in the destination directory, so a hard link
            # provides an atomic create-if-absent operation on the Windows/NTFS MVP.
            os.link(temporary, output)
            temporary.unlink()
    except ValidationFailure:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        raise
    except OSError as exc:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        raise FileFailure(f"Unable to write output '{output}': {exc}") from exc


def _success_payload(
    input_path: Path,
    output_path: Path,
    model: str,
    result: LayoutResult,
    elapsed_ms: int,
) -> dict[str, Any]:
    canvas_width, canvas_height = result.image.size
    bbox = result.subject_bbox
    occupancy = {
        "width": round((bbox[2] - bbox[0]) / canvas_width, 6),
        "height": round((bbox[3] - bbox[1]) / canvas_height, 6),
    }
    warnings: list[str] = []
    if result.upscaled:
        warnings.append("upscaled")
    return {
        "status": "success",
        "inputPath": str(input_path),
        "outputPath": str(output_path),
        "model": model,
        "canvas": {"width": canvas_width, "height": canvas_height},
        "sourceSubjectBbox": _bbox_json(result.source_bbox),
        "subjectBbox": _bbox_json(result.subject_bbox),
        "subjectOccupancy": occupancy,
        "scaleFactor": round(result.scale_factor, 8),
        "elapsedMs": elapsed_ms,
        "warnings": warnings,
    }


def _emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), flush=True)


def main(argv: Sequence[str] | None = None, backend: Backend | None = None) -> int:
    started = time.perf_counter()
    try:
        args = build_parser().parse_args(argv)
        _validate_modes(args)
        input_path = Path(args.input).expanduser().resolve(strict=False)
        if not input_path.is_file():
            raise FileFailure(f"Input file does not exist: {input_path}")
        output_path = _output_path(input_path, args.output)
        if output_path.exists() and not args.overwrite:
            raise ValidationFailure(f"Output already exists: {output_path}")
        try:
            with Image.open(input_path) as opened:
                source = ImageOps.exif_transpose(opened).convert("RGB")
        except (UnidentifiedImageError, OSError) as exc:
            raise FileFailure(f"Unable to read input '{input_path}': {exc}") from exc

        active_backend = backend or RembgBackend()
        cutout = active_backend.remove_background(source, args.model)
        if args.aspect_ratio is not None:
            result = layout_aspect_ratio(
                cutout,
                parse_aspect_ratio(args.aspect_ratio),
                args.subject_scale,
                args.alpha_threshold,
            )
        else:
            result = layout_exact_size(
                cutout,
                args.width,
                args.height,
                args.subject_scale,
                args.alpha_threshold,
            )
        _atomic_save_png(result.image, output_path, args.overwrite)
        _emit(
            _success_payload(
                input_path,
                output_path,
                args.model,
                result,
                round((time.perf_counter() - started) * 1000),
            )
        )
        return 0
    except ProcessingError as exc:
        _emit(
            {
                "status": "error",
                "code": exc.error_code,
                "message": str(exc),
                "elapsedMs": round((time.perf_counter() - started) * 1000),
            }
        )
        return exc.exit_code
    except Exception as exc:
        failure = InferenceFailure(f"Unexpected processing failure: {exc}")
        print(f"Unexpected failure: {exc}", file=sys.stderr)
        _emit(
            {
                "status": "error",
                "code": failure.error_code,
                "message": str(failure),
                "elapsedMs": round((time.perf_counter() - started) * 1000),
            }
        )
        return failure.exit_code
