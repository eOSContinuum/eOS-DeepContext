---
tagline: DSPy is the foundational paper for treating LM pipelines as text-transformation graphs -- imperative computational graphs where LMs are invoked through declarative modules with a compiler that optimizes any DSPy pipeline to maximize specified metrics; the framework that makes the variable-vs-token-space distinction load-bearing
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Foundational Framework Naming the Variable-vs-Token-Space Distinction]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# DSPy Compiling Declarative Language Model Calls (Khattab et al., 2023)

URL: <https://arxiv.org/abs/2310.03714>

The paper proposes DSPy, a programming model that replaces hand-coded prompt templates with systematic optimizable language-model pipelines. The framework treats LM pipelines as "text transformation graphs, i.e., imperative computational graphs where LMs are invoked through declarative modules." Modules are parameterized; a compiler optimizes any DSPy pipeline to maximize specified metrics. The empirical claim is over 25 percent and 65 percent improvement over standard few-shot prompting across multiple benchmarks.

### Adopted

DSPy is the foundational framework that the [[Recursive Language Models (Zhang et al., 2025)|RLM]] research direction extends. The "writing programs that compile down to prompts" framing is conceptually downstream of the substrate-vs-glue diagnostic this graph names: programs need a substrate to compile into; pipelines need a runtime to run on. Khattab's own subsequent work (RLM, Agent Skills) elaborates on the framework's substrate dependencies, naming the variable-vs-token-space distinction this graph's harness-as-tool inversion ([[Agent Harnesses Drive the Runtime, Not the Reverse]]) makes load-bearing. eOS Continuum is the substrate-LAYER answer to the substrate question DSPy raises and works around in user-space.

### Not adopted (yet)

DSPy operates as a Python-runtime compilation framework; the substrate underneath is whatever Python provides, which is the wrong substrate for the workload (no orthogonal persistence, no capability separation, no atomic operations as primitives). The compilation framework itself is downstream of substrate concerns; eOS Continuum does not adopt DSPy's compilation model -- it adopts the framework's diagnosis that LM-pipelines-as-programs need a substrate, and provides the substrate.

## Sources

- **arXiv**: <https://arxiv.org/abs/2310.03714>
- **Authors**: Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, plus nine additional collaborators
- **Date**: 2023-10
- **Venue**: arXiv preprint
- **Stub note**: Authored 2026-05-03 as the foundational framework reference for the Khattab axis. Body to be expanded with the per-component analysis (Signatures, Modules, Optimizers, the seven-step loop) and the substrate-property correspondence to eOS Continuum's primitives in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - The foundational framework reference for the Khattab axis (DSPy as user-space framework; RLM as inference pattern).

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - DSPy's seven-step pipeline (spec then program then metric then baseline then GEPA then export then deploy) needs atomic operations across steps, capability separation between modules, and persistent state across optimizer runs. eOS Continuum's substrate provides these as primitives.

- composes_with::[[Recursive Language Models (Zhang et al., 2025)]]
  - Khattab co-authors RLM and created DSPy. The Khattab axis is one coherent research program whose architectural conclusions arrive at the substrate eOS Continuum names from the opposite direction.

- composes_with::[[Why I Built DSPy Agent Skills (codeandcontext.ai, 2025)]]
  - The post that integrates GEPA optimization, RLM for long context, and procedural workflow as the three pillars of agent-skills authoring.

- composes_with::[[Model-Harness-Fit (Bustamante, 2026)]]
  - The Khattab axis (DSPy as user-space framework, RLM as inference pattern) is one coherent program inside the matched-pair regime the Bustamante thread anatomizes. The thread's diagnosis of post-training co-evolution applies directly: DSPy compiles down to prompt shapes that the matched model's instincts have been trained against. eOS Continuum extends the architectural shape DSPy/RLM proves at user-space scale into the substrate layer, where the matched-pair coupling stops being load-bearing for the customer's durable infrastructure.
