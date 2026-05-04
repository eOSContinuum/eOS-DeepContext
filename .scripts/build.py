"""Build entry point: runs slugify -> linkify -> render -> generate_indexes.

Usage:
    python .scripts/build.py [repo-root]

Default repo root is the current working directory.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# Ensure sibling modules are importable when run via `python .scripts/build.py`.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import render  # noqa: E402
from emit_skills import SKILLS_TARGET_DIRS, emit_skill_aliases  # noqa: E402
from generate_indexes import (  # noqa: E402
    copy_attachments,
    copy_style,
    write_cname,
    write_landing_page,
    write_nojekyll,
    write_taxonomy_indexes,
)
from linkify import linkify_file  # noqa: E402
from render import render_file  # noqa: E402
from slugify import TAXONOMIES, build_donor_table, build_slug_table  # noqa: E402


def render_nodes(
    *,
    root: Path,
    build_dir: Path,
    slug_table: dict[str, dict],
    donors: list,
) -> int:
    rendered = 0
    seen = set()
    for entry in slug_table.values():
        if entry["path"] in seen:
            continue
        seen.add(entry["path"])
        source = entry["path"]
        linkified = linkify_file(source, slug_table, donors)
        taxonomy_url = f"/nodes/{entry['taxonomy']}/"
        source_rel = str(source.relative_to(root))
        html_text = render_file(
            source_path=source,
            linkified_text=linkified,
            title=entry["title"],
            taxonomy_name=entry["taxonomy_name"],
            taxonomy_url=taxonomy_url,
            source_rel_path=source_rel,
        )
        out = build_dir / "nodes" / entry["taxonomy"] / entry["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html_text, encoding="utf-8")
        rendered += 1
    return rendered


def build(root: Path) -> None:
    build_dir = root / ".build"
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True)

    render.INCEPTION_DID = render.compute_inception_did(root)

    slug_table = build_slug_table(root)
    donors = build_donor_table(root)
    node_count = render_nodes(
        root=root, build_dir=build_dir, slug_table=slug_table, donors=donors
    )

    write_taxonomy_indexes(
        root=root, build_dir=build_dir, slug_table=slug_table, donors=donors
    )
    write_landing_page(
        root=root, build_dir=build_dir, slug_table=slug_table, donors=donors
    )
    copy_style(root=root, build_dir=build_dir)
    copy_attachments(root=root, build_dir=build_dir)
    write_nojekyll(build_dir)
    write_cname(build_dir)

    skill_count = emit_skill_aliases(root=root)

    skill_targets = ", ".join(f"{t}/" for t in SKILLS_TARGET_DIRS)
    print(f"Built {node_count} node pages across {len(TAXONOMIES)} taxonomies")
    print(f"Emitted {skill_count} skill alias(es) to {skill_targets}")
    print(f"Site output: {build_dir}")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    build(root.resolve())


if __name__ == "__main__":
    main()
