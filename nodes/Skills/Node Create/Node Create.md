---
runtime_name: node-create
tagline: Authors a new node conforming to the form Contract it claims: filename pattern, identity predicate block, required body sections, annotated Relations edges
description: |
  Authors a new node conforming to this graph's Markdown Node Contract and the form-specific contract the new node claims. Interviews for form, applies the filename pattern, drafts the identity predicate block above the H1, drafts the required body sections the form specifies, and drafts annotated Relations edges.

  WHEN: the user wants to add a new node to the graph; the user says "add a Decision", "new Gloss", "record an Observation", "write a Conviction", "create a Pattern", "define a Predicate", "add a Reference", or "new node"; the agent is drafting a node structured as the graph expects.

  WHEN NOT: editing an existing node (use Node Read to orient, then edit directly); drafting prose outside the graph's form system; proposing a new predicate to the local vocabulary (use Predicate Propose, which gates the addition and drafts the Predicate node).
---

- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Node Create

Authors a new node that conforms to `Markdown Node Contract` and the form-specific contract the node claims. The skill's job is to force the structural requirements to be satisfied at write time — filename pattern, identity predicate block above the H1, required body sections, annotated Relations edges — rather than relying on later validation to catch drift.

An agent invokes this skill when the user wants a new node in `nodes/<Taxonomy>/`. The skill does not author prose outside the form system, does not propose new predicates to the local vocabulary, and does not edit existing nodes. Each of those operations has (or will have) its own skill; treating Node Create as a catch-all would dilute the form-specific drafting discipline this skill exists to enforce.

## Steps

### Step 1: Determine the form

Ask the user which form the new node takes. The graph's active forms are:

- `Decision` — a committed choice with a Why, Alternatives Considered, What Would Change It, `has_commitment::`, and `decided_on::`.
- `Conviction` — a held normative stance with Why-It-Is-Held and Drift Recognition sections.
- `Observation` — an empirical claim carrying `has_epistemic_status::` and matched Grounds / Revision Conditions.
- `Pattern` — a craft move, with a Heart at card scale, Forces, and the authored moves the pattern resolves.
- `Gloss` — a term definition, filename-carries-definition via ` -- `, body restates and elaborates.
- `Predicate` — a typed-edge definition, with Carries / Crescent per neighbor / Typing sections.
- `Reference` — an external source pointer, with an `## Adopted` / `## Not adopted (yet)` split and `serves_as::` where applicable.
- `Contract` — a specification node; only draft when 2-3 conforming nodes already want the same shape.
- `Aspiration` — a pulled-toward target, with Gap / Work / Progress Recognition.
- `Skill` — an agent-invocable workflow; see `Skill Form Contract`.

If the user is unsure, present the top three or four forms their described content could be, named with the distinction each form carries, and let them choose. Do not guess silently; the form choice commits to a filename pattern, predicate vocabulary, and body shape that is costly to change later.

### Step 2: Read the form's contract

Read `nodes/Contracts/<Form> Form Contract.md` (or `Markdown Node Contract.md` for `Contract` / non-form-specific nodes). Each Form Contract carries the filename pattern, identity predicate requirements, body section requirements, and form-specific predicates as explicit Requirements in its `## Requirements` section.

Also read `Markdown Node Contract.md` if not already loaded — every form inherits its file form, node atomicity, layered structure, YAML restriction, Relations section, named-edge syntax, and predicate atomicity rules.

### Step 3: Draft the filename

Apply the form's filename pattern:

- `Decision` — action-verb lead or `<Subject> as <Role>` declarative; no ` -- ` separator.
- `Gloss` — `<Concept> -- <one-clause definition>.md`.
- `Predicate` — `<predicate> -- <one-clause sense>.md` (inherits Gloss).
- `Conviction` — held-stance filename shape per `Require Held-Stance Filename Shape for Convictions`.
- `Pattern` — Alexandrian evocation per `Name Patterns by Alexandrian Evocation`.
- `Reference` — citation parenthetical per `Embed Citation Parenthetical in Reference Filenames`.
- `Contract` — `<Concept> Form Contract.md` or `<Concept> Contract.md` per `Contract Form Contract`'s filename rules.
- `Skill` — Title Case folder name matching the concept; lead file matches folder name per `Skill Form Contract`.

Every filename MUST follow `Markdown Node Contract`'s ASCII-dash rule — no em-dashes, no en-dashes, `--` for visual dashes in filenames.

### Step 4: Draft the identity predicate block

Write the identity block as bullets above the H1. Every node carries `conforms_to::[[<Form> Form Contract]]`. Most carry `in_domain::`, `authored_by::`, `has_lifecycle::`, `has_curation::`.

Form-specific additions, reserved by `Reserve Predicate Vocabularies to Specific Forms`:

- `Decision` — `has_commitment::[[Provisional Commitment]]` or `[[Firm Commitment]]`, and `decided_on::YYYY-MM-DD`.
- `Observation` — `has_epistemic_status::`.
- `Reference` — `serves_as::` where applicable, plus `under_license::` and `authored_by::` for the external source.

Do not carry a form-specific predicate on a node whose form does not own it — `has_commitment::` on a Conviction is a category error, not a stylistic choice.

### Step 5: Draft the H1 and opening

The H1 is the concept name — not a sentence, not the filename with a definition appended (unless the form explicitly requires it, which none currently do). The opening prose states the node's claim at card scale per `Adopt Layered Node Structure` and `Progressive Summary Before Substance`. An agent reading only the identity block, the H1, and the opening paragraph should be able to orient to the node's position in the graph.

