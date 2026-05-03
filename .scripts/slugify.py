"""Build filename-stem -> slug table for all nodes under nodes/.

Rules:
- Lowercase, spaces -> hyphens, non-alphanumeric (except `_` in predicates) dropped.
- Gloss files (`<Concept> -- <definition>.md`): slug is the concept side only.
- Predicate files (`<predicate> -- <gloss>.md`): slug is the predicate name with underscores preserved.
- Collision check: fails loudly if two files map to the same slug.

Returns a dict: {filename_stem: {"slug": str, "taxonomy": str, "title": str, "path": Path}}
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Taxonomy folders and their slug forms (lowercase, plural).
TAXONOMIES = {
    "Contracts": "contracts",
    "Decisions": "decisions",
    "Convictions": "convictions",
    "Aspirations": "aspirations",
    "Observations": "observations",
    "Patterns": "patterns",
    "Predicates": "predicates",
    "Glosses": "glosses",
    "References": "references",
    "Skills": "skills",
}

# Taxonomies whose nodes are compound-node folders (`<Folder>/<Folder>.md`)
# rather than flat markdown files. See Skill Form Contract for the layout rule.
COMPOUND_NODE_TAXONOMIES = {"Skills"}


def _slug_general(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def _slug_predicate(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9_\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def _concept_side(filename_stem: str) -> str:
    """For '<Concept> -- <definition>' return '<Concept>'; else return the stem."""
    if " -- " in filename_stem:
        return filename_stem.split(" -- ", 1)[0]
    return filename_stem


def build_slug_table(root: Path) -> dict[str, dict]:
    """Walk nodes/ and build a slug table.

    Each entry keys on the filename stem (what wikilinks resolve against)
    and also on the concept side of Gloss/Predicate stems so that
    `[[Atomic Node]]` resolves to a Gloss file whose stem is
    `Atomic Node -- a single markdown file...`.
    """
    nodes_dir = root / "nodes"
    if not nodes_dir.is_dir():
        raise SystemExit(f"nodes/ not found at {nodes_dir}")

    table: dict[str, dict] = {}
    slug_owner: dict[tuple[str, str], str] = {}  # (taxonomy_slug, slug) -> filename_stem

    for taxonomy_name, taxonomy_slug in TAXONOMIES.items():
        tax_dir = nodes_dir / taxonomy_name
        if not tax_dir.is_dir():
            continue

        if taxonomy_name in COMPOUND_NODE_TAXONOMIES:
            md_files = sorted(
                subdir / f"{subdir.name}.md"
                for subdir in tax_dir.iterdir()
                if subdir.is_dir() and (subdir / f"{subdir.name}.md").is_file()
            )
        else:
            md_files = sorted(tax_dir.glob("*.md"))

        for md in md_files:
            stem = md.stem
            concept = _concept_side(stem)

            if taxonomy_name == "Predicates":
                slug = _slug_predicate(concept)
            else:
                slug = _slug_general(concept)

            if not slug:
                raise SystemExit(f"Empty slug for {md}")

            key = (taxonomy_slug, slug)
            if key in slug_owner:
                raise SystemExit(
                    f"Slug collision: '{taxonomy_slug}/{slug}' maps from both "
                    f"'{slug_owner[key]}' and '{stem}'"
                )
            slug_owner[key] = stem

            entry = {
                "slug": slug,
                "taxonomy": taxonomy_slug,
                "taxonomy_name": taxonomy_name,
                "title": concept,
                "path": md,
                "url": f"/nodes/{taxonomy_slug}/{slug}/",
            }

            # Register under the full filename stem (what wikilinks use when they
            # include the full `Concept -- definition` form).
            if stem in table:
                raise SystemExit(f"Duplicate filename stem: {stem}")
            table[stem] = entry

            # Also register under the concept side for Gloss and Predicate
            # so that `[[Atomic Node]]` or `[[conforms_to]]` resolves.
            if concept != stem:
                if concept in table and table[concept]["path"] != md:
                    raise SystemExit(
                        f"Concept-side collision: '{concept}' claimed by both "
                        f"'{table[concept]['path'].name}' and '{md.name}'"
                    )
                table[concept] = entry

    return table


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    table = build_slug_table(root)
    print(f"Indexed {len(table)} wikilink targets across {len(TAXONOMIES)} taxonomies")
    for stem, entry in sorted(table.items()):
        print(f"  [[{stem}]] -> {entry['url']}")


if __name__ == "__main__":
    main()
