---
tagline: Self-Reflective Language Models extend RLM's recursive scheme with uncertainty-aware program-trajectory selection in the same Python REPL environment, achieving 22 percent accuracy improvement under identical wall-clock budgets without changing the substrate
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[RLM Successor Validating the Prompt-as-Environment Direction]]
- in_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Self-Reflective Language Models (Alizadeh et al., 2026)

URL: <https://arxiv.org/abs/2603.15653>

The paper extends [[Recursive Language Models (Zhang et al., 2025)|RLM]]'s recursive context-interaction scheme with uncertainty-aware program-trajectory selection. SRLM operates in the same sandboxed Python REPL environment RLM defines; what it adds is three intrinsic uncertainty signals (self-consistency across K=8 sampled programs, verbalized confidence via JSON self-assessment, and reasoning-trace length as behavioral uncertainty) that select among candidate context-interaction programs without recursive sub-calls. The empirical claim is a 22 percent accuracy improvement over RLM on BrowseComp+ (37.1 percent to 59.7 percent with Qwen3-Coder) under identical wall-clock budgets, and the surprising finding that "self-reflection can actually outperform recursion in both performance and cost (wall-clock time) under long-context settings."

### Adopted

The paper's confirmation that RLM's substrate shape (Python REPL with prompt-as-variable plus LM-as-tool inside the environment) generalizes across reflective and recursive variants is supporting evidence for the harness-as-tool inversion this graph's [[Agent Harnesses Drive the Runtime, Not the Reverse]] Conviction names. SRLM does not change the substrate; it changes how the LM picks among trajectories the substrate makes available. The substrate-vs-glue diagnostic still applies to SRLM's substrate (Python REPL) just as it did to RLM's.

### Not adopted (yet)

The uncertainty-aware trajectory-selection mechanism itself is downstream of substrate concerns -- it is a harness-side or evaluator-side choice that operates on whatever environment the substrate provides. eOS Continuum's substrate-LAYER position is upstream of this choice; the substrate makes the trajectories available, then SRLM-style selection or another method picks among them.

## Sources

- **arXiv**: <https://arxiv.org/abs/2603.15653>
- **Authors**: Alizadeh et al.
- **Date**: 2026-03
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 alongside the RLM Reference. Body to be expanded with the per-uncertainty-signal correspondence to substrate primitives (self-consistency vs atomic operations; verbalized confidence vs state introspection; reasoning length vs persistent context) in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - Authored as a stub alongside [[Recursive Language Models (Zhang et al., 2025)]].

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - Confirms the substrate shape RLM proves at single-recursion scale generalizes; the Python REPL substrate's gaps (no orthogonal persistence, no capability separation) persist regardless of whether the LM uses recursion or reflection.

- composes_with::[[Recursive Language Models (Zhang et al., 2025)]]
  - SRLM is the RLM successor; both rest on the same Python REPL substrate with state in named variables and LM-as-tool inside.
