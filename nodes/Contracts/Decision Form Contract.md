---
tagline: A committed choice with Why, Alternatives Considered, and What Would Change It; situational rather than standing
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Decision Form Contract

A Decision is a node that records a commitment — a choice made by the project about how some aspect of the graph, the practice, or the convention layer should work. It carries the choice, the reasoning, the conditions that would make the choice worth revisiting, and the typed edges that connect it to its antecedents and consequences.

A Decision is not a Gloss (which defines a term), not a Reference (which points at external authoritative material), not a Conviction (which records a held normative stance), and not an Inquiry (which frames an open question). A Decision has committed to an answer — even when that commitment is Provisional and explicitly revisitable. What distinguishes a Decision from a Conviction is that a Decision is situational: it records a specific choice made at a specific moment, with the context that made it the right choice at that moment, and it carries `decided_on::` and `has_commitment::` predicates a Conviction does not.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

Enforces [[Name Decisions by Action Verb or Role Declarative]].

- The filename MUST take one of two shapes: an action-verb lead (`Adopt <X>`, `Use <X>`, `Prefer <X>`, `Require <X>`, `Treat <X>`, `No <X>`) or a `<Subject> as <Role>` declarative.
- Bare noun phrases and shapes beginning with the subject (`<X> Over <Y>`, `<X> Is <Y>`, `<X> Carries <Y>`) MUST NOT be used.
- When a Decision's subject is a thing with an established title (a named convention, tool, person, practice, or existing node), the filename MUST embed that subject verbatim with only a decision-shape verb or connector added. Paraphrase, re-wording, and appended category nouns are forbidden.
- The filename MUST NOT use the `<Concept> -- <definition>.md` separator.

### Identity predicate block

Enforces [[Reserve Predicate Vocabularies to Specific Forms]].

- The identity block above the H1 MUST include `conforms_to::[[Decision Form Contract]]`.
- The identity block MUST include `has_commitment::[[<X>]]` where the value is one of `[[Provisional Commitment]]` (decided but revisitable) or `[[Firm Commitment]]` (decided and expensive to change). Items that would otherwise carry `has_commitment::[[Open Question]]` are Inquiries, not Decisions.
- The identity block MUST include `decided_on::YYYY-MM-DD` recording the date the commitment was made.
- The identity block SHOULD include `in_domain::[[<Domain>]]`.
- The identity block MAY include `authored_by::`, `has_lifecycle::`, and `has_curation::` as for any Markdown Node.

### H1

- The H1 MUST match the filename exactly (minus the `.md` extension).

### Body: Why

Enforces [[Require Prose, Capability-First Why in Decisions]].

- The body MUST contain content that states why the commitment was made.
- Short decisions MAY use an opening paragraph immediately after the H1. Longer decisions with multiple reasons SHOULD use an explicit `## Why` heading.
- The Why content MUST be prose, not a bullet list.
- When a Decision responds to a reported symptom, the Why SHOULD lead with the underlying capability the commitment provides. The symptom names the forcing case; the capability names what the commitment is for.

### Body: Alternatives Considered, Consequences, What Would Change It

Enforces [[Require Alternatives, Consequences, and What Would Change It in Decisions]].

- A Decision SHOULD include a `## Alternatives Considered` section when the commitment was reached by weighing multiple viable options. Each alternative MUST name the option, state its shape, and state the reason it was rejected, identifying a specific weakness.
- A Decision SHOULD include a `## Consequences` section when the commitment has been operative long enough to observe its effects. Consequences MUST be factual observations. Both positive and negative consequences SHOULD be named.
- The body MUST contain a section headed `## What Would Change It` (or, for short decisions, a final paragraph beginning "What would change it:"). This section MUST describe the specific conditions under which the decision would be revisited.
- When a decision bundles multiple parts with asymmetric revisit criteria, the What Would Change It section SHOULD split the conditions by part.
- "Nothing plausible" is permitted when the decision is irreducibly foundational, but SHOULD be accompanied by one sentence explaining why no revisit criterion is meaningful.

### Superseding

Enforces [[Require Supersession Chain for Revised Decisions]].

