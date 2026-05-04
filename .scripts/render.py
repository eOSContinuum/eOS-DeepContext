"""Render a linkified markdown string to HTML using python-markdown."""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

import markdown

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

MD_EXTENSIONS = ["tables", "fenced_code", "attr_list", "sane_lists"]

BULLET_RE = re.compile(r"^( {0,4})([*+\-]|\d+[.)]) ")

# Site brand displayed in crumb and footer. Forks should set this to their
# own name.
SITE_NAME = "eOS-DeepContext"

# GitHub source link for the "Edit on GitHub" footer widget. Scions should set
# GITHUB_REPO_URL to their own repo or to an empty string to suppress the link.
GITHUB_REPO_URL = "https://github.com/eOSContinuum/eOS-DeepContext"
GITHUB_BRANCH = "main"

# OI inception DID for this repo, of the form did:repo:<sha1-of-root-commit>.
# Set by build.py via compute_inception_did() before rendering. Scions get
# their own DID automatically because their root commit differs; no hardcoded
# value needs updating.
INCEPTION_DID: str | None = None


def compute_inception_did(root: Path) -> str | None:
    """Return the did:repo:<sha1> of the repo's OI inception commit, or None.

    The inception commit is the repo's root commit (no parents). Shallow
    clones do not have it; the Actions workflow uses fetch-depth: 0 so CI
    builds can compute this. When the value cannot be computed, the footer
    simply omits the DID widget.
    """
    try:
        result = subprocess.run(
            ["git", "rev-list", "--max-parents=0", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=str(root),
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    shas = result.stdout.strip().splitlines()
    if not shas:
        return None
    return f"did:repo:{shas[0]}"


def normalize_list_indents(text: str) -> str:
    """Convert 2-space bullet-indent under a list item to 4-space (python-markdown nesting).

    The graph's convention puts annotation bullets directly below a predicate bullet
    at 2-space indent; python-markdown needs 4-space indent to nest lists. We promote
    only the 2-space case — anything already at 4+ is left untouched.
    """
    out: list[str] = []
    in_list = False

    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        m = BULLET_RE.match(stripped)
        if m:
            indent = len(m.group(1))
            if indent == 2 and in_list:
                out.append("    " + stripped[2:] + "\n")
            else:
                in_list = True
                out.append(line)
        else:
            # Continuation lines inside a list item: keep current in_list state.
            # A fully blank line ends the list.
            if stripped.strip() == "":
                in_list = False
            out.append(line)

    return "".join(out)


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end():]
    raw = m.group(1)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        meta[key] = value
    return meta, body


def strip_identity_block(body: str) -> str:
    """Strip the leading identity-block bullets from a node body.

    The identity block is the bullet list between the YAML frontmatter and
    the H1 -- bullets like `- conforms_to::[[X]]`, `- in_practice_domain::[[Y]]`,
    etc. Reader-facing forms (notably Touch Point) opt to hide these from
    the rendered output via `hide_identity_block: true` in their frontmatter,
    so the page reads as orientation prose rather than as a technical
    predicate dump.

    Strip skips leading blank lines, then drops every consecutive bullet
    line (starting with `- ` or `* `) until a non-bullet, non-blank line is
    reached. The H1 (and everything after) is preserved as-is.
    """
    lines = body.splitlines(keepends=True)
    out: list[str] = []
    in_block = False
    block_done = False
    for line in lines:
        if block_done:
            out.append(line)
            continue
        stripped = line.lstrip()
        if not in_block:
            if stripped == "" or stripped.startswith("\n"):
                # Leading blank line — preserve and keep looking
                out.append(line)
                continue
            if stripped.startswith("- ") or stripped.startswith("* "):
                in_block = True
                # Drop the bullet line
                continue
            # First non-blank, non-bullet line before any bullets — no
            # identity block to strip; keep the line and stop looking.
            block_done = True
            out.append(line)
            continue
        # Inside the block
        if stripped == "" or stripped.startswith("\n"):
            # Blank line ends the block
            block_done = True
            out.append(line)
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            # Continuation of the identity-block bullets — drop
            continue
        # Non-bullet, non-blank line ends the block
        block_done = True
        out.append(line)
    return "".join(out)


def render_html(
    markdown_body: str,
    *,
    title: str,
    taxonomy_name: str | None,
    taxonomy_url: str | None,
    source_rel_path: str | None = None,
    style_href: str = "/style.css",
    is_home: bool = False,
) -> str:
    normalized = normalize_list_indents(markdown_body)
    html_body = markdown.markdown(normalized, extensions=MD_EXTENSIONS)

    crumb = ""
    if not is_home:
        segments = [f'<a href="/">{html.escape(SITE_NAME)}</a>']
        if taxonomy_name and taxonomy_url:
            segments.append(
                f'<a href="{html.escape(taxonomy_url)}">{html.escape(taxonomy_name)}</a>'
            )
        crumb = '<nav class="crumb">' + " / ".join(segments) + "</nav>"

    source_link = ""
    if source_rel_path and GITHUB_REPO_URL:
        encoded = quote(source_rel_path, safe="/")
        source_url = f"{GITHUB_REPO_URL}/blob/{GITHUB_BRANCH}/{encoded}"
        source_link = (
            f'<a class="source-link" href="{html.escape(source_url)}">'
            "Edit on GitHub</a>"
        )

    did_widget = ""
    if INCEPTION_DID:
        short_hash = INCEPTION_DID[len("did:repo:"):len("did:repo:") + 8]
        if source_rel_path:
            # Scion Address: compound DID of the form did:repo:<sha1>/<url-encoded-path>
            # (W3C DID-URL path syntax, host-agnostic — no /blob/main/ insert).
            encoded_path = quote(source_rel_path, safe="/")
            full_did = f"{INCEPTION_DID}/{encoded_path}"
            basename = source_rel_path.split("/")[-1]
            if basename.endswith(".md"):
                basename = basename[:-3]
            short_display = f"did:repo:{short_hash}…/{basename}"
        else:
            # Generated taxonomy indexes have no source_rel_path; fall back to
            # the repo-level DID.
            full_did = INCEPTION_DID
            short_display = f"did:repo:{short_hash}…"
        did_widget = (
            f'<a class="did-link" href="{html.escape(full_did)}" '
            f'title="{html.escape(full_did)}">'
            f"{html.escape(short_display)}</a>"
        )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{html.escape(style_href)}">
</head>
<body>
<header>{crumb}</header>
<main>
{html_body}
</main>
<footer><a href="/">{html.escape(SITE_NAME)}</a>{did_widget}{source_link}</footer>
</body>
</html>
"""


def render_file(
    source_path: Path,
    linkified_text: str,
    *,
    title: str,
    taxonomy_name: str | None,
    taxonomy_url: str | None,
    source_rel_path: str | None = None,
) -> str:
    meta, body = strip_frontmatter(linkified_text)
    if meta.get("hide_identity_block", "").strip().lower() == "true":
        body = strip_identity_block(body)
    return render_html(
        body,
        title=title,
        taxonomy_name=taxonomy_name,
        taxonomy_url=taxonomy_url,
        source_rel_path=source_rel_path,
    )
