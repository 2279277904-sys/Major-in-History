# Apple 原生应用图片资产决策指南

本文用于在用户不确定图片应该如何调整分辨率、选择格式、压缩或交付给 Apple 原生应用时提供决策依据。

调研基线截至 2026 年 6 月 6 日。WWDC26 尚未开始，结论基于当时已公开的 Apple Human Interface Guidelines、Xcode / Asset Catalog 文档、App Store Connect 帮助和 WWDC24–25 资料。Apple 后续可能更新平台能力；涉及新系统硬性规格时应重新核对官方文档。

## 快速结论

- 应用内图片优先放入 Xcode Asset Catalog，而不是把松散图片直接放进 bundle。
- 先按点值 `pt` 设计，再按平台倍率换算成像素 `px`。
- Apple 标准 image set 倍率是 `@1x`、`@2x`、`@3x`，没有标准 `@4x` 槽位。
- 普通矢量 UI 优先单尺度 PDF；系统图标优先 SF Symbols；自定义 Symbol 使用 SVG。
- 需要精确透明边缘的位图使用 PNG；照片、大图和内容封面优先 JPEG 或 HEIF。
- 默认使用 sRGB；只有设计、审阅和交付链路明确支持广色域时才使用 Display P3。
- 不要为了显示成几百像素的图片，让应用完整解码数千像素原图；应提前生成接近显示尺寸的派生图或在运行时下采样。

## 不确定时的决策流程

### 第一步：判断资产类型

| 资产类型 | 优先方案 | 备用方案 |
|---|---|---|
| Apple 平台通用 UI 图标 | SF Symbols | Custom Symbol |
| 品牌化自定义单色图标 | SVG 导入 Symbol Image Set | 单尺度 PDF |
| 普通矢量 UI、几何插图 | 单尺度 PDF，并保留矢量信息 | 按倍率 PNG |
| 带透明边缘、蒙版、像素级细节的位图 | PNG | WebP 仅用于明确支持的分发场景 |
| 照片、截图、内容封面、复杂大图 | JPEG 或 HEIF | PNG 仅在确实需要无损时使用 |
| App Icon | Icon Composer / Asset Catalog | 按当前 Xcode 要求交付 |
| SpriteKit 大量小贴图 | Texture Atlas | 独立图片 |

### 第二步：判断实际显示尺寸

1. 优先向用户确认图片在界面中的显示点值，例如 `24 pt` 图标、`80 pt` 缩略图。
2. 根据目标平台和设备换算像素。
3. 用户无法提供显示尺寸时：
   - 小图标按 `20–24 pt` 评估。
   - 列表缩略图按 `60–96 pt` 评估。
   - 大图按布局容器最大宽度评估，不按设备原始屏幕像素盲目导出。
4. 对照片或大图，可以保留一份高质量母版，再针对实际使用场景生成派生版本。

换算公式：

```text
像素尺寸 = 点值 × 显示倍率
```

### 第三步：判断是否允许有损压缩

- 图标、蒙版、锐利 UI 边缘、透明主资产：默认无损 PNG，并使用 `oxipng`。
- 照片、背景、内容封面、复杂插画：允许有损，优先 JPEG / HEIF；Web 分发可使用 WebP / AVIF。
- 透明 PNG 确实需要进一步缩小时：显式使用 `--png-lossy`，并人工检查边缘、渐变和颜色数量。
- 用户只说“压缩一下”但没有说明用途时：保留无损主资产，同时生成有损分发版本供对比，不覆盖原图。

## 点值与像素速查

Apple 标准倍率只使用 `@1x`、`@2x`、`@3x`。

| 点值 | @1x | @2x | @3x |
|---:|---:|---:|---:|
| 16 pt | 16 px | 32 px | 48 px |
| 18 pt | 18 px | 36 px | 54 px |
| 20 pt | 20 px | 40 px | 60 px |
| 24 pt | 24 px | 48 px | 72 px |
| 28 pt | 28 px | 56 px | 84 px |
| 32 pt | 32 px | 64 px | 96 px |
| 44 pt | 44 px | 88 px | 132 px |
| 60 pt | 60 px | 120 px | 180 px |
| 68 pt | 68 px | 136 px | 204 px |
| 80 pt | 80 px | 160 px | 240 px |
| 96 pt | 96 px | 192 px | 288 px |
| 128 pt | 128 px | 256 px | 384 px |
| 256 pt | 256 px | 512 px | 768 px |

