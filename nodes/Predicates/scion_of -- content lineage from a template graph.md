---
tagline: Content lineage from a template graph
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# scion_of

A predicate declaring that the subject is a scion whose content was instantiated from the object, which is a template graph. The object is identified by its `did:repo:<sha1>` DID with an `↗` external marker — the template lives in another graph (a different repository with a different inception commit). The subject carries its own DID derived from its own Open Integrity inception commit; the object's DID is distinct. The edge names content lineage without claiming cryptographic identity inheritance.

The edge's canonical record lives in the scion's `.deep-context-identity.yml` — a root-level dotfile that Bootstrap writes when the scion is first stood up. The file holds the template's DID under `scion_of:` and the scion's own DID under `this_did:`; graph tools that want to traverse the scion-of edge read the YAML value. The scion may additionally carry the wikilink form (`scion_of::[[did:repo:<template-sha1>]]↗`) in its identity predicate block if traversability via graph-layer queries matters on that scion. The edge is not expected to appear in DeepContext.com itself, which is the root template and has no template of its own to derive from.

## Carries

The predicate names a template-to-scion relationship from the scion's perspective. The subject is the scion; the object is the template the scion was instantiated from. The edge carries two specific claims at once: first, that the scion's content shape (conventions, form contracts, pipeline, seed nodes as starting material) came from the template; second, that the scion's cryptographic identity is separate from the template's, because Open Integrity inception requires a fresh empty-root commit rather than a shared one. Content is inherited; identity is not.

A reader encountering `S scion_of::T↗` learns that the subject S is a template-derived graph whose content began as a copy of T's, that S has since diverged or will diverge as its authors see fit, and that S's own DID is what makes it addressable as distinct from T. The edge does not carry sync obligation — S is not expected to pull changes from T — and does not carry normative inheritance — S may revise any Convictions, Decisions, or Contracts it inherited, and the revisions are S's to own without reference back to T.

## Crescent

### Against [[built_on -- foundational substrate the subject rests on]]

`built_on::` names substrate dependence — a file format, platform, or infrastructure the subject rests atop. `scion_of::` names graph-instance lineage — both subject and object are first-class graphs with their own DIDs, and the relationship is instantiation rather than substrate layering. A Markdown Node is `built_on::[[CommonMark Markdown]]↗` because CommonMark is the format underneath it; a scion is `scion_of::[[did:repo:<template-sha1>]]↗` because the template is a peer graph that the scion was stood up from. Substrate is below; template is alongside.

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` names dependence on a normative or structural commitment — a Decision, Conviction, or Contract whose reasoning the subject inherits. `scion_of::` is narrower and does not carry normative inheritance automatically. A scion inherits the template's Convictions by default (see `Adopt Self-Sovereign Graph Publication`), but the scion may revise any of them without losing its scion-of relationship. `grounded_in::` asserts that removing the grounding breaks the subject; `scion_of::` asserts only that the subject's content began as an instantiation of the object's.

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` names content influence across adjacent nodes or external sources — one node's reasoning draws on another's without being forced by it. `scion_of::` is specifically the template-to-scion instantiation relation at the graph-instance layer, with the additional cryptographic commitment that the subject's DID is not the object's. `informed_by::` could connect two references or two Convictions within one graph; `scion_of::` connects two graphs.

### Against [[extends_contract -- strict inheritance between form contracts]]

`extends_contract::` names strict inheritance between form contracts — one Contract inherits all requirements of another and may add more. `scion_of::` names graph-instance lineage — one graph was instantiated from another and may revise anything it inherited. Contract extension is tight and rule-preserving; scion instantiation is loose and revision-permitting.

## Typing

- **Subject:** A scion repository. The canonical record lives in the scion's `.deep-context-identity.yml` at the repository root; when a graph-layer wikilink form is additionally used, it lands in the scion's identity predicate block on a markdown file the scion designates. The subject is the graph that carries the edge; the graph's own DID is not named by this edge but by the `did:repo:<sha1>` of its own inception commit.
- **Object:** A template graph, identified by its `did:repo:<sha1>` DID, external marker `↗`. The template lives in a different repository with a different inception commit. Human-facing annotation may accompany the DID to name the template's URL or common name.

## Instances

No instances exist in this graph. DeepContext.com is the root template, not a scion of anything, and carries no `scion_of::` edges. The predicate is seeded here because every scion instantiated from this template will record the relationship in its own `.deep-context-identity.yml` (structural record) and may additionally carry the wikilink form in its identity predicate block (graph-traversable record).

A hypothetical scion's `.deep-context-identity.yml` carries:

```yaml
this_did: did:repo:<scion-inception-sha1>                   # the scion's own DID, written by Bootstrap
scion_of: did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae # the DID of the graph this scion was cloned from
```

The root template (DeepContext.com) ships the same file with `this_did:` set to its own DID and `scion_of: null` — the root has no template to derive from. An annotation accompanying the record (either in the file's comments or in a Relations edge on a graph-layer node) may name the template's URL, the practical provenance, and any specific keep/extend/override decisions the scion has made about the template's Convictions.

## Relations

- contrasts_with::[[built_on -- foundational substrate the subject rests on]]
  - Substrate vs template. Substrate is below the subject (the subject runs on top); a template is alongside the subject (they are peer graphs with the template-scion relationship expressed explicitly).

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Normative inheritance vs instantiation. A scion can revise any inherited commitment without losing its scion-of relationship; a node cannot revise its grounding without the grounded_in edge ceasing to hold.

- grounded_in::[[Decisions/Adopt Self-Sovereign Graph Publication]]↗
  - The Decision that names the template-plus-scion architecture this predicate operates inside of. Without the scion Decision, this predicate would have no graph-instance layer to edge across. The predicate is the graph-layer mechanism by which the scion Decision's identity-sovereignty commitment is expressed on a specific scion.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - Each predicate answers one question. `scion_of::` answers "what template was this graph instantiated from?" — an axis distinct from substrate dependence (built_on), normative foundation (grounded_in), and content influence (informed_by).

- grounded_in::[[References/Open Integrity Project (Blockchain Commons, 2025)]]↗
  - The specification that makes the subject-and-object-have-distinct-DIDs claim cryptographically load-bearing rather than merely conceptual. Without Open Integrity, a scion and its template would share git history and therefore share inception commits; the predicate expresses a distinction that Open Integrity is what makes real.

- composes_with::[[Glosses/Scion Address -- the compound DID form identifying a specific node within a specific graph]]↗
  - The compound form the predicate's object takes when referenced at node granularity. A `scion_of::[[did:repo:<sha1>]]↗` edge names the template repo; a Scion Address extends that same DID to `did:repo:<sha1>/<path>` for node-level addressing. The predicate and the Gloss are two scales of the same identifier system.

- composes_with::[[Glosses/External Node -- a node that lives in another graph, referenced without being imported]]↗
  - The predicate's object is always an External Node — a node that lives in another graph and whose DID is necessarily distinct from the subject's. `scion_of::` is the specific predicate that names one kind of relationship to an External Node (content lineage); other edges may name other relationships (citation, contrast, composition) to other External Nodes.
