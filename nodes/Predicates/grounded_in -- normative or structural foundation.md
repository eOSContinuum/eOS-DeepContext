---
tagline: Normative or structural foundation
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# grounded_in

A predicate declaring that the subject rests on the object as its normative or structural foundation — a substrate the subject cannot hold without. The relationship is stronger than influence: a subject `grounded_in::` a target depends on that target for its own coherence, and removing the target would undermine the subject's claim to stand.

The edge lands in Relations when the subject is a node whose grounding is load-bearing for its authority — a Contract grounded in a Decision, a Requirement grounded in a Conviction, a Pattern grounded in a prior Pattern whose Forces the new Pattern inherits.

## Carries

The predicate names a foundation: the subject rests on the object as substrate, and the object's authority is what the subject's authority flows from. When a Contract's Requirement is `grounded_in::[[X Decision]]`, the Decision is what the Requirement cites as its source of commitment — the Requirement enforces what the Decision commits. When a Conviction is `grounded_in::[[Y Substrate Conviction]]`, the derivative Conviction specializes the substrate one and inherits its normative force. The web of associations the predicate activates is the stack of grounding under any claim in the graph — a reader traversing `grounded_in::` edges from a Requirement backwards reads the chain of commitments the Requirement rests on.

Grounding is structural, not decorative. A subject removed from its grounding is a subject without a foundation, and its authority is not recoverable from any other edge on the node. This is what distinguishes grounding from weaker influence relations like precedent or inspiration.

## Crescent

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` names weaker influence: the subject draws on the object as precedent or shape, but the object is not the subject's substrate. A subject `informed_by::` a target continues to stand if the target is weakened or withdrawn; a subject `grounded_in::` a target does not. The distinction is between shape-without-dependence (informed_by) and structural dependence (grounded_in). Authors making the choice between them signal how load-bearing the relation is: choosing `grounded_in::` is a stronger commitment than choosing `informed_by::`, and the predicate carries that weight.

### Against [[derived_from]]

Ghost link; `derived_from::` is not yet seeded as a Predicate. `derived_from::` is construction provenance — how this node came to exist, the antecedent conversation or meeting or prior reasoning that produced it. `grounded_in::` is normative or structural foundation — what this node rests on for its authority. The distinction is between construction (how it was built) and foundation (what it stands on). The same source can sometimes ground a node *and* be its construction antecedent; when that happens, both edges are appropriate, each carrying a distinct kind of relationship to the same target.

## Typing

- **Subject:** Any node whose coherence rests on a substrate — typically Contracts, Requirements, Convictions, Patterns, or other nodes whose authority is claim-bearing.
- **Object:** Typically a Conviction, Decision, or established Reference. The object MUST be a node whose own authority can bear the subject's weight.

### Conviction-to-Decision case: structural corollary

A Conviction MAY use `grounded_in::[[X Decision]]` when the Conviction is a *structural corollary* of the Decision — when the Decision's property is what makes the Conviction's stance possible to hold. The direction of authority in this case runs Decision → Conviction: the Decision enables the Conviction, and the Conviction would lose its basis if the Decision were withdrawn. Example: [[Convictions/Folders Serve Human Legibility, Not the Graph]]↗ carries `grounded_in::[[Decisions/Adopt Wikilinks and Named Edges]]↗` because without wikilinks-by-filename and author-declared edges, folders would have to carry graph semantics, and the folder-independence stance could not be held.

This case contrasts with the substrate-side relation, where a Conviction is the normative substrate that *generates* a Decision — that direction uses `informs_downstream::` from the Conviction (see [[informs_downstream -- providing substrate or evidence to a downstream node|informs_downstream]] Typing). Both predicates may legitimately connect a Conviction and a Decision; the choice between them encodes which one is the normative source and which is the structural corollary, and the distinction is preserved by writing the edge on the dependent side in each case.

## Instances

- `prototype/nodes/Contracts/Gloss Form Contract.md` carries `grounded_in::[[Decisions/Use Double-Hyphen Separator for Gloss Definitions]]↗` — the Contract's filename-pattern Requirement rests on the Decision's commitment. Removing the Decision from the graph would leave the Requirement without a basis.
- `prototype/nodes/Convictions/Translation Over Convergence.md` carries `grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗` — the specialized Conviction rests on the substrate Conviction. The translation-over-convergence operational rule has no normative basis without the diversity-is-a-feature stance underneath it.

## Relations

- contrasts_with::[[informed_by -- weaker influence than grounded_in]]
  - Same direction, different weight. `grounded_in::` is structural dependence; `informed_by::` is shape-without-dependence. The author's choice between them signals the relation's load-bearing level.

- contrasts_with::[[derived_from]]
  - Ghost link; target Predicate not yet seeded. The Crescent names the distinction between normative/structural foundation (grounded_in) and construction provenance (derived_from).

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes naming the grounded_in-vs-informed_by distinction load-bearing at the predicate layer. The distinction encodes a specific kind of dependence that the project commits to preserving against convergence pressure.

- contrasts_with::[[in_practice_domain -- membership in a Practice Domain]]
  - `grounded_in::` is normative or structural dependence on a foundation node; `in_practice_domain::` is membership of a concept in a community-of-practice's shared language. Same node may grouned_in:: a Conviction and live in_practice_domain:: a Gloss; the Predicates name different kinds of belonging.

- contrasts_with::[[scion_of -- content lineage from a template graph]]
  - `grounded_in::` carries a normative or structural relation between graph-internal nodes; `scion_of::` carries graph-level lineage between this graph and a template graph. The first is internal authority, the second is genealogical provenance.

- contrasts_with::[[has_component -- mereological relation where the subject contains the object as a component]]
  - `grounded_in::` is foundation (object supports subject); `has_component::` is mereology (object is part of subject). Both are structural but the inversion of containment direction is load-bearing.
