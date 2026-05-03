---
tagline: A-MEM proposes agentic memory for LLM agents organized as a Zettelkasten-inspired interconnected knowledge network with dynamic indexing and linking, achieving 85-93 percent token reduction vs MemGPT -- the first major successor in the agent-memory lineage downstream of the OS-as-LLM framing
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Successor in the Agent-Memory Lineage After MemGPT]]
- in_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# A-MEM Agentic Memory (Xu et al., 2025)

URL: <https://arxiv.org/abs/2502.12110>

The paper proposes A-MEM (Agentic Memory), a memory system for LLM agents that dynamically organizes memories using the Zettelkasten method -- creating interconnected knowledge networks through dynamic indexing and linking. The empirical claim is an 85-93 percent reduction in token usage compared to [[MemGPT Towards LLMs as Operating Systems (Packer et al., 2023)|MemGPT]], indicating the lineage's progression toward more substrate-shaped memory organization while still operating in user-space.

### Adopted

A-MEM is one node in the agent-memory lineage that this graph cites as evidence for the substrate-vs-glue diagnostic. The improvement over MemGPT signals that user-space memory frameworks are progressively moving toward substrate-shaped abstractions (interconnected typed-edge networks, dynamic linking) -- which is exactly what the eOS Continuum substrate provides as primitives via [[Runtime State Is Persistent by Default, Not by Application Discipline|orthogonal persistence]] and [[Runtime State Is Queryable Directly, Not Through a Synthesized API|state introspection]].

### Not adopted (yet)

A-MEM operates as user-space orchestration over a vector-database substrate. The Zettelkasten-inspired link structure is conceptually similar to the typed-edge graph this DeepContext convention uses, but it lives as application-layer indexing rather than as a runtime primitive. eOS Continuum's substrate-LAYER position is that this kind of structure should be a substrate property, not a memory framework's contribution.

## Sources

- **arXiv**: <https://arxiv.org/abs/2502.12110>
- **Authors**: Xu et al.
- **Date**: 2025-02
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as one node in the MemGPT-to-ClawVM agent-memory lineage. Body to be expanded with the Zettelkasten mechanism details and the per-feature comparison to substrate primitives in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - One node in the agent-memory lineage stub set.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - User-space memory frameworks progressively rebuild substrate properties; A-MEM's Zettelkasten-inspired linking is one such rebuild.

- composes_with::[[MemGPT Towards LLMs as Operating Systems (Packer et al., 2023)]]
  - The first major successor to MemGPT in the agent-memory lineage; the 85-93 percent token reduction marks the trajectory toward more substrate-shaped memory abstractions.