- When a Decision is revised, a new Decision node MUST be created with a new filename reflecting the new commitment.
- The older Decision's filename MUST NOT change.
- The new Decision MUST declare `supersedes::[[Old Decision Name]]` in its identity block or Relations section.
- The older Decision SHOULD be updated to include `superseded_by::[[New Decision Name]]` in its Relations section.
- Both Decisions remain in the graph; the supersession chain is the record of how the commitment evolved.

### Relations section

- The Relations section follows the base Markdown Node Contract.
- A Decision MAY carry these decision-specific edges:
  - `supersedes::[[Older Decision]]` — this decision replaces an earlier one.
  - `superseded_by::[[Newer Decision]]` — the inverse; added to the older decision when a successor is written.
  - `extended_by::[[Refining Decision]]` — a later decision that refines but does not replace this one.
  - `derived_from::[[Source]]` — the occasion or antecedent that produced this decision. This is a construction predicate and SHOULD carry an annotation noting the expected upgrade once the source becomes a first-class node.
  - `informs_downstream::[[Downstream Node]]` — for contracts, nodes, or further decisions that implement this commitment.

### Bundling and splitting

- A Decision MAY bundle multiple logically-related commitments when (a) the commitments arrived as a named external package, (b) the commitments co-specify, (c) rollback is bundled, or (d) the Why would be identical across splits.
- A Decision MUST be split when (a) independent revisit criteria exist at decision time, (b) commitment levels differ, (c) the parts were adopted at different times, or (d) the Why paragraphs would differ substantially.
- Hypothetical future asymmetry is not grounds for preemptive splitting.
- **Paired accountability sections are a bundling signal.** When a Contract requires two or more body sections whose Why and rollback are shared across the sections, those sections SHOULD be grounded in one bundled Decision rather than in separate Decisions. Exemplars in this graph: the Decision form's Alternatives Considered / Consequences / What Would Change It sections bundled in `Require Alternatives, Consequences, and What Would Change It in Decisions`; the Conviction form's What-It-Asks and Drift Recognition sections bundled in `Require What-It-Asks and Drift Recognition in Convictions`; the Aspiration form's Gap / Work / Progress Recognition sections bundled in `Require Gap, Work, and Progress Recognition in Aspirations`. The bundling test is whether the sections share one Why and roll back together.
- **Before creating a new Decision, verify independence.** A candidate Decision MUST have an independent Why, independent Alternatives, and independent What Would Change It. If the candidate's Why restates another Decision's derivation and its revisit conditions are essentially that other Decision's revisit conditions, the candidate is a derivation, not an independent commitment — fold the content into the substrate Decision rather than creating a separate node. (Exemplar: placement rules about the identity block above the H1 fold into `Adopt Layered Node Structure` because they restate that Decision's cost-gradient derivation without independent commitment content.)

### Optional scalar metadata

- YAML frontmatter MAY include `created:` (ISO date of node file creation, distinct from `decided_on::`), `tagline:`, and `brief_summary:`.
- YAML is OPTIONAL for Decisions.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the commitment-phrased filename pattern, the `has_commitment::` and `decided_on::` identity predicates, and the required Why and What Would Change It body sections.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- contrasts_with::[[Gloss Form Contract]]
  - A Gloss defines a term (filename carries definition, body elaborates); a Decision records a commitment (filename states the choice, body gives rationale and revisit conditions).

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The commitment that makes named-edge predicates the structural spine.

- grounded_in::[[Name Decisions by Action Verb or Role Declarative]]
  - Grounds the filename pattern Requirement.

- grounded_in::[[Require Prose, Capability-First Why in Decisions]]
  - Grounds the paired prose-Why and capability-first framing rules in the Body-Why Requirement. The two rules share one durability Why and reinforce each other.

- grounded_in::[[Require Alternatives, Consequences, and What Would Change It in Decisions]]
  - Grounds the three body-section requirements.

- grounded_in::[[Require Supersession Chain for Revised Decisions]]
  - Grounds the Superseding Requirement.

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - Grounds the `has_commitment::` and `decided_on::` reservation in the identity predicate block Requirement.