## 平台建议

以下图标和缩略图尺寸属于工程建议，不是 Apple App Review 的统一硬性像素要求。触控命中框最小 `44 × 44 pt` 是重要的 Apple 设计基线。

### iPhone

2026 年工程交付主要关注 `@2x` 和 `@3x`，现代 iPhone 通常重点检查 `@3x`。

| 用途 | 建议点值 | @2x | @3x | 建议格式 |
|---|---:|---:|---:|---|
| 行内小图标 | 16–18 pt | 32–36 px | 48–54 px | SF Symbol / PDF |
| 导航栏、工具栏动作图标 | 20 pt | 40 px | 60 px | SF Symbol / PDF |
| 主要标签、强调动作图标 | 24 pt | 48 px | 72 px | SF Symbol / PDF |
| 大按钮强调图标 | 28 pt | 56 px | 84 px | SF Symbol / PDF |
| 最小触控命中框 | 44 pt | 88 px | 132 px | 布局约束 |
| 小缩略图 | 60 pt | 120 px | 180 px | PNG / JPEG / HEIF |
| 中缩略图、卡片图 | 80 pt | 160 px | 240 px | PNG / JPEG / HEIF |

不要把某一台 iPhone 的完整屏幕像素当作所有应用内大图的固定导出尺寸。应根据容器、裁切方式和横竖屏适配决定。

### iPad

iPad 的关键不是额外倍率，而是多窗口、分栏、Stage Manager 和外接显示器导致的可变布局。

| 用途 | 建议点值 | @2x | 建议格式 |
|---|---:|---:|---|
| 行内、工具栏图标 | 20 pt | 40 px | SF Symbol / PDF |
| 主动作图标 | 24 pt | 48 px | SF Symbol / PDF |
| 最小触控命中框 | 44 pt | 88 px | 布局约束 |
| 小缩略图 | 64 pt | 128 px | PNG / JPEG / HEIF |
| 中缩略图 | 96 pt | 192 px | PNG / JPEG / HEIF |

iPad 大图应优先保证可裁切、可重排和不同窗口宽度下的表现，不要只适配单一全屏画布。

### macOS

macOS 应考虑可变窗口、非 Retina、Retina 和外接显示器。高分屏仍然使用 `@2x` 语义，不需要额外准备 `@4x`。

| 用途 | 建议点值 | @1x | @2x | 建议格式 |
|---|---:|---:|---:|---|
| 小工具栏、侧边栏图标 | 16 pt | 16 px | 32 px | SF Symbol / PDF / NSImage 多表示 |
| 标准工具栏图标 | 20 pt | 20 px | 40 px | SF Symbol / PDF / NSImage 多表示 |
| Inspector、Canvas 图标 | 24 pt | 24 px | 48 px | SF Symbol / PDF / NSImage 多表示 |
| 小缩略图 | 64 pt | 64 px | 128 px | PNG / JPEG / HEIF |
| 中缩略图 | 96 pt | 96 px | 192 px | PNG / JPEG / HEIF |
| 大型内容 Tile | 256 pt | 256 px | 512 px | PNG / JPEG / HEIF / PDF |

普通 AppKit 位图可使用 `<name>.png` 与 `<name>@2x.png` 配对，但 Asset Catalog 仍然是优先组织方式。

## 格式与压缩策略

### PNG

适合：

- 透明主资产。
- 蒙版、锐利边缘、像素级 UI。
- 需要严格无损的图形。

默认处理：

```bash
python <skill-dir>/scripts/image_assets_cli.py resize \
  --input /path/to/images \
  --output /path/to/output \
  --width 512 \
  --format png
```

