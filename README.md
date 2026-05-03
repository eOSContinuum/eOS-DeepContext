# eOS-DeepContext

A typed knowledge graph capturing the architectural case for an image-
persistent runtime substrate for agentic AI. Plain-markdown nodes with
named-edge predicates carry the values, patterns, decisions, observations,
and convictions that anchor the [eOS Continuum](https://github.com/eOSContinuum)
project.

The published site is the reader-facing view, served at
[eoscontinuum.com](https://eoscontinuum.com/) (HTTPS provisions
automatically once GitHub completes domain verification; the github.io
URL works during provisioning). This README is the GitHub-facing view:
what you need to read, build, or contribute.

## Status

In progress. The meta-layer is in place (12 Form Contracts, 11 Predicates,
7 generic graph-operation Skills under [`nodes/`](nodes/)). [`landing.md`](landing.md)
carries the project's current public framing -- the substrate-vs-glue
diagnostic, the eight runtime primitives with orthogonal persistence as
foundational, the harness-as-tool inversion, five-axis containment for
LLM-authored code, the lineage and the demonstration target. 14 Reference
stubs in [`nodes/References/`](nodes/References/) capture supporting
evidence from the recent agentic-runtime literature (Recursive Language
Models and its successors, ClawVM and the harness-managed-virtual-memory
lineage, MemGPT-through-MemMachine agent-memory work, the DSPy / Khattab
axis, the Compound AI Systems framing).

What is forthcoming:

- **Founding Decision and grounding Convictions** -- the load-bearing
  architectural commitments this graph rests on. The eight runtime-
  primitive Convictions named in `landing.md` are currently ghost links
  (most exist in the `eos-harness` graph and will scion or be authored
  fresh here, with the architectural-hierarchy reordering -- orthogonal
  persistence as foundational, others derived -- applied at migration).
- **Content nodes** -- Decisions, Aspirations, Observations, Patterns
  elaborating the architectural argument. Three customer-pattern Patterns
  named in `landing.md` belong in `nodes/Patterns/` once authored.
- **Reference stub bodies** -- the 14 Reference stubs are minimal;
  Adopted / Not adopted detail and per-feature correspondence to substrate
  primitives is to be expanded.

The static-site build pipeline at [`.scripts/`](.scripts/) ports unmodified
from [ChristopherA/DeepContext.com](https://github.com/ChristopherA/DeepContext.com).
CI deploys to GitHub Pages on push to `main`.

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

## Contributing

eOS-DeepContext is open to contributions. The workflow:

1. **Fork** the repository to your account or organization.
2. **Clone** your fork locally.
3. **Read** [`AGENTS.md`](AGENTS.md) for the graph conventions, the
   authoring stance, and the form-contract obligations each node form
   carries. The `Graph Orient` Skill at
   [`nodes/Skills/Graph Orient/`](nodes/Skills/Graph%20Orient/) walks the
   first-entry orientation.
4. **Branch** for the change (`feature/<short-name>` or `add-<node>` are
   reasonable conventions). Atomic, focused branches review faster.
5. **Author or edit** nodes per the form contract for the relevant node
   form. Run the `Node Validate` Skill on each authored or modified node;
   the validator catches structural deviations from the form contract.
6. **Commit signed**: `git commit -S -s -m "<message>"`. The repository's
   Open Integrity inception established a signed-commit chain; signed
   commits keep the chain intact.
7. **Push** to your fork.
8. **Open a pull request** against `main` of
   `eOSContinuum/eOS-DeepContext`. Reference the relevant nodes (existing
   or newly authored) in the PR description.
9. **Review and merge** by [@ChristopherA](https://github.com/ChristopherA),
   who maintains `main`. Larger architectural proposals (new Conviction
   sets, graph-restructure work, new Decisions with load-bearing
   Alternatives) may benefit from an open issue or discussion before
   authoring nodes.

For agent-driven contributions, point your LLM harness at
[`AGENTS.md`](AGENTS.md). The file carries the orientation an agent needs
to make changes that fit the graph's conventions, including the
contributing workflow above with the agent-specific Skill invocations
and behavior imperatives.

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
git clone https://github.com/eOSContinuum/eOS-DeepContext my-graph
cd my-graph
sh .scripts/graph-inception.sh
```

The Graph Inception script removes the cloned `.git`, runs
`oi-inception.sh` to produce a fresh signed inception commit, updates
`.deep-context-identity.yml` so `this_did` carries the new SHA1 and
leaves `scion_of: null` (the new graph is its own thing, not a scion of
this one), and stages plus commits the working tree as the new graph's
first content commit. Pass `--claim-scion-of` to claim scion-of lineage
from this graph (the rare parallel-fork-tracking case); otherwise
`scion_of:` stays null and per-node graft provenance can be recorded
via `grafted_from::` edges.

After the ceremony, push the new graph to its own GitHub repository under
the first steward's account or organization.

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
