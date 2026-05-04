---
tagline: Providing substrate or evidence to a downstream node
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# informs_downstream

A predicate declaring that the subject provides substrate, evidence, or influence to the object — the forward edge on the substrate side of a relationship whose dependent-side edge is `grounded_in::` or `informed_by::`. The subject is what the object draws on; the edge makes the subject's downstream role visible from the subject's own node.

The edge lands in Relations on nodes that have downstream work — a Reference that informs multiple Decisions, a Decision that informs a Contract's Requirements, a Conviction that informs specialized Convictions. Authors choose whether to document the relationship from the substrate side (`informs_downstream::`) or the dependent side (`grounded_in::` / `informed_by::`); both sides documenting is common and preserves the bidirectional visibility.

## Carries

The predicate names a substrate-to-dependent direction. The subject is the providing side; the object is the drawing side. When a Decision writes `informs_downstream::[[X Contract]]`, the Decision declares that the Contract's Requirement carries the thin enforcement clause pointing back at it — the reader standing at the Decision can trace forward to where the Decision is cashed out. When a Reference writes `informs_downstream::[[Y Conviction]]`, the Reference declares its downstream role in the Conviction's argumentative substrate.

The web of associations the predicate activates is the forward side of provenance — from source to use, from commitment to enforcement, from substrate to specialization. The predicate is the graph's way of making a node's downstream presence visible without requiring a reader to crawl backwards from every potential dependent. Navigability improves when both directions carry edges; traversal is symmetric rather than one-sided.

## Crescent

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` is the dependent-side edge for structural dependence; `informs_downstream::` is the substrate-side edge. They describe the same relationship from opposite ends — a Contract's Requirement `grounded_in::` a Decision and the Decision `informs_downstream::` the Contract are two edges on the same relation, each documented on the respective node. The distinction between the two predicates is direction and location, not substance: one is written on the dependent, the other on the substrate. Authors document both when navigability from either direction is useful; they document only one when the direction-asymmetry is acceptable.

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` is the dependent-side edge for weaker influence; `informs_downstream::` is the substrate-side edge that can carry either the weaker or stronger kind of relationship. When the author writes `informs_downstream::[[Y]]` on a source node, the downstream node's own declaration (`grounded_in::` or `informed_by::`) carries the weight distinction — `informs_downstream::` does not specify whether the downstream draws on this node as substrate or as influence. This is a deliberate asymmetry: the dependent side owns the weight claim because the dependent is what would or would not continue to stand without the substrate.

## Typing

- **Subject:** Any node that has downstream presence in the graph.
- **Object:** Any node that draws on the subject as substrate or influence. The object MUST carry a corresponding `grounded_in::` or `informed_by::` edge back to the subject for the relation to be mutually visible; partial visibility (only `informs_downstream::` on the subject) is permitted but weaker.

### Conviction-to-Decision case: normative substrate

A Conviction MAY use `informs_downstream::[[X Decision]]` when the Conviction is the *normative substrate* the Decision serves — when the stance commits the project to something the Decision is the structural realization of. The direction of authority runs Conviction → Decision: the Conviction generates the Decision, and the Decision would lose its grounding if the Conviction were weakened. Example: [[Convictions/Human Authority Over Augmentation Systems]]↗ carries `informs_downstream::[[Decisions/Adopt Wikilinks and Named Edges]]↗` because the commitment to human authority over augmentation is what generates the requirement that edges be author-declared rather than tool-inferred.

This case contrasts with the corollary-side relation, where a Conviction is a structural corollary *enabled by* a Decision — that direction uses `grounded_in::` from the Conviction (see [[grounded_in -- normative or structural foundation|grounded_in]] Typing). Both predicates may legitimately connect a Conviction and a Decision; the choice between them encodes whether the Conviction generates the Decision (normative substrate) or the Decision enables the Conviction (structural corollary). Back-edges from the Decision (`informs_downstream::` or `informed_by::` pointing back at the Conviction) are optional and discovered by search, matching minimal-back-edges practice rather than being part of the convention.

## Instances

- `prototype/nodes/Decisions/Require Body Elaboration Beyond Filename Definition.md` carries `informs_downstream::[[Gloss Form Contract]]` — the Decision declares that Gloss Form Contract's Body-shape Requirement carries the thin enforcement clause pointing at this Decision. The corresponding `grounded_in::` edge is on Gloss Form Contract itself.
- `prototype/nodes/Decisions/Require Carries Section in Predicate Nodes.md` carries `informs_downstream::[[Predicate Form Contract]]` — the Decision seeded in this plan declares its downstream role in Predicate Form Contract's Body-Carries Requirement.

## Relations

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Same relation, opposite direction: `grounded_in::` on the dependent side, `informs_downstream::` on the substrate side. The predicate pair carries a bidirectional edge split into two one-sided declarations.

- contrasts_with::[[informed_by -- weaker influence than grounded_in]]
  - Same relation, opposite direction (with the weight distinction owned by the dependent side). `informed_by::` on the dependent side, `informs_downstream::` on the substrate side. The substrate-side predicate does not specify the weight; the dependent side does.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes authoring bidirectional provenance edges load-bearing. Leaving the substrate-side visible on its own node (rather than requiring dependents to declare their own draws) preserves navigability that an extraction agent could otherwise flatten.

- contrasts_with::[[frames_lens_on -- frames a reader's lens onto a region of the graph]]
  - `informs_downstream::` is substrate-side provenance directed at dependent nodes; `frames_lens_on::` is reader-orientation directed at a region of the graph from a Touch Point. The first carries causal/normative influence outward; the second carries a curated way of looking inward.
