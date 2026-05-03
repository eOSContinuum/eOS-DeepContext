---
tagline: A directional target the project works toward, carrying its acknowledged Gap, current Work, and Progress-Recognition markers
---

- conforms_to::[[Contract Form Contract]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Aspiration Form Contract

An Aspiration is a node that records a directional target the project works toward — an end-state the authors are committed to pursuing without claiming to have achieved. It carries the target, the value grounding that makes the target worth pursuing, the honest account of the current gap between the project's state and the target, the work taking the aspiration seriously asks, and the markers by which progress toward the target would be recognized.

An Aspiration is not a Conviction (which records a stance the project currently maintains), not a Decision (which commits to a specific situational choice), not a Contract Requirement (which states a structural MUST rule that currently holds), and not an Observation (which reports on what is the case). An Aspiration says "we work toward X, which is not yet the case, and here is how progress would be known." An Aspiration with no acknowledged gap is a Conviction mislabeled; a Conviction with no claim of present validity is an Aspiration mislabeled. The distinction matters because Aspirations are accountable for progress, while Convictions are accountable for fidelity.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

- The filename MUST read as a directional target — an end-state the reader can evaluate as moved-toward or drifted-from. Typical shapes: end-state claim (`Contributors Across Vocabularies Can Collaborate`), target relation (`The Graph Survives Its Tooling`), directional commitment (`Curation Becomes Participatory`).
- A bare noun phrase MUST NOT be used as an Aspiration filename.
- The filename MUST NOT use the `<Concept> -- <definition>.md` separator.

### Identity predicate block

Enforces [[Reserve Predicate Vocabularies to Specific Forms]].

- The identity block above the H1 MUST include `conforms_to::[[Aspiration Form Contract]]`.
- The identity block SHOULD include `in_domain::[[<Domain>]]`.
- The identity block MAY include `authored_by::`, `has_lifecycle::`, and `has_curation::` as for any Markdown Node.
- An Aspiration MUST NOT carry `has_commitment::` or `decided_on::` — those are Decision predicates.
- An Aspiration MUST NOT carry `has_epistemic_status::` — that predicate is Observation-specific.

### H1

- The H1 MUST match the filename exactly (minus the `.md` extension).

### Body: the target

- The body MUST open by stating the directional target in one or two prose sentences — what the project works toward.
- The opening MUST be prose, not a bullet list.

### Body: why it is worth pursuing

- The body MUST elaborate the values, prior convictions, or observations that make the target worth pursuing.
- This elaboration MAY be an unheaded paragraph for compact aspirations, or an explicit subsection heading when the justification rests on multiple distinct supporting arguments.
- Where an Aspiration rests on another node's argument, that node SHOULD appear in `## Relations` via `grounded_in::` or `informed_by::` with an annotation naming the load-bearing claim.

### Body: current gap

Enforces [[Require Gap, Work, and Progress Recognition in Aspirations]].

- The body MUST contain a section headed `## Current Gap` (or equivalent) that gives an honest account of where the project currently is relative to the target — what is missing, incomplete, untested, or misaligned.
- The Gap section is what distinguishes an Aspiration from a Conviction. A Gap section that effectively says "no gap" reveals the node is a Conviction, not an Aspiration; such a node SHOULD be reclassified.
- The Gap SHOULD name concrete shortfalls — specific capabilities not yet present, practices not yet adopted, tests not yet passed — rather than abstract hand-waving about the target being "hard."

### Body: work it asks

Enforces [[Require Gap, Work, and Progress Recognition in Aspirations]].

- The body MUST describe what taking the aspiration seriously asks — the concrete moves, investments, or commitments the project would make to progress toward the target.
- The Work SHOULD name moves the project can actually take given its current resources and practices, not a wish list contingent on circumstances the project does not control.

### Body: progress recognition

Enforces [[Require Gap, Work, and Progress Recognition in Aspirations]].

- The body MUST contain a section that names observable markers by which progress toward the target would be recognized.
- Progress markers MUST be specific enough that a contributor (or a later reviewer) can assess whether the project has moved toward the target since the Aspiration was seeded. Vague markers ("things feel better") are insufficient.

### Sources section

- When the aspiration draws on external sources, a `## Sources` section MUST appear after the body and before `## Relations`.

### Relations section

- The Relations section follows the base Markdown Node Contract.
- An Aspiration typically carries these edges:
  - `grounded_in::[[Value or Conviction]]` — the substrate that makes the target worth pursuing.
  - `informed_by::[[Observation or Reference]]` — evidence or external work that shapes how the target is framed or pursued.
  - `informs_downstream::[[Downstream Node]]` — Decisions, Patterns, or further Aspirations the target motivates.
  - `contrasts_with::[[Adjacent Aspiration]]` — a sibling aspiration occupying adjacent territory.
  - `composes_with::[[Related Aspiration]]` — another aspiration routinely pursued alongside this one.

### Optional scalar metadata

- YAML frontmatter MAY include `created:`, `tagline:`, and `brief_summary:`.
- YAML is OPTIONAL for Aspirations.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the directional-target filename pattern, the prohibition on `has_commitment::`, `decided_on::`, and `has_epistemic_status::`, and the required Target plus Why plus Gap plus Work plus Progress Recognition body structure.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- contrasts_with::[[Conviction Form Contract]]
  - A Conviction records a stance currently held; an Aspiration records a target worked toward but not yet achieved. The Gap section is the structural difference.

- contrasts_with::[[Decision Form Contract]]
  - A Decision is a situational choice made at a moment with revisit conditions; an Aspiration is a directional target pursued over time.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine that lets `grounded_in::`, `informed_by::`, `informs_downstream::`, `contrasts_with::`, and `composes_with::` land as first-class relational edges.

- grounded_in::[[Require Gap, Work, and Progress Recognition in Aspirations]]
  - Grounds the three paired body-section Requirements (Gap, Work, Progress Recognition). The three sections share one accountability Why and roll back together.

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - Grounds the prohibitions on `has_commitment::`, `decided_on::`, and `has_epistemic_status::` in the identity predicate block Requirement.
