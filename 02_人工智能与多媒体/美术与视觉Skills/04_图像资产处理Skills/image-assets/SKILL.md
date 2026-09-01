---
name: image-assets
description: "Prepare image assets. Use for background removal, transparent PNGs, resizing, compression, format conversion, multi-size variants, splitting N-grid sprite sheets into frames, generating transparent animated GIFs, cutout model comparison, or fixing image-processing toolchains."
---

# Image Assets

## 与 imagegen 的边界

- `imagegen` 只负责生成或编辑视觉源素材，例如角色、背景底板或参考图变体；它不负责可复现的帧处理和交付编码。
- `image-assets` 负责将已有源素材确定性地抠图、合成、切帧、对齐、转码、编码和验收，输出最终 PNG/WebP/AVIF/JPEG/GIF 等资产。
- 同时涉及两者时，固定顺序为：`imagegen` 生成/编辑源素材 → `image-assets` 处理和验收最终资产。不要让生成模型直接代替严格角度分帧、统一锚点或 GIF 编码。

## 核心判断

- 最终 APP 素材抠图优先用 `rmbg2` (`briaai/RMBG-2.0`)；无授权或要对比时用 `birefnet`。
- 默认使用 `--background-mode auto` 从四角识别白色或其他均匀纯色背景，自动去除对应色边，并用 `--shadow-mode auto` 恢复主体附近被分割模型忽略的渐变投影。
- 复杂背景只使用模型分割结果，不自动反推边缘颜色。已知背景色时用 `--background-color '#RRGGBB'`；需要完全关闭背景色后处理时用 `--background-mode off --shadow-mode off`。
- 尺寸修改、WebP/AVIF/JPEG/PNG 转码压缩优先走 `sharp/libvips`，缩放默认 Lanczos3。
- 默认压缩以保留色彩和细节为先：`optimize` 默认质量 90，APP 派生图默认质量 92，`web-optimized` 默认质量 88；JPEG 使用 `4:4:4` 色度抽样。
- 透明主资产保留 PNG；分发或包体优化再生成 WebP/AVIF/JPEG 派生版本。
- N 宫格像素素材生成动画时优先用 `grid-gif --cutout-mode color`：自动识别分隔线，按边缘连通区域去除纯色背景，避免模型破坏像素轮廓。复杂背景再切 `rmbg2` 或 `birefnet`。
- 处理 N 宫格 GIF，或排查动画抖动、主体透明洞、分隔线残留、换底和播放顺序问题前，读取 `references/sprite-sheet-gif.md`；其中记录完整流水线、验收清单和已否决方案。
- 固定角度旋转（转台、口型/眼睛为轴的旋转 GIF）必须由图像处理按几何关系合成：先得到单张透明主体，锁定源图枢轴，再生成 `0°、360/N° ... (N-1)*360/N°` 共 `N` 帧；每帧的枢轴坐标和画布尺寸必须相同。不得让生成模型直接产出 N 宫格充当精确角度帧。
- 纯色键控主体的键色不得与主体主色接近。绿色叶片等绿色主体用 `#ff00ff`，不使用绿幕；出现去边色导致的褪色时，先禁用去溢色处理并重新检查棋盘格预览，再调整阈值。
- 深色背景搭配深色主体时使用保守换底：默认容差 12，只把边缘连通的背景替换成唯一洋红键色后精确设透明。不要直接把容差提高到 20 以上，否则黑色衣裤可能被一并删除。
- GIF 各帧必须保留统一画布，并默认用 `--anchor feet` 将脚部中心与最低接地点对齐；锚点检测先过滤孤立边缘噪点，再只取前景底部 8%，避免尾巴或衣摆污染横向坐标。不要逐帧独立紧裁。像素画放大使用整数 `--scale` 和最近邻缩放，避免动画抖动或像素发糊。
- 连续动作默认 `--playback forward`，播放为 `12341234...`；起止姿势需要平滑往返时用 `--playback ping-pong`，播放为 `1234321...`，首尾端点不会重复编码导致停顿。
- 日常优先用 preset，只有用户明确要控制模型、尺寸、质量、格式时再展开高级参数。
- 用户不知道应该使用什么尺寸、格式、质量，或图片将用于 iOS、iPadOS、macOS 原生应用时，先读取 `references/apple-native-assets.md`，根据目标平台、显示点值和资产类型选择方案，再执行处理。
- 从彩色 App Icon 派生 macOS 菜单栏 / 状态栏图标时，先读 `references/apple-native-assets.md` 的「从彩色 App Icon 提炼菜单栏模板图标」；默认提炼语义轮廓并重绘透明单色资产，不把整张彩色图机械阈值化。

## 常用命令

一键生成 APP 资产：先抠图，再输出常用尺寸 PNG/WebP。

```bash
python <skill-dir>/scripts/image_assets_cli.py app-assets \
  --input /path/to/images \
  --output /path/to/assets
```

默认 PNG 派生图只做无损 `oxipng`；需要更小体积且能接受轻微有损时加 `--png-lossy`，文件名会出现 `pnglossy-qXX`，实际是否调用 `pngquant` 以 `manifest.json` 为准。

只抠图，输出透明 PNG：

```bash
python <skill-dir>/scripts/image_assets_cli.py app-transparent \
  --input /path/to/images \
  --output /path/to/cutouts
```

把 4×4 像素素材切成 16 帧、抠图并生成透明 GIF：

```bash
python <skill-dir>/scripts/image_assets_cli.py grid-gif \
  --input /path/to/sprite-sheet.png \
  --output /path/to/animation.gif \
  --grid 4x4 \
  --duration 120 \
  --playback ping-pong \
  --anchor feet \
  --keep-frames
```

