---
runtime_name: node-validate
tagline: Verifies a single node against the Form Contract it conforms to, walking the inheritance chain and distinguishing mechanical violations from semantic ones
description: |
  Verifies a single node against the Requirements of the Form Contract it conforms to, walking the inheritance chain from Markdown Node Contract through the form-specific Contract. Reports each violation with a specific remediation, distinguishing mechanical breaks (filename, identity-block presence, ASCII dashes) from semantic ones (missing body sections, form-specific predicate reservations, un-annotated edges).

  WHEN: the user asks to validate a node, check a draft, verify conformance, lint a node, or confirm a node is ready to commit; Node Create's Step 8 delegates here; the user has edited a node and wants to re-check against its contract; the agent is curating an existing node whose lifecycle or curation state is advancing.

  WHEN NOT: sweeping the graph for drift across many nodes (use Graph Audit once it exists); editing the node to fix violations (fix directly with the Edit tool after validation reports them); drafting a new node from scratch (use Node Create, which validates as its penultimate step); validating work in a node whose form is unknown or whose conforms_to target does not yet exist.
---

- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Node Validate

Checks a single node against every Requirement of the Form Contract it claims. Validation is the mirror of authoring — where Node Create applies a Contract at write time, Node Validate reads the same Contract at verification time and reports where the node does not satisfy it. The two skills share their grounding Decisions because both are ways of enforcing the same commitments, from opposite sides of the file.

An agent invokes this skill when a draft needs to clear its contract before commit, when an existing node's curation state is advancing (Working Draft → Stable → Canonical), or when a node's claim is about to be cited and the citer wants to know the target is structurally trustworthy. The skill does not fix violations — fixing is a separate act, usually direct editing. Reporting a remediation per violation lets the user or a follow-up skill close the gap without re-deriving what the violation means.

## Steps

### Step 1: Load the node

Read the node file with the Read tool. The file may be a flat `nodes/<Taxonomy>/<Name>.md`, a compound-node lead `nodes/<Taxonomy>/<Name>/<Name>.md`, or a Skill lead `nodes/Skills/<Folder>/<Folder>.md`. If the path resolves to a folder, read the lead file whose name matches the folder.

If the file does not exist, stop and report the path that was requested. Do not infer the intended node.

### Step 2: Identify the form

Find the `conforms_to::[[<Form> Contract]]` line in the identity predicate block above the H1. That target names the Form Contract the node claims.

If no `conforms_to::` line exists, the node violates `Markdown Node Contract`'s Identity predicate block Requirement — report that as the first finding and stop; no form-specific checks apply because the form is not declared.

If the `conforms_to::` line exists but the target does not resolve to a file under `nodes/Contracts/`, record this as a violation with target `<name>`; the agent may still attempt base-contract checks against `Markdown Node Contract` but cannot run form-specific checks.

### Step 3: Walk the Contract inheritance chain

Read the Form Contract's `## Requirements` section. Contracts extend other Contracts via `extends_contract::[[Parent Contract]]` in their Relations section. Walk the chain upward: if the form's Contract extends `Markdown Node Contract` (the common case), collect Requirements from both. If the chain is deeper (for example, `Predicate Form Contract` extends `Gloss Form Contract` extends `Markdown Node Contract`), collect Requirements from every level.

The validation set is the union of every Requirement in the chain. Inheritance is strict per `Contract Form Contract` — a child Contract may add Requirements and may refine a parent Requirement by naming it, but cannot silently override.

### Step 4: Check base Requirements

Apply `Markdown Node Contract`'s Requirements to the node:

