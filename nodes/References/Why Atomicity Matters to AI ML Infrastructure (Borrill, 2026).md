---
tagline: A paper arguing atomicity must be explicitly constructed as protocol convergence in AI/ML training infrastructure rather than assumed as a temporal property -- shared philosophical posture with the substrate-vs-glue diagnostic, applied to a different domain (training-time checkpointing across thousands of GPUs); tangentially relevant
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Tangential Philosophical Companion on Atomicity in AI Infrastructure]]
- in_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Why Atomicity Matters to AI ML Infrastructure (Borrill, 2026)

URL: <https://arxiv.org/abs/2603.02603>

The paper argues atomicity in AI/ML training infrastructure is impossible under asynchronous distributed execution with failures. It claims large-scale AI training systems rest on two false assumptions: (1) "a checkpoint represents a single coherent global state -- there exists a time t at which everything was saved"; (2) "firmware and infrastructure updates can be applied to the cluster without any reachable execution in which different nodes operate under different protocol semantics." Both assumptions, the paper argues, are structurally unsound. The "Forward-In-Time-Only Category Mistake" the title names is the confusion between temporal predicates ("at clock time t, all components reflect epoch e") and protocol properties ("the distributed protocol has converged to epoch e"). The paper's argument: "atomicity must be explicitly constructed as protocol convergence -- through bilateral commit, consensus-mediated transitions, and validation checkpoints -- rather than assumed as a temporal property."

### Adopted

The paper shares a philosophical posture with this graph: atomicity belongs in the runtime substrate as a protocol mechanism, not in application code as best-effort. The "different logical types" framing (temporal predicates vs protocol properties) is the same insight the substrate-vs-glue diagnostic ([[Agent Runtimes Require Substrate Primitives, Not External Glue]]) names: the gap between "infrastructure magically ensures atomicity at time t" and "the substrate implements a distributed coordination protocol" is exactly the gap between user-space rebuild and substrate primitive.

### Not adopted (yet)

The paper concerns training-time checkpointing across thousands of GPUs in distributed AI/ML training systems. eOS Continuum's substrate is single-coherence-domain by design ([[Adopt Single-Coherence-Domain Architecture]]); the distributed-atomicity question the paper engages does not apply to a single-machine substrate. The relevance is at the philosophical-posture level (substrate-as-protocol-mechanism) rather than at the implementation level. Tangentially relevant; included for completeness in the supporting-evidence inventory.

## Sources

- **arXiv**: <https://arxiv.org/abs/2603.02603>
- **Authors**: Borrill (single author)
- **Date**: 2026-03
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as the tangentially-relevant philosophical companion. Body to be expanded with the per-claim correspondence to substrate-vs-glue framing and the deliberate scope-bounding (training-time vs agent-runtime) in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - Tangentially relevant; included for completeness because the philosophical posture aligns with the substrate-vs-glue diagnostic across domains.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - Same architectural insight (substrate-as-protocol-mechanism vs application-as-best-effort) applied to a different domain (distributed AI/ML training infrastructure rather than agent runtimes).

- contrasts_with::[[Adopt Single-Coherence-Domain Architecture]]
  - The paper's distributed-atomicity question is upstream of and orthogonal to the single-coherence-domain commitment; eOS Continuum's substrate avoids the distributed-atomicity question by design.
