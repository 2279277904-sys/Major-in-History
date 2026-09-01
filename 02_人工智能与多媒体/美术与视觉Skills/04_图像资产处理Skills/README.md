# image-skills

Open-source, agent-ready skills for a reliable image workflow: generate or edit source visuals first, then turn them into validated production assets deterministically.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-5A67D8?logo=anthropic&logoColor=white)](https://claude.ai/code)

**Languages:** [English](#english) | [中文](#中文)

---

<a id="english"></a>
## English

### Why this exists

Image generation and image delivery are different jobs. A generative model is excellent at creating a character, scene, or background plate, but it is not a deterministic compositor: it may skip turntable angles, redraw a static background per frame, or shift a character between frames. `image-skills` keeps the asset-production stage reproducible and testable.

### Included skills

#### `image-assets` — Deterministic image asset processing

Prepare final image assets: background removal, transparent PNG cutouts, resize/compression/format conversion, icon variants, sprite-sheet splitting, alignment, and GIF encoding with visual QA.

For a combined workflow, use an image-generation tool to create or edit the source visual, then use `image-assets` for the final output. The repository intentionally does not redistribute Codex's bundled `imagegen` system skill.

### Quick install

```bash
git clone https://github.com/x0c/image-skills.git ~/.claude/skills/image-skills
cp -r ~/.claude/skills/image-skills/image-assets ~/.claude/skills/
```

Restart your agent client. Each skill entry point is its `SKILL.md`.

### Repository layout

```text
image-assets/
├── SKILL.md
├── agents/
├── references/
├── scripts/
└── tests/
```

### License

MIT

---

<a id="中文"></a>
## 中文

### 为什么需要它

图像生成与最终素材交付是两件事。生成模型适合产出角色、场景和背景底板，却无法可靠承担确定性合成：它可能漏掉转台角度、在每帧重绘静态背景，或让角色帧间偏移。`image-skills` 将最终资产处理收敛为可复现、可验收的流程。

### 已收录 Skill

#### `image-assets` — 确定性图像资产处理

用于最终资产的抠图、透明 PNG、缩放、压缩与格式转换、图标多尺寸派生、精灵表切帧、帧对齐和 GIF 编码验收。

涉及生成与交付时，先用图像生成工具产出或编辑源素材，再用 `image-assets` 完成最终资产。仓库不会重新分发 Codex 内置的 `imagegen` system Skill。

### 快速安装

```bash
git clone https://github.com/x0c/image-skills.git ~/.claude/skills/image-skills
cp -r ~/.claude/skills/image-skills/image-assets ~/.claude/skills/
```

重启 Agent 客户端即可；每个 Skill 的入口是其 `SKILL.md`。

### 目录结构

```text
image-assets/
├── SKILL.md
├── agents/
├── references/
├── scripts/
└── tests/
```

### 协议

MIT
