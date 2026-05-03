"""Emit skill-runtime-alias symlink trees from nodes/Skills/.

Source of truth is nodes/Skills/<Title Case>/<Title Case>.md (compound-node
lead file matching its folder per Skill Form Contract). Two agent runtimes
discover skills under lowercase-hyphenated paths:

  .agents/skills/<runtime_name>/SKILL.md   -- Anthropic Agent Skills runtime
  .claude/skills/<runtime_name>/SKILL.md   -- Claude Code CLI slash commands

This module emits symlink trees at both paths, each pointing at the single
source-of-truth lead file. Keeping both trees in the repository means a
clone or fresh scion has working runtime layouts and CLI autocomplete
without running build.py locally.

Usage:
    python .scripts/emit_skills.py [repo-root]
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

SKILLS_SOURCE_DIR = "nodes/Skills"
SKILLS_TARGET_DIRS = (".agents/skills", ".claude/skills")
SKILL_SUBDIRS = ("scripts", "references")

_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_RUNTIME_NAME_RE = re.compile(r"^runtime_name:\s*(\S+)\s*$", re.MULTILINE)


def _derive_runtime_name(folder_name: str) -> str:
    """'Node Create' -> 'node-create'."""
    return folder_name.strip().lower().replace(" ", "-")


def _read_runtime_name(lead_file: Path) -> str | None:
    """Return runtime_name from YAML frontmatter, or None if absent.

    Intentionally small: only the `runtime_name` scalar is needed by this
    module, and adding a YAML dependency for one field is not worth the cost.
    If the frontmatter format grows, replace this with a proper YAML parser.
    """
    text = lead_file.read_text(encoding="utf-8")
    fm_match = _FRONTMATTER_RE.match(text)
    if not fm_match:
        return None
    rn_match = _RUNTIME_NAME_RE.search(fm_match.group(1))
    if not rn_match:
        return None
    return rn_match.group(1)


def _clear_target(target_dir: Path) -> None:
    """Remove everything under target_dir; caller is responsible for recreating it."""
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
    """Emit symlinks for every compound-node skill under nodes/Skills/ into
    each of the SKILLS_TARGET_DIRS. Returns the count of skills emitted
    (same count per target).
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
        runtime_name = _read_runtime_name(lead_file) or _derive_runtime_name(
            skill_folder.name
        )
        skills.append((skill_folder, lead_file, runtime_name))

    for target_name in SKILLS_TARGET_DIRS:
        target_dir = root / target_name
        target_dir.mkdir(parents=True, exist_ok=True)
        _clear_target(target_dir)

        for skill_folder, lead_file, runtime_name in skills:
            alias_dir = target_dir / runtime_name
            alias_dir.mkdir(parents=True, exist_ok=True)
            _link_into(alias_dir / "SKILL.md", lead_file)

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
