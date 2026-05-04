---
tagline: Memoria is a modular memory framework that augments LLM-based conversational systems with persistent, interpretable, and context-rich memory, integrating dynamic session-level summarization and a weighted knowledge graph-based user-modelling engine -- another lineage entry showing the user-space substrate rebuild trajectory
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Modular User-Space Memory Framework Demonstrating the Substrate-Rebuild Pattern]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# Memoria Modular Memory Framework (Sarin et al., 2025)

URL: <https://arxiv.org/abs/2512.12686>

The paper proposes Memoria, a modular memory framework augmenting LLM-based conversational systems with persistent, interpretable, and context-rich memory. The framework integrates dynamic session-level summarization with a weighted knowledge-graph-based user-modelling engine. The contribution is in the modular composition: separable summarization, user-modelling, retrieval, and update components.

### Adopted

Memoria is one node in the MemGPT-to-ClawVM agent-memory lineage; cited in this graph's recent-supporting-evidence section as evidence of the user-space substrate-rebuild trajectory's continued evolution. The weighted knowledge-graph user-modelling engine is structurally similar to the typed-edge graph this DeepContext convention uses; both reassemble substrate-shaped relational structure on top of substrates that do not natively carry it.

### Not adopted (yet)

Memoria's modularity is a strength against the inadequate-substrate position: by separating concerns, the framework can be tuned per use case. The substrate-LAYER position is that this modularity is unnecessary if the substrate carries the relational structure as a primitive; the components Memoria modularizes are unified in the substrate's persistent state graph.

## Sources

- **arXiv**: <https://arxiv.org/abs/2512.12686>
- **Authors**: Sarin et al.
- **Date**: 2025-12
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as one node in the agent-memory lineage. Body to be expanded with the per-component analysis and the substrate-property mapping in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - One node in the agent-memory lineage stub set.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - The user-space modular rebuild of substrate-shaped abstractions; the weighted-knowledge-graph component is what state introspection plus persistence delivers as primitives.

- composes_with::[[MemGPT Towards LLMs as Operating Systems (Packer et al., 2023)]]
  - One node in the lineage downstream of MemGPT.
