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
    "Touch Points": "touch-points",
}

# Taxonomies whose nodes are compound-node folders (`<Folder>/<Folder>.md`)
# rather than flat markdown files. See Skill Form Contract for the layout rule.
COMPOUND_NODE_TAXONOMIES = {"Skills"}


def slug_general(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def slug_predicate(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9_\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


# Backward-compatible aliases (the underscore-prefixed names were used as
# private helpers before being needed in linkify.py for external wikilink
# resolution; the public names are now the canonical entry points).
_slug_general = slug_general
_slug_predicate = slug_predicate


_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _parse_scalar_frontmatter(text: str) -> dict:
    """Minimal YAML scalar-frontmatter parser.

    Reads only the top-level scalar fields. Sufficient for donor-table
    detection (`url:`, `this_did:`); does not attempt nested structures
    or sequences.
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        meta[key] = value
    return meta


def build_donor_table(root: Path) -> list:
    """Walk nodes/References/ and build a list of donor graphs.

    A donor Reference is a Reference node that proxies another Deep Context
    graph. It is identified by carrying both `this_did:` (the donor graph's
    `did:repo:<sha1>` DID) and `url:` (the donor graph's site URL) in its
    YAML frontmatter. Other Reference nodes (papers, gists, websites) carry
    `url:` but not `this_did:` and are not donors for the purposes of
    external-wikilink resolution.

    Returns a list of dicts: {"name": str, "url": str, "this_did": str, "path": Path}
    """
    references_dir = root / "nodes" / "References"
    if not references_dir.is_dir():
        return []

    donors: list = []
    for md in sorted(references_dir.glob("*.md")):
        meta = _parse_scalar_frontmatter(md.read_text(encoding="utf-8"))
        this_did = meta.get("this_did", "").strip()
        url = meta.get("url", "").strip()
        if not this_did or not url:
            continue
        donors.append({
            "name": md.stem,
            "url": url,
            "this_did": this_did,
            "path": md,
        })
    return donors


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
