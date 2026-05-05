"""Per-graph site configuration.

The other modules in `.scripts/` are intended to be byte-identical between
graphs that share this build pipeline; configuration that legitimately
varies per graph lives only here. When grafting build scripts from a donor
graph, do not graft this file -- each graph commits its own values.

Adding a new per-graph constant: add it here, import it from the canonical
script that needs it, and verify `diff -rq .scripts/` between peer graphs
still shows only this file as differing.
"""

# Site brand displayed in crumb and footer.
SITE_NAME = "eOS-DeepContext"

# GitHub source link for the "Edit on GitHub" footer widget. Set to an
# empty string to suppress the link.
GITHUB_REPO_URL = "https://github.com/eOSContinuum/eOS-DeepContext"

# Hostname for the GitHub Pages CNAME file. Set to an empty string for
# default *.github.io hosting (no CNAME emitted).
CUSTOM_DOMAIN = "eoscontinuum.com"
