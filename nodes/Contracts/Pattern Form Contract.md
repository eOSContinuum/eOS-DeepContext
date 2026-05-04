---
tagline: A recurring craft move named from practice, with Heart at card scale, Problem, Forces, Solution, and Consequences
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Pattern Form Contract

A Pattern is a node that names a recurring craft move — a process applied when a recognizable situation recurs in the graph. It carries a compact statement of the pattern (the Heart), the recurring difficulty it addresses (the Problem), the competing demands that make the difficulty hard (the Forces), the move that resolves those demands (the Solution), and the effects the move produces (the Consequences). Patterns are observed and named from practice; they are not prescribed.

A Pattern is not a Decision (which records a commitment made at a specific moment with revisit conditions), not a Contract Requirement (which states a structural rule the graph's forms enforce), not a Conviction (which records a held normative stance), and not a Gloss (which defines a term). A Decision says "we chose X at time T"; a Requirement says "X MUST hold, structurally"; a Conviction says "we hold that X ought to be the case"; a Pattern says "when you encounter situation X with forces Y, apply move Z — and here are its tradeoffs."

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

Enforces [[Decisions/Name Patterns by Alexandrian Evocation]]↗.

- The filename MUST read as a move the reader can make (or as a recognizable situation the reader can see), not as a topic the node describes. Typical shapes: imperative verb plus object (`Refactor the Predicate's Axes`), timing imperative (`Split Before Ossify`, `Progressive Summary Before Substance`), or named failure-mode claim for anti-patterns (`Informal Edges Poison the Graph`).
- A bare noun phrase MUST NOT be used; rewrite as a move or a condition.
- The filename MUST NOT use the `<Concept> -- <definition>.md` separator.
- Pattern names SHOULD be Alexandrian-evocative — name the move or the situation with specificity and imagery, not with abstract category labels.

### Identity predicate block

Enforces [[Decisions/Reserve Predicate Vocabularies to Specific Forms]]↗.

- The identity block above the H1 MUST include `conforms_to::[[Pattern Form Contract]]`.
- The identity block SHOULD include `in_practice_domain::[[<Practice Domain>]]`.
- The identity block MAY include `authored_by::`, `has_lifecycle::`, and `has_curation::` as for any Markdown Node.
- A Pattern MUST NOT carry `has_commitment::` or `decided_on::` — those are Decision predicates.

### H1

- The H1 MUST match the filename exactly (minus the `.md` extension).

### Body: Heart

Enforces [[Decisions/Require Heart Section at Pattern Card Scale]]↗.

- The body MUST open with a `## Heart` section of two to three prose sentences that stand alone as the pattern at card scale.
- The Heart is not a summary of the longer body. It is the pattern compressed: the move and the moment of its use carried in just enough sentences to be actionable.

### Body: Problem

- A `## Problem` section MUST state the recurring difficulty the pattern addresses, in concrete terms drawn from actual graph or practice experience.
- The Problem MUST be recognizable by a reader who has not yet applied the pattern.

### Body: Forces

Enforces [[Decisions/Require Forces Authenticity in Patterns]]↗.

- A `## Forces` section MUST name at least two competing demands or constraints in genuine tension.
- Each Force SHOULD be named as a noun phrase and elaborated in one or two sentences describing what the Force wants and why it resists the other Forces.
- A Force that nobody would disagree with is not a Force — it is a value; genuine Forces pull against each other.

### Body: Solution

- A `## Solution` section MUST state the move that resolves the Forces, directly and imperatively. "Do X"; not "one could consider X."
- The Solution SHOULD show the move at work in the predicate or structural vocabulary of the prototype.

### Body: Consequences

- A `## Consequences` section SHOULD describe what follows from applying the Solution — benefits, costs, and the work the move takes on.
- A Consequences section that records only positives is a post-hoc justification, not an honest record.

### Body: Instances

- An `## Instances` section SHOULD list concrete cases where the pattern has been applied.
- Each instance SHOULD name the situation and the resolution.

### Body: Also Known As (Optional)

- An `## Also Known As` section MAY list alternate names the pattern carries in other vocabularies or traditions.

### Relations section

- The Relations section follows the base Markdown Node Contract.
- A Pattern typically carries these edges:
  - `grounded_in::[[Markdown Node Contract]]` or `grounded_in::[[Conviction Name]]` — the standing claim this Pattern realizes or restores. The paired node typically carries the inverse `informs_downstream::[[Pattern]]`.
  - `contrasts_with::[[Adjacent Pattern]]` — a sibling pattern occupying adjacent territory where the distinction is load-bearing.
  - `composes_with::[[Related Pattern]]` — another pattern routinely applied alongside this one.
  - `informs_downstream::[[Downstream Node]]` — nodes (contracts, conventions, other patterns) that encode or invoke this pattern's move.

### Optional scalar metadata

- YAML frontmatter SHOULD include `tagline:` (per Markdown Node Contract — surfaced on the Patterns index page row); MAY include `created:` and `brief_summary:`.
- Beyond the recommended `tagline:`, YAML is OPTIONAL for Patterns.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the move-or-condition filename pattern, the prohibition on `has_commitment::` and `decided_on::`, and the required Heart plus Problem plus Forces plus Solution body structure.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- contrasts_with::[[Decision Form Contract]]
  - A Decision records a situational commitment with `decided_on::` and `has_commitment::`; a Pattern records a recurring move without those predicates. A Decision may instantiate a Pattern in a specific context; the Pattern names the move the Decision embodies.

- grounded_in::[[Decisions/Adopt Wikilinks and Named Edges]]↗
  - The named-edge spine that lets a Pattern's `grounded_in::`, `contrasts_with::`, and `composes_with::` edges land as first-class relational claims rather than prose.

- grounded_in::[[Decisions/Name Patterns by Alexandrian Evocation]]↗
  - Grounds the filename pattern Requirement.

- grounded_in::[[Decisions/Require Heart Section at Pattern Card Scale]]↗
  - Grounds the Body-Heart Requirement.

- grounded_in::[[Decisions/Require Forces Authenticity in Patterns]]↗
  - Grounds the Body-Forces Requirement.

- grounded_in::[[Decisions/Reserve Predicate Vocabularies to Specific Forms]]↗
  - Grounds the prohibition on `has_commitment::` and `decided_on::` in the identity predicate block Requirement.

- grounded_in::[[References/A Pattern Language (Christopher Alexander et al., 1977)]]↗
  - The Alexandrian tradition's Heart-Problem-Forces-Solution structural shape is the parent vocabulary this contract mirrors. Downstream descendants of the tradition (Coplien's software patterns, Björk and Holopainen's game-design patterns, the Group Works deck's card-scale patterns) inherit the same shape; the local Reference aggregates the tradition rather than singling out any one descendant.
