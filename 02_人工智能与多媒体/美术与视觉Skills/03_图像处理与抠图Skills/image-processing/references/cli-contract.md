# CLI Contract

## Entry point

Run `scripts/process-image.ps1` with one input and one layout mode:

```text
--input PATH [--output PATH]
(--width INT --height INT | --aspect-ratio A:B)
[--model birefnet-general|birefnet-general-lite|u2net]
[--subject-scale FLOAT] [--alpha-threshold INT] [--overwrite]
```

Defaults are model `birefnet-general`, subject scale `0.8`, alpha threshold `8`, and output `<input-stem>.processed.png`. Only `.png` output is accepted.

## Standard output

Stdout contains exactly one compact JSON object. On success it includes:

- `status`, `inputPath`, `outputPath`, and `model`
- `canvas` with integer `width` and `height`
- `sourceSubjectBbox` and final `subjectBbox`
- `subjectOccupancy` fractions for width and height
- `scaleFactor`, `elapsedMs`, and `warnings`

Errors include `status: "error"`, a stable `code`, `message`, and `elapsedMs`. Diagnostic logs go to stderr.

## Exit codes

- `0`: success
- `2`: argument, validation, empty-alpha, or overwrite error
- `3`: environment or model missing
- `4`: inference failure
- `5`: input or output file failure
