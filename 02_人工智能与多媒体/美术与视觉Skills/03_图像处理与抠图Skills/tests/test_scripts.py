from __future__ import annotations

from pathlib import Path


SKILL = Path(__file__).parents[1] / "image-processing"


def test_wrappers_pin_model_cache_inside_skill():
    wrapper = (SKILL / "scripts" / "process-image.ps1").read_text(encoding="utf-8")
    setup = (SKILL / "scripts" / "setup.ps1").read_text(encoding="utf-8")
    for script in (wrapper, setup):
        assert "$env:REMBG_HOME = $modelsDir" in script
        assert "$env:U2NET_HOME = $modelsDir" in script


def test_setup_validates_model_without_initializing_onnx_session():
    setup = (SKILL / "scripts" / "setup.ps1").read_text(encoding="utf-8")
    assert "BiRefNetSessionGeneral.download_models()" in setup
    assert "new_session('birefnet-general')" not in setup


def test_setup_requires_hashed_binary_dependencies_and_sha256_model():
    setup = (SKILL / "scripts" / "setup.ps1").read_text(encoding="utf-8")
    requirements = (SKILL / "requirements.in").read_text(encoding="utf-8")
    assert "--require-hashes" in setup
    assert "--only-binary=:all:" in setup
    assert "Get-FileHash" in setup
    assert "58f621f00f5d756097615970a88a791584600dcf7c45b18a0a6267535a1ebd3c" in setup
    assert "rembg[cpu]==2.0.77" in requirements
    assert "rembg[cpu,cli]" not in requirements
