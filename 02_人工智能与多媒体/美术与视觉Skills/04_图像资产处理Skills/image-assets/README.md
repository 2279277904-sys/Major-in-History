# image-assets

> A **Claude Code** / **Codex CLI** skill for preparing image assets: background removal, N-grid sprite-sheet to transparent GIF animation, resizing, WebP/AVIF/JPEG/PNG compression, multi-size app icon generation, and cutout-model comparison — all cross-platform (Windows/macOS/Linux) via a single Python entry point.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-5A67D8?logo=anthropic&logoColor=white)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Skill-10A37F?logo=openai&logoColor=white)](https://github.com/openai/codex)

**Languages:** [English](#english) | [中文](#中文)

---

<a id="english"></a>
## English

### What it does

- **Background removal / transparent PNG cutouts** using `BRIA RMBG-2.0` (default, high quality) or `ZhengPeng7/BiRefNet` (open, no gated access needed). Automatically detects uniform solid backgrounds and recovers soft drop shadows the segmentation model would otherwise discard.
- **Resize, compress, and convert** to WebP/AVIF/JPEG/PNG via `sharp`/`libvips` (Lanczos3 scaling, 4:4:4 chroma subsampling for JPEG).
- **One-shot app asset pipeline**: cutout + multi-size PNG/WebP variants in a single command.
- **N-grid sprite-sheet animation**: detect separators, split frames, remove solid-color or model-segmented backgrounds, and generate a transparent GIF with a manifest.
- **App icon multi-size generation** and a **web/bundle-size optimization** preset.
- **Side-by-side comparison images** between cutout models.
- Every run writes a `manifest.json` recording inputs, outputs, dimensions, format, quality, and model used.

### Prerequisites

- **Python 3** on PATH is enough for solid-color `grid-gif`; the first run creates an isolated `.venv/` and installs only `Pillow` and `NumPy`.
- **Node.js** is needed only for resize/compression/conversion commands; they auto-install `sharp` into `.node-deps/`.
- Model cutouts (`rmbg2` or `birefnet`) additionally auto-install `torch`, `transformers`, and related packages into `.venv/` (several hundred MB). These dependency directories are one-time, local to the skill, and gitignored.
- **Model license note**: `RMBG-2.0` is free for non-commercial use only (commercial use requires a paid license from BRIA — see the [model page](https://huggingface.co/briaai/RMBG-2.0)); `BiRefNet` is fully open and free for any use, including commercial.
- `RMBG-2.0` is a gated Hugging Face model — request access on its model page, then provide a token via `HF_TOKEN=<token>` or `huggingface-cli login`. Never commit a token to a script or repo.

### Quick Install

**Claude Code:**

```bash
git clone https://github.com/x0c/image-assets-skill.git ~/.claude/skills/image-assets
```

**Codex CLI:**

```bash
git clone https://github.com/x0c/image-assets-skill.git ~/.codex/skills/image-assets
```

Restart your agent. The entry point is `SKILL.md`; `agents/openai.yaml` provides the Codex-specific interface metadata.

### Usage

One-shot app asset pipeline (cutout + multi-size PNG/WebP):

```bash
python scripts/image_assets_cli.py app-assets \
  --input /path/to/images \
  --output /path/to/assets
```

Transparent cutout only:

```bash
python scripts/image_assets_cli.py app-transparent \
  --input /path/to/images \
  --output /path/to/cutouts
```

Turn a 4×4 pixel-art sprite sheet into a transparent animated GIF:

```bash
python scripts/image_assets_cli.py grid-gif \
  --input /path/to/sprite-sheet.png \
  --output /path/to/animation.gif \
  --grid 4x4 \
  --duration 120 \
  --playback ping-pong \
  --anchor feet \
  --keep-frames
```

Use `--frames 16` when only the total frame count is known. `--playback forward` produces `12341234...`; `--playback ping-pong` produces a smooth `1234321...` sequence without duplicated endpoint pauses. Frames align to the detected feet by default after isolated edge noise is filtered, preventing tails or clothing hems from corrupting horizontal alignment; use `--anchor bottom-center`, `center`, or `cell` when needed. Solid-color backgrounds use a conservative connected chroma-key replacement with tolerance 12 so dark clothing is preserved. Every run writes checkerboard `*_alignment.png` and a final decoded `*_checker.gif` for visual QA. Complex backgrounds can use `--cutout-mode rmbg2` or `--cutout-mode birefnet`.

Resize / re-encode:

```bash
python scripts/image_assets_cli.py resize --input DIR --output DIR --width 1024 --format png
python scripts/image_assets_cli.py optimize --input DIR --output DIR --format webp --quality 90
python scripts/image_assets_cli.py web-optimized --input DIR --output DIR
python scripts/image_assets_cli.py app-icons --input DIR --output DIR --sizes 256,512,1024
```

Compare two cutout models side by side:

```bash
python scripts/image_assets_cli.py compare \
  --left /path/to/birefnet-output \
  --right /path/to/rmbg2-output \
  --output /path/to/model-comparison.png \
  --left-label BiRefNet --right-label RMBG-2.0
```

Run `python scripts/image_assets_cli.py --help` for the full command list. See `SKILL.md` for the complete decision guide, `references/sprite-sheet-gif.md` for sprite-sheet animation failure modes and acceptance checks, and `references/environment.md` for environment recovery and troubleshooting.

### License

[MIT](LICENSE)

---

<a id="中文"></a>
## 中文

### 核心能力

- **背景移除 / 透明 PNG 抠图**：默认用 `BRIA RMBG-2.0`（高质量），或用开放模型 `ZhengPeng7/BiRefNet`（无需申请授权）。自动识别均匀纯色背景，并恢复分割模型容易忽略的柔和投影。
- **尺寸调整、压缩与格式转换**：基于 `sharp`/`libvips`，输出 WebP/AVIF/JPEG/PNG（Lanczos3 缩放，JPEG 用 4:4:4 色度抽样保留细节）。
- **一键 APP 素材流水线**：一条命令完成抠图 + 多尺寸 PNG/WebP 派生图。
- **N 宫格动画生成**：自动识别分隔线、切帧、去除纯色或模型分割背景，并生成带清单的透明 GIF。
- **图标多尺寸生成** 和 **网站/包体压缩预设**。
- **抠图模型并排对比图**。
- 每次运行都会生成 `manifest.json`，记录输入、输出、尺寸、格式、质量和所用模型。

### 前置条件

- 纯色背景 `grid-gif` 只要求系统 PATH 中有 **Python 3**；首次运行会创建隔离的 `.venv/`，并且只安装 `Pillow` 和 `NumPy`。
- 调整尺寸、压缩和格式转换命令才需要 **Node.js**，对应的 `sharp` 会自动安装到 `.node-deps/`。
- 使用 `rmbg2` 或 `birefnet` 模型抠图时，才会额外把 `torch`、`transformers` 等数百 MB 依赖装进 `.venv/`。这些依赖目录都只需安装一次，并已被 `.gitignore` 排除。
- **模型授权提醒**：`RMBG-2.0` 免费仅授权非商业用途，商用需要向 BRIA 购买授权（详见[模型页](https://huggingface.co/briaai/RMBG-2.0)）；`BiRefNet` 完全开放，任何用途（含商用）均可免费使用。
- `RMBG-2.0` 是 Hugging Face 上的 gated 模型，需先在模型页申请获批，再通过 `HF_TOKEN=<token>` 或 `huggingface-cli login` 提供访问凭据；不要把 token 提交进脚本或仓库。

### 快速安装

**Claude Code:**

```bash
git clone https://github.com/x0c/image-assets-skill.git ~/.claude/skills/image-assets
```

**Codex CLI:**

```bash
git clone https://github.com/x0c/image-assets-skill.git ~/.codex/skills/image-assets
```

重启 Agent 即可。入口是 `SKILL.md`；`agents/openai.yaml` 提供 Codex 侧的接口元数据。

### 用法

一键 APP 素材流水线（抠图 + 多尺寸 PNG/WebP）：

```bash
python scripts/image_assets_cli.py app-assets \
  --input /path/to/images \
  --output /path/to/assets
```

只抠图：

```bash
python scripts/image_assets_cli.py app-transparent \
  --input /path/to/images \
  --output /path/to/cutouts
```

把 4×4 像素素材生成透明 GIF：

```bash
python scripts/image_assets_cli.py grid-gif \
  --input /path/to/sprite-sheet.png \
  --output /path/to/animation.gif \
  --grid 4x4 \
  --duration 120 \
  --playback ping-pong \
  --anchor feet \
  --keep-frames
```

只知道总帧数时可用 `--frames 16` 自动推断行列。`--playback forward` 生成 `12341234...`，`--playback ping-pong` 生成平滑的 `1234321...`，且不会重复端点造成停顿。默认先过滤孤立边缘噪点，再检测脚部中心与最低接地点作为锚点，避免尾巴或衣摆污染横向坐标；也可切换为 `--anchor bottom-center`、`center` 或 `cell`。纯色背景默认使用容差 12 的保守连通换底，先替换为唯一键色再精确透明，保护深色衣裤。每次还会生成棋盘格 `*_alignment.png` 和从最终 GIF 解码的 `*_checker.gif` 用于目视验收；复杂背景可切换为 `--cutout-mode rmbg2` 或 `--cutout-mode birefnet`。

调整尺寸 / 转码：

```bash
python scripts/image_assets_cli.py resize --input DIR --output DIR --width 1024 --format png
python scripts/image_assets_cli.py optimize --input DIR --output DIR --format webp --quality 90
python scripts/image_assets_cli.py web-optimized --input DIR --output DIR
python scripts/image_assets_cli.py app-icons --input DIR --output DIR --sizes 256,512,1024
```

生成两个抠图模型的并排对比图：

```bash
python scripts/image_assets_cli.py compare \
  --left /path/to/birefnet-output \
  --right /path/to/rmbg2-output \
  --output /path/to/model-comparison.png \
  --left-label BiRefNet --right-label RMBG-2.0
```

完整命令列表见 `python scripts/image_assets_cli.py --help`；完整决策指南见 `SKILL.md`；N 宫格动画的失败模式与验收清单见 `references/sprite-sheet-gif.md`；环境恢复与故障排查见 `references/environment.md`。

### License

[MIT](LICENSE)
