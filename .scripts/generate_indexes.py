"""Generate per-taxonomy index pages.

For each taxonomy folder under nodes/:
- If a README.md exists in the folder, render it as the taxonomy index (hand-authored).
- Else, walk the folder and build a list page from each node's tagline/brief_summary.
"""

from __future__ import annotations

import re
import shutil
from collections import defaultdict
from pathlib import Path

from linkify import linkify_text
from render import render_html, strip_frontmatter, strip_identity_block
from site_config import CUSTOM_DOMAIN, SITE_NAME
from slugify import TAXONOMIES

GRAFT_MARKER = "⊕"  # ⊕

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


_GRAFTED_FROM_RE = re.compile(r"^- grafted_from::\[\[(.+?)\]\]", re.MULTILINE)


def _node_donor(path: Path, donors: list) -> tuple[str, str] | None:
    """Return (donor_name, donor_url) if the node carries a grafted_from:: edge.

    Looks for the first identity-block bullet of shape `- grafted_from::[[<name>]]`,
    resolves that name against the donor table built from References, and returns
    the donor's site URL. Returns None when the node is not grafted or the donor
    cannot be resolved.
    """
    if not donors:
        return None
    text = path.read_text(encoding="utf-8")
    m = _GRAFTED_FROM_RE.search(text)
    if not m:
        return None
    target = m.group(1).strip()
    # Donor table entries have name = filename stem; the wikilink may be the
    # full stem or the concept side.
    target_concept = target.split(" -- ", 1)[0].strip()
    for d in donors:
        if d["name"] == target or d["name"].split(" -- ", 1)[0].strip() == target_concept:
            return (d["name"], d["url"].rstrip("/"))
    return None


TAXONOMY_SINGULAR: dict[str, str] = {
    "Aspirations": "Aspiration",
    "Contracts": "Contract",
    "Convictions": "Conviction",
    "Decisions": "Decision",
    "Glosses": "Gloss",
    "Observations": "Observation",
    "Patterns": "Pattern",
    "Predicates": "Predicate",
    "References": "Reference",
    "Skills": "Skill",
    "Touch Points": "Touch Point",
}


def build_node_directory(*, slug_table: dict[str, dict], donors: list) -> str:
    """Build markdown for the global Browse-all-nodes directory.

    Two surfaces, one page:
    - **By form type** — compact list of taxonomies linking to each
      taxonomy index page. The "drill into one form" workflow.
    - **All nodes** — single alphabetical list across the whole graph,
      each entry showing form chip + tagline. The "find by name" workflow.

    The graft marker (⊕) appears on nodes carrying a grafted_from:: edge,
    linking to the donor's source URL for that node so the lineage is
    one click away.
    """
    # Collect every unique node, dedup by path.
    by_tax: dict[str, list[dict]] = defaultdict(list)
    seen: set[Path] = set()
    for entry in slug_table.values():
        if entry["path"] in seen:
            continue
        seen.add(entry["path"])
        by_tax[entry["taxonomy_name"]].append(entry)

    total = sum(len(v) for v in by_tax.values())
    all_entries: list[dict] = []
    for tax_entries in by_tax.values():
        all_entries.extend(tax_entries)

    has_grafts = any(_node_donor(e["path"], donors) for e in all_entries)

    lines = [
        "# Browse all nodes",
        "",
        f"Every node in this graph. {total} nodes across {len(by_tax)} form types.",
        "",
    ]
    if has_grafts:
        lines.append(
            f"Entries marked **{GRAFT_MARKER}** were grafted from a donor graph; the marker links to the donor's source for that node."
        )
        lines.append("")

    # Section 1: Form types — compact navigation hub.
    lines.append("## By form type")
    lines.append("")
    lines.append(
        "Each form type has its own index page listing nodes of that form with their summaries. Use this when you want to drill into a specific form."
    )
    lines.append("")
    for tax_name, tax_slug in TAXONOMIES.items():
        if tax_name not in by_tax:
            continue
        count = len(by_tax[tax_name])
        description = TAXONOMY_DESCRIPTIONS.get(tax_name, "")
        line = f"- [{tax_name}](/nodes/{tax_slug}/) ({count})"
        if description:
            line += f" — {description}"
        lines.append(line)
    lines.append("")

    # Section 2: Alphabetical flat list — find-by-name workflow.
    lines.append(f"## All nodes alphabetically ({total})")
    lines.append("")
    lines.append(
        "Every node in one list, sorted by title. Each entry shows its form type so you can tell what kind of node it is. Use this when you remember a name but not the form, or when you want to scan the whole graph at once."
    )
    lines.append("")
    alphabetical = sorted(all_entries, key=lambda e: e["title"].lower())
    for entry in alphabetical:
        label = entry["title"]
        url = entry["url"]
        tax_name = entry["taxonomy_name"]
        tax_slug = TAXONOMIES.get(tax_name, entry["taxonomy"])
        form_singular = TAXONOMY_SINGULAR.get(tax_name, tax_name)
        tagline = _entry_summary(entry["path"])
        graft = ""
        donor = _node_donor(entry["path"], donors)
        if donor:
            donor_name, donor_url = donor
            donor_node_url = f"{donor_url}/nodes/{tax_slug}/{entry['slug']}/"
            graft = f' [{GRAFT_MARKER}]({donor_node_url} "Grafted from {donor_name}")'
        line = f"- [{label}]({url}) — *{form_singular}*"
        if tagline:
            line += f" — {tagline}"
        line += graft
        lines.append(line)
    lines.append("")

    return "\n".join(lines) + "\n"


def write_node_directory(
    *,
    root: Path,
    build_dir: Path,
    slug_table: dict[str, dict],
    donors: list | None = None,
) -> None:
    """Emit the global node directory at /nodes/index.html."""
    donors = donors or []
    markdown_source = build_node_directory(slug_table=slug_table, donors=donors)
    linkified = linkify_text(markdown_source, slug_table, donors)
    _, body = strip_frontmatter(linkified)
    page = render_html(
        body,
        title=f"Browse all nodes - {SITE_NAME}",
        taxonomy_name=None,
        taxonomy_url=None,
        source_rel_path=None,
        is_browse=True,
    )
    out = build_dir / "nodes" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")


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
            title=f"{taxonomy_name} - {SITE_NAME}",
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
        title=SITE_NAME,
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


def write_cname(build_dir: Path) -> None:
    if not CUSTOM_DOMAIN:
        return
    (build_dir / "CNAME").write_text(CUSTOM_DOMAIN + "\n", encoding="utf-8")
