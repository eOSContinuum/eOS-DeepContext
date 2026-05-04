---
tagline: ClawVM proposes harness-layer enforcement of atomicity, persistence, and capability boundaries for stateful tool-using LLM agents, arriving independently at the substrate-properties-belong-in-the-runtime diagnostic this graph names -- the closest external cousin to eOS Continuum's thesis, at one architectural layer above
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Closest External Cousin to the Substrate-vs-Glue Diagnostic]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# ClawVM Harness-Managed Virtual Memory (Rafique and Bindschaedler, 2026)

URL: <https://arxiv.org/abs/2604.10352>

The paper proposes ClawVM, a runtime layer interposed within the agent harness that enforces three semantic properties at lifecycle boundaries: atomicity (three-phase staged-updates plus validation plus scoped-commit transaction preventing destructive overwrites), persistence guarantees (minimum-fidelity invariants ensure critical state survives destruction), and capability boundaries (pages carry scope metadata; the writeback protocol checks requested scope is allowed for the active principal). The load-bearing architectural claim, quoted: "when a runtime manages a fast, scarce tier alongside slow, durable storage, the answer is virtual memory, not best-effort heuristics." And: "Operating systems solved this decades ago... State management is reframed as an OS-level concern, not agent policy."

### Adopted

ClawVM is the closest external evidence for this graph's [[Agent Runtimes Require Substrate Primitives, Not External Glue]] diagnostic, arrived at independently from the LLM-agents direction rather than the DGD-lineage direction. The empirical claims (ClawVM eliminates "all policy-controllable faults" producing up to 67.8 mean faults to zero across budgets; 100 percent task success vs 76.7 percent for practitioner-configured baselines at tight budget; less than 50 microseconds median policy-engine overhead per turn) validate the substrate-properties-belong-in-the-substrate position empirically. The paper's positioning vs MemGPT, A-MEM, and Mem0 is also adopted: MemGPT "leaves residency and writeback to model discretion; ClawVM moves both to the harness with replayable enforcement."

### Not adopted (yet)

ClawVM is harness-LAYER. It enforces substrate properties on top of a Python plus storage substrate that does not natively carry them; it is a thin enforcement layer rather than a runtime where the properties are primitives. eOS Continuum's substrate-LAYER position takes the same diagnosis to its conclusion -- instead of building an OS-shaped enforcement layer on Python, the runtime IS the substrate, with [[Runtime State Is Persistent by Default, Not by Application Discipline|orthogonal persistence]] as a foundational primitive and the other seven primitives derived from it. The capability-OS lineage (KeyKOS, EROS, CapROS, Coyotos) and the DGD-on-iChat production-soak credential remain this project's specific architectural ground.

## Sources

- **arXiv**: <https://arxiv.org/abs/2604.10352>
- **Authors**: Rafique and Bindschaedler
- **Date**: 2026-04
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 to capture the strongest external evidence found during the eOS Continuum project's research synthesis. Body to be expanded with the per-property comparison table (ClawVM at harness-layer vs eOS Continuum substrate at runtime-layer), the empirical-claim breakdown, and the explicit positioning quote on MemGPT predecessors in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - The strongest external evidence for the substrate-vs-glue diagnostic among the recent literature. Worth its own deep treatment in a follow-up authoring pass.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - Independent statement of the same diagnostic from the LLM-agents direction. The paper's "operating systems solved this decades ago" framing is the same architectural insight the eos-harness graph's diagnostic Conviction names; ClawVM stops at the harness-layer enforcement; eOS Continuum extends to the substrate-layer primitive.

- contrasts_with::[[MemGPT Towards LLMs as Operating Systems (Packer et al., 2023)]]
  - The ClawVM paper explicitly positions itself against MemGPT's "leaves residency and writeback to model discretion" approach, moving both concerns to the harness with replayable enforcement. MemGPT is the foundational framing; ClawVM is the recent enforcement-flavored evolution.
