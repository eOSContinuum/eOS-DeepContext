"""Rewrite wikilinks and image embeds in source markdown.

Transforms (in-memory; callers write to .build/ via render.py):
    [[Target]]                       -> <a class="wikilink" href="/nodes/<tax>/<slug>/">[[Target]]</a>
    [[Target|Display]]               -> [Display](/nodes/<tax>/<slug>/)         (pipe drops brackets)
    [[Target]]                       -> <span class="ghost-link">[[Target]]</span>
    [[Target]]\u2197                   -> <span class="external-ref">[[Target]]\u2197</span>          (unresolved external)
    [[Taxonomy/Target]]\u2197          -> <a class="external-ref" href="<donor-url>/nodes/...">...</a>\u2197  (resolved against donor)
    ![[Attachments/x.png]]           -> ![x](/Attachments/x.png)                (Obsidian-style embed)
    ![[path.png|alt text]]           -> ![alt text](/path.png)                  (pipe sets alt)

Fenced code blocks and inline code spans are protected during the rewrite.
The image-embed form translates Obsidian's wikilink embed syntax into a
standard markdown image reference so python-markdown renders an <img> tag;
the path is resolved as site-root-relative (leading slash added) so embeds
work uniformly from the landing page and from any node-detail page.

The bare-wikilink form preserves `[[brackets]]` in the rendered output as a
deliberate convention so the source pattern stays legible on the site. The
piped form drops the brackets so the display text reads naturally in prose.
See Decision node 'Render Bare Wikilinks with Visible Brackets'.

External wikilinks (`[[Target]]\u2197`) without a taxonomy prefix render as
non-resolving spans (current behavior). External wikilinks with a taxonomy
prefix (`[[Decisions/Adopt Wikilinks and Named Edges]]\u2197`) resolve against
the first donor Reference node found in `nodes/References/` (a Reference
that carries both `this_did:` and `url:` in its frontmatter). The donor's
URL is combined with the slugified taxonomy and target to form a working
external link. This composes with the graft-vs-link distinction: nodes the
local LLM/build needs are grafted (local wikilinks resolve); nodes the
local graph cites but does not own are external (resolve to the donor's
published URL).
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from slugify import TAXONOMIES, slug_general, slug_predicate

# Image-embed must run BEFORE the wikilink pattern, since `![[...]]` would
# otherwise match `[[...]]` with a stray `!` kept in front.
EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")
# Match [[...]] optionally followed by an external arrow.
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\](\u2197?)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")


def _resolve_external_url(target: str, donors: list) -> str | None:
    """Resolve an external wikilink target against donor references.

    Accepts targets in `Taxonomy/Concept` form; returns the donor URL for
    the corresponding node if a donor is available, else None. Targets
    without a taxonomy prefix, with an unrecognized taxonomy, or with no
    donor in scope return None (caller falls back to non-resolving span).
    """
    if not donors or "/" not in target:
        return None
    taxonomy_part, _, target_part = target.partition("/")
    taxonomy_part = taxonomy_part.strip()
    target_part = target_part.strip()

    if taxonomy_part not in TAXONOMIES:
        return None

    # Reduce a full filename form (`Concept -- definition`) to the concept side.
    concept = target_part.split(" -- ", 1)[0].strip()
    if not concept:
        return None

    if taxonomy_part == "Predicates":
        slug = slug_predicate(concept)
    else:
        slug = slug_general(concept)

    if not slug:
        return None

    taxonomy_slug = TAXONOMIES[taxonomy_part]
    # Single-donor case: use the first donor. Multi-donor disambiguation
    # via explicit `[[donor:Taxonomy/Target]]\u2197` is a future extension.
    donor_url = donors[0]["url"].rstrip("/")
    return f"{donor_url}/nodes/{taxonomy_slug}/{slug}/"


def _replace_embed(m: re.Match[str]) -> str:
    inner = m.group(1).strip()
    if "|" in inner:
        path, alt = (p.strip() for p in inner.split("|", 1))
    else:
        path = inner
        alt = Path(path).stem
    if not path.lower().endswith(IMAGE_EXTS):
        # Only image embeds are translated; non-image embeds pass through
        # unchanged for future extension (transclusion, etc.).
        return m.group(0)
    url = "/" + path.lstrip("/")
    return f"![{alt}]({url})"


def linkify_text(
    text: str,
    slug_table: dict[str, dict],
    donors: list | None = None,
) -> str:
    donors = donors or []
    placeholders: list[str] = []

    def _save_fence(m: re.Match[str]) -> str:
        placeholders.append(m.group(0))
        return f"\x00FENCE{len(placeholders) - 1}\x00"

    text = FENCE_RE.sub(_save_fence, text)
    text = INLINE_CODE_RE.sub(_save_fence, text)

    text = EMBED_RE.sub(_replace_embed, text)

    def _replace(m: re.Match[str]) -> str:
        raw_target = m.group(1)
        arrow = m.group(2) or ""

        if "|" in raw_target:
            target_part, display = raw_target.split("|", 1)
        else:
            target_part, display = raw_target, None
        target_stripped = target_part.strip()

        if arrow:
            external_url = _resolve_external_url(target_stripped, donors)
            if external_url:
                # Resolved external: render as anchor with arrow inside
                # (one click target). Pipe form drops brackets; bare form
                # preserves them per Render Bare Wikilinks Decision.
                url_escaped = html.escape(external_url)
                if display is not None:
                    display_escaped = html.escape(display.strip())
                    return (
                        f'<a class="external-ref" href="{url_escaped}">'
                        f"{display_escaped}\u2197</a>"
                    )
                # Bare form: show the concept side (drop the taxonomy prefix
                # and any ` -- definition` suffix) inside preserved brackets.
                _, _, leaf = target_stripped.partition("/")
                concept = leaf.split(" -- ", 1)[0].strip() or target_stripped
                concept_escaped = html.escape(concept)
                return (
                    f'<a class="external-ref" href="{url_escaped}">'
                    f"[[{concept_escaped}]]\u2197</a>"
                )
            # Unresolved external (no donor, no taxonomy prefix, or
            # unrecognized taxonomy): preserve span behavior.
            return f'<span class="external-ref">[[{raw_target}]]\u2197</span>'

        entry = slug_table.get(target_stripped)
        if entry is None:
            # Unresolved local: render as ghost link span.
            return f'<span class="ghost-link">[[{raw_target}]]</span>'

        url = entry["url"]
        if display is not None:
            # Pipe wikilink: display text only, brackets dropped.
            return f"[{display.strip()}]({url})"
        # Bare wikilink: preserve [[brackets]] in the rendered link.
        target_escaped = html.escape(target_stripped)
        return f'<a class="wikilink" href="{url}">[[{target_escaped}]]</a>'

    text = WIKILINK_RE.sub(_replace, text)

    for i, fence in enumerate(placeholders):
        text = text.replace(f"\x00FENCE{i}\x00", fence)

    return text


def linkify_file(
    path: Path,
    slug_table: dict[str, dict],
    donors: list | None = None,
) -> str:
    return linkify_text(path.read_text(encoding="utf-8"), slug_table, donors)


_GRAFT_BULLET_RE = re.compile(
    r'^- grafted_from::<a class="wikilink" href="[^"]+">\[\[([^\]]+)\]\]</a>',
    re.MULTILINE,
)


def add_identity_graft_marker(
    text: str,
    *,
    donors: list,
    taxonomy_slug: str,
    node_slug: str,
) -> str:
    """Append a ⊕ marker to the identity-block grafted_from:: edge.

    Same UX as the global directory's graft markers — a reader of a
    grafted node sees one click to the donor's source for THIS specific
    node, not just the donor graph at large. The marker is added to the
    bullet line in the linkified markdown source; python-markdown carries
    it through into the rendered <li>.

    Only the line-anchored `- grafted_from::<linkified-wikilink>` form
    matches; backtick-coded mentions in prose or other-predicate
    references in Relations annotations are unaffected.
    """
    if not donors:
        return text

    def _replace(match: re.Match) -> str:
        donor_target = match.group(1).strip()
        donor_concept = donor_target.split(" -- ", 1)[0].strip()
        donor_url: str | None = None
        for d in donors:
            if (
                d["name"] == donor_target
                or d["name"].split(" -- ", 1)[0].strip() == donor_concept
            ):
                donor_url = d["url"].rstrip("/")
                break
        if not donor_url:
            return match.group(0)
        source_url = f"{donor_url}/nodes/{taxonomy_slug}/{node_slug}/"
        marker = (
            f' <a class="graft-marker" href="{html.escape(source_url)}"'
            f' title="Grafted from {html.escape(donor_target)}">⊕</a>'
        )
        return match.group(0) + marker

    return _GRAFT_BULLET_RE.sub(_replace, text, count=1)
