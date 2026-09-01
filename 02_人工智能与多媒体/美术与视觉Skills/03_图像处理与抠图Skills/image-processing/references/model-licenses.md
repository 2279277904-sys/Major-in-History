# Model Policy, Provenance, and License Scope

The runtime allowlist is intentionally limited to:

- `birefnet-general` (default)
- `birefnet-general-lite`
- `u2net`

Always pass the selected model to `rembg.new_session`. Never rely on rembg's changing default and never fall back to `bria-rmbg` or another unlisted model.

The repository's MIT license covers only code and documentation authored in this
repository. It does not relicense third-party packages or model weights.

Upstream source licenses at the time of this release:

- rembg source: MIT, <https://github.com/danielgatis/rembg/blob/main/LICENSE.txt>
- BiRefNet source: MIT, <https://github.com/ZhengPeng7/BiRefNet/blob/main/LICENSE>
- U-2-Net source: Apache-2.0, <https://github.com/xuebinqin/U-2-Net/blob/master/LICENSE>
- ONNX Runtime source: MIT, <https://github.com/microsoft/onnxruntime/blob/main/LICENSE>
- Pillow source: HPND, <https://github.com/python-pillow/Pillow/blob/main/LICENSE>

Model weights are not stored or redistributed by this repository. The setup
script asks rembg to download the selected upstream release asset into the
local `.models` directory and independently verifies the default General
asset's SHA-256. Release-asset provenance and weight-specific terms can differ
from source-code licenses and may not be fully documented upstream.

Before commercial deployment, redistribution, conversion, or bundling of model
weights, review the current upstream terms and obtain legal advice when needed.
This Skill grants no additional rights to third-party packages, datasets, or
weights.
