# AGENTS

Orientation for AI agents working on this graph. Read this first; then open
the Contracts under `nodes/Contracts/` for the structural rules, and
[the home Touch Point](nodes/Touch%20Points/eOS%20Continuum%20Welcome.md) for the project's framing.

## The graph in one paragraph

eOS-DeepContext is a typed knowledge graph that captures the architectural
case for an image-persistent runtime substrate for agentic AI -- the values,
patterns, decisions with their alternatives and revisit conditions,
observations with their epistemic grounds, convictions with their drift
recognition. Each node is a plain-markdown file with a block of identity
predicates above the H1, a body shaped by the node's form contract, and a
`## Relations` section carrying typed edges to other nodes. The graph is
its own Deep Context graph (not a scion of any other graph); meta-layer
Contracts, Predicates, and generic graph-operation Skills were **grafted**
from [ChristopherA/DeepContext.com](https://github.com/ChristopherA/DeepContext.com)
at instantiation, with per-node graft provenance recorded via the
`grafted_from::` predicate.

## Status

In progress. The meta-layer is in place (13 Form Contracts including the
eOS-specific Inquiry Form, 18 Predicates, 8 generic Skills under `nodes/`).
[The home Touch Point](nodes/Touch%20Points/eOS%20Continuum%20Welcome.md) carries the
project's current public framing. 14 Reference stubs in
[`nodes/References/`](nodes/References/) capture supporting evidence from
the recent agentic-runtime literature (Recursive Language Models and its
successors, ClawVM and the harness-managed-virtual-memory lineage,
MemGPT-through-MemMachine agent-memory work, the Khattab axis of DSPy
plus DSPy Agent Skills, the Compound AI Systems framing, plus the Prime
Intellect endorsement of long-horizon agent-task framing).

What is forthcoming:

- **Founding Decision and grounding Convictions** -- the load-bearing
  architectural commitments this graph rests on, including the eight
  runtime-primitive Convictions named in the home Touch Point. Most exist in the
  `eos-harness` graph and will be grafted or authored fresh here. The
  architectural-hierarchy reordering -- orthogonal persistence as
  foundational, the other seven `grounded_in::` it -- applies at
  migration time.
- **Content nodes** -- Decisions, Aspirations, Observations, and Patterns
  elaborating the architectural argument. Three customer-pattern Patterns
  named in the home Touch Point (customer-authored automation in a SaaS product,
  long-running stateful workflows, AI-authored tools and durable agent
  memory) belong in `nodes/Patterns/` once authored.
- **Reference stub bodies** -- the 14 Reference stubs are minimal;
  Adopted / Not adopted detail and per-feature correspondence to substrate
  primitives is to be expanded.

The static-site build pipeline at `.scripts/` ports unmodified from
upstream; CI builds via GitHub Actions deploy to GitHub Pages on push to
`main`. The site is served at [eoscontinuum.com](https://eoscontinuum.com/).

## Graph conventions (short form)

- Nodes live in `nodes/<Taxonomy>/` where taxonomy is one of Contracts,
  Decisions, Convictions, Aspirations, Observations, Patterns, Predicates,
  Glosses, References, Skills.
- Wikilinks: `[[Target]]` resolves by filename stem (or by the concept
  side of a `Concept -- definition` Gloss or Predicate). Pipe form
  `[[Target|Display]]` shows the alias. External marker `[[Target]]↗`
  names a concept in another graph. The external marker uses the actual
  `↗` character (U+2197 NORTH EAST ARROW) in source text -- not the
  escape `↗`, which renders literally.
- Named edges: `predicate::[[Target]]` bullets in the identity block and
  in the `## Relations` section carry the graph's typed structure. Each
  Relations-section edge carries an indented annotation explaining why
  the edge matters -- unannotated edges are tag spaghetti, not graph.
- Each Predicate under `nodes/Predicates/` defines its own typed edge with
  a Carries section (what the predicate asserts), a per-neighbor Crescent
  section (what it holds that near-neighbors do not), and Typing (what
  kinds of nodes it connects).

Detailed specs: `nodes/Contracts/Markdown Node Contract.md` is the base
that every node form extends. Form-specific Contracts (Aspiration, Conviction,
Decision, Gloss, Inquiry, Observation, Pattern, Predicate, Reference, Skill)
add structural requirements per form.

## Role for agents

The project's stance on agent behavior follows the broader DeepContext
tradition: curate, translate, name what is rather than what tradition makes
of it.

**Curate, do not overwrite.** Suggest annotations, flag conflation, propose
upgrades to construction predicates. Never rewrite a contributor's
vocabulary without explicit confirmation.

**Translate across vocabularies rather than normalize them.** When two
contributors use different terms for adjacent territory, both edges land
in the graph as distinct claims. Read across them; do not collapse them
into a canonical form.

**Name features, not traditions.** Predicates carry what they assert today
within this graph -- not what tradition (RDF, Linked Data, schema.org)
makes them carry. The graph's vocabulary is a tool kit the contributors
choose, not a standard imposed from outside.

**Treat new common vocabulary as proposal.** When introducing a predicate
not yet backed by a node in `nodes/Predicates/`, the Skill `Predicate
Propose` walks the proposal: establish the axis, check existing
vocabulary, identify near-neighbors, draft a Predicate node.

**Preserve reasoning in the form.** Decisions carry Why, Alternatives
Considered, and What Would Change It. Observations carry epistemic status.
Convictions carry Drift Recognition. The forms exist so reasoning survives
the moment of authorship.

**Remain authored-by, not authoring.** The graph's claims belong to the
contributors who hold them, not to the assistant that renders them.

## First operations

For an agent entering this graph:

1. Run the `Graph Orient` Skill (`nodes/Skills/Graph Orient/`) to walk
   AGENTS.md, the home Touch Point, the Contracts at identity-block
   scale, the Convictions, and the Predicate vocabulary in a prescribed
   cheap-read order before any task work.
2. Read the form Contract for the node form you intend to author or edit
   (`Conviction Form Contract`, `Decision Form Contract`, etc.). The
   Contracts are the thinnest, most authoritative description of what each
   node form must satisfy.
3. Check `nodes/Predicates/` before introducing new typed edges. If the
   relation does not fit an existing predicate, use `Predicate Propose` to
   author a backing Predicate node before claiming the edge in a relations
   bullet.

## Contributing changes

The repo is fork-and-PR. To contribute (whether you are a human running an
agent or working directly):

1. **Fork** to your account or organization. Clone your fork locally.
2. **Run the `Graph Orient` Skill** to walk this file plus
   [the home Touch Point](nodes/Touch%20Points/eOS%20Continuum%20Welcome.md), the form Contracts at identity-block scale,
   the Convictions when authored, and the Predicate vocabulary -- the
   cheapest read that produces enough context for the operations that
   follow.
3. **Branch** for the change (`feature/<short-name>` or `add-<node>` are
   reasonable conventions). Atomic, focused branches review faster.
4. **Author or edit** nodes per the form Contract for the relevant node
   form -- `Conviction Form Contract`, `Decision Form Contract`, and so
   on. Each form's Requirements are the authoritative test of what the
   node must satisfy.
5. **Run `Node Validate`** on each authored or modified node. The
   validator catches structural deviations from the form Contract --
   filename pattern, identity block, body shape, named-edge syntax.
6. **Check `Predicate Propose`** before introducing typed edges that are
   not backed by an existing node in `nodes/Predicates/`. The skill walks
   the proposal: establish the axis the predicate answers, check existing
   vocabulary, identify near-neighbors, draft a Predicate node before
   claiming the edge.
7. **Commit signed**: `git commit -S -s -m "<message>"`. The repository's
   Open Integrity inception established a signed-commit chain; signed
   commits keep the chain intact.
8. **Push** to your fork.
9. **Open a pull request** against `main` of
   `eOSContinuum/eOS-DeepContext`. Reference the relevant nodes (existing
   or newly authored) in the PR description.
10. **Review and merge** by [@ChristopherA](https://github.com/ChristopherA),
    who maintains `main`. Larger architectural proposals (new Conviction
    sets, new Decisions with load-bearing Alternatives, graph-restructure
    work) may benefit from an open issue or discussion before authoring.

For LLM-driven contributions, point the harness at this file. The
conventions stated above plus the form Contracts plus the Skills
(`Graph Orient`, `Node Read`, `Node Create`, `Node Validate`,
`Predicate Propose`, `Graph Audit`, `Graph Load Audit`) are the operative
instruction set. The Curate-not-overwrite, Translate-not-normalize,
Name-features-not-traditions, and Authored-by-not-authoring imperatives
stated above govern agent behavior. If your harness needs a more
prescriptive workflow than this section provides, consider authoring a
`Contribute to eOS-DeepContext` Skill at `nodes/Skills/` that walks the
fork-branch-author-validate-commit-push-PR sequence with explicit Skill
invocations between each step; until then, this section is the
authoritative instruction set.

## Build and deploy

Local build with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python .scripts/build.py
```

Output lands in `.build/` (gitignored). CI deploys to GitHub Pages on push
to `main` via `.github/workflows/build-and-deploy.yml`. The CI workflow
verifies `.deep-context-identity.yml`'s `this_did:` matches the repository's
root commit SHA before deploying, so a freshly-incepted graph cannot
publish under any donor graph's DID by accident.
