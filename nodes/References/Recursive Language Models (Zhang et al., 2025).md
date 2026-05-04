---
tagline: Recursive Language Models treat the prompt as an external Python REPL environment the LM examines, decomposes, and recursively calls itself over -- a microcosm of the harness-as-tool inversion at single-recursion scale, with limitations the paper names that orthogonal persistence and capability separation as substrate primitives directly address
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Microcosm of the Harness-as-Tool Inversion at Single-Recursion Scale]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# Recursive Language Models (Zhang et al., 2025)

URL: <https://arxiv.org/abs/2512.24601>

The paper proposes Recursive Language Models (RLMs): the LM is given a Python REPL programming environment in which the input prompt is bound to a string variable, and the LM writes Python code that programmatically transforms the prompt and calls `llm_query()` to invoke sub-LMs on derived snippets. Intermediate results accumulate in named REPL variables; only constant-size metadata about each step's stdout feeds back into the root LM's history. The architectural claim, quoted: "Given a prompt P, the RLM initializes a Read-Eval-Print Loop (REPL) programming environment in which P is set as the value of a variable... code running inside the environment must be able to invoke the model on programmatically constructed transformations of P, storing intermediate results symbolically." The empirical claim is processing inputs "two orders of magnitude beyond model context windows" with comparable cost to vanilla LLMs.

### Adopted

The architectural shape RLM proves at single-recursion scale -- code-execution environment with state in named variables, LM-as-tool inside the environment, token-space discipline (data lives in variable space; only metadata feeds back to the LM) -- is a microcosm of the harness-as-tool inversion this graph names in [[Agent Harnesses Drive the Runtime, Not the Reverse]]. The paper's named limitations (sub-calls are blocking; recursion depth bounded; REPL state evaporates on process death) are exactly what the eight runtime primitives the eOS Continuum substrate provides as primitives address: asynchronous events for blocking sub-calls, orthogonal persistence for recursion that survives restarts, capability separation for code that does not escape the bounded namespace.

### Not adopted (yet)

The paper does not endorse orthogonal persistence as foundational, single-coherence-domain by design, or capability-OS-tradition lineage. RLM works on Python -- the wrong substrate for what the paper's own limitations section asks. eOS Continuum's substrate-LAYER answer extends the architectural shape RLM proves at user-space scale; the deeper architectural commitments are this project's, not endorsed by the cited authors.

## Sources

- **arXiv**: <https://arxiv.org/abs/2512.24601>
- **Authors**: Alex L. Zhang, Tim Kraska, Omar Khattab
- **Date**: 2025-12
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 to capture the relevance discovered during the eOS Continuum project's research synthesis. Body to be expanded in a future session with the per-axis correspondence table (RLM-on-Python vs eOS-substrate primitive coverage), the load-bearing quotes from the paper's mechanism section, and the relationship to [[Self-Reflective Language Models (Alizadeh et al., 2026)]] as the RLM successor.

## Relations

- conforms_to::[[Reference Form Contract]]
  - First Reference-form node in the eOS-DeepContext graph capturing supporting evidence for the substrate-vs-glue diagnostic from the prompt-as-environment direction.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - The paper's mechanism (LM uses REPL as environment; calls LM-as-tool inside; state in variables) is structurally identical to the harness-as-tool inversion this graph's load-bearing diagnostic Conviction names. The paper's limitations are an inventory of the substrate properties the diagnostic argues belong in the runtime.

- informs_downstream::[[Agent Harnesses Drive the Runtime, Not the Reverse]]
  - RLM at single-recursion scale is the same architectural inversion the harness-as-tool Conviction names at agent-platform scale: substrate-shaped state plus LM-as-tool consumption plus code-as-LM-output plus metadata-only token feedback.

- composes_with::[[Self-Reflective Language Models (Alizadeh et al., 2026)]]
  - SRLM is the RLM successor that extends RLM's recursive scheme with uncertainty-aware trajectory selection in the same Python REPL environment; both stand together as evidence that the prompt-as-environment direction has academic-systems weight.

- composes_with::[[DSPy Compiling Declarative Language Model Calls (Khattab et al., 2023)]]
  - Khattab co-authors RLM and created DSPy. The Khattab axis (DSPy as user-space framework; RLM as inference pattern) is one coherent research program whose architectural conclusions arrive at the substrate eOS Continuum names from the opposite direction.

- composes_with::[[Meriadoc (ChatTheatre, 2026)]]
  - RLM proves the harness-as-tool inversion at single-recursion scale on Python and names its own limitations -- sub-calls blocking, recursion depth bounded, REPL state evaporates on process death. Meriadoc realizes the same inversion at substrate scale: handlers, tools, and intermediate sub-call results live in the orthogonally persistent state graph, lifting the limitations RLM names. The two References compose -- RLM names the technique; Meriadoc is the substrate-layer realization.
