"""Validate the repository's Codex Skill structure and UI metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")


def fail(message: str) -> int:
    print(f"Skill validation failed: {message}", file=sys.stderr)
    return 1


def main(skill_argument: str) -> int:
    skill = Path(skill_argument).resolve()
    manifest = skill / "SKILL.md"
    metadata = skill / "agents" / "openai.yaml"
    if not manifest.is_file():
        return fail("SKILL.md is missing")
    if not metadata.is_file():
        return fail("agents/openai.yaml is missing")

    content = manifest.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not match:
        return fail("SKILL.md frontmatter is missing or malformed")
    frontmatter = yaml.safe_load(match.group(1))
    if not isinstance(frontmatter, dict):
        return fail("frontmatter must be a mapping")

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        return fail("name must use lowercase letters, digits, or hyphens and be at most 64 characters")
    if name != skill.name:
        return fail("frontmatter name must match the Skill directory")
    if not isinstance(description, str) or not description.strip():
        return fail("description must be non-empty")

    ui = yaml.safe_load(metadata.read_text(encoding="utf-8"))
    interface = ui.get("interface") if isinstance(ui, dict) else None
    if not isinstance(interface, dict):
        return fail("openai.yaml must define interface metadata")
    for key in ("display_name", "short_description", "default_prompt"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            return fail(f"interface.{key} must be non-empty")
    if f"${name}" not in interface["default_prompt"]:
        return fail("default_prompt must explicitly mention the Skill")

    if any(token in content for token in ("TODO", "TBD", "<skill-name>")):
        return fail("unfinished scaffold placeholder found")
    print(f"Skill is valid: {skill}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate-skill.py <skill-directory>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
