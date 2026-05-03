---
tagline: Open tension with adjacent concept
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# contends_with

A predicate declaring that the subject sits inside an unresolved tension with the object — the tension is a load-bearing feature of both nodes, not a drift signal to be resolved by picking a side. The edge carries the author's recognition that two legitimate stances are in conflict and that the conflict is itself what the relationship contributes.

The edge lands in Relations on nodes whose content is partly defined by the tension they hold with adjacent nodes. A Conviction may contend with a practical constraint; a Decision may contend with an Aspiration that it does not yet fully satisfy; a Pattern may contend with another Pattern whose Forces overlap.

## Carries

The predicate names tension-as-first-class-content: the subject's relationship to the object is characterized by unresolved debate, pulling in different directions, or claims that cannot be simultaneously satisfied. Both sides are legitimate — neither the subject nor the object is claimed wrong — and the tension is what the relationship preserves rather than a problem it points toward. The web of associations the predicate activates is the network of open tensions the graph has explicitly acknowledged; any node carrying `contends_with::` is declaring that a load-bearing debate is present.

Holding tension rather than resolving it is a deliberate stance. The alternative — privileging one side and documenting the other as rejected or obsolete — would flatten a real tension into a false resolution. The predicate is the graph's way of saying "these two are in conflict; the conflict is real; both are kept."

## Crescent

### Against [[contrasts_with -- adjacent concept occupying different territory]]

`contrasts_with::` names distinction without tension: the subject and object are different, the difference is preserved, but neither side is in debate. `contends_with::` names tension as first-class content: the subject and object are in unresolved conflict, and the conflict is what the relationship carries. Contrast is a stable stance toward adjacency; contention is an active stance toward disagreement. A relationship may legitimately shift between the two — a contrast can escalate to contention when tension emerges, and a contention can de-escalate to contrast when the tension resolves — but the predicates are distinct because they describe different authorial stances at the moment of authoring.

### Against [[contradicts]]

Ghost link; `contradicts::` is used in adjacent vocabularies but not seeded as a Predicate in this graph. `contradicts::` names directional negation: the subject claims the object is wrong, and the two sides are held as incompatible. `contends_with::` holds both sides as legitimate and the tension between them as first-class content — neither is claimed wrong. The distinction is load-bearing at the cross-vocabulary level because a graph that uses `contradicts::` to name disagreements records a different stance than one that uses `contends_with::`: contradiction asserts a winner-to-be, contention preserves the unresolved state. An author migrating between vocabularies carries the stance difference, not merely the word choice.

## Typing

- **Subject:** Any node where a standing tension with another node is acknowledged.
- **Object:** Any node that is the other side of the tension.

## Instances

- `Contract Form Contract` carries `contends_with::[[Convention Overhead vs Graph Quality]]` — the Contract's existence raises the cost of authoring a new Contract, and the trade-off between the discipline the Contract enforces and the friction that discipline creates is acknowledged as an unresolved tension rather than resolved by picking a side.
- `Skill Form Contract` carries `contends_with::[[Convention Overhead vs Graph Quality]]` — same shape, at a different layer: the Skill Form Contract raises the cost of authoring a skill in exchange for structural legibility of skills as graph nodes, and the edge declares the trade-off as open rather than resolved.

## Relations

- contrasts_with::[[contrasts_with -- adjacent concept occupying different territory]]
  - Different stances toward adjacency: contention holds tension as first-class; contrast preserves distinction without tension.

- contrasts_with::[[contradicts]]
  - Ghost link; target Predicate not seeded. Held-as-legitimate tension vs directional negation.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes naming tension-vs-contrast-vs-contradiction load-bearing. Each stance toward disagreement is a distinct predicate in this vocabulary, and the distinctions are the content the project commits to preserving.
