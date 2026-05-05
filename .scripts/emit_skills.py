"""Emit skill-runtime-alias trees from nodes/Skills/.

Source of truth is nodes/Skills/<Title Case>/<Title Case>.md (compound-node
lead file matching its folder per Skill Form Contract). Two agent runtimes
discover skills under lowercase-hyphenated paths:

  .agents/skills/<name>/SKILL.md   -- Anthropic Agent Skills runtime
  .claude/skills/<name>/SKILL.md   -- Claude Code CLI slash commands

The emitted SKILL.md is a transformed version of the source. The Skill Form
Contract permits source-only fields like `tagline` for index-page rendering;
the Anthropic Agent Skills spec only recognizes a small set of keys (name,
description, license, allowed-tools, compatibility, metadata) and silently
rejects skills with descriptions exceeding 1024 characters at slash-command
discovery time. This module strips source-only keys, validates the spec's
character cap, and writes a regular SKILL.md (not a symlink) that is
runtime-loadable. Subdirectories `scripts/` and `references/` remain
directory symlinks because they carry no frontmatter.

Usage:
    python .scripts/emit_skills.py [repo-root]
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path
from typing import Optional

SKILLS_SOURCE_DIR = "nodes/Skills"
SKILLS_TARGET_DIRS = (".agents/skills", ".claude/skills")
SKILL_SUBDIRS = ("scripts", "references")

# Anthropic Agent Skills spec frontmatter keys passed through to runtime SKILL.md.
SPEC_KEYS = ("name", "description", "license", "allowed-tools", "compatibility", "metadata")

# Anthropic Agent Skills runtime cap on `description` length. Descriptions
# exceeding the cap are silently rejected at slash-command discovery time.
DESCRIPTION_CAP = 1024

_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_KEY_LINE_RE = re.compile(r"^([a-z][a-z_-]*):\s*(.*)$")


def _derive_name(folder_name: str) -> str:
    """'Node Create' -> 'node-create'."""
    return folder_name.strip().lower().replace(" ", "-")


def _split_frontmatter(text: str) -> Optional[tuple]:
    """Return (frontmatter_text, body) or None if no frontmatter."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    return m.group(1), text[m.end():]


def _parse_yaml_simple(fm: str) -> dict:
    """Parse a subset of YAML sufficient for flat skill frontmatter.

    Handles inline scalars (`key: value`) and block scalars (`key: |` or
    `key: >`). For block scalars, collects indented continuation lines and
    preserves their content as a string. Quoted inline values are stripped.
    Does not handle nested mappings or sequences; skill frontmatter per the
    Skill Form Contract is flat.
    """
    out = {}
    lines = fm.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        m = _KEY_LINE_RE.match(line)
        if not m:
            i += 1
            continue
        key, value = m.group(1), m.group(2)
        if value in ("|", ">"):
            # Block scalar -- collect indented (or blank) continuation lines.
            block_lines = []
            i += 1
            while i < len(lines):
                cont = lines[i]
                if cont.startswith("  "):
                    block_lines.append(cont[2:])
                elif not cont.strip():
                    block_lines.append("")
                else:
                    break
                i += 1
            # Preserve newlines verbatim; the runtime reads the resulting
                # string regardless of YAML scalar style.
            out[key] = "\n".join(block_lines).rstrip("\n")
            continue
        # Inline scalar -- strip surrounding quotes.
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        out[key] = value
        i += 1
    return out


def _format_block_scalar(text: str, indent: str = "  ") -> str:
    """Format a string as a YAML literal-block-scalar body, indenting
    each line. Blank lines render with no trailing whitespace.
    """
    return "\n".join(indent + line if line else "" for line in text.split("\n"))


def _build_runtime_frontmatter(*, name: str, fm: dict) -> str:
    """Build runtime-spec frontmatter text from source frontmatter.

    Includes only Anthropic Agent Skills spec keys; strips source-only fields
    like `tagline`. Validates the description character cap. Returns the
    frontmatter text without the surrounding `---` fences.
    """
    description = fm.get("description", "")
    if len(description) > DESCRIPTION_CAP:
        raise ValueError(
            f"description for skill '{name}' is {len(description)} chars "
            f"(cap is {DESCRIPTION_CAP}). Trim the source description."
        )

    lines = [f"name: {name}"]
    if description:
        lines.append("description: |")
        lines.append(_format_block_scalar(description))
    for key in SPEC_KEYS:
        if key in ("name", "description"):
            continue
        if key in fm:
            lines.append(f"{key}: {fm[key]}")
    return "\n".join(lines)


def _emit_skill_md(*, name: str, fm: dict, body: str, target: Path) -> None:
    """Write a spec-compliant SKILL.md to target. Body is copied verbatim."""
    runtime_fm = _build_runtime_frontmatter(name=name, fm=fm)
    body_text = body if body.startswith("\n") else "\n" + body
    target.write_text(f"---\n{runtime_fm}\n---{body_text}", encoding="utf-8")


def _clear_target(target_dir: Path) -> None:
    """Remove everything under target_dir; caller recreates it."""
    if not target_dir.exists():
        return
    for entry in target_dir.iterdir():
        if entry.is_symlink() or entry.is_file():
            entry.unlink()
        else:
            shutil.rmtree(entry)


def _link_into(link_path: Path, source_path: Path) -> None:
    """Create a relative symlink at link_path pointing to source_path."""
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()
    relative = os.path.relpath(source_path, link_path.parent)
    link_path.symlink_to(relative, target_is_directory=source_path.is_dir())


def emit_skill_aliases(*, root: Path) -> int:
    """Emit transformed SKILL.md files (and directory symlinks for scripts/
    and references/) for every compound-node skill under nodes/Skills/.
    Returns the count of skills emitted (same count per target directory).
    """
    source_dir = root / SKILLS_SOURCE_DIR
    if not source_dir.is_dir():
        return 0

    skills = []
    for skill_folder in sorted(source_dir.iterdir()):
        if not skill_folder.is_dir():
            continue
        lead_file = skill_folder / f"{skill_folder.name}.md"
        if not lead_file.is_file():
            continue
        text = lead_file.read_text(encoding="utf-8")
        split = _split_frontmatter(text)
        if split is None:
            continue
        fm_text, body = split
        fm = _parse_yaml_simple(fm_text)
        name = fm.get("name") or _derive_name(skill_folder.name)
        skills.append((skill_folder, fm, body, name))

    for target_name in SKILLS_TARGET_DIRS:
        target_dir = root / target_name
        target_dir.mkdir(parents=True, exist_ok=True)
        _clear_target(target_dir)

        for skill_folder, fm, body, name in skills:
            alias_dir = target_dir / name
            alias_dir.mkdir(parents=True, exist_ok=True)
            _emit_skill_md(name=name, fm=fm, body=body, target=alias_dir / "SKILL.md")

            for subdir_name in SKILL_SUBDIRS:
                source_sub = skill_folder / subdir_name
                if source_sub.is_dir():
                    _link_into(alias_dir / subdir_name, source_sub)

    return len(skills)


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    count = emit_skill_aliases(root=root.resolve())
    targets = ", ".join(f"{t}/" for t in SKILLS_TARGET_DIRS)
    print(f"Emitted {count} skill alias(es) to {targets}")


if __name__ == "__main__":
    main()
