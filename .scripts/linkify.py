"""Rewrite wikilinks and image embeds in source markdown.

Transforms (in-memory; callers write to .build/ via render.py):
    [[Target]]              -> <a class="wikilink" href="/nodes/<tax>/<slug>/">[[Target]]</a>
    [[Target|Display]]      -> [Display](/nodes/<tax>/<slug>/)          (pipe drops brackets)
    [[Target]]              -> <span class="ghost-link">[[Target]]</span>
    [[Target]]\u2197          -> <span class="external-ref">[[Target]]\u2197</span>
    ![[Attachments/x.png]]  -> ![x](/Attachments/x.png)                 (Obsidian-style embed)
    ![[path.png|alt text]]  -> ![alt text](/path.png)                   (pipe sets alt)

Fenced code blocks and inline code spans are protected during the rewrite.
The image-embed form translates Obsidian's wikilink embed syntax into a
standard markdown image reference so python-markdown renders an <img> tag;
the path is resolved as site-root-relative (leading slash added) so embeds
work uniformly from the landing page and from any node-detail page.

The bare-wikilink form preserves `[[brackets]]` in the rendered output as a
deliberate convention so the source pattern stays legible on the site. The
piped form drops the brackets so the display text reads naturally in prose.
See Decision node 'Render Bare Wikilinks with Visible Brackets'.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

# Image-embed must run BEFORE the wikilink pattern, since `![[...]]` would
# otherwise match `[[...]]` with a stray `!` kept in front.
EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")
# Match [[...]] optionally followed by an external arrow.
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\](\u2197?)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")


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


def linkify_text(text: str, slug_table: dict[str, dict]) -> str:
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

        if arrow:
            # External marker: preserve verbatim, styled via span.
            return f'<span class="external-ref">[[{raw_target}]]\u2197</span>'

        if "|" in raw_target:
            target, display = raw_target.split("|", 1)
        else:
            target, display = raw_target, None

        target_stripped = target.strip()
        entry = slug_table.get(target_stripped)

        if entry is None:
            # Unresolved: render as ghost link span.
            return f'<span class="ghost-link">[[{raw_target}]]</span>'

        url = entry["url"]
        if display is not None:
            # Pipe wikilink: display text only, brackets dropped.
            return f"[{display.strip()}]({url})"
        # Bare wikilink: preserve [[brackets]] in the rendered link.
        target_escaped = html.escape(target.strip())
        return f'<a class="wikilink" href="{url}">[[{target_escaped}]]</a>'

    text = WIKILINK_RE.sub(_replace, text)

    for i, fence in enumerate(placeholders):
        text = text.replace(f"\x00FENCE{i}\x00", fence)

    return text


def linkify_file(path: Path, slug_table: dict[str, dict]) -> str:
    return linkify_text(path.read_text(encoding="utf-8"), slug_table)
