---
tagline: Foundational substrate the subject rests on
---

- conforms_to::[[Predicate Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# built_on

A predicate declaring that the subject rests on the object as a foundational substrate -- a file format, platform, protocol, or infrastructure layer the subject depends on in order to exist. The subject is the thing built; the object is the foundation. Unlike `has_component::` (which declares a part-of relationship), `built_on::` declares that the subject presupposes the object rather than being composed of it.

The edge lands in Relations on nodes whose identity or operation depends on a substrate layer below them: a Markdown Node built on CommonMark Markdown, a Contract built on the same substrate, a Decision coupled to a specific hosting platform. External targets (`↗`) are common because substrates frequently live in other graphs or traditions.

## Carries

The predicate names a dependent-to-substrate direction from the dependent's perspective. The subject is the thing that rests on something; the object is the foundation. The edge carries both technical foundations (the platform a system runs on) and conceptual ones (the file format a reading discipline layers on top of). When the subject is software and the object is infrastructure, the edge names the platform coupling. When the subject is a convention and the object is a file format, the edge names the substrate the convention presupposes.

A reader encountering `X built_on::Y` learns that X could not stand as itself without Y -- the substrate is a precondition, not a constituent. Changes at the substrate layer propagate to the subject; the subject's authors take on the object as an assumption they do not have to restate.

## Crescent

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` names dependence on a normative or structural commitment -- a Decision, Conviction, or Contract whose reasoning the subject inherits. `built_on::` names dependence on a substrate -- a file format, platform, or infrastructure layer. The axes are distinct: grounding runs through reasoning and justification; building-on runs through technical or conceptual foundations that are presupposed rather than reasoned-about. A Decision grounded_in a Conviction inherits normative force; a Contract built_on CommonMark presupposes CommonMark's existence. A node may carry both edges to different objects without the claims collapsing.

### Against [[has_component -- mereological relation where the subject contains the object as a component]]

`has_component::` names partial mereological composition -- the object is part of the subject. `built_on::` names substrate dependence -- the subject rests on the object without being composed of it. A Markdown Node has_component Wikilink Syntax (wikilinks are one of the things that make it a node); a Markdown Node built_on CommonMark (CommonMark is the file format the node-reading discipline layers atop). The same subject can carry both edges to the same object when the foundation doubles as a constituent, but the claims are distinct and typically attach to different objects.

## Typing

- **Subject:** Any node representing a thing that rests on a substrate -- a system, convention, artifact, or practice whose identity presupposes a lower layer.
- **Object:** Any node representing the substrate, platform, or foundational layer the subject depends on. Often an external (`↗`) reference to a file format, protocol, or hosting platform that lives in another graph.

## Instances

- `Markdown Node Contract` built_on `CommonMark Markdown` ↗ -- the Contract adds reading and authoring discipline on top of the CommonMark file format.
- `Markdown Node` built_on `CommonMark Markdown` ↗ -- a Markdown Node stays valid CommonMark; the node-reading discipline is layered on top, not a divergent dialect.
- `Link Rendered Pages to Markdown Source on GitHub` built_on `GitHub Pages` ↗ -- the Decision couples to GitHub Pages as the hosting platform; scions publishing elsewhere revise the coupling.

## Relations

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Substrate dependence vs reasoning dependence. The same subject often carries both edges (to different objects), but the axes are distinct.

- contrasts_with::[[has_component -- mereological relation where the subject contains the object as a component]]
  - Foundation vs constituent part. A substrate can be neither composed of nor exhaustively built-from the dependent; the dependent rests on the substrate without containing it.

- grounded_in::[[Adopt Predicate Atomicity]]
  - Each predicate answers one question. built_on answers "what substrate does X depend on?" -- an axis distinct from part-of-ness (has_component) and from reasoning-grounded-ness (grounded_in).

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes authoring substrate edges load-bearing. Leaving substrate dependence visible as a typed edge rather than as prose preserves the graph's navigability into external traditions (CommonMark, GitHub Pages) that the project builds on without adopting.
