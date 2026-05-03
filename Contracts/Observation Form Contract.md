---
tagline: A descriptive claim with matched epistemic grounds (Empirical, Retrospective, Contested, On-Faith) and the conditions that would revise it
---

- conforms_to::[[Contract Form Contract]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Observation Form Contract

An Observation is a node that records a descriptive claim about how things are or have been — a statement about the world, the graph, or the practice whose force rests on evidence rather than on commitment or structural necessity. It carries the claim, the epistemic grounds on which the claim rests, the evidence or reasoning that supports it, and the conditions under which the claim would be revised.

An Observation is not a Conviction (which records a held normative stance), not a Decision (which commits to a situational choice), not a Contract Requirement (which states a structural MUST rule), and not a Pattern (which names a recurring move). An Observation says "X is the case, on these grounds, at this epistemic tier." Observations may support Convictions and inform Requirements as evidence, but they are not themselves commitments; they are claims about the world that evidence can revise.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

- The filename MUST read as a descriptive claim the reader can evaluate, not as a topic the node discusses. Typical shapes: declarative claim about the world (`Agent Generation Is Cheaper Than Agent Verification`), empirical relation (`Contribution Follows Heavy-Tailed Distribution`), attribution claim (`Wikis Without Curation Drift Toward Write-Only`).
- A bare noun phrase MUST NOT be used as an Observation filename.
- The filename MUST NOT use the `<Concept> -- <definition>.md` separator.

### Identity predicate block

Enforces [[Classify Observations by Epistemic Status With Matched Grounds]] and [[Reserve Predicate Vocabularies to Specific Forms]].

- The identity block above the H1 MUST include `conforms_to::[[Observation Form Contract]]`.
- The identity block MUST include `has_epistemic_status::[[<Status>]]` where the value is one of `[[Empirical Observation]]`, `[[Retrospective Observation]]`, `[[On-Faith Observation]]`, or `[[Contested Observation]]`.
- The identity block SHOULD include `in_domain::[[<Domain>]]`.
- The identity block MAY include `authored_by::`, `has_lifecycle::`, and `has_curation::` as for any Markdown Node.
- The identity block MAY include `drawn_from::[[Canonical Set]]` when the Observation was imported from a named external set.
- An Observation MUST NOT carry `has_commitment::` or `decided_on::` — those are Decision predicates.

### H1

- The H1 MUST match the filename exactly (minus the `.md` extension).

### Body: Claim

- The body MUST open by stating the claim in one or two prose sentences.
- The opening MUST be prose, not a bullet list.

### Body: Grounds

Enforces [[Classify Observations by Epistemic Status With Matched Grounds]].

- The body MUST describe the grounds on which the claim rests. The grounds MUST match the declared `has_epistemic_status::`.
- An `[[Empirical Observation]]` MUST name the measurement, experiment, or direct observation that produced the claim.
- A `[[Retrospective Observation]]` MUST name the record or reconstruction the claim rests on and acknowledge the limits of that record.
- An `[[On-Faith Observation]]` MUST name the source adopted and the reason for accepting it provisionally, and SHOULD name what it would take to promote the claim to empirical or retrospective status.
- A `[[Contested Observation]]` MUST name the sides of the contest and why the debate is load-bearing for this graph.

### Body: What Would Revise It

Enforces [[Require Revision Conditions on Observations]].

- The body MUST describe the conditions under which the observation would be updated, downgraded, or abandoned.
- The revision conditions MUST be concrete: new measurement, contradicting record, promotion of a premise to empirical status, resolution of the contest.

### Sources section

- When the observation draws on external sources, a `## Sources` section MUST appear after the body and before `## Relations`.
- Sources are listed as bulleted URLs with brief annotations.

### Relations section

- The Relations section follows the base Markdown Node Contract.
- An Observation typically carries these edges:
  - `grounded_in::[[Prior Observation or Reference]]` — the substrate the claim rests on.
  - `informed_by::[[Precedent Observation]]` — a precedent that influences how the claim is framed.
  - `informs_downstream::[[Downstream Node]]` — Convictions, Decisions, Contract Requirements, or Patterns the observation supports as evidence.
  - `contrasts_with::[[Adjacent Observation]]` — a sibling observation occupying adjacent territory.
  - `drawn_from::[[Canonical Set]]` — when the observation was imported from a named external set.

### Optional scalar metadata

- YAML frontmatter MAY include `created:`, `tagline:`, and `brief_summary:`.
- YAML is OPTIONAL for Observations.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the descriptive-claim filename pattern, the required `has_epistemic_status::` identity predicate, the prohibition on `has_commitment::` and `decided_on::`, and the required Claim plus Grounds plus What Would Revise It body structure.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- contrasts_with::[[Conviction Form Contract]]
  - A Conviction records a held normative stance — what the project's authors hold ought to be the case; an Observation records a descriptive claim about what is the case. An Observation may support a Conviction as evidence (via `informs_downstream::`), but an Observation does not commit to anything.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine that lets `has_epistemic_status::`, `grounded_in::`, `informs_downstream::`, and `drawn_from::` land as first-class classification and relational edges.

- grounded_in::[[Classify Observations by Epistemic Status With Matched Grounds]]
  - Grounds the `has_epistemic_status::` predicate and its matched body-Grounds requirements.

- grounded_in::[[Require Revision Conditions on Observations]]
  - Grounds the Body-What-Would-Revise-It Requirement.

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - Grounds the `has_epistemic_status::` reservation and the prohibition on `has_commitment::` and `decided_on::` in the identity predicate block Requirement.
