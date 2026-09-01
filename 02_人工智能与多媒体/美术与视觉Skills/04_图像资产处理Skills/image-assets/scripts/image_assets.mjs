#!/usr/bin/env node
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';
import { stat, mkdir, writeFile, copyFile, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';

const require = createRequire(import.meta.url);
const sharp = require(process.env.SHARP_MODULE_PATH || 'sharp');

const IMAGE_SUFFIXES = new Set(['.png', '.jpg', '.jpeg', '.webp', '.avif', '.tif', '.tiff', '.bmp']);

function log(message) {
  console.error(`[图片素材] ${message}`);
}

function usage() {
  console.error(`用法（一般通过 image_assets_cli.py 转发调用，不需要直接执行本文件）:
  image_assets_cli.py app-icons --input DIR --output DIR [--sizes 256,512,1024] [--formats png,webp]
  image_assets_cli.py web-optimized --input DIR --output DIR [--max-width 2048] [--formats webp,avif,jpeg] [--quality 88]
  image_assets_cli.py resize --input DIR --output DIR --width 1024 [--height 1024] [--format png]
  image_assets_cli.py optimize --input DIR --output DIR --format webp [--quality 90]
  image_assets_cli.py pipeline --input DIR --output DIR --sizes 512,1024 --formats png,webp`);
}

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith('--')) {
      args._.push(token);
      continue;
    }
    const key = token.slice(2).replaceAll('-', '_');
    const next = argv[i + 1];
    if (!next || next.startsWith('--')) {
      args[key] = true;
    } else {
      args[key] = next;
      i += 1;
    }
  }
  return args;
}

function required(args, key) {
  if (!args[key]) {
    throw new Error(`缺少必要参数 --${key.replaceAll('_', '-')}`);
  }
  return args[key];
}

function splitList(value, fallback) {
  const raw = value || fallback;
  return raw.split(',').map((item) => item.trim()).filter(Boolean);
}

async function collectImages(input) {
  const inputPath = path.resolve(input);
  const info = await stat(inputPath);
  if (info.isFile()) {
    return [inputPath];
  }
  const fs = await import('node:fs/promises');
  const names = await fs.readdir(inputPath);
  return names
    .map((name) => path.join(inputPath, name))
    .filter((file) => IMAGE_SUFFIXES.has(path.extname(file).toLowerCase()))
    .filter((file) => {
      const name = path.basename(file);
      return !name.startsWith('preview_') && !/_alpha(?:-|\.|_)/.test(name);
    })
    .sort((a, b) => a.localeCompare(b));
}

function normalizeFormat(format, source) {
  if (format && format !== 'same') {
    return format === 'jpg' ? 'jpeg' : format;
  }
  const ext = path.extname(source).toLowerCase().slice(1);
  return ext === 'jpg' ? 'jpeg' : ext;
}

function outputExt(format) {
  return format === 'jpeg' ? 'jpg' : format;
}

function buildName(source, ops, format) {
  const stem = path.basename(source, path.extname(source));
  return `${stem}_${ops.filter(Boolean).join('_')}.${outputExt(format)}`;
}

function toInt(value, fallback = undefined) {
  if (value === undefined || value === null || value === '') {
    return fallback;
  }
  const parsed = Number.parseInt(value, 10);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    throw new Error(`数字参数无效: ${value}`);
  }
  return parsed;
}

function commandExists(command) {
  // 直接尝试调起目标命令，而不是依赖 `which`（Windows 上没有这个命令，等价物是 `where`）。
  const result = spawnSync(command, ['--version'], { stdio: 'ignore' });
  return !result.error;
}

function runTool(command, args) {
  const result = spawnSync(command, args, { stdio: 'pipe', encoding: 'utf8' });
  if (result.status !== 0) {
    log(`${command} 未改写输出，已保留当前文件，退出码 ${result.status}: ${(result.stderr || result.stdout || '').trim()}`);
    return false;
  }
  return true;
}

async function maybeOptimizePng(file, quality, usePngquant) {
  const before = (await stat(file)).size;
  const used = [];
  if (usePngquant && commandExists('pngquant')) {
    const tmp = `${file}.pngquant.png`;
    if (runTool('pngquant', ['--force', '--skip-if-larger', `--quality=${Math.max(1, quality - 12)}-${quality}`, '--output', tmp, file])) {
      if (existsSync(tmp)) {
        await copyFile(tmp, file);
        await unlink(tmp);
        used.push('pngquant');
      }
    }
  }
  if (commandExists('oxipng')) {
    if (runTool('oxipng', ['-o', '4', '--strip', 'safe', file])) {
      used.push('oxipng');
    }
  }
  const after = (await stat(file)).size;
  return { before, after, tools: used };
}

function applyFormat(image, format, quality, pngLossy) {
  if (format === 'webp') {
    return image.webp({ quality, effort: 6, smartSubsample: true });
  }
  if (format === 'avif') {
    return image.avif({ quality, effort: 6 });
  }
  if (format === 'jpeg') {
    return image.flatten({ background: '#ffffff' }).jpeg({
      quality,
      chromaSubsampling: '4:4:4',
      mozjpeg: true,
      progressive: true,
    });
  }
  if (format === 'png') {
    return image.png({
      compressionLevel: 9,
      adaptiveFiltering: true,
      palette: Boolean(pngLossy),
      quality,
      effort: 10,
    });
  }
  throw new Error(`暂不支持输出格式: ${format}`);
}