- **File form** — UTF-8, `.md` extension, no em-dashes or en-dashes in the filename. When a visual dash appears in the filename, it MUST be `--` (double ASCII hyphen).
- **Node atomicity** — the file addresses one concept. If the body legibly splits into two independent sections serving two different concepts, record a split recommendation.
- **YAML frontmatter** — when present, carries scalar metadata only; named-edge predicates MUST NOT appear in YAML.
- **Identity predicate block** — a bullet list above the H1, including `conforms_to::[[<Form> Contract]]`.
- **H1** — exactly one H1 in the file; the H1 carries the concept name (not a sentence, not a definition).
- **Body** — prose follows the H1; inline wikilinks are readable references, not structural edges.
- **Layered structure** — identity block above H1, opening card-scale claim, elaboration body, Relations section; cheaper layers precede expensive prose.
- **Relations section** — if the node carries relational edges, they appear under `## Relations` after the body; each edge is a top-level bullet in `- predicate::[[Target]]` form, with an indented sub-bullet annotation explaining why the edge matters. The `relates_to::` predicate MUST NOT be used.
- **Named-edge syntax** — predicates are multi-word, lower-case, joined by underscores; wikilink targets are multi-word; external targets carry the literal `↗` character (U+2197), never the escape notation. Named-edge values are wikilink targets in `[[Target]]` or `[[Target]]↗` form, or scalar values when a form-specific Contract explicitly introduces a scalar-valued predicate (currently `decided_on::YYYY-MM-DD` on Decisions).
- **Pipe wikilinks for ` -- `-suffixed targets** — When a wikilink target resolves to a file whose name contains ` -- `, the reference form depends on context. In **prose flow** (running text in the elaboration body, Why, Grounds, etc.), the reference MUST use the pipe form `[[<full filename>|<concept>]]` per `Use Pipe Wikilinks for Display-Target Divergence`. In **structural contexts** — `## Relations` edges, identity-block predicate edges, `### Against [[adjacent]]` H3 subsection headings, and other index-shaped locations — the bare full filename `[[<full filename>]]` is permitted; the ` -- sense` suffix there carries the target's working definition at the edge. The bare concept form `[[<concept>]]` is never permitted for a ` -- `-suffixed target, because it does not resolve in standard wiki tooling. Report any bare-concept reference to a ` -- `-suffixed target as a violation regardless of context.
- **Predicate atomicity** — each predicate answers one axis; predicate values MUST NOT cluster into subgroups answering different questions.

For each check that fails, record the Requirement's short name, what was found, and what the Requirement expects.

### Step 5: Check form-specific Requirements

Apply the form-specific Contract's Requirements. The exact checks vary by form:

- `Decision Form Contract` — action-verb or `<Subject> as <Role>` filename; `has_commitment::[[Provisional Commitment]]` or `[[Firm Commitment]]`; `decided_on::YYYY-MM-DD`; H1 matches filename; Why (prose, capability-first); Alternatives Considered (each with a named weakness); What Would Change It.
- `Conviction Form Contract` — held-stance filename; Why It Is Held; Drift Recognition; no `has_commitment::`, `decided_on::`, or `has_epistemic_status::`.
- `Observation Form Contract` — `has_epistemic_status::` matched to Grounds; What Would Revise It.
- `Pattern Form Contract` — Alexandrian evocation filename; Heart at card scale; Forces; no `has_commitment::` or `decided_on::`.
- `Gloss Form Contract` — `<Concept> -- <one-clause definition>.md` filename; H1 is the bare concept; opening restates and elaborates the filename definition (not a verbatim repeat).
- `Predicate Form Contract` — `<predicate> -- <one-clause sense>.md` filename; Carries (positive sense); Crescent subsection per `contrasts_with::` edge (each headed `### Against [[adjacent]]`); Typing (subject and object shape); every `contrasts_with::` edge pairs with a Crescent subsection.
- `Reference Form Contract` — citation parenthetical filename; URL; Adopted / Not adopted (yet) sections as applicable.
- `Contract Form Contract` — filename ends with ` Contract.md`; `## Requirements` with `### <short name>` subsections using RFC 2119 keywords; opening prose precedes Requirements; self-conformance if the Contract is itself a Contract.
- `Aspiration Form Contract` — Gap; Work; Progress Recognition; no `has_commitment::`, `decided_on::`, or `has_epistemic_status::`.
- `Skill Form Contract` — compound-node folder with lead file matching folder name; YAML frontmatter with `runtime_name` and Anthropic-spec `description`; numbered Steps; Scripts section when `scripts/` present.

The form-specific predicate reservations come from `Reserve Predicate Vocabularies to Specific Forms`. A `has_commitment::` on a Conviction, a `has_epistemic_status::` on a Decision, or a `serves_as::` on a Gloss is a category error — flag it with the reserving Contract named.

### Step 6: Check Relations annotations

For each edge in `## Relations`, verify:

- The predicate is multi-word, lower-case, underscore-joined.
- The target is multi-word (or is a ghost-link target that will become a multi-word node).
- An indented sub-bullet annotation follows the edge, stating why the relationship matters.
- The predicate is not `relates_to::`.