脚本默认使用 `oxipng` 做无损优化。只有能接受轻微有损时才加 `--png-lossy`。

### JPEG

适合：

- 不需要透明度的照片、截图、内容封面和背景。
- 需要广泛兼容的有损分发版本。

建议质量起点：

- 高质量母版派生：`quality 90–94`
- 常规应用内内容：`quality 88–92`
- 对体积敏感且允许轻微损失：`quality 85–87`，必须人工检查
- 对体积非常敏感且允许明显损失：低于 `85`，必须与原图并排检查

脚本输出 JPEG 时默认使用 `4:4:4` 色度抽样，避免高饱和色边缘、细线和小字号文字因色度降采样而模糊。

### HEIF

适合 Apple 原生生态中的照片和高压缩比内容图，但要确认项目链路、服务端和外部工具兼容性。当前一键脚本未默认输出 HEIF；用户明确需要时再扩展或使用平台工具。

### WebP

适合网站、跨平台分发和支持 WebP 的应用资源管线。透明图也可生成 WebP 派生版本，但不应替代 PNG 主资产。

建议质量起点：`88–92`。

### AVIF

适合对体积敏感、能接受更慢编码且运行环境明确支持的分发场景。它不应作为 Apple Asset Catalog 普通 image set 的默认交付格式。

建议质量起点：`85–90`，并与 WebP / JPEG 做肉眼对比。

### PDF 与 SVG

- 普通 Asset Catalog 矢量 UI：使用单尺度 PDF，必要时开启 `preserves-vector-representation`。
- Custom Symbol：使用 SVG 导入 Symbol Image Set。
- App Icon 分层流程：使用 Icon Composer 支持的 SVG 或 PNG 源。
- 不要默认把 SVG 当作普通 image set 的标准交付格式。

## Asset Catalog 交付规则

Asset Catalog 可根据以下维度自动选择资源：

- 平台和设备类型 `idiom`
- 显示倍率 `scale`
- Light / Dark 等外观
- sRGB / Display P3 色域
- compact / regular 尺寸类
- LTR / RTL 语言方向
- 内存档位和图形能力
- On-Demand Resources 标签
- original / template 渲染意图

工程交付时应使用语义化 asset name，通过 SwiftUI `Image("name")`、UIKit `UIImage(named:)` 或 AppKit 命名加载访问，不要让业务代码手工拼接 `@2x`、`@3x` 文件名。

注意区分：

- 应用内图片：Asset Catalog。
- 启动界面：Launch Screen storyboard，不是 launch image。
- App Store 截图：上传到 App Store Connect，不属于应用 bundle 内资源。

## 从彩色 App Icon 提炼菜单栏模板图标

macOS 菜单栏 / 状态栏图标不是彩色 App Icon 的等比缩小版。稳定做法是把原图当作语义参考，保留最能识别产品的轮廓关系，再重绘成透明底的单色模板图标。

### 提炼顺序

1. 先写出原图在极小尺寸下仍必须被认出的图形关系，例如「三层卡片 + 带凹口的收纳托盘」。
2. 删除背景色、渐变、阴影、高光、材质和颜色层级；这些信息缩到菜单栏后只会变成噪点。
3. 优先保留外轮廓、层叠关系和关键负空间。主体较复杂时用克制的单色描边，不要把所有层叠面合成一块黑色实心团。
4. 在 `16–20 pt` 区间先做母版；macOS 常用 `@1x` 与 `@2x`，例如 `18 × 18 px` 和 `36 × 36 px`。
5. 输出黑色主体 + 全透明背景的 RGBA PNG，或使用适合当前工程的单尺度 PDF / 自定义 Symbol；放入 Asset Catalog，并把渲染意图设为 `template`。
6. 由系统根据浅色、深色和选中状态着色，不在图片里写死白色 / 黑色双版本。

### 为什么不应机械抠图后阈值化

- 彩色主体可能与背景色接近，按颜色抠除会误删关键层级。
- App Icon 的阴影和高光会被阈值化成毛边、断线或额外色块。
- 直接把完整主体填黑，层叠结构会在 `18 pt` 附近糊成一团。

