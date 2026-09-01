# Third-Party Notices

This repository contains integration code but does not contain or redistribute
third-party model weights.

Runtime dependencies include:

- rembg, MIT: <https://github.com/danielgatis/rembg>
- BiRefNet source, MIT: <https://github.com/ZhengPeng7/BiRefNet>
- U-2-Net source, Apache-2.0: <https://github.com/xuebinqin/U-2-Net>
- ONNX Runtime, MIT: <https://github.com/microsoft/onnxruntime>
- Pillow, HPND: <https://github.com/python-pillow/Pillow>
- pytest, MIT: <https://github.com/pytest-dev/pytest>

The complete Python dependency set and exact versions are recorded in
`image-processing/requirements.lock`.

The repository MIT license applies only to code and documentation authored in
this repository. Model weights downloaded by rembg remain subject to their
upstream terms. Users are responsible for confirming that their intended use,
especially redistribution or commercial deployment, complies with all
applicable third-party licenses and dataset terms.