不知道行列、只知道总帧数时用 `--frames 16` 自动推断；`--grid` 的格式是“列数x行数”。默认按行从左到右读取，可用 `--order column-major` 改为按列读取。动作需要来回衔接时使用 `--playback ping-pong`。纯色背景默认走 `color`；复杂背景可用 `--cutout-mode rmbg2` 或 `--cutout-mode birefnet`。角色没有脚或脚部变化过大时，依次尝试 `--anchor bottom-center`、`--anchor center`；只有需要完全保留格子原始位置时才用 `--anchor cell`。

彩色纯色背景会被自动识别。自动识别失败或需要精确指定时：

```bash
python <skill-dir>/scripts/image_assets_cli.py app-transparent \
  --input /path/to/images \
  --output /path/to/cutouts \
  --background-color '#36C5F0'
```

复杂背景不应做纯色反推：

```bash
python <skill-dir>/scripts/image_assets_cli.py app-transparent \
  --input /path/to/images \
  --output /path/to/cutouts \
  --background-mode off \
  --shadow-mode off
```

从已透明图片生成图标多尺寸：

```bash
python <skill-dir>/scripts/image_assets_cli.py app-icons \
  --input /path/to/cutouts \
  --output /path/to/icons
```

网站/包体优化：

```bash
python <skill-dir>/scripts/image_assets_cli.py web-optimized \
  --input /path/to/images \
  --output /path/to/web-assets
```

`web-optimized` 是保守压缩 preset，默认 `quality 88`。只有明确接受颜色渐变、细线和纹理损失时才降低到 `quality 85` 以下，并在交付前做原图对比。

高级抠图对比时显式切模型：

```bash
python <skill-dir>/scripts/image_assets_cli.py cutout \
  --input /path/to/images \
  --output /path/to/cutouts-rmbg2 \
  --model rmbg2
```

```bash
python <skill-dir>/scripts/image_assets_cli.py cutout \
  --input /path/to/images \
  --output /path/to/cutouts-birefnet \
  --model birefnet
```

精确改分辨率或格式：

```bash
python <skill-dir>/scripts/image_assets_cli.py resize \
  --input /path/to/images \
  --output /path/to/resized \
  --width 1024 \
  --format png
```

```bash
python <skill-dir>/scripts/image_assets_cli.py optimize \
  --input /path/to/images \
  --output /path/to/optimized \
  --format webp \
  --quality 90
```

## 输出命名

必须显式传 `--output`；脚本不设置默认输出目录。

输出文件名自动写入关键处理参数，规则是：

```text
<原名>_<处理步骤>_<关键参数>.<格式>
```

示例：

- `icon_cutout-rmbg2.png`
- `chair_cutout-rmbg2-shadow.png`
- `icon_cutout-rmbg2_asset_w512.webp`
- `banner_resize_w1920_jpg-q88.jpg`
- `photo_pipe_w2048_avif-q82.avif`
- `animation.gif` 与同目录的 `animation.manifest.json`

只记录影响结果的关键参数：抠图模型、尺寸、输出格式、质量、是否走 PNG 有损量化。每个输出目录都会生成 `manifest.json`，记录源文件、输出文件、尺寸、格式、质量、模型、实际优化工具和文件大小变化。

## Token 和授权

使用 RMBG-2.0 时不要索要账号密码，不要把 token 写进脚本、Markdown、git commit 或输出路径。使用以下任一方式：

- `HF_TOKEN=<read-token> python <skill-dir>/scripts/image_assets_cli.py app-transparent ...`
- 先运行 `huggingface-cli login`
- 模型已缓存时给抠图命令加 `--local-files-only`

用户在聊天里给过临时 Hugging Face token 时，完成后提醒 revoke。

## 质量检查

- 抠图后必须检查 `preview_dark.png` 和 `preview_checker.png`，尤其留意彩色背景造成的边缘染色。
- 透明 PNG 应为 `RGBA`，四角 alpha 应为 0。
- 检查 `manifest.json` 中每张图的 `background_color`、`background_detected` 和 `decontaminate_background`；自动背景色不可靠时显式传 `--background-color` 或关闭背景后处理。
- 压缩/改尺寸后检查 `manifest.json`，确认输出尺寸、格式、体积变化符合预期。
- 有损压缩必须抽查高饱和色边缘、渐变、细线、文字和暗部纹理；质量低于 85 时必须与原图并排检查。
- `grid-gif` 后必须目视检查自动生成的棋盘格 `*_alignment.png` 和从最终 GIF 解码得到的 `*_checker.gif`：前者的红线应稳定穿过横向锚点、绿线应稳定落在脚底，后者不应在主体内出现棋盘格透明洞。不能只用同一锚点算法或中间 PNG 自证。另检查 GIF 帧数、帧时长、循环次数、四角透明度和分隔线残留；加 `--keep-frames` 时抽查逐帧 PNG。
- 质量敏感时生成对比图：

```bash
python <skill-dir>/scripts/image_assets_cli.py compare \
  --left /path/to/birefnet-output \
  --right /path/to/rmbg2-output \
  --output /path/to/model-comparison.png \
  --left-label BiRefNet \
  --right-label RMBG-2.0
```

## 环境恢复

只有在环境安装失败、换电脑恢复、需要解释模型/授权/压缩工具行为时，读取 `references/environment.md`。

## 决策参考

- 处理或排查 N 宫格切帧、抠图、锚点对齐、透明 GIF 编码时，读取 `references/sprite-sheet-gif.md`。
- 用户不知道如何压缩、调整分辨率、选择格式，或需要 Apple 原生应用资产交付建议时，读取 `references/apple-native-assets.md`。
- 该参考文档包含 `pt × scale` 换算、iPhone/iPad/macOS 建议尺寸、格式与压缩决策、Asset Catalog 交付规则、性能和可访问性注意事项。