### Step 6: Draft the required body sections

Each form's Contract specifies required body sections:

- `Decision` — Why (prose, capability-first), Alternatives Considered (each with a named weakness), Consequences (when operative), What Would Change It.
- `Conviction` — Why It Is Held, Drift Recognition.
- `Observation` — Grounds (matched to epistemic status), What Would Revise It.
- `Pattern` — Heart at card scale, Forces (authentic tensions), the moves the pattern resolves.
- `Gloss` — restate-and-elaborate opening; optionally a paragraph distinguishing the concept from an alternative.
- `Predicate` — Carries (positive sense), Crescent (per adjacent predicate in an H3 `### Against [[adjacent]]` subsection), Typing (subject and object shape), optional Instances.
- `Reference` — Adopted / Not adopted (yet) split; URL in body or `## Sources` for multi-source references.
- `Contract` — `## Requirements` with `### <short name>` subsections using RFC 2119 keywords; opening prose before Requirements.
- `Aspiration` — Gap, Work, Progress Recognition.
- `Skill` — opening orientation, numbered Steps, Scripts section when `scripts/` present.

Do not drop a required section because it "feels redundant" — the form sections are the structural home for the reasoning the node is committing to carry. Preserve contributor voice; do not generalize into a house style.

### Step 7: Draft the Relations section

Add `## Relations` at the end if the node carries relational edges. Each edge is a top-level bullet `- predicate::[[Target]]` followed by an indented sub-bullet annotation explaining why the edge matters. The annotation is required by `Annotate Edges With Why-They-Matter`; an edge without an annotation is tag spaghetti, not graph.

Choose the most specific predicate the graph's vocabulary supports. `relates_to::` is prohibited by `No Generic relates_to Predicate` — pick `grounded_in::`, `informs_downstream::`, `informed_by::`, `built_on::`, `composes_with::`, `contrasts_with::`, `contends_with::`, `extends_contract::`, or invoke [[Predicate Propose]] to add a new predicate to the vocabulary rather than fall back on a generic.

If a target node does not yet exist, the edge is a ghost link — permitted per `Markdown Node Contract` and a planning signal that the graph wants to grow there. Use `↗` (the literal U+2197 NORTH EAST ARROW character, never the escape notation `↗`) to mark external wiki targets.

### Step 8: Validate before writing

Before writing the file to disk, re-read the node draft against the form's `## Requirements` section. Check:

- Filename matches the form's pattern and uses ASCII dashes only.
- Identity block is above the H1, includes `conforms_to::`, and carries the form-specific predicates the form owns.
- H1 matches the filename (or the filename's concept side, for forms with the ` -- ` separator).
- Every required body section is present and carries content, not placeholder prose.
- Relations edges are annotated; no `relates_to::` slipped in; predicate-form-reservation boundaries are respected.

If any check fails, fix the draft before writing. Validation at read time is a weaker guarantee than refusing to write a non-conforming draft.

### Step 9: Write and confirm

Write the file at `nodes/<Taxonomy>/<Filename>.md` (or `nodes/Skills/<Folder>/<Folder>.md` for Skills). Report the path to the user. Do not stage or commit — the user authors the commit after reviewing the draft.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill is itself a Skill node and declares compliance with the Skill Form Contract's Requirements — YAML frontmatter carrying `runtime_name` and Anthropic `description`, compound-node layout, numbered Steps, Relations grounded in the Decisions the skill enforces.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The spine commitment this skill realizes at write time. Every node this skill produces carries identity predicates and annotated Relations edges; the skill exists to make those the default output, not an afterthought.

- grounded_in::[[Adopt Node Atomicity]]
  - The commitment that one file addresses one concept. Step 1's form-selection interview forces the author to name which one concept the node carries before drafting begins; Step 3's filename drafting reinforces atomicity because the filename names the concept.

- grounded_in::[[Adopt Predicate Atomicity]]
  - The commitment that each predicate answers one axis. Step 4's form-specific-predicate reservation encodes predicate atomicity at the identity-block scale; Step 7's annotation and specificity rules encode it at the Relations scale.

- grounded_in::[[Adopt Layered Node Structure]]
  - The commitment to identity-block-above-H1 and progressive-cost-graded layers. Steps 4, 5, 6, and 7 walk the layers in order — identity block, H1 and opening, body, Relations — and Step 5 names `Progressive Summary Before Substance` as the move the opening paragraph realizes.

- grounded_in::[[Annotate Edges With Why-They-Matter]]
  - Step 7's annotation requirement enforces this Decision. Unannotated edges are rejected at the validate-before-write gate in Step 8.

- grounded_in::[[No Generic relates_to Predicate]]
  - Step 7's specific-predicate rule enforces this Decision. A node proposing `relates_to::` is routed to Predicate Propose or to the existing vocabulary; the skill does not write `relates_to::`.

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - Step 4's form-specific-predicate reservation encodes this Decision's cross-form boundaries. The skill does not attach `has_commitment::` to a Conviction, `has_epistemic_status::` to a Decision, or `serves_as::` to a Gloss.

- informs_downstream::[[Markdown Node Contract]]
  - This skill realizes the base Contract's Requirements at write time. The Contract states the standing structural rule; the skill carries the authoring workflow that satisfies it.

- composes_with::[[Node Read]]
  - Node Read is the read-side companion: when the author wants to model a new node on an existing neighbor, Node Read orients them to the neighbor first; Node Create drafts the new node. Both skills walk the same layered structure, in opposite directions.
