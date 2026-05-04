---
tagline: MemGPT is the foundational paper framing agent memory as an OS-shaped concern, treating the LLM context window as physical memory and external storage as disk with virtual-memory-style paging -- the source of the OS-as-LLM metaphor that the agent-memory lineage runs on
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Foundational OS-as-LLM Framing]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# MemGPT Towards LLMs as Operating Systems (Packer et al., 2023)

URL: <https://arxiv.org/abs/2310.08560>

The paper proposes MemGPT, a system that frames the LLM context window as physical memory and external storage (vector database, file store) as disk; the system uses virtual-memory-style paging to move information between the two. The framing is the load-bearing contribution: agent memory is an operating-system concern, not an application concern. The title's "Towards LLMs as Operating Systems" names a research direction the agent-memory lineage has run on for two-plus years.

### Adopted

The OS-as-LLM framing is the conceptual ancestor of every agent-memory paper this graph cites in its recent-supporting-evidence section. eOS Continuum's substrate-vs-glue diagnostic ([[Agent Runtimes Require Substrate Primitives, Not External Glue]]) is the deepening of this framing: if memory is an OS concern, atomicity is also an OS concern, capability separation is also an OS concern, and so are coherent multi-agent semantics, hot reload, sandboxed code load, asynchronous events, and state introspection. MemGPT names one primitive (memory) as an OS concern; eOS Continuum names eight.

### Not adopted (yet)

MemGPT operates as user-space orchestration over a substrate that does not natively carry the OS properties. The agent-memory lineage that follows MemGPT (A-MEM, Mem0, MemMachine, Memoria, EverMemOS, ClawVM) progressively moves more of the OS shape into harness-layer enforcement, but the substrate underneath remains Python plus database. eOS Continuum's position is that the OS properties belong as substrate primitives in a runtime that has them, not as harness-layer enforcement on a substrate that does not.

## Sources

- **arXiv**: <https://arxiv.org/abs/2310.08560>
- **Authors**: Packer et al.
- **Date**: 2023-10
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as the foundational framing reference for the agent-memory lineage. Body to be expanded with the specific MemGPT mechanism (the page-management primitives the paper proposes) and the lineage trace from MemGPT through A-MEM, Mem0, MemMachine, Memoria, EverMemOS, to ClawVM in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - Foundational reference for the agent-memory-as-OS-concern lineage.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - The OS-as-LLM framing is the conceptual root of this graph's diagnostic Conviction. MemGPT names memory specifically; eOS Continuum extends the framing to the eight runtime primitives.

- composes_with::[[A-MEM Agentic Memory (Xu et al., 2025)]]
  - The first major successor to MemGPT in the agent-memory lineage; reduces token usage by 85-93 percent vs MemGPT via Zettelkasten-inspired memory organization.

- composes_with::[[ClawVM Harness-Managed Virtual Memory (Rafique and Bindschaedler, 2026)]]
  - The recent enforcement-flavored evolution of MemGPT; explicitly positions itself against MemGPT's "leaves residency and writeback to model discretion" approach.
