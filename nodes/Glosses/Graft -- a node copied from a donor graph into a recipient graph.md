---
tagline: A node copied from a donor graph into a recipient graph
created: 2026-05-03
---

- conforms_to::[[Gloss Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Graft

A graft is a node whose content was copied from one Deep Context graph (the donor) into another (the recipient), with the recipient taking ownership of the node's subsequent evolution. The donor's edits past the graft point do not flow into the recipient automatically -- a graft is a one-time content event with provenance recorded, not a sync relationship.

In horticultural terms a graft is the operation that joins a cutting from one plant onto another; in this graph the metaphor narrows to per-node copies. A recipient graph may carry grafts from any number of donors, and an individual node may have been grafted from a graph that itself grafted that node from elsewhere -- the recorded provenance is the immediate donor, not the chain.

A graft differs from a [[Decisions/Adopt Self-Sovereign Graph Publication|Scion]]↗ (a graph that claims wholesale lineage from a donor via `scion_of::`, intending to track upstream) and from an [[Glosses/External Node -- a node that lives in another graph, referenced without being imported|External Node]]↗ (a node referenced from another graph but not imported into it). The graft has copied; the scion has claimed; the external node has neither. A recipient graph may carry many grafts without being a scion, and a scion typically carries grafts as well -- the two axes (per-node copy vs graph-level lineage) compose rather than overlap.

## Relations

- composes_with::[[grafted_from -- per-node content provenance from a donor graph]]
  - The Predicate that records a graft as a typed edge on the recipient node, pointing to a Reference node that proxies the donor graph's external identity. The Gloss names the operation; the Predicate is its graph-layer expression.

- contrasts_with::[[Glosses/External Node -- a node that lives in another graph, referenced without being imported]]↗
  - A graft has been copied into the recipient graph and is owned-and-edited locally; an External Node lives elsewhere and is referenced without import. Both name cross-graph relationships, but the boundary status differs: the graft has crossed, the external node has not.

- composes_with::[[Reference Form Contract]]
  - A donor Reference (one carrying both `this_did:` and `url:` in its frontmatter) is the proxy through which a graft's donor graph is identified. The Reference Form Contract specifies what makes a Reference a donor; the Graft Gloss names the act of copying from one.
