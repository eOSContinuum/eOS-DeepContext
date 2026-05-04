---
tagline: Membership in a Practice Domain — the shared language community a node participates in
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# in_practice_domain

A predicate declaring that the subject node belongs to the Practice Domain the object names — the shared language community of practitioners and conventions within a bounded context where specific terms carry compressed meaning. Replaces the earlier bare `in_domain::`, whose generic noun ("domain") conflated multiple senses (web domain, library-science knowledge domain, problem domain). `in_practice_domain::` names the kind of domain explicitly: a shared-language community in this graph's vocabulary. The object is a Gloss whose concept side names the community of practice (e.g., `[[Glosses/Deep Context Architecture]]↗`, `[[Self-Sovereign Identity]]`, `[[Anthropology]]`).

The predicate is multi-valued in principle. Most nodes belong to a single Practice Domain (the one whose conventions they were authored under). Bridge content — Concept Facets that cross practitioner communities, References cited across multiple fields — may carry several `in_practice_domain::` edges, recording participation in each community's shared language.

## Carries

The predicate names a node-to-Practice-Domain membership relation from the node's perspective. The subject is the node; the object is the Practice Domain. The edge carries the claim that the node's vocabulary, conventions, and audience are shaped by the named Practice Domain — readers approaching the node should expect terms to carry the meanings the Practice Domain assigns them, and authoring choices to follow that community's conventions.

A reader encountering `X in_practice_domain::Y` learns that X participates in Y's shared language community. The edge does not assert that X is unique to Y (multiple `in_practice_domain::` edges are permitted), nor that X covers all of Y (a Practice Domain accumulates many member nodes; this edge is just one membership claim). The edge does not carry sync obligation — the node's evolution is not bound to the Practice Domain's evolution — and does not carry normative inheritance — the node's specific reasoning lives in its own `grounded_in::` and `informed_by::` edges, not implied by community membership.

## Crescent

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` names normative or structural dependence — a node's reasoning rests on a specific Decision, Conviction, or Contract. `in_practice_domain::` names community membership — a node's vocabulary belongs to a shared language community. A node may carry both edges to different objects without contradiction: grounding runs through reasoning and justification, community membership runs through shared language and conventions. Removing a `grounded_in::` target would break the subject's claim; removing the `in_practice_domain::` edge would not break the subject but would orphan its vocabulary from any community.

### Against [[built_on -- foundational substrate the subject rests on]]

`built_on::` names substrate dependence — a file format, platform, or infrastructure layer below the subject. `in_practice_domain::` names community membership above the subject in the social-cultural sense. A Markdown Node Contract may be `built_on::[[CommonMark Markdown]]↗` (substrate technical layer) and simultaneously `in_practice_domain::[[Glosses/Deep Context Architecture]]↗` (community cultural layer); the edges name relations on orthogonal axes.

## Typing

- **Subject:** Any node in the graph. Every authored node SHOULD carry at least one `in_practice_domain::` edge in its identity block, naming the community whose shared language it participates in. Nodes without such an edge are vocabulary-orphaned — readable only by readers who already know which community's terms apply.
- **Object:** A Gloss whose concept side names a community of practice (e.g., `[[Glosses/Deep Context Architecture]]↗`, `[[Self-Sovereign Identity]]`). The Gloss's body defines the community and may carry SKOS-style `narrower::`/`broader::`/`related::` edges to other communities. A separate Practice Domain Form Contract was considered but not authored: the structural-index work (Scope, Key Nodes, Open Questions) is optional body content a Gloss may carry by convention, not a form-level requirement.

## Instances

Every meta-layer node in this graph carries `in_practice_domain::[[Glosses/Deep Context Architecture]]↗` — Deep Context Architecture is the practitioner community whose shared language and conventions this graph documents. Other graphs that graft Deep Context Architecture's meta-layer (e.g., the eOS-DeepContext graph) carry the same edge on grafted nodes; their project-specific content nodes carry edges to their own Practice Domains.

A bridge example, for a Concept Facet that crosses multiple communities:

```
- in_practice_domain::[[Anthropology]]
- in_practice_domain::[[Management Theory]]
```

…recording that the Concept Facet's vocabulary is read in each community's specific way, with the cross-community framing being load-bearing for the facet's claims.

## Relations

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Community membership vs reasoning dependence. The same subject often carries both edges (to different objects), expressing that the node belongs to a community and rests on specific reasoning within or alongside it. Removing membership orphans vocabulary; removing grounding breaks the subject's claim.

- contrasts_with::[[built_on -- foundational substrate the subject rests on]]
  - Cultural-layer membership vs technical-layer substrate. A node may be in a Practice Domain (community) and built on a substrate (technology) without contradiction; the edges name relations on different axes.

- composes_with::[[Gloss Form Contract]]
  - The object's typing rests on the Gloss form: a node whose filename carries its working definition. The Predicate names node-to-community-of-practice membership; the object Gloss carries the community's definition and may decorate itself with SKOS-style edges to other communities. A separate Practice Domain Form Contract was considered but not authored — Gloss form is sufficient.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - Each predicate answers one question. `in_practice_domain::` answers "what shared language community does this node belong to?" — distinct from substrate dependence (`built_on`), normative foundation (`grounded_in`), and content provenance (`grafted_from`).

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes Practice-Domain membership load-bearing rather than collapsible. Recording which community a node participates in preserves the recipient's ability to translate across communities without losing the trace of which vocabulary the node's terms come from.
