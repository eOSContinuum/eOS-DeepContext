---
tagline: A survey of optimization methods, challenges, and future directions for compound AI systems -- the higher-level abstraction over orchestration-of-multiple-LLMs-and-tools that the harness-as-driver pattern realizes; the literature where compound systems are studied as graphs of operations
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Survey-Level Reference for the Compound AI Systems Framing]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# Compound AI Systems Optimization Survey (Lee et al., 2025)

URL: <https://arxiv.org/abs/2506.08234>

The paper surveys the recent compound-AI-systems literature -- the design and optimization of complex AI workflows where compound systems perform sophisticated tasks through integration of multiple components (multiple LMs, retrievers, tool calls, orchestration logic). The survey covers optimization methods, identifies open challenges, and points at future directions for the compound-AI-systems research community.

### Adopted

The compound-AI-systems framing (popularized by Berkeley's "Shift from Models to Compound AI Systems" essay, Zaharia et al., 2024) is the higher-level abstraction over the harness-as-driver pattern this graph's [[Agent Harnesses Drive the Runtime, Not the Reverse]] Conviction names. Compound AI systems orchestrate multiple LMs and tools as a graph of operations; the survey's enumeration of optimization concerns (cost, latency, accuracy, model selection) is the kind of orchestration concern the harness owns. eOS Continuum's substrate is what makes those graphs of operations tractable: atomic operations across the graph, capability separation between components, persistent state shared across invocations.

### Not adopted (yet)

The survey assumes a substrate; few of the compound-AI-systems papers it covers name what makes the substrate well-formed. eOS Continuum's substrate-LAYER position is upstream of the survey's optimization concerns -- the optimization questions become tractable once the substrate carries atomicity, persistence, and capability separation as primitives. Adopting the compound-AI-systems vocabulary verbatim would obscure the substrate-LAYER distinction.

## Sources

- **arXiv**: <https://arxiv.org/abs/2506.08234>
- **Authors**: Lee et al.
- **Date**: 2025-06
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as the survey-level reference for the compound-AI-systems literature. Body to be expanded with the per-optimization-concern correspondence to substrate primitives in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - Survey-level reference covering the compound-AI-systems literature.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - The survey's optimization concerns (cost, latency, accuracy, model selection across compound graphs) presuppose a substrate; eOS Continuum's substrate-vs-glue diagnostic names what makes the substrate well-formed.

- composes_with::[[Towards Resource-Efficient Compound AI Systems (Chaudhry et al., 2025)]]
  - The same compound-AI-systems literature; Resource-Efficient CAIS proposes a declarative workflow programming model and adaptive runtime system.
