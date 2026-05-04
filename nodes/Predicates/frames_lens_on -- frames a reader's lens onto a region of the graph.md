---
tagline: Frames a reader's lens onto a region of the graph — the Touch Point's relation to its target
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# frames_lens_on

A predicate declaring that the subject Touch Point frames a reader's lens onto the target — a Gloss naming a community of practice, a Gloss naming a cross-cutting concept, or another concept-bearing node that names a region of the graph the reader is being oriented toward. The predicate's name carries its job: a *lens* (perspective, way of looking), framed *on* a target, by the subject Touch Point. The relation is directional from Touch Point to target with the reader as the implicit beneficiary.

The predicate is multi-valued in principle. A Touch Point may frame a coherent multi-part region by carrying several `frames_lens_on::` edges — for example, a home Touch Point may simultaneously orient readers to the Practice Domain Gloss, to the founding-decision Gloss, and to the project's two or three load-bearing argument-Glosses. Each edge names one facet of what the Touch Point's lens is *on*.

## Carries

The predicate names a Touch-Point-to-target framing relation from the Touch Point's perspective. The subject is the Touch Point; the object is what the reader is oriented toward. The edge carries three claims at once: that the subject's role is reader-orientation (not summary, not exhaustive coverage); that the target is a region the reader is being introduced to with a specific way-of-looking; and that the implicit beneficiary is the reader (human or LLM) approaching the target through the Touch Point.

A reader encountering `X frames_lens_on::Y` learns that X is a curated welcome that frames Y for them — the Touch Point offers a lens, and Y is what's looked-at-through-it. The edge does not assert that X covers Y exhaustively (Touch Points aren't summaries), nor that Y is the Touch Point's only target (multiple `frames_lens_on::` edges are permitted), nor that the lens X offers is the only valid lens (other Touch Points may frame Y differently for different readers).

## Crescent

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` names content influence on the subject's authoring — one node's reasoning draws on another's. The direction is toward the subject (the subject is shaped by the object). `frames_lens_on::` names reader-orientation from the subject — the subject (a Touch Point) frames the reader's encounter with the object. The direction is away from the subject (the subject orients the reader toward the object). Influence-on-authoring vs orientation-of-reader: opposite directions, different work. A Touch Point may carry both edges — `informed_by::` to a Reference whose framing shaped the Touch Point's authoring, and `frames_lens_on::` to the region it orients readers toward.

### Against [[informs_downstream -- providing substrate or evidence to a downstream node]]

`informs_downstream::` names a node's substrate-or-evidence relation to downstream nodes — the subject provides foundation for the object. `frames_lens_on::` names a Touch Point's reader-orientation relation to its target — the subject frames the reader's encounter with the object. Both are forward-directional from the subject, but the work differs: `informs_downstream::` provides substance the downstream node rests on; `frames_lens_on::` provides framing the reader looks through. Substrate vs lens.

## Typing

- **Subject:** A node conforming to the [[Touch Point Form Contract]]. The Touch Point's body provides the framing prose and Entry Points; the `frames_lens_on::` edges in its identity block name the framing's targets.
- **Object:** A concept-bearing node — typically a Gloss whose concept side names a community of practice, a cross-cutting concept, an argument, or any other named region of the graph. Polymorphic: the object MAY be a Gloss naming a community of practice (e.g., `[[Glosses/Deep Context Architecture]]↗`), a Gloss naming a specific concept (e.g., `[[Glosses/Minimum Viable Architecture]]↗`), a Decision the project is making (e.g., `[[Decisions/Adopt Wikilinks and Named Edges]]↗`), or any other node that names something a reader can be oriented toward. Touch Points point inward at the local graph; for cross-graph orientation, the object is a local Reference proxying the remote graph (per the Reference-as-proxy pattern that `grafted_from::` also uses).

## Instances

The graph's home Touch Point — `Deep Context Welcome -- a guided introduction to the practice for first-time readers` (designated by `is_home: true` in its YAML frontmatter) — carries the canonical instances:

```
- frames_lens_on::[[Glosses/Deep Context Architecture]]↗
- frames_lens_on::[[Decisions/Deep Context as an Architecture for Captured Reasoning]]↗
```

…orienting readers to the Practice Domain Gloss and the founding Decision simultaneously. Additional Touch Points may carry their own `frames_lens_on::` edges naming sub-regions, cross-cutting concepts, or arguments the project is making.

## Relations

- contrasts_with::[[informed_by -- weaker influence than grounded_in]]
  - Authoring-influence vs reader-orientation. Both edges may co-occur on a Touch Point: informed_by:: where the Touch Point's framing was shaped; frames_lens_on:: where the framing is now offered.

- contrasts_with::[[informs_downstream -- providing substrate or evidence to a downstream node]]
  - Substrate vs lens. Both forward-directional, but informs_downstream provides substance; frames_lens_on provides framing for a reader's encounter.

- composes_with::[[Touch Point Form Contract]]
  - The subject's typing rests on the Touch Point Form Contract — this edge appears specifically on Touch Point instances and is required by the Form. Without the Form, the predicate would lack a clear subject type; together they specify a coherent subject-and-relation pair.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - Each predicate answers one question. `frames_lens_on::` answers "what region is this Touch Point's lens on?" — distinct from substrate dependence (`built_on`), normative foundation (`grounded_in`), and authoring influence (`informed_by`).

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes reader-orientation load-bearing rather than collapsible. A region's "right way to look at it" varies across communities of practice; Touch Points (and this predicate) let multiple lenses on the same region coexist without forcing convergence.
