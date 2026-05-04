"""Generate per-taxonomy index pages.

For each taxonomy folder under nodes/:
- If a README.md exists in the folder, render it as the taxonomy index (hand-authored).
- Else, walk the folder and build a list page from each node's tagline/brief_summary.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from linkify import linkify_text
from render import render_html, strip_frontmatter, strip_identity_block
from slugify import TAXONOMIES

TAXONOMY_DESCRIPTIONS: dict[str, str] = {
    "Contracts": "Form specifications — thin compliance rules with RFC 2119 keywords.",
    "Decisions": "Recorded choices with Why, Alternatives Considered, and What Would Change It.",
    "Convictions": "Normative stances the project holds about how to work.",
    "Aspirations": "Directional targets with acknowledged gaps and recognition criteria.",
    "Observations": "Descriptive claims with epistemic grounds (Empirical, Retrospective, Contested).",
    "Patterns": "Recurring craft moves that resolve specific tensions.",
    "Predicates": "Typed edges with Carries, Crescent-per-neighbor, and Typing sections.",
    "Glosses": "Interpretive definitions that frame concepts through a broader lens.",
    "References": "External sources the graph draws on, with publication metadata.",
    "Skills": "Agent-invocable workflows with numbered steps, grounded in the Decisions they enforce.",
    "Touch Points": "Guided introductions that frame a reader's lens onto a region of the graph — not summaries.",
}


def _first_clause(text: str) -> str:
    """Return the clause before the first em-dash or double-hyphen separator."""
    for sep in (" \u2014 ", " -- "):
        idx = text.find(sep)
        if idx > 0:
            return text[:idx].rstrip()
    return text


def _entry_summary(path: Path) -> str:
    """Pick the taxonomy-index summary for a node.

    Use the tagline's first clause (before an em-dash or double-hyphen break);
    fall back to brief_summary when no tagline is present.
    """
    meta, _ = strip_frontmatter(path.read_text(encoding="utf-8"))
    tagline = meta.get("tagline", "").strip()
    if tagline:
        clause = _first_clause(tagline)
        if len(clause) <= 180:
            return clause
        return clause[:177].rstrip() + "..."

    brief = meta.get("brief_summary", "").strip()
    if len(brief) > 180:
        return brief[:177].rstrip() + "..."
    return brief


def build_taxonomy_index(
    *, taxonomy_name: str, taxonomy_slug: str, slug_table: dict[str, dict]
) -> str:
    description = TAXONOMY_DESCRIPTIONS.get(taxonomy_name, "")
    entries = [
        e for e in slug_table.values() if e["taxonomy"] == taxonomy_slug
    ]
    # Deduplicate (concept-side registrations share entries with full-stem ones).
    seen = set()
    unique: list[dict] = []
    for e in entries:
        if e["path"] in seen:
            continue
        seen.add(e["path"])
        unique.append(e)
    unique.sort(key=lambda e: e["title"].lower())

    lines = [f"# {taxonomy_name}", ""]
    if description:
        lines += [description, ""]
    for entry in unique:
        summary = _entry_summary(entry["path"])
        label = entry["title"]
        # Emit as a bare wikilink so linkify renders it with visible brackets,
        # matching the Render Bare Wikilinks with Visible Brackets Decision.
        if summary:
            lines.append(f"- [[{label}]] -- {summary}")
        else:
            lines.append(f"- [[{label}]]")
    lines.append("")
    lines.append(f"*{len(unique)} nodes in this section.*")
    return "\n".join(lines) + "\n"


def write_taxonomy_indexes(
    *,
    root: Path,
    build_dir: Path,
    slug_table: dict[str, dict],
    donors: list | None = None,
) -> None:
    donors = donors or []
    nodes_dir = root / "nodes"
    for taxonomy_name, taxonomy_slug in TAXONOMIES.items():
        tax_dir = nodes_dir / taxonomy_name
        if not tax_dir.is_dir():
            continue

        readme = tax_dir / "README.md"
        if readme.exists():
            markdown_source = readme.read_text(encoding="utf-8")
            source_rel = str(readme.relative_to(root))
        else:
            markdown_source = build_taxonomy_index(
                taxonomy_name=taxonomy_name,
                taxonomy_slug=taxonomy_slug,
                slug_table=slug_table,
            )
            source_rel = None

        linkified = linkify_text(markdown_source, slug_table, donors)
        _, body = strip_frontmatter(linkified)
        page = render_html(
            body,
            title=f"{taxonomy_name} - DeepContext",
            taxonomy_name=None,
            taxonomy_url=None,
            source_rel_path=source_rel,
        )

        out = build_dir / "nodes" / taxonomy_slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")


def _find_home_touch_point(root: Path) -> Path | None:
    """Find the Touch Point node with `is_home: true` in YAML frontmatter.

    Per Touch Point Form Contract: exactly one Touch Point per graph
    SHOULD carry `is_home: true`; the build pipeline renders it to the
    site root URL. Multiple homes are an error; zero homes degrades to
    a fallback (legacy `landing.md` at repo root, if present).
    """
    touch_points_dir = root / "nodes" / "Touch Points"
    if not touch_points_dir.is_dir():
        return None
    homes: list[Path] = []
    for md in sorted(touch_points_dir.glob("*.md")):
        meta, _ = strip_frontmatter(md.read_text(encoding="utf-8"))
        is_home = meta.get("is_home", "").strip().lower()
        if is_home == "true":
            homes.append(md)
    if len(homes) > 1:
        raise SystemExit(
            "Multiple Touch Points carry is_home: true: "
            + ", ".join(str(h.relative_to(root)) for h in homes)
        )
    return homes[0] if homes else None


def write_landing_page(
    *,
    root: Path,
    build_dir: Path,
    slug_table: dict[str, dict],
    donors: list | None = None,
) -> None:
    donors = donors or []
    # First preference: a Touch Point with is_home: true in frontmatter
    home = _find_home_touch_point(root)
    if home is None:
        # Fallback: legacy landing.md at repo root, retained transitionally
        # while the home page migration is in progress.
        legacy = root / "landing.md"
        if not legacy.exists():
            return
        home = legacy
    linkified = linkify_text(home.read_text(encoding="utf-8"), slug_table, donors)
    meta, body = strip_frontmatter(linkified)
    if meta.get("hide_identity_block", "").strip().lower() == "true":
        body = strip_identity_block(body)
    page = render_html(
        body,
        title="DeepContext",
        taxonomy_name=None,
        taxonomy_url=None,
        source_rel_path=str(home.relative_to(root)),
        is_home=True,
    )
    (build_dir / "index.html").write_text(page, encoding="utf-8")


def copy_style(*, root: Path, build_dir: Path) -> None:
    style_src = root / ".scripts" / "style.css"
    if not style_src.exists():
        return
    (build_dir / "style.css").write_text(style_src.read_text(encoding="utf-8"), encoding="utf-8")


def copy_attachments(*, root: Path, build_dir: Path) -> None:
    """Copy root-level Attachments/ tree into the build output.

    Images and other attachments referenced via Obsidian-style embeds
    (`![[Attachments/name.png]]`) resolve at render time to site-root URLs
    (`/Attachments/name.png`). This copy makes the paths live.
    """
    attachments_src = root / "Attachments"
    if not attachments_src.is_dir():
        return
    attachments_dest = build_dir / "Attachments"
    shutil.copytree(attachments_src, attachments_dest)


def write_nojekyll(build_dir: Path) -> None:
    (build_dir / ".nojekyll").write_text("", encoding="utf-8")


# Canonical hostname for GitHub Pages custom domain. Forks should set this to
# their own domain or to an empty string to disable custom-domain routing.
CUSTOM_DOMAIN = "eoscontinuum.com"


def write_cname(build_dir: Path) -> None:
    if not CUSTOM_DOMAIN:
        return
    (build_dir / "CNAME").write_text(CUSTOM_DOMAIN + "\n", encoding="utf-8")
