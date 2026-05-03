---
tagline: A blog post arguing that procedural knowledge differs fundamentally from raw information availability for agents, framing GEPA optimization plus RLM long context plus procedural workflow as the three building blocks DSPy needs -- the user-space pain inventory that names exactly what eOS Continuum's substrate primitives provide
created: 2026-05-03
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[User-Space Pain Inventory Naming the Substrate Properties eOS Continuum Provides]]
- in_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Why I Built DSPy Agent Skills (codeandcontext.ai, 2025)

URL: <https://codeandcontext.ai/why-i-built-dspy-agent-skills/>

A blog post by the author of the dspy-agent-skills project arguing that DSPy research, tooling, and documentation exist separately, but there is no curated, spec-compliant way to hand an agent the relevant knowledge once. The post identifies that procedural knowledge differs fundamentally from raw information availability -- coding agents like Claude Code repeatedly fail to generate idiomatic DSPy code despite access to all the materials. Three building blocks named: (1) GEPA optimization where metrics explain why failures occur (not just return scalars); (2) RLM for long context, separating variable space (REPL memory) and token space (what the LM sees); (3) procedural workflow with a seven-step loop (spec then program then metric then baseline then GEPA then export then deploy).

### Adopted

The post's "variable space vs token space" distinction is the [[Agent Harnesses Drive the Runtime, Not the Reverse|harness-as-tool inversion]] this graph names, restated in DSPy's vocabulary. The substrate holds state; the LM consumes a projection of it. The post also references "observational memory keeping agents from unauthorized state mutations" and "handoffs across agent instances" as related Agent Skills concerns -- both of which are exactly what [[Capability Boundaries Are Runtime-Enforced, Not Policy-Checked]] and [[Runtime State Is Persistent by Default, Not by Application Discipline]] provide as substrate primitives.

### Not adopted (yet)

DSPy Agent Skills is a user-space framework on Python. The post acknowledges the gap (procedural knowledge is hard to embed; coding agents fail at idiomatic DSPy code) but solves it with embedded-knowledge skills rather than substrate primitives. eOS Continuum's substrate-LAYER position addresses the substrate gap that drives the user-space rebuild.

## Sources

- **URL**: <https://codeandcontext.ai/why-i-built-dspy-agent-skills/>
- **Date**: 2025
- **Venue**: codeandcontext.ai blog
- **Stub note**: Authored 2026-05-03 as the public companion to the [[DSPy Compiling Declarative Language Model Calls (Khattab et al., 2023)|DSPy paper]]. Body to be expanded with per-building-block correspondence to substrate primitives (GEPA optimization to atomic operations plus state introspection; RLM long context to persistent state; procedural workflow to atomic operations across steps) in a future session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - Industry blog post serving as the public-facing companion to the DSPy paper; passes URL-resolvability.

- informs_downstream::[[Agent Runtimes Require Substrate Primitives, Not External Glue]]
  - The post identifies user-space pain points (variable-vs-token-space, observational memory, handoffs across instances) that are exactly the substrate properties this graph's diagnostic Conviction names.

- composes_with::[[DSPy Compiling Declarative Language Model Calls (Khattab et al., 2023)]]
  - The post is the public companion to the DSPy paper; both rest on the same Khattab-axis research program.

- composes_with::[[Recursive Language Models (Zhang et al., 2025)]]
  - The post explicitly integrates RLM as one of the three DSPy building blocks; the Khattab axis runs through both papers and this post.
