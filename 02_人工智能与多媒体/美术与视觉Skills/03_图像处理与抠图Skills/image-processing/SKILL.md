---
name: image-processing
description: Remove image backgrounds locally, produce transparent PNG cutouts, and place a detected subject on an exact-size or exact-aspect-ratio transparent canvas. Use for background removal, product or portrait cutouts, transparent backgrounds, subject centering, image resizing, or fitting a subject within a requested canvas while preserving safety margins.
---

# Image Processing

Use the bundled deterministic pipeline for local CPU background removal and subject layout. Keep image algorithms in the scripts; use this file to choose the mode, invoke the entry point, and interpret its JSON result.

## Workflow

1. Identify the input image and requested layout:
   - Use `--width W --height H` when exact pixel dimensions are requested. The subject may be enlarged and will fit within 80% of both canvas dimensions by default.
   - Use `--aspect-ratio A:B` when only a ratio is requested. The subject is never enlarged; the script creates the smallest matching transparent canvas that preserves the default safety margin.
2. Choose an output path only when the user specified one. Otherwise allow the script to create `<input-stem>.processed.png` beside the source.
3. Run `scripts/process-image.ps1` from this skill directory. Quote every filesystem path.
4. Read stdout as JSON. Treat `status: "success"` as completion and report the output path, canvas size, warnings, and relevant occupancy. Treat other statuses according to `references/cli-contract.md`.
5. When the user asks to inspect the result, render or open the output image and check the edge quality and spacing.

## Invocation

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "<skill-directory>\scripts\process-image.ps1" `
  --input "<input-path>" `
  --output "<optional-output-path>" `
  --width 1200 --height 1200
```

For ratio-only processing, replace the size arguments with `--aspect-ratio 3:4`.

Use `--overwrite` only when the user explicitly authorizes replacing an existing output. Use `--model` only for one of `birefnet-general`, `birefnet-general-lite`, or `u2net`. Never select or fall back to BRIA models. The default is always `birefnet-general`.

If the wrapper reports exit code 3 because the local environment or model is missing, explain that setup is required before running `scripts/setup.ps1`; setup installs pinned packages and downloads the model. Do not run setup implicitly when network access or installation approval is required.

## Constraints

- Output only transparent PNG in this MVP.
- Preserve EXIF orientation before inference.
- Do not overwrite existing files by default.
- Keep user images and generated acceptance outputs outside Git.
- Use one input image per invocation; batch processing is not part of this MVP.

Read `references/cli-contract.md` for the complete JSON and exit-code contract. Read `references/model-licenses.md` before changing the model allowlist.
