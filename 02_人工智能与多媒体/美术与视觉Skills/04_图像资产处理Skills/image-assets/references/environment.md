# 环境与模型恢复

## 一键恢复

优先运行统一入口 `scripts/image_assets_cli.py`（跨平台，Windows/macOS/Linux 通用，需要系统已装 Python 3；只有尺寸、压缩和转码命令需要 Node.js）。它会按命令自动恢复所需环境：

- 抠图/对比：创建 Python venv（`.venv`），安装 `torch`、`torchvision`、`transformers`、`timm`、`einops`、`kornia`、`Pillow` 等依赖。
- 纯色背景 N 宫格 GIF：创建或复用 Python venv（`.venv`），只安装经过验收并按 Python 版本锁定的 Pillow / NumPy；不会下载模型权重。Python 3.14 使用 Pillow 12.3.0 + NumPy 2.4.6，Python 3.13 使用 Pillow 11.3.0 + NumPy 2.3.5，更早版本使用 Pillow 11.3.0 + NumPy 2.0.2。只有 `--cutout-mode rmbg2|birefnet` 才安装模型依赖。
- 尺寸修改/压缩/格式转换：在 skill 目录的 `.node-deps` 安装 `sharp`，使用其内置/绑定的 `libvips`。

```bash
python <skill-dir>/scripts/image_assets_cli.py app-assets --input /path/to/images --output /path/to/assets
```

N 宫格 GIF 跨环境冒烟命令：

```bash
python <skill-dir>/scripts/image_assets_cli.py grid-gif --help
python <skill-dir>/scripts/image_assets_cli.py grid-gif \
  --input /path/to/sprite-sheet.png \
  --output /path/to/animation.gif \
  --grid 4x4 \
  --playback ping-pong \
  --anchor feet \
  --keep-frames
```

`--output` 必填；脚本没有默认输出目录。

可用环境变量：

- `IMAGE_ASSETS_VENV=/path/to/venv`：复用已有 Python venv，避免重复安装模型依赖。
- `CUTOUT_VENV=/path/to/venv`：旧变量名，仍兼容。
- `IMAGE_ASSETS_NODE_DEPS=/path/to/node-deps`：复用已有 Node 依赖目录。
- `PYTHON=/path/to/python3`：指定 Python。
- `NODE=/path/to/node`、`NPM=/path/to/npm`：指定 Node/npm。
- `HF_TOKEN=...`：提供 Hugging Face read token。不要写入脚本或文档。

## 推荐模型与工具

- `rmbg2` -> `briaai/RMBG-2.0`：优先用于最终资产。Hugging Face gated，需要账号获批访问。权重约 885MB。
- `birefnet` -> `ZhengPeng7/BiRefNet`：开放可下载，适合作为无授权兜底或对比版本。权重约 424MB。
- `sharp/libvips`：默认用于 resize、WebP、AVIF、JPEG、PNG 输出；缩放使用 Lanczos3，JPEG 使用 `4:4:4` 色度抽样以保留彩色细节。
- `pngquant`：可选 PNG 有损量化，适合透明 PNG 追求更小体积。
- `oxipng`：可选 PNG 无损重压缩，适合透明主资产。

`pngquant` 和 `oxipng` 没装时，脚本仍会完成 sharp 输出；装好后会自动用于 PNG 二次优化。

macOS 可用：

```bash
brew install pngquant oxipng
```

## 常见问题

- `403 gated repo`：账号未获批访问 RMBG-2.0，先在模型页申请并同意条款，再设置 `HF_TOKEN` 或 `huggingface-cli login`。
- `Illegal header value b'Bearer '`：传入了空 token。不要传空字符串；改用 `HF_TOKEN=实际token` 或本地登录。
- `Input type float and bias type Half should be the same`：Apple MPS dtype 问题。脚本已用 `model.float()` 规避。
- `AutoModelForImageSegmentation` 不存在或模型无法识别：重新运行 `scripts/image_assets_cli.py app-transparent` 安装当前依赖，或删除旧 `.venv` 后重建。
- `Cannot find module sharp`：重新运行 `scripts/image_assets_cli.py resize ...`，脚本会在 `.node-deps` 安装 sharp。
- Python 3.13/3.14 下 NumPy 从源码编译失败：不要强装旧版本；重新运行统一入口，它会按 Python 版本选择有官方 wheel 的锁定依赖。旧 `.venv` 已经装到一半时，删除该运行时缓存后再运行一次。
- 下载很慢：Hugging Face 大文件进度可能长时间不刷新；缓存位于 `~/.cache/huggingface`，下次会续用。
- 下载卡死在接近完成处（透明代理掐大文件）：`hf_hub_download` 可能在最后几 MB 处僵住，`.incomplete` blob 大小长时间不变、日志无输出（常见于家里网关 OpenClash 透明代理把长连接掐断）。`HF_ENDPOINT=hf-mirror.com` 镜像对 gated repo 无效（不暴露权重，报 `does not appear to have a file named model.safetensors`）。可行解法：用 `curl -L -C -` 直接续传补完，再校验落位——
  1. 找到半成品 blob：`~/.cache/huggingface/hub/models--<org>--<repo>/blobs/<sha256>.<rand>.incomplete`；
  2. `curl -L -C - -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/<org>/<repo>/resolve/main/<file>" -o <该 .incomplete 路径>`（`-L` 跟 302 到 cas-bridge.xethub.hf.co，`-C -` 自动续传，几 MB 秒级补完）；
  3. `shasum -a 256` 校验等于文件名里的 sha256 → `mv` 去掉 `.<rand>.incomplete` 后缀成正式 blob；
  4. 在 `snapshots/<commit>/` 下 `ln -sf ../../blobs/<sha256> <file>` 建软链；
  5. 之后给抠图命令加 `--local-files-only` 走本地缓存即可，不会重下。

## 质量检查

处理完成后至少检查：

1. `preview_dark.png`：深色 APP 背景下是否有白边。
2. `preview_checker.png`：透明区域是否完整。
3. PNG 模式是否为 `RGBA`，四角 alpha 是否为 0。
4. `manifest.json`：输出尺寸、格式、质量、文件大小变化是否符合预期。

N 宫格 GIF 还必须检查 `*_alignment.png` 和从最终 GIF 解码生成的 `*_checker.gif`。详细验收与失败方案见 `sprite-sheet-gif.md`。

对生成式纯色背景图标，保留默认的 `--background-mode auto`。脚本会从四角识别均匀背景色，再反推去除对应色边；它比简单按颜色阈值删除更能保护主体中与背景同色的区域。背景色自动识别不可靠时，显式传 `--background-color '#RRGGBB'`。

纯色背景图片默认启用 `--shadow-mode auto`：识别到背景色后，会将模型主体 alpha 与背景色偏差反推的渐变投影 alpha 合并，并限制在主体附近。输出文件名出现 `-shadow` 表示投影恢复已生效；不需要投影时传 `--shadow-mode off`。

照片、纹理、渐变等复杂背景不会自动做颜色反推。需要强制只用分割模型时传 `--background-mode off --shadow-mode off`。
