---
tagline: Routinely used alongside
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# composes_with

A predicate declaring that the subject and object are adjacent concepts routinely applied together — the composition is a recurring move rather than a singular pairing. The edge carries the author's recognition that using the subject typically implies using the object, or that a reader who understands one is more likely to need the other close at hand.

The edge lands in Relations on nodes whose practical use is paired with another node's. Unlike `contrasts_with::`, which keeps adjacent concepts separate, `composes_with::` treats the adjacency as a resource: the subject and object compose in practice, and the graph carries the composition as a named move.

## Carries

The predicate names adjacency-with-pairing: the subject and object sit next to each other in conceptual space, and their use is typically paired. The pairing is not accidental co-occurrence; it is a recognizable move — a Pattern that routinely invokes another Pattern, a Contract whose Requirements are typically applied alongside another Contract's, a Predicate that commonly appears on nodes that also carry another named Predicate. The web of associations the predicate activates is the network of recurring compositions the graph has explicitly named; any node carrying `composes_with::` is declaring that its practical use is paired with the object's practical use.

Composition is an authorial observation, not a mechanical correlation. Two nodes that happen to be cited together do not automatically carry `composes_with::`; the edge is declared only when the author recognizes that the composition is a move worth naming, and that readers benefit from knowing the subject and object are typically used together.

## Crescent

### Against [[contrasts_with -- adjacent concept occupying different territory]]

`contrasts_with::` names adjacency-with-separation; `composes_with::` names adjacency-with-pairing. Both describe conceptual adjacency, but the authorial stance toward that adjacency is opposite. Contrast treats the adjacency as a distinction to preserve; composition treats it as a pairing to name. Choosing the wrong predicate inverts the intended reader response, as discussed in the `contrasts_with::` Crescent from the opposite side.

### Against [[has_component -- mereological relation where the subject contains the object as a component]]

`has_component::` names whole-to-part structural containment — the subject is made of the object as a part. `composes_with::` names adjacency composition — the subject and object are separate nodes typically used together. The distinction is structural: containment implies the object is inside the subject's own boundaries; composition implies the two remain separate and meet at a usage site. A compound node `has_component::` its constituent atomic nodes; a Pattern `composes_with::` another Pattern means the two Patterns are typically invoked in the same work even though they remain separate nodes. `has_component::` absorbed the previous `composed_of::` predicate when the partial/exhaustive distinction was consolidated; the adjacency-versus-containment contrast this Crescent names now runs against the single mereological predicate.

## Typing

- **Subject:** Any node whose practical use is paired with another node's.
- **Object:** Any node that pairs with the subject in practice.

## Instances

- `prototype/nodes/Convictions/Translation Over Convergence.md` and `prototype/nodes/Convictions/Vocabulary Diversity Is a Feature.md` compose in practice: authors reasoning about vocabulary decisions typically engage both Convictions together, since the substrate stance (diversity is a feature) and the operational rule (translation over convergence) are routinely applied jointly. A future `composes_with::` edge between them would formalize this recurring pairing.
- `prototype/nodes/Patterns/Progressive Summary Before Substance.md` and `prototype/nodes/Patterns/Reconcile the Standing Account.md` compose in practice: the summary-first pattern is typically invoked during the reconciliation pass's scan phase. A future `composes_with::` edge between them would formalize this recurring pairing.

## Relations

- contrasts_with::[[contrasts_with -- adjacent concept occupying different territory]]
  - Opposite authorial stances toward the same geometric adjacency: composition pairs, contrast separates.

- contrasts_with::[[has_component -- mereological relation where the subject contains the object as a component]]
  - Adjacency composition vs whole-to-part containment. The `has_component` Predicate absorbed the previously-separate `composed_of` predicate when the mereological axis was consolidated; the contrast this Crescent carries now runs against a single target.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes the composes_with-vs-contrasts_with stance distinction load-bearing. The same geometric adjacency supports two authorial stances; keeping both predicates preserves the difference.
