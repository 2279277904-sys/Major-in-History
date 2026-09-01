from __future__ import annotations

import json

import pytest
from PIL import Image, ImageDraw

from image_processing.cli import main
from image_processing.errors import InferenceFailure


class FakeBackend:
    def remove_background(self, image, model_name):
        result = Image.new("RGBA", image.size, (0, 0, 0, 0))
        ImageDraw.Draw(result).rectangle(
            (2, 2, image.width - 3, image.height - 3), fill="red"
        )
        return result


def write_input(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (20, 30), "white").save(path)


def payload(capsys):
    return json.loads(capsys.readouterr().out)


@pytest.mark.parametrize(
    "args",
    [
        ["--input", "x.png", "--width", "100"],
        [
            "--input",
            "x.png",
            "--width",
            "100",
            "--height",
            "100",
            "--aspect-ratio",
            "1:1",
        ],
        ["--input", "x.png"],
    ],
)
def test_modes_are_mutually_exclusive(args, capsys):
    assert main(args, FakeBackend()) == 2
    assert payload(capsys)["status"] == "error"


def test_default_name_json_schema_and_chinese_space_path(tmp_path, capsys):
    source = tmp_path / "中文 文件" / "商品 图.jpg"
    write_input(source)
    assert (
        main(
            ["--input", str(source), "--width", "100", "--height", "120"],
            FakeBackend(),
        )
        == 0
    )
    data = payload(capsys)
    output = source.with_name("商品 图.processed.png")
    assert output.is_file()
    assert data["status"] == "success"
    assert data["model"] == "birefnet-general"
    assert data["canvas"] == {"width": 100, "height": 120}
    assert set(data) >= {
        "inputPath",
        "outputPath",
        "subjectBbox",
        "subjectOccupancy",
        "elapsedMs",
        "warnings",
    }


def test_existing_output_is_not_overwritten(tmp_path, capsys):
    source = tmp_path / "input.png"
    output = tmp_path / "result.png"
    write_input(source)
    output.write_bytes(b"keep")
    assert (
        main(
            [
                "--input",
                str(source),
                "--output",
                str(output),
                "--aspect-ratio",
                "3:4",
            ],
            FakeBackend(),
        )
        == 2
    )
    assert output.read_bytes() == b"keep"
    assert payload(capsys)["code"] == "validation_error"


def test_model_allowlist_rejects_bria_before_reading_file(capsys):
    assert (
        main(
            [
                "--input",
                "missing.png",
                "--aspect-ratio",
                "1:1",
                "--model",
                "bria-rmbg",
            ],
            FakeBackend(),
        )
        == 2
    )
    assert "Unsupported model" in payload(capsys)["message"]


def test_missing_input_uses_file_exit_code(capsys):
    assert main(["--input", "missing.png", "--aspect-ratio", "1:1"], FakeBackend()) == 5
    assert payload(capsys)["code"] == "file_error"


def test_inference_failure_uses_exit_code_four(tmp_path, capsys):
    source = tmp_path / "input.png"
    write_input(source)

    class BrokenBackend:
        def remove_background(self, image, model_name):
            raise InferenceFailure("boom")

    assert (
        main(["--input", str(source), "--aspect-ratio", "1:1"], BrokenBackend())
        == 4
    )
    assert payload(capsys)["code"] == "inference_error"
