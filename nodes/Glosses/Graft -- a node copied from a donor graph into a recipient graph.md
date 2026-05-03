---
tagline: A node copied from a donor graph into a recipient graph
created: 2026-05-03
---

- conforms_to::[[Gloss Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Graft

A graft is a node whose content was copied from one Deep Context graph (the donor) into another (the recipient), with the recipient taking ownership of the node's subsequent evolution. The donor's edits past the graft point do not flow into the recipient automatically -- a graft is a one-time content event with provenance recorded, not a sync relationship.

In horticultural terms a graft is the operation that joins a cutting from one plant onto another; in this graph the metaphor narrows to per-node copies. A recipient graph may carry grafts from any number of donors, and an individual node may have been grafted from a graph that itself grafted that node from elsewhere -- the recorded provenance is the immediate donor, not the chain.

A graft differs from a [[Adopt Scion Publication Model|Scion]] (a graph that claims wholesale lineage from a donor via `scion_of::`, intending to track upstream) and from an [[External Node -- a node that lives in another graph, referenced without being imported|External Node]] (a node referenced from another graph but not imported into it). The graft has copied; the scion has claimed; the external node has neither. A recipient graph may carry many grafts without being a scion, and a scion typically carries grafts as well -- the two axes (per-node copy vs graph-level lineage) compose rather than overlap.

## Relations

- composes_with::[[grafted_from -- per-node content provenance from a donor graph]]
  - The Predicate that records a graft as a typed edge on the recipient node, pointing to a Reference node that proxies the donor graph's external identity. The Gloss names the operation; the Predicate is its graph-layer expression.

- contrasts_with::[[External Node -- a node that lives in another graph, referenced without being imported]]
  - A graft has been copied into the recipient graph and is owned-and-edited locally; an External Node lives elsewhere and is referenced without import. Both name cross-graph relationships, but the boundary status differs: the graft has crossed, the external node has not.
