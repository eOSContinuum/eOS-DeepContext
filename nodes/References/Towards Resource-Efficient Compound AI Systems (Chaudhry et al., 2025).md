---
tagline: Proposes a declarative workflow programming model and an adaptive runtime system for dynamic scheduling and resource-aware decision-making in compound AI systems -- a runtime-shaped answer to the compound-AI-systems framing that arrives close to the substrate-vs-glue diagnostic without naming the substrate primitives
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Runtime-Shaped Answer to the Compound AI Systems Framing]]
- in_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Towards Resource-Efficient Compound AI Systems (Chaudhry et al., 2025)

URL: <https://arxiv.org/abs/2501.16634>

The paper proposes a vision for resource-efficient compound AI systems through a declarative workflow programming model paired with an adaptive runtime system for dynamic scheduling and resource-aware decision-making. The contribution is the runtime framing: compound AI systems need a runtime that handles scheduling, resource allocation, and decision-making across components -- not just an orchestration layer over external services.

### Adopted

The paper's runtime framing arrives close to this graph's substrate-vs-glue diagnostic. Compound AI systems integrating multiple components (LMs, retrievers, external tools) need a runtime that owns the scheduling and resource decisions; that runtime is in substrate territory, not orchestration territory. The eOS Continuum substrate goes further: the runtime owns not just scheduling and resource decisions but also state, atomicity, capability separation, multi-agent coherence, hot reload, sandboxed code load, asynchronous events, and direct state introspection.

### Not adopted (yet)

The paper's runtime is concerned with scheduling and resource allocation; it does not name the eight runtime primitives this graph's [[Agent Runtimes Require Substrate Primitives, Not External Glue]] Conviction names. The runtime-LAYER framing is right; the specific substrate commitments (orthogonal persistence as foundational, single-coherence-domain by design, capability-OS-tradition lineage) are this project's contribution.

## Sources

- **arXiv**: <https://arxiv.org/abs/2501.16634>
- **Authors**: Chaudhry et al.
- **Date**: 2025-01
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as one node in the compound-AI-systems literature stub set. Body to be expanded with the declarative workflow programming model details and the per-substrate-primitive correspondence in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - One node in the compound-AI-systems literature stub set.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - The paper's runtime-shaped answer is one architectural layer above the substrate-LAYER answer eOS Continuum gives; both name the runtime as the right place for these concerns.

- composes_with::[[Compound AI Systems Optimization Survey (Lee et al., 2025)]]
  - Sibling in the compound-AI-systems literature; the survey covers methods like the one this paper proposes.