Vocabulary health — whether a predicate has a backing Predicate node, whether a provisional predicate should be codified, whether two predicates have drifted into synonyms — is Graph Audit's concern, not Node Validate's. Per-node vocabulary reporting conflates base-contract predicates (introduced by `Markdown Node Contract` and form-specific Contracts — `conforms_to`, `authored_by`, `has_lifecycle`, `has_commitment`, `extends_contract`, and so on) with genuinely provisional predicates, producing noise on every node. Defer vocabulary questions to Graph Audit, which separates backed predicates from base-contract predicates from provisional drift at graph scope.

An edge with no annotation is tag spaghetti by `Annotate Edges With Why-They-Matter`; report each unannotated edge as its own finding with the edge text quoted.

### Step 7: Report findings

Group findings by severity:

- **Violation** — the node contradicts a MUST or MUST NOT Requirement. The node does not conform; the user cannot commit it as the form it claims until this is resolved.
- **Shortfall** — the node misses a SHOULD Requirement. The node conforms but carries lower quality than the Contract asks for.
- **Signal** — the node raises a concern the Contract flags as worth noticing. Not a violation; an invitation. Signals are usually surfaced by cross-node patterns (Graph Audit) rather than by per-node inspection; Node Validate reports Signals only when they are locally visible without graph-wide context.

For each finding, report:

- The Requirement's short name, quoted.
- The originating Contract's filename.
- What was found in the node, quoted.
- A specific remediation — what edit would resolve the finding.

Order findings from cheapest-to-fix (filename, ASCII dashes, missing `conforms_to::`) to most expensive (missing body section, node-atomicity split, predicate axis refactor). Cheaper fixes unlock later checks; running them first is usually productive.

If no findings, report "Conforms to `<Form Contract>`" and name the Contracts walked in the inheritance chain. A clean report is itself information the user can act on.

### Step 8: Stop

Do not edit the node. Do not stage or commit. Validation produces findings; fixing is a separate act the user or a follow-up skill performs.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements. Used alongside Node Create and Node Read as the read-side-plus-verification triad for the first-session scion-author arc.

- composes_with::[[Node Create]]
  - Node Create's Step 8 delegates its pre-write validation to this skill's logic. Running Node Validate on a just-drafted node reproduces that check; running it on an existing node verifies the draft has not drifted from its claim.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The spine commitment this skill enforces at verification time. Every check in Steps 4 through 6 traces back to a named-edge or wikilink Requirement.

- grounded_in::[[Adopt Node Atomicity]]
  - Step 4's node-atomicity check enforces this Decision. A node whose body splits into two concepts triggers a split recommendation, not a silent pass.

- grounded_in::[[Adopt Predicate Atomicity]]
  - Step 4's predicate-atomicity check and Step 5's form-specific-predicate-reservation check both realize this Decision. A predicate carrying two axes or appearing on the wrong form fails the same discipline from different angles.

- grounded_in::[[Adopt Layered Node Structure]]
  - Step 4's layered-structure check enforces this Decision. Identity block above H1, card-scale opening, elaboration body, Relations at the end is the order the Contract specifies and this skill verifies.

- grounded_in::[[Annotate Edges With Why-They-Matter]]
  - Step 6's annotation check enforces this Decision directly. An unannotated edge is a per-edge finding, not a single aggregated one, so the author can see exactly which Relations bullets need the sub-bullet.

- grounded_in::[[No Generic relates_to Predicate]]
  - Step 6's `relates_to::` check enforces this Decision. A `relates_to::` edge is always a violation, never a shortfall or signal.

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - Step 5's form-specific-predicate-reservation check enforces this Decision's cross-form boundaries. `has_commitment::` on non-Decisions, `has_epistemic_status::` on non-Observations, and `serves_as::` on non-References each produce a named violation with the reserving Contract quoted.

- grounded_in::[[Use ASCII Dashes in Filenames]]
  - Step 4's filename-dash check enforces this Decision. Em-dashes and en-dashes in filenames are mechanical breaks with a one-line remediation.

- informs_downstream::[[Markdown Node Contract]]
  - The base Contract specifies the structural shape this skill verifies. The Contract states the standing structural rule; this skill carries the verification workflow that tests conformance.
