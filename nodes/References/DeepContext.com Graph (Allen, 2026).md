---
tagline: The seed Deep Context graph; donor of the meta-layer (Form Contracts, Predicates, generic graph-operation Skills) grafted into eOS-DeepContext at instantiation
created: 2026-05-03
url: https://deepcontext.com/
this_did: did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae
graft_revision: e8ae680
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Donor of the Deep Context Meta-Layer]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# DeepContext.com Graph (Allen, 2026)

URL: <https://deepcontext.com/>

DID: `did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae` (the SHA1 of DeepContext.com's Open Integrity inception commit, derived per [[References/Open Integrity Project (Blockchain Commons, 2025)]]↗).

DeepContext.com is the seed Deep Context graph -- a typed knowledge graph that captures reasoning as plain-markdown nodes connected by named-edge predicates. It is the donor from which eOS-DeepContext grafted the meta-layer at instantiation and on subsequent refreshes: the Form Contracts that specify node shapes (including the Touch Point Form Contract added in DeepContext.com's 2026-05-03 push), the typed-edge Predicates that compose into graph structure (`assists_by`, `built_on`, `composes_with`, `conforms_to`, `contends_with`, `contrasts_with`, `extends_contract`, `frames_lens_on`, `grafted_from`, `grounded_in`, `has_component`, `in_practice_domain`, `informed_by`, `informs_downstream`, `responds_to`, `scion_of`, `source_voice`), and the generic graph-operation Skills (Graph Audit, Graph Inception, Graph Load Audit, Graph Orient, Node Create, Node Read, Node Validate, Predicate Propose) that make the graph agent-operable. The Graft Gloss is grafted alongside its `grafted_from::` Predicate, completing the per-node graft-provenance vocabulary.

eOS-DeepContext is **not** a scion of DeepContext.com. eOS-DeepContext has its own Open Integrity inception (`did:repo:9dc47a293f5b2352dba288b3e2ef9c73c508ca0f`), its own purpose (carrying the eOS Continuum project's architectural argument for an image-persistent runtime substrate for agentic AI), and its own evolution. The relationship to DeepContext.com is per-node graft, not graph-level lineage; the corrected framing in DeepContext.com's [[Decisions/Adopt Self-Sovereign Graph Publication]]↗ Decision distinguishes the two.

### Adopted

The full meta-layer was grafted: every Form Contract under `nodes/Contracts/`, every Predicate under `nodes/Predicates/`, every generic Skill under `nodes/Skills/`, and (as of 2026-05-03) the Graft Gloss and `grafted_from::` Predicate. The graft adopts DeepContext.com's structural conventions for knowledge-graph authoring: the H1-with-identity-block-above-it node shape, the `predicate::[[Target]]` typed-edge syntax, the per-form Requirements-and-Relations bodies, the Crescent-against-adjacent-Predicate discipline, the curate-not-overwrite agent stance. These conventions travel with the nodes; eOS-DeepContext applies them to its own architectural content.

### Not adopted (yet)

DeepContext.com's content nodes -- its Decisions, Convictions, Aspirations, Observations, Patterns, References -- are not grafted because they carry the Deep Context Community's own reasoning about collaborative knowledge work, not eOS-DeepContext's reasoning about runtime substrates for agentic AI. eOS-DeepContext authors its own content under those forms. The `Scion Bootstrap` Skill (since renamed to `Graph Inception` in DeepContext.com) was not grafted because eOS-DeepContext does not act as a graph-publication entry point for further graphs; the script-level operational primitives (`graph-inception.sh`, `oi-inception.sh`) are present in `.scripts/` but the agent-invocable Skill wrapper is not.

The donor's `landing.md`, `README.md`, `AGENTS.md`, `CLAUDE.md`, build pipeline (`.scripts/`), CI workflow (`.github/workflows/`), and Open-Integrity identity infrastructure (`.deep-context-identity.yml`) were grafted at instantiation as the operational substrate; they have since diverged locally to carry eOS-DeepContext's purpose and identity. Those pieces are tracked as ordinary local files rather than per-node grafts because their evolution is fully eOS-DeepContext's now.

## Sources

- **URL**: <https://deepcontext.com/>
- **Repository**: <https://github.com/ChristopherA/DeepContext.com>
- **DID**: `did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae`
- **Graft revision**: `e8ae680` (donor commit at the time this Reference was authored; eOS-DeepContext's grafted nodes may correspond to earlier donor revisions for individual files, given the meta-layer was first grafted at eOS-DeepContext's instantiation circa 2026-04-26 and per-node sync to the donor's later revisions has not been done)
- **Authors**: Christopher Allen and the Deep Context Community
- **Date**: 2026 (graph instantiation; ongoing)
- **Stub note**: Authored 2026-05-03 to proxy the donor for `grafted_from::` edges across the grafted meta-layer. Per-node forensic detail (which file at which donor revision was grafted into which recipient file at what date) lives in eOS-DeepContext's git history rather than in this Reference's body.

## Relations

- conforms_to::[[Reference Form Contract]]
  - The first Reference node that proxies a donor graph rather than an external paper or website. Its existence makes per-node `grafted_from::` edges resolvable as local wikilinks across the grafted meta-layer.

- informs_downstream::[[grafted_from -- per-node content provenance from a donor graph]]
  - The Predicate whose `grafted_from::[[DeepContext.com Graph (Allen, 2026)]]` edges across the grafted meta-layer point at this Reference. The Reference is the canonical donor proxy; the Predicate is the per-node provenance edge; together they make the graft visible at graph-traversal time without claiming graph-level lineage.

- contrasts_with::[[scion_of -- content lineage from a template graph]]
  - This Reference proxies a graph that eOS-DeepContext **grafted from** but is **not a scion of**. The distinction between graph-level lineage (scion-of) and per-node copy (graft) is the architectural commitment behind why this Reference exists rather than a `scion_of::` edge in `.deep-context-identity.yml`.
