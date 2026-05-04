---
tagline: MemMachine stores raw conversational episodes and indexes them at sentence level, minimizing LLM dependence for routine memory operations and preserving factual integrity using approximately 80 percent fewer input tokens than Mem0 -- a recent agent-memory-lineage entry pushing further toward substrate-shaped efficiency
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Recent Agent-Memory-Lineage Entry Reducing User-Space Substrate-Rebuild Cost]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# MemMachine Ground-Truth-Preserving Memory (Wang et al., 2026)

URL: <https://arxiv.org/abs/2604.04853>

The paper proposes MemMachine, an agent memory system that stores raw conversational episodes and indexes them at sentence level. The design minimizes LLM dependence for routine memory operations, preserving factual integrity via direct episode retention rather than fact extraction. The empirical claim is approximately 80 percent fewer input tokens than [[Mem0 Production Memory (Chhikara et al., 2025)|Mem0]].

### Adopted

MemMachine is one node in the MemGPT-to-ClawVM agent-memory lineage. The "ground-truth-preserving" framing -- raw episode retention rather than LLM-extracted summaries -- parallels the substrate-LAYER position that the runtime IS the state. eOS Continuum's [[Runtime State Is Persistent by Default, Not by Application Discipline|orthogonal persistence]] primitive provides ground-truth-preservation as a substrate guarantee, eliminating the extract-versus-store tradeoff Mem0 and similar frameworks face.

### Not adopted (yet)

MemMachine still operates as user-space indexing over a substrate that does not carry the in-memory state durably. The 80-percent-fewer-tokens improvement is real but is engineering against a substrate gap; the substrate-LAYER answer would not require the indexing layer at all.

## Sources

- **arXiv**: <https://arxiv.org/abs/2604.04853>
- **Authors**: Wang et al.
- **Date**: 2026-04
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as one node in the agent-memory lineage. Body to be expanded with the sentence-level indexing mechanism and the comparison to substrate-state-graph queryability in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - One node in the agent-memory lineage stub set.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - Ground-truth preservation is a substrate concern; MemMachine reassembles it in user-space because the substrate underneath does not natively carry it.

- composes_with::[[Mem0 Production Memory (Chhikara et al., 2025)]]
  - The 80 percent token reduction vs Mem0 marks continued lineage progression toward substrate-shaped efficiency.
