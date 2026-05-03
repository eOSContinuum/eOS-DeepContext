# eOS-DeepContext

A typed knowledge graph capturing the architectural case for an image-
persistent runtime substrate for agentic AI. Plain-markdown nodes with
named-edge predicates carry the values, patterns, decisions, observations,
and convictions that anchor the [eOS Continuum](https://github.com/eOSContinuum)
project.

The published site is the reader-facing view (forthcoming on push-to-main
deploy via GitHub Pages); this README is the GitHub-facing view: what you
need to stand up, build, or contribute.

## Status

Pre-content. The meta-layer (12 Form Contracts, 11 Predicates, 7 generic
graph-operation Skills) is in place under `nodes/`. The static-site build
pipeline at `.scripts/` ports unmodified from
[ChristopherA/DeepContext.com](https://github.com/ChristopherA/DeepContext.com).
CI deploys to GitHub Pages on push to `main`.

A landing page (`landing.md`) is forthcoming -- derived from the eOS
Continuum project's most current concept briefs (the agentic-runtime concept
brief and its slides) integrating supporting evidence from the recent
agentic-runtime literature.

## Lineage

This graph is a scion of [ChristopherA/DeepContext.com](https://github.com/ChristopherA/DeepContext.com).
Its meta-layer (Contracts, Predicates, generic graph-operation Skills) is
inherited from the parent template; content nodes will be authored to carry
the eOS Continuum project's architectural argument.

- `this_did: did:repo:9dc47a293f5b2352dba288b3e2ef9c73c508ca0f`
- `scion_of: did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae`

The `did:repo:<sha1>` form is W3C DID-URL-style identifier where the SHA1
is the repository's Open Integrity inception commit -- a signed empty root
commit that cryptographically binds the repository's identity to its
founding key.

## Build

Local build with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python .scripts/build.py
```

Output lands in `.build/` (gitignored). The build pipeline:

1. Walks `nodes/<Taxonomy>/` to build a slug table (`slugify.py`).
2. Linkifies wikilinks against the slug table (`linkify.py`).
3. Renders each node to HTML (`render.py`) with title, taxonomy crumb,
   "Edit on GitHub" link, and DID footer widget.
4. Generates per-taxonomy index pages (`generate_indexes.py`).
5. Renders `landing.md` to `index.html` (when present).
6. Copies `style.css` and `Attachments/` (when present) into the build
   output.
7. Emits `.agents/skills/<runtime-name>/SKILL.md` and
   `.claude/skills/<runtime-name>/SKILL.md` symlink trees pointing at
   `nodes/Skills/<Title>/<Title>.md` for runtime discoverability.

## Scioning

A DeepContext **scion** is a repository whose content began as a clone of
another DeepContext graph and was re-rooted locally with its own Open
Integrity inception commit. Each scion has its own `did:repo:<sha1>` DID,
its own Pages site, and its own content to diverge as its first steward
sees fit.

Standing up a scion is a local ceremony. The inception commit must be
signed by the first steward's own SSH key; no one-click GitHub path works
because Actions cannot sign as the steward. The template-repository
setting on this repository is intentionally not enabled.

### Prerequisites

- `git config user.name`, `git config user.email`, and
  `git config user.signingkey` set; the corresponding SSH public key
  registered for signing at <https://github.com/settings/ssh/signing>.
- `ssh-keygen` on PATH (standard on macOS and most Linux).
- `gh` CLI authenticated; or manual `git push` with the new GitHub remote.

### Ceremony

```sh
git clone https://github.com/eOSContinuum/eOS-DeepContext my-scion
cd my-scion
sh .scripts/scion-bootstrap.sh
```

The Scion Bootstrap script removes the cloned `.git`, runs
`scion-inception.sh` to produce a fresh signed inception commit, updates
`.scion-identity.yml` so `this_did` carries the new SHA1 and `scion_of`
carries this template's `this_did`, and stages plus commits the working
tree as the scion's first content commit.

After the ceremony, push the scion to its own GitHub repository under the
first steward's account or organization.

## Graph conventions

See [AGENTS.md](AGENTS.md) for agent-orientation framing and the short-form
conventions. The form contracts under `nodes/Contracts/` carry the
structural rules for each node form; the Predicate Glosses under
`nodes/Predicates/` define the typed-edge vocabulary the graph speaks.

## License

License posture is to be declared. The
[eOS Continuum](https://github.com/eOSContinuum) project's preferred
direction is BSD-2-Clause-Patent at the application layer; eOS-DeepContext's
declaration is pending alongside the founding-Decision authoring work.
