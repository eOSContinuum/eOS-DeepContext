---
tagline: Weaker influence than grounded_in
---

- conforms_to::[[Predicate Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# informed_by

A predicate declaring that the subject draws on the object as precedent or influence without structural dependence — the object shapes the subject without being its substrate. The subject continues to stand if the object is weakened or withdrawn; the relationship marks source or inspiration, not foundation.

The edge lands in Relations to record precedents, prior reasoning, and external sources the subject takes shape from. It is the most common provenance predicate in the graph — many nodes are informed by external sources, by earlier Decisions, or by adjacent Observations without being structurally dependent on them.

## Carries

The predicate names shape-without-dependence: the subject takes influence from the object — the object's concepts, framing, or prior reasoning leave marks on the subject's content — but the subject does not rest on the object for its own coherence. Removing the object from the graph weakens the subject's context and readability, but the subject's claim still stands on its other grounding. The web of associations the predicate activates is a provenance trail of influences and precedents — a reader traversing `informed_by::` edges reads the context that shaped the subject without tracing a load-bearing foundation.

The predicate is the graph's default for acknowledging intellectual debts. When a Conviction draws on an external gist for its argumentative substrate, `informed_by::` is the honest predicate — the Conviction restates and specializes the source's argument, but the Conviction's authority comes from being held by the project, not from citing the source. When a Decision cites an earlier Decision as precedent for its framing, `informed_by::` is the honest predicate — the precedent shaped the later Decision's structure, but the later Decision does not inherit the earlier one's commitment.

## Crescent

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` names structural dependence; `informed_by::` names shape-without-dependence. The distinction matters at authoring time — the author chooses which predicate by asking whether the subject continues to stand without the object. If the subject would lose its foundation, `grounded_in::` is the predicate; if the subject would lose context but still stand, `informed_by::` is the predicate. Getting the choice wrong understates or overstates the relationship's weight, either promoting a precedent to foundation (inflating its authority) or demoting a foundation to precedent (losing the grounding trail).

### Against [[responds_to -- direct reply creating a conversation thread]]

`informed_by::` describes diffuse influence at any temporal distance, with no requirement that the subject be a reply to the object. `responds_to::` describes a direct reply: the subject is authored as a response to a specific target, and the two together form a conversation thread the reader can trace. A node `informed_by::` a gist written years earlier is shaped by the gist across a long distance with no reply structure; a meeting note `responds_to::` a specific proposal document creates a thread with short temporal distance and a specific referent. The distinction preserves conversation structure that `informed_by::` alone flattens.

## Typing

- **Subject:** Any node.
- **Object:** Any node, commonly a Reference, Observation, or earlier Decision. The object's shape is the source the subject draws on; any node that has left an authorial trace can serve.

## Instances

- [[Vocabulary Diversity Is a Feature]] (Conviction) carries `informed_by::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]` — the gist supplies the argumentative substrate the Conviction compresses (the three-cost analysis of convergence), but the Conviction stands as its own held stance independent of the gist's continued accessibility.
- [[Translation Over Convergence]] (Conviction) carries `informed_by::[[Consensus Creates Priesthoods]]` — the Observation supplies empirical grounding for one of the convergence costs the Conviction's Why rests on, but the Conviction does not structurally depend on the Observation (the held stance stands even if the empirical grounding weakens).

## Relations

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Same direction, different weight. `informed_by::` is shape-without-dependence; `grounded_in::` is structural dependence. The author's choice signals the relation's load-bearing level.

- contrasts_with::[[responds_to -- direct reply creating a conversation thread]]
  - `informed_by::` is diffuse influence at any temporal distance; `responds_to::` is direct reply within a thread. Both are provenance predicates but they preserve different structures — influence versus conversation.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes the informed_by-vs-grounded_in weight distinction and the informed_by-vs-responds_to conversation distinction load-bearing. Both distinctions encode specific relational kinds the project commits to preserving.