因此这里的「抠图 + 单色」应理解为**语义轮廓提炼**：原图负责定义身份，菜单栏资产按小尺寸重新组织线条和负空间。只有主体本身已经是边界清晰的单色几何图形时，才适合直接使用抠图蒙版。

### 验收

- 分别检查实际 `@1x` 和放大的预览，不能只看大尺寸母版。
- 四角 alpha 必须为 `0`；所有非透明像素的 RGB 应保持纯黑，明暗交给 alpha 抗锯齿。
- 在白底、深色底和棋盘格背景上检查边缘、断线、层级与关键负空间。
- 用 Asset Catalog 检查工具确认 `template` 渲染意图已进入最终包；仅在源文件里写黑色不等于系统会按模板图标处理。
- 启动正式安装位置的 App 做一次真实菜单栏验收，避免只检查编译目录里的临时产物。

## 性能与包体

- 实际内存成本取决于解码后的像素，而不仅是磁盘文件大小。
- 只显示为 `300 pt` 宽的图片，不应直接完整解码 `4000 px` 原图。
- 长列表应结合懒加载和接近显示尺寸的派生图。
- 大型插画包、教程图、离线地图、场景背景可考虑 App Thinning 和 On-Demand Resources。
- SpriteKit 大量小贴图使用 Texture Atlas；普通 SwiftUI / UIKit 表单页面不需要为了图片优化强行使用 atlas。
- UI 动画优先使用 SF Symbols effects、SwiftUI 动画或 Core Animation；不要因为高刷新率设备额外制作 `@4x` 图片。

## 色彩、透明度与可访问性

- 默认 sRGB；Display P3 只在设计、导出和审阅链路均可控时使用。
- 图像应携带正确 color profile。
- 需要跟随系统前景色的图标应使用 template image 或 symbol，不要写死成彩色 PNG。
- 至少检查 Increase Contrast、Reduce Transparency、Reduce Motion 和 Differentiate Without Color Alone。
- 动画图标应提供 Reduce Motion 替代方案。

## 使用本 skill 时的推荐动作

当用户不知道如何处理时，先说明建议，再执行：

1. 询问或推断目标平台、用途和实际显示点值。
2. 选择主资产格式，默认保留原图和无损主资产。
3. 根据 `pt × scale` 生成所需像素尺寸，不生成标准体系中不存在的 `@4x`。
4. 对照片和内容图生成压缩派生版本；对透明 UI 图保留 PNG。
5. 输出文件名记录尺寸、格式和质量，并检查 `manifest.json`。
6. 对有损版本进行肉眼对比，尤其检查透明边缘、文字、渐变、肤色和品牌色。

常见推荐：

```bash
# 已透明的 APP 图标，生成常用尺寸 PNG / WebP
python <skill-dir>/scripts/image_assets_cli.py app-icons \
  --input /path/to/cutouts \
  --output /path/to/icons \
  --sizes 48,60,72,88,96,132 \
  --formats png,webp
```

```bash
# 照片或内容大图，生成网站/分发版本
python <skill-dir>/scripts/image_assets_cli.py web-optimized \
  --input /path/to/images \
  --output /path/to/web-assets \
  --max-width 2048
```

```bash
# 透明 PNG 在确认可接受轻微有损后进一步缩小
python <skill-dir>/scripts/image_assets_cli.py pipeline \
  --input /path/to/cutouts \
  --output /path/to/compact-assets \
  --sizes 256,512,1024 \
  --formats png,webp \
  --quality 85 \
  --png-lossy
```

## 边界与未明确项

- Apple 没有为所有普通应用内 toolbar / nav / button icon 发布统一硬性像素表；本文对应尺寸属于工程建议。
- Apple 没有发布所有应用通用的图片内存预算上限，应通过 Instruments 和真实设备测试验证。
- Apple 没有把第三方 Lottie 定义为平台级图片或动画资产标准。
- App Icon 和 App Store 截图有独立规格，不应与普通应用内图片规则混用。
