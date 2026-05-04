---
tagline: Mereological relation where the subject contains the object as a component
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# has_component

A predicate declaring that the subject contains the object as one of its components -- a mereological relation where the subject is a whole and the object is a named part. The edge names partial inclusion; the subject may carry additional `has_component::` edges to other parts, and the object may be a component of other wholes.

The edge lands in Relations on nodes that are composite concepts, artifacts, or systems. A Markdown Node has Wikilink Syntax and Named Edge as components; a Named Edge has Wikilink Syntax as a component; a Compound Node has Markdown Node as its constituent (previously written as `composed_of::`, consolidated into this predicate).

## Carries

The predicate names a whole-to-part direction. The subject is the containing whole; the object is a named component. The edge does not claim that the object is the sole or exhaustive component of the subject -- additional `has_component::` edges on the same subject name additional components, each its own partial-inclusion claim. The edge also does not claim that the object exclusively belongs to this subject; the same component can appear in multiple wholes.

A reader encountering `X has_component::Y` learns that Y is part of X's composition without learning whether Y is the whole of it. The partial-inclusion sense is what distinguishes this predicate from the substrate-dependence and reasoning-dependence predicates in the graph's vocabulary.

## Crescent

### Against [[built_on -- foundational substrate the subject rests on]]

`built_on::` names a foundation-to-dependent direction where the subject rests on an underlying substrate (a file format, a platform, an infrastructure layer). `has_component::` names mereological composition. The two predicates can apply to the same subject-object pair when a component also serves as a substrate, but they carry distinct claims: `has_component::` says "Y is part of X"; `built_on::` says "X depends on Y as foundation." A Markdown Node has_component Wikilink Syntax (wikilinks are part of what makes a file a node); a Markdown Node built_on CommonMark (CommonMark is the substrate file format that predates the node-reading discipline).

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` names intellectual or structural dependence on prior commitments -- a Decision grounded in a Conviction, a Requirement grounded in a Decision. `has_component::` names constitutive composition. The axes are distinct: grounding runs through reasoning and justification; component-containment runs through constitution. A Decision does not "have as a component" the Conviction that grounds it; it reasons from it. A Markdown Node does have as a component the Wikilink Syntax it contains.

## Typing

- **Subject:** Any node representing a composite concept, artifact, or system -- a Gloss whose referent decomposes into named parts, a Contract that includes other Contracts as components, a system whose structure is legibly compositional.
- **Object:** Any node representing one of the subject's constituent parts, components, or elements. External targets (`↗`) are permitted when the component lives in another graph or tradition.

## Instances

- `Markdown Node` has_component `Wikilink Syntax` ↗ and `Named Edge` -- wikilinks and named edges are among the components that make a file readable as a node in this graph.
- `Named Edge` has_component `Wikilink Syntax` ↗ -- the target half of a Named Edge is a wikilink.
- `Ghost Link` has_component `Wikilink Syntax` ↗ -- a ghost link uses the same syntactic substrate as a resolved wikilink.
- `Compound Node` has_component `Markdown Node` -- a compound's lead and sub-files are each Markdown Nodes; the folder groups them without adding node-level status to itself. This edge previously read as `composed_of::` before the consolidation.

## Relations

- contrasts_with::[[built_on -- foundational substrate the subject rests on]]
  - Mereology (part-of) vs foundation (rests-on). Both can apply to the same pair when a component doubles as a substrate, but the claims are distinct.

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Composition vs reasoning-dependence. has_component is about what a thing is made of; grounded_in is about what a thing reasons from.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - Each predicate answers one question. has_component answers "what is X made of?" at the partial-inclusion scale; the axis deliberately does not carry the exhaustive-constitution sense that would have motivated a separate predicate. The provisional `composed_of::` predicate that had emerged for exhaustive constitution was consolidated into this predicate because the partial/exhaustive distinction was not being worked in practice -- one edge existed, and its sense was expressible by annotating a `has_component::` edge.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes authoring mereological edges load-bearing. Leaving whole-to-part structure visible on the whole's node rather than requiring readers to infer it from prose preserves navigability at the edge-scanning scale.