async function renderOne({ source, outputDir, width, height, fit, format, quality, extraOps, pngLossy }) {
  const actualFormat = normalizeFormat(format, source);
  const image = sharp(source, { animated: false, limitInputPixels: false }).rotate();
  const metadata = await image.metadata();
  const resizeOptions = {};
  if (width) resizeOptions.width = width;
  if (height) resizeOptions.height = height;
  if (width || height) {
    resizeOptions.fit = fit;
    resizeOptions.withoutEnlargement = true;
    resizeOptions.kernel = sharp.kernel.lanczos3;
    image.resize(resizeOptions);
  }
  const ops = [...extraOps];
  if (width) ops.push(`w${width}`);
  if (height) ops.push(`h${height}`);
  if ((width || height) && fit && fit !== 'inside') ops.push(`fit-${fit}`);
  if (actualFormat === 'png' && pngLossy) {
    ops.push(`pnglossy-q${quality}`);
  } else if (actualFormat !== normalizeFormat('same', source)) {
    ops.push(actualFormat === 'jpeg' ? `jpg-q${quality}` : `${actualFormat}-q${quality}`);
  } else if (actualFormat !== 'png') {
    ops.push(`${actualFormat}-q${quality}`);
  }
  const out = path.join(outputDir, buildName(source, ops, actualFormat));
  await mkdir(outputDir, { recursive: true });
  await applyFormat(image, actualFormat, quality, pngLossy).toFile(out);
  let pngOptimization = null;
  if (actualFormat === 'png') {
    pngOptimization = await maybeOptimizePng(out, quality, pngLossy);
  }
  const outMeta = await sharp(out).metadata();
  const sourceInfo = await stat(source);
  const outputInfo = await stat(out);
  return {
    source,
    output: out,
    operations: ops,
    source_width: metadata.width,
    source_height: metadata.height,
    output_width: outMeta.width,
    output_height: outMeta.height,
    format: outputExt(actualFormat),
    quality,
    source_bytes: sourceInfo.size,
    output_bytes: outputInfo.size,
    png_optimization: pngOptimization,
  };
}

async function runResize(args) {
  const input = required(args, 'input');
  const output = required(args, 'output');
  const width = toInt(args.width);
  const height = toInt(args.height);
  if (!width && !height) {
    throw new Error('resize 必须传 --width 或 --height');
  }
  return processImages({
    input,
    output,
    widths: [width],
    height,
    formats: [args.format ? normalizeFormat(args.format, '') : 'same'],
    quality: toInt(args.quality, 92),
    fit: args.fit || 'inside',
    extraOps: ['resize'],
    pngLossy: Boolean(args.png_lossy),
  });
}

async function runOptimize(args) {
  const input = required(args, 'input');
  const output = required(args, 'output');
  return processImages({
    input,
    output,
    widths: [undefined],
    height: undefined,
    formats: splitList(args.format || args.formats, 'webp').map((item) => normalizeFormat(item, '')),
    quality: toInt(args.quality, 90),
    fit: args.fit || 'inside',
    extraOps: ['opt'],
    pngLossy: Boolean(args.png_lossy),
  });
}

async function runPipeline(args) {
  const input = required(args, 'input');
  const output = required(args, 'output');
  return processImages({
    input,
    output,
    widths: splitList(args.sizes, '512,1024').map((value) => toInt(value)),
    height: toInt(args.height),
    formats: splitList(args.formats, 'png,webp').map((item) => normalizeFormat(item, '')),
    quality: toInt(args.quality, 92),
    fit: args.fit || 'inside',
    extraOps: args.transparent ? ['asset'] : ['pipe'],
    pngLossy: Boolean(args.png_lossy),
  });
}

async function processImages(options) {
  const files = await collectImages(options.input);
  if (!files.length) {
    throw new Error('没有找到可处理图片');
  }
  const manifest = {
    tool: 'image-assets sharp/libvips',
    started_at: new Date().toISOString(),
    input: path.resolve(options.input),
    output: path.resolve(options.output),
    sharp: sharp.versions,
    items: [],
  };
  log(`输入图片: ${files.length}`);
  log(`输出目录: ${manifest.output}`);
  for (const source of files) {
    for (const width of options.widths) {
      for (const format of options.formats) {
        const item = await renderOne({
          source,
          outputDir: manifest.output,
          width,
          height: options.height,
          fit: options.fit,
          format,
          quality: options.quality,
          extraOps: options.extraOps,
          pngLossy: options.pngLossy,
        });
        manifest.items.push(item);
        log(`${path.basename(source)} -> ${path.basename(item.output)} (${item.output_bytes} bytes)`);
      }
    }
  }
  manifest.finished_at = new Date().toISOString();
  manifest.count = manifest.items.length;
  await writeFile(path.join(manifest.output, 'manifest.json'), JSON.stringify(manifest, null, 2), 'utf8');
  log(`处理清单: ${path.join(manifest.output, 'manifest.json')}`);
  return manifest;
}

async function main() {
  const [command, ...rest] = process.argv.slice(2);
  const args = parseArgs(rest);
  if (!command || command === 'help' || command === '--help' || command === '-h') {
    usage();
    return 0;
  }
  if (command === 'resize') {
    await runResize(args);
    return 0;
  }
  if (command === 'optimize') {
    await runOptimize(args);
    return 0;
  }
  if (command === 'pipeline') {
    await runPipeline(args);
    return 0;
  }
  if (command === 'app-icons') {
    args.sizes ??= '256,512,1024';
    args.formats ??= 'png,webp';
    args.transparent = true;
    await runPipeline(args);
    return 0;
  }
  if (command === 'web-optimized') {
    args.sizes ??= String(toInt(args.max_width, 2048));
    args.formats ??= 'webp,avif,jpeg';
    args.quality ??= '88';
    await runPipeline(args);
    return 0;
  }
  throw new Error(`未知命令: ${command}`);
}

main().catch((error) => {
  log(`失败: ${error.message}`);
  process.exitCode = 1;
});
