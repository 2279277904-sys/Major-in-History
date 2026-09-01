"""Regenerate the Windows x64 CPython 3.12 wheel-hash lock."""

from __future__ import annotations

import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from importlib import metadata
from pathlib import Path

from packaging.requirements import Requirement
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name, parse_wheel_filename


REPOSITORY = Path(__file__).resolve().parents[1]
OUTPUT = REPOSITORY / "image-processing" / "requirements.lock"
ROOTS = {"rembg", "onnxruntime", "pillow", "pytest", "pyyaml"}
ROOT_EXTRAS = {"rembg": {"cpu"}}


def installed_distributions() -> dict[str, metadata.Distribution]:
    return {
        canonicalize_name(dist.metadata["Name"]): dist
        for dist in metadata.distributions()
        if dist.metadata.get("Name")
    }


def required_versions() -> dict[str, str]:
    installed = installed_distributions()
    keep = set(ROOTS)
    extras = {name: set(values) for name, values in ROOT_EXTRAS.items()}
    queue = list(ROOTS)
    while queue:
        name = queue.pop()
        dist = installed.get(name)
        if dist is None:
            raise RuntimeError(f"Required distribution is not installed: {name}")
        marker_extras = extras.get(name) or {""}
        for raw_requirement in dist.requires or []:
            requirement = Requirement(raw_requirement)
            if requirement.marker and not any(
                requirement.marker.evaluate({"extra": extra}) for extra in marker_extras
            ):
                continue
            child = canonicalize_name(requirement.name)
            if child not in installed:
                raise RuntimeError(f"Missing installed dependency: {requirement}")
            child_extras = set(requirement.extras)
            previous = extras.setdefault(child, set())
            changed = not child_extras.issubset(previous)
            previous.update(child_extras)
            if child not in keep or changed:
                keep.add(child)
                queue.append(child)
    return {name: installed[name].version for name in sorted(keep)}


def compatible_wheel(item: tuple[str, str]) -> tuple[str, str, str]:
    name, version = item
    with urllib.request.urlopen(
        f"https://pypi.org/pypi/{name}/{version}/json", timeout=60
    ) as response:
        payload = json.load(response)

    rank = {tag: index for index, tag in enumerate(sys_tags())}
    candidates: list[tuple[int, str, str]] = []
    for artifact in payload.get("urls", []):
        filename = artifact.get("filename", "")
        if artifact.get("packagetype") != "bdist_wheel" or not filename.endswith(".whl"):
            continue
        _, wheel_version, _, tags = parse_wheel_filename(filename)
        if str(wheel_version) != version:
            continue
        ranks = [rank[tag] for tag in tags if tag in rank]
        digest = artifact.get("digests", {}).get("sha256")
        if ranks and digest:
            candidates.append((min(ranks), filename, digest))
    if not candidates:
        raise RuntimeError(f"No compatible wheel found for {name}=={version}")
    _, filename, digest = min(candidates)
    return name, filename, digest


def main() -> int:
    if sys.platform != "win32" or sys.version_info[:2] != (3, 12):
        raise RuntimeError("Lock generation requires Windows CPython 3.12")
    versions = required_versions()
    with ThreadPoolExecutor(max_workers=8) as executor:
        artifacts = {
            name: (filename, digest)
            for name, filename, digest in executor.map(compatible_wheel, versions.items())
        }

    lines = [
        "# Generated for Windows x64 CPython 3.12.",
        "# Every requirement is pinned to one compatible PyPI wheel SHA-256.",
        "# Regenerate from requirements.in before changing dependencies.",
        "",
    ]
    for name, version in versions.items():
        filename, digest = artifacts[name]
        lines.extend(
            [
                f"{name}=={version} \\",
                f"    --hash=sha256:{digest}  # {filename}",
            ]
        )
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": "ok", "packages": len(versions), "output": str(OUTPUT)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
