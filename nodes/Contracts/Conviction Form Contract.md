---
tagline: A held normative stance the project asks contributors to share, carrying Why-It-Is-Held and Drift Recognition sections
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Conviction Form Contract

A Conviction is a node that records a held normative stance — a commitment the project's authors make about what ought to be the case in the domain the graph concerns. It carries the stance, the values or prior commitments it rests on, what taking the stance asks of the project in practice, and how drift away from the stance would be recognized.

A Conviction is not an Observation (which records a descriptive claim about what is the case), not a Decision (which commits to a specific situational choice with revisit conditions), not a Pattern (which names a recurring move), and not a Contract Requirement (which states a structural MUST rule the graph's forms enforce). A Conviction says "we hold that X ought to be the case, and here is what that commitment asks of us." A Conviction may imply Requirements (structural consequences that follow from taking the stance seriously) and may be supported by Observations (evidence that the stance is warranted), but the Conviction itself is the normative commitment.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

Enforces [[Decisions/Require Held-Stance Filename Shape for Convictions]]↗.

- The filename MUST read as a held stance. Typical shapes: scoped authority claim (`Human Authority Over Augmentation Systems`), value declaration (`Vocabulary Diversity Is a Feature`), directional commitment (`Content Over Container`), bounded stance (`Translation Over Convergence`), or subject-carries-object declarative (`Folders Serve Human Legibility, Not the Graph`).
- A bare noun phrase MUST NOT be used.
- The filename MUST NOT begin with an imperative action verb (`Adopt <X>`, `Use <X>`, `Prefer <X>`, `No <X>`) and MUST NOT use the `<Subject> as <Role>` shape. Both belong to [[Decision Form Contract]].
- The filename MUST NOT use the `<Concept> -- <definition>.md` separator.

### Identity predicate block

Enforces [[Decisions/Reserve Predicate Vocabularies to Specific Forms]]↗.

- The identity block above the H1 MUST include `conforms_to::[[Conviction Form Contract]]`.
- The identity block SHOULD include `in_practice_domain::[[<Practice Domain>]]`.
- The identity block MAY include `authored_by::`, `has_lifecycle::`, and `has_curation::` as for any Markdown Node.
- A Conviction MUST NOT carry `has_commitment::` or `decided_on::` — those are Decision predicates.
- A Conviction MUST NOT carry `has_epistemic_status::` — that predicate is Observation-specific.

### H1

- The H1 MUST match the filename exactly (minus the `.md` extension).

### Body: the stance

- The body MUST open by stating the conviction in one or two prose sentences — the normative commitment as held.
- The opening MUST be prose, not a bullet list.

### Body: why it is held

- The body MUST elaborate the values, prior convictions, or load-bearing arguments that make the stance worth holding.
- This elaboration MAY be an unheaded paragraph for compact convictions, or an explicit subsection heading when the stance rests on multiple distinct supporting arguments.
- Where a Conviction rests on another node's argument, that node SHOULD appear in `## Relations` via `grounded_in::` or `informed_by::` with an annotation naming the load-bearing claim.

### Body: what it asks

Enforces [[Decisions/Require What-It-Asks and Drift Recognition in Convictions]]↗.

- The body MUST describe what taking the stance seriously asks of the project — the observable commitments, mechanisms, boundaries, or practices that follow when contributors hold this conviction.
- Subsections MAY partition the asks by level of application (e.g., session-level, architectural, knowledge-level) when a conviction's consequences span scales.

### Body: drift recognition

Enforces [[Decisions/Require What-It-Asks and Drift Recognition in Convictions]]↗.

- The body MUST describe how a reader or contributor would recognize drift from the stance — the practices, outputs, or omissions that would indicate the conviction has weakened without being explicitly revoked.
- Drift recognition differs from a Contract Requirement's violation condition. A Requirement is violated when its structural MUST rule fails; a Conviction drifts when contributors stop acting as though the stance were held. The recognition is cumulative and cultural rather than pointwise and structural.
- The criterion MAY appear as a closing paragraph of the "what it asks" section or as its own brief section.

### Sources section

- When the conviction draws on external sources, a `## Sources` section MUST appear after the body and before `## Relations`.

### Relations section

- The Relations section follows the base Markdown Node Contract.
- A Conviction typically carries these edges:
  - `grounded_in::[[Prior Conviction or Value]]` — the substrate the stance rests on.
  - `informed_by::[[Observation or Reference]]` — evidence or external work that supports the stance.
  - `informs_downstream::[[Downstream Node]]` — Decisions, Patterns, Contract Requirements, or further Convictions the stance motivates.
  - `contrasts_with::[[Adjacent Conviction]]` — a sibling conviction occupying adjacent territory.

### Optional scalar metadata

- YAML frontmatter SHOULD include `tagline:` (per Markdown Node Contract — surfaced on the Convictions index page row); MAY include `created:` and `brief_summary:`.
- Beyond the recommended `tagline:`, YAML is OPTIONAL for Convictions.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the held-stance filename pattern, the prohibition on `has_commitment::`, `decided_on::`, and `has_epistemic_status::`, and the required Stance plus Why It Is Held plus What It Asks body structure.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- contrasts_with::[[Observation Form Contract]]
  - An Observation reports a descriptive claim about what is the case on some epistemic grounds; a Conviction records a held normative stance about what ought to be the case.

- contrasts_with::[[Aspiration Form Contract]]
  - An Aspiration records a directional target the project works toward but has not achieved; a Conviction records a stance the project currently holds. An Aspiration acknowledges a gap between the current state and the target; a Conviction claims the stance is currently maintained.

- contrasts_with::[[Decision Form Contract]]
  - A Decision records a situational choice made at a moment with revisit conditions; a Conviction records a held stance without `has_commitment::` or `decided_on::`. The filename shapes enforce the distinction.

- grounded_in::[[Decisions/Adopt Wikilinks and Named Edges]]↗
  - The named-edge spine that lets `grounded_in::`, `informed_by::`, `informs_downstream::`, and `contrasts_with::` land as first-class relational edges.

- grounded_in::[[Decisions/Require Held-Stance Filename Shape for Convictions]]↗
  - Grounds the Filename pattern Requirement.

- grounded_in::[[Decisions/Require What-It-Asks and Drift Recognition in Convictions]]↗
  - Grounds the paired Body-what-it-asks and Body-drift-recognition Requirements. The two sections share an accountability Why and roll back together.

- grounded_in::[[Decisions/Reserve Predicate Vocabularies to Specific Forms]]↗
  - Grounds the prohibitions on `has_commitment::`, `decided_on::`, and `has_epistemic_status::` in the identity predicate block Requirement.
