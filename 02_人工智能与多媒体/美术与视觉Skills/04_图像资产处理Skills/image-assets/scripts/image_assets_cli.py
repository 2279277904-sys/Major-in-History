#!/usr/bin/env python3
"""图片素材处理统一入口，跨平台（Windows/macOS/Linux）。

替代原先的 image-assets.sh / cutout.sh / compare_cutouts.sh 三个 bash 脚本，
按子命令自动准备 Python venv（抠图/对比模型依赖）或 Node 依赖（sharp/libvips），
再转发给对应实现脚本。
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from _env import SKILL_DIR, ensure_node_deps, ensure_python_venv, log, node_binary

CUTOUT_PROBE = (
    "import einops\n"
    "import kornia\n"
    "import numpy\n"
    "import PIL\n"
    "import timm\n"
    "import torch\n"
    "import torchvision\n"
    "import transformers\n"
    "from transformers import AutoModelForImageSegmentation\n"
)
CUTOUT_PIP_PACKAGES = [
    "pillow",
    "numpy",
    "torch",
    "torchvision",
    "transformers",
    "timm",
    "einops",
    "kornia",
    "huggingface_hub",
    "safetensors",
    "accelerate",
]
COMPARE_PROBE = "import PIL\n"
COMPARE_PIP_PACKAGES = ["pillow"]
GRID_GIF_PROBE = (
    "import sys\n"
    "import numpy\n"
    "import PIL\n"
    "pillow_version = '12.3.0' if sys.version_info >= (3, 14) else '11.3.0'\n"
    "numpy_version = ('2.4.6' if sys.version_info >= (3, 14) "
    "else '2.3.5' if sys.version_info >= (3, 13) else '2.0.2')\n"
    "assert PIL.__version__ == pillow_version\n"
    "assert numpy.__version__ == numpy_version\n"
)
GRID_GIF_PIP_PACKAGES = [
    "pillow==11.3.0; python_version < '3.14'",
    "pillow==12.3.0; python_version >= '3.14'",
    "numpy==2.0.2; python_version < '3.13'",
    "numpy==2.3.5; python_version >= '3.13' and python_version < '3.14'",
    "numpy==2.4.6; python_version >= '3.14'",
]

NODE_COMMANDS = {"resize", "optimize", "pipeline", "app-icons", "web-optimized"}


def usage() -> None:
    print(
        """用法:
  image_assets_cli.py app-assets --input DIR --output DIR [--model rmbg2] [--background-mode auto] [--background-color '#RRGGBB'] [--sizes 512,1024,2048] [--quality 92] [--png-lossy]
  image_assets_cli.py app-transparent --input DIR --output DIR [--model rmbg2] [--background-mode auto] [--background-color '#RRGGBB']
  image_assets_cli.py cutout --input DIR --output DIR [--model rmbg2] [--background-mode auto] [--background-color '#RRGGBB']
  image_assets_cli.py app-icons --input DIR --output DIR [--sizes 256,512,1024]
  image_assets_cli.py resize --input DIR --output DIR --width 1024 [--format png]
  image_assets_cli.py optimize --input DIR --output DIR --format webp [--quality 90]
  image_assets_cli.py web-optimized --input DIR --output DIR [--max-width 2048] [--formats webp,avif,jpeg] [--quality 88]
  image_assets_cli.py pipeline --input DIR --output DIR --sizes 512,1024 --formats png,webp
  image_assets_cli.py grid-gif --input FILE --output FILE.gif (--grid 4x4 | --frames 16) [--cutout-mode color] [--duration 120] [--playback forward|ping-pong] [--anchor feet] [--keep-frames]
  image_assets_cli.py compare --left DIR --right DIR --output FILE [--left-label A] [--right-label B]""",
        file=sys.stderr,
    )


def take_flag_value(args: list[str], flag: str) -> str | None:
    for i, token in enumerate(args):
        if token == flag and i + 1 < len(args):
            return args[i + 1]
    return None


def filter_out(args: list[str], flags_with_value: set[str], flags_bool: set[str]) -> list[str]:
    result: list[str] = []
    i = 0
    while i < len(args):
        token = args[i]
        if token in flags_with_value:
            i += 2
            continue
        if token in flags_bool:
            i += 1
            continue
        result.append(token)
        i += 1
    return result


def venv_dir() -> Path:
    return Path(os.environ.get("IMAGE_ASSETS_VENV") or os.environ.get("CUTOUT_VENV") or (SKILL_DIR / ".venv"))


def node_deps_dir() -> Path:
    return Path(os.environ.get("IMAGE_ASSETS_NODE_DEPS") or (SKILL_DIR / ".node-deps"))


def run_cutout(args: list[str]) -> int:
    python_bin = ensure_python_venv(venv_dir(), CUTOUT_PROBE, CUTOUT_PIP_PACKAGES)
    cmd = [str(python_bin), str(SKILL_DIR / "scripts" / "cutout_images.py"), *args]
    return subprocess.run(cmd).returncode


def run_compare(args: list[str]) -> int:
    python_bin = ensure_python_venv(venv_dir(), COMPARE_PROBE, COMPARE_PIP_PACKAGES)
    cmd = [str(python_bin), str(SKILL_DIR / "scripts" / "compare_cutouts.py"), *args]
    return subprocess.run(cmd).returncode


def run_grid_gif(args: list[str]) -> int:
    cutout_mode = take_flag_value(args, "--cutout-mode") or "color"
    if cutout_mode in {"rmbg2", "birefnet"}:
        python_bin = ensure_python_venv(venv_dir(), CUTOUT_PROBE, CUTOUT_PIP_PACKAGES)
    else:
        python_bin = ensure_python_venv(venv_dir(), GRID_GIF_PROBE, GRID_GIF_PIP_PACKAGES)
    cmd = [str(python_bin), str(SKILL_DIR / "scripts" / "grid_gif.py"), *args]
    return subprocess.run(cmd).returncode


def run_node(command: str, args: list[str]) -> int:
    sharp_dir = ensure_node_deps(node_deps_dir())
    env = os.environ.copy()
    env["SHARP_MODULE_PATH"] = str(sharp_dir)
    cmd = [node_binary(), str(SKILL_DIR / "scripts" / "image_assets.mjs"), command, *args]
    return subprocess.run(cmd, env=env).returncode


def run_app_assets(args: list[str]) -> int:
    input_value = take_flag_value(args, "--input")
    output_value = take_flag_value(args, "--output")
    model = take_flag_value(args, "--model") or os.environ.get("IMAGE_ASSETS_CUTOUT_MODEL", "rmbg2")
    sizes = take_flag_value(args, "--sizes") or "512,1024,2048"
    formats = take_flag_value(args, "--formats") or "png,webp"
    quality = take_flag_value(args, "--quality") or "92"
    png_lossy = "--png-lossy" in args

    if not input_value or not output_value:
        log("app-assets 必须传 --input 和 --output")
        return 2

    output_dir = Path(output_value)
    cutout_dir = output_dir / f"cutout-{model}"
    variant_dir = output_dir / "variants"

    log(f"第一步：抠图输出到 {cutout_dir}")
    rest_args = filter_out(
        args,
        {"--input", "--output", "--sizes", "--quality", "--formats", "--model"},
        {"--png-lossy"},
    )
    cutout_rc = run_cutout(["--input", input_value, "--output", str(cutout_dir), "--model", model, *rest_args])
    if cutout_rc != 0:
        return cutout_rc

    log("第二步：生成 APP 派生尺寸和压缩格式")
    pipeline_args = [
        "--input", str(cutout_dir),
        "--output", str(variant_dir),
        "--sizes", sizes,
        "--formats", formats,
        "--quality", quality,
        "--transparent",
    ]
    if png_lossy:
        pipeline_args.append("--png-lossy")
    return run_node("pipeline", pipeline_args)


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help", "help"):
        usage()
        return 0 if argv else 2

    command, *rest = argv

    if command == "cutout":
        return run_cutout(rest)
    if command == "app-transparent":
        model = os.environ.get("IMAGE_ASSETS_CUTOUT_MODEL", "rmbg2")
        return run_cutout(["--model", model, *rest])
    if command == "app-assets":
        return run_app_assets(rest)
    if command == "compare":
        return run_compare(rest)
    if command == "grid-gif":
        return run_grid_gif(rest)
    if command in NODE_COMMANDS:
        return run_node(command, rest)

    log(f"未知命令: {command}")
    usage()
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        log("用户中断。")
        raise SystemExit(130)
    except Exception as exc:  # noqa: BLE001 - 顶层入口需要把任意失败转成可读日志
        log(f"失败: {exc}")
        raise SystemExit(1)
