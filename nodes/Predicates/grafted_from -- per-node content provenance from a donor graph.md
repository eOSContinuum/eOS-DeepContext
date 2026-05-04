---
tagline: Per-node content provenance from a donor graph
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# grafted_from

A predicate declaring that the subject node was grafted into this graph from the donor graph the object names. The object is a Reference node in the recipient's `nodes/References/` that proxies the donor graph -- the Reference carries the donor's URL, DID, and revision at graft time as scalar metadata, while the predicate itself stays a clean local wikilink. The edge names per-node content provenance without claiming graph-level lineage.

The Reference-as-proxy pattern lets `grafted_from::` resolve as a normal local wikilink rather than as a DID-stuffed external marker. A donor graph need not have a DID resolver to be cited; the recipient's Reference node carries enough about the donor for a reader to navigate, and any DID-resolver future can extend the Reference without changing the graft edge's shape. A recipient with grafts from multiple donors carries one Reference node per donor, even when many recipient nodes were grafted from the same source.

## Carries

The predicate names a content-copy event from the recipient's perspective. The subject is the grafted node in this graph; the object is a Reference node describing the donor graph. The edge carries three claims at once: that the subject's content originated as a copy of a node in the donor graph; that the recipient has taken ownership of subsequent evolution; and that no upstream-tracking relationship exists between the recipient and the donor by virtue of this edge alone.

A reader encountering `X grafted_from::Y` learns that X's content originated outside this graph and entered through a one-time copy event whose donor metadata lives in the Y Reference node. The edge does not carry sync obligation -- the donor's later edits do not flow into X automatically -- and does not carry normative inheritance -- X may be revised freely by the recipient without reference back to the donor.

## Crescent

### Against [[scion_of -- content lineage from a template graph]]

`scion_of::` names a graph-level wholesale-lineage claim: the subject is a scion graph that intends the object as its template and may pull updates or peer with siblings. `grafted_from::` names a node-level content-copy event with no lineage claim and no upstream-tracking implication. A graph may carry many `grafted_from::` edges (one per grafted node) without being a scion; a scion typically carries `grafted_from::` edges as well, but the `scion_of::` edge is what claims the lineage. Per-node copy is one axis; whole-graph lineage is another, and the same recipient may carry both kinds of edges to the same donor without contradiction.

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` names content influence without copy -- one node's reasoning draws on another's, but the content was authored locally. `grafted_from::` names content copy -- the bytes came from elsewhere. A node informed_by an adjacent node read the adjacent node and authored its own content; a node grafted_from a donor copied the donor's content and may have edited it since. Reading vs copying is the distinction the crescent holds; the same recipient node may carry both edges to different objects, with grafted_from naming where it came from and informed_by naming what shaped subsequent local edits.

## Typing

- **Subject:** A node in the recipient graph whose content was copied from a node in another graph. Any node form may be the subject of a `grafted_from::` edge; Contracts, Predicates, Skills, and Glosses are common subjects when meta-layer content is grafted.
- **Object:** A Reference node in the recipient graph (`nodes/References/`) that proxies the donor graph. The Reference's frontmatter carries the donor's URL and the donor's DID (`this_did:` from the donor's identity file), and may carry the donor's commit SHA at graft time. The Reference body uses the standard Reference Form Contract shape with Adopted / Not adopted sections naming what was grafted and what was deliberately not.

## Instances

No instances exist in this graph. DeepContext.com is the seed graph with no grafts of its own; recipients of grafts (such as eOS-DeepContext, which grafted the meta-layer from this graph) carry the predicate on their grafted nodes once provenance is recorded.

A hypothetical graft recorded in a recipient graph would carry on each grafted node:

```
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
```

…where `DeepContext.com Graph (Allen, 2026)` is a Reference node in the recipient's `nodes/References/` carrying DeepContext.com's URL, DID (`did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae`), and the donor's commit SHA at graft time.

## Relations

- contrasts_with::[[scion_of -- content lineage from a template graph]]
  - Per-node copy vs whole-graph lineage. Both are cross-graph relationships, but at different scales: scion_of attaches to a graph (recorded canonically in `.deep-context-identity.yml`), grafted_from attaches to nodes individually.

- contrasts_with::[[informed_by -- weaker influence than grounded_in]]
  - Copying vs reading. informed_by names content influence; grafted_from names content origin. A node may carry both edges to different objects.

- composes_with::[[Reference Form Contract]]
  - The object's typing depends on the Reference Form Contract. The Reference proxies the donor graph as an external source; the predicate's wikilink target is local but the donor it proxies is external. Without the Reference Form, this predicate would have no clean place to land its donor metadata.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - Each predicate answers one question. grafted_from answers "what donor graph did this node's content come from?" -- distinct from graph lineage (scion_of), influence (informed_by), and substrate dependence (built_on).

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes per-node provenance load-bearing rather than collapsible into a graph-level claim. Recording the donor of a specific node preserves the recipient's ability to diverge from the donor's vocabulary without losing the trace of where the content originated.

- composes_with::[[Graft -- a node copied from a donor graph into a recipient graph]]
  - The Gloss that names the act this Predicate records. A Graft is the node-level copy operation; `grafted_from::` is the edge that captures which donor the copy came from. The Predicate is the structural counterpart to the Gloss's vocabulary entry.
