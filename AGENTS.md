# AGENTS

Orientation for AI agents working on this graph. Read this first; then open
the Contracts under `nodes/Contracts/` for the structural rules, and the
landing page (forthcoming) for the project's framing.

## The graph in one paragraph

eOS-DeepContext is a typed knowledge graph that captures the architectural
case for an image-persistent runtime substrate for agentic AI -- the values,
patterns, decisions with their alternatives and revisit conditions,
observations with their epistemic grounds, convictions with their drift
recognition. Each node is a plain-markdown file with a block of identity
predicates above the H1, a body shaped by the node's form contract, and a
`## Relations` section carrying typed edges to other nodes. The graph is a
scion of [ChristopherA/DeepContext.com](https://github.com/ChristopherA/DeepContext.com)
(`scion_of: did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae`); meta-layer
Contracts, Predicates, and generic graph-operation Skills are inherited.

## Status

Pre-content. The meta-layer (12 Form Contracts, 11 Predicates, 7 generic
Skills) is in place under `nodes/`. The static-site build pipeline at
`.scripts/` ports unmodified from upstream; CI builds via GitHub Actions
deploy to GitHub Pages on push to `main`.

What is forthcoming:

- **`landing.md`** -- the project's public framing. Derived from the eOS
  Continuum project's most current concept briefs (the agentic-runtime
  concept brief and its slides) integrating supporting evidence from the
  recent agentic-runtime literature (Recursive Language Models and its
  successors, ClawVM and the harness-managed-virtual-memory lineage,
  MemGPT-through-MemMachine agent-memory work, Compound AI Systems framing).
- **Founding Decision and grounding Convictions** -- the load-bearing
  architectural commitments this graph rests on. Authored once `landing.md`
  establishes the framing.
- **Content nodes** -- Decisions, Convictions, Aspirations, References,
  Observations, Patterns elaborating the architectural argument. Some will
  scion from work currently held in the `eos-harness` graph; some will be
  authored fresh.

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
   AGENTS.md, `landing.md` (when present), the Contracts at identity-block
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

## Build and deploy

Local build with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python .scripts/build.py
```

Output lands in `.build/` (gitignored). CI deploys to GitHub Pages on push
to `main` via `.github/workflows/build-and-deploy.yml`. The CI workflow
verifies `.scion-identity.yml`'s `this_did:` matches the repository's root
commit SHA before deploying, so a freshly-bootstrapped scion cannot
publish under the parent template's DID by accident.
