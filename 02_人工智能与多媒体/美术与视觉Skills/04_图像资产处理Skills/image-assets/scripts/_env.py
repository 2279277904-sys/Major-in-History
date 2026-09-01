#!/usr/bin/env python3
"""跨平台运行环境自举：Python venv 与 Node/npm 依赖，供各命令入口复用。

只负责准备依赖、返回可执行文件路径，不做业务逻辑；Windows/macOS/Linux 通用。
"""
import shutil
import subprocess
import sys
import urllib.request
import venv
from pathlib import Path

GET_PIP_URL = "https://bootstrap.pypa.io/get-pip.py"

SKILL_DIR = Path(__file__).resolve().parent.parent


def log(message: str) -> None:
    print(f"[图片素材] {message}", file=sys.stderr, flush=True)


def venv_python(venv_dir: Path) -> Path:
    """按平台返回 venv 内 python 可执行文件路径。"""
    if sys.platform == "win32":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def _bootstrap_pip_via_get_pip(python_bin: Path) -> None:
    """当系统 Python 缺少 ensurepip（常见于精简版 Debian/Ubuntu）时，手动引导 pip。"""
    get_pip_path = python_bin.parent / "get-pip.py"
    log("系统 Python 缺少 ensurepip，尝试下载 get-pip.py 手动安装 pip")
    urllib.request.urlretrieve(GET_PIP_URL, get_pip_path)
    try:
        subprocess.run([str(python_bin), str(get_pip_path)], check=True, stdout=subprocess.DEVNULL)
    finally:
        get_pip_path.unlink(missing_ok=True)


def ensure_python_venv(venv_dir: Path, probe_code: str, pip_packages: list[str]) -> Path:
    """确保存在带指定依赖的隔离 venv，返回 venv 内 python 路径。"""
    python_bin = venv_python(venv_dir)
    if not python_bin.exists():
        log(f"创建隔离 Python 环境: {venv_dir}")
        # 故意用 with_pip=False 自己建：venv.EnvBuilder(with_pip=True) 在 ensurepip
        # 缺失时会直接 sys.exit(1)（SystemExit 不是 Exception 子类，try/except 也挡不住），
        # 自己控制 pip 引导步骤才能在这种环境下继续走兜底逻辑。
        venv.EnvBuilder(with_pip=False).create(venv_dir)
        pip_check = subprocess.run(
            [str(python_bin), "-m", "pip", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if pip_check.returncode != 0:
            ensurepip_result = subprocess.run(
                [str(python_bin), "-Im", "ensurepip", "--upgrade"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if ensurepip_result.returncode != 0:
                # 常见根因：系统 Python 缺少 ensurepip（Debian/Ubuntu 上表现为
                # "python3-venv" 包只装了一半，完整装法是 `sudo apt install python3-venv`）。
                log("系统 Python 缺少 ensurepip，改用 get-pip.py 兜底安装 pip")
                _bootstrap_pip_via_get_pip(python_bin)

    probe = subprocess.run(
        [str(python_bin), "-c", probe_code],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if probe.returncode == 0:
        log("依赖已存在，跳过安装")
    else:
        log("安装 Python 图片依赖")
        subprocess.run(
            [str(python_bin), "-m", "pip", "install", "--upgrade", "pip"],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            [str(python_bin), "-m", "pip", "install", *pip_packages],
            check=True,
            stdout=subprocess.DEVNULL,
        )
    return python_bin


def npm_binary() -> str:
    """定位 npm 可执行文件；Windows 上 shutil.which 会按 PATHEXT 自动解析到 npm.cmd。"""
    npm = shutil.which("npm")
    if not npm:
        raise RuntimeError("未找到 npm，请先安装 Node.js（https://nodejs.org）后重试。")
    return npm


def node_binary() -> str:
    node = shutil.which("node")
    if not node:
        raise RuntimeError("未找到 node，请先安装 Node.js（https://nodejs.org）后重试。")
    return node


def ensure_node_deps(node_deps_dir: Path) -> Path:
    """确保 sharp 已安装到隔离目录，返回 sharp 模块目录路径。"""
    sharp_dir = node_deps_dir / "node_modules" / "sharp"
    if sharp_dir.exists():
        log("Node 图片依赖已存在，跳过安装")
        return sharp_dir

    log(f"安装 sharp/libvips 依赖: {node_deps_dir}")
    node_deps_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [npm_binary(), "--prefix", str(node_deps_dir), "install", "sharp@latest"],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    return sharp_dir
