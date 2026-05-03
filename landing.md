# eOS Continuum

*A persistent substrate for agentic AI.*

A common reference for the small team and early collaborators on what we are working toward and why, in plain language. The substantive claims live in the linked nodes; this page is the orientation. What this site is not: a marketing document, a fundraising pitch, a specification, a product requirements document. What it is: the team's shared reference, said plainly, to a sophisticated reader who arrived without context.

## What we are addressing

Agent platforms today are orchestration layers wrapped around stateless LLM calls. Everything an agent doing real work actually needs -- accumulated memory, durable identity, atomicity across multi-step plans, capability boundaries, coordination with other agents -- is engineered as a separate vendor on a separate substrate that was never designed for the agent use case. A vector database approximates memory. JSON files approximate tool definitions. Queues approximate workflow durability. IAM middleware approximates capability bounds. Bespoke retry logic approximates atomicity. Each approximation is a separate failure mode, a separate cost line, a separate piece of state to keep in sync.

The mismatch is between [[The Agent's Logical Model]] -- *I remember what I did, I have tools, I can coordinate with peers, I survive a restart* -- and the substrate's actual model: *I am a stateless function call against external services with no persistent identity*. Most contemporary bugs in agent infrastructure are artifacts of this impedance mismatch: serialization boundaries between reasoning and stored memory, partial-failure ambiguity in multi-step plans, retry-versus-replay confusion when tool calls error mid-execution, vector-database-versus-ground-truth divergence, schema drift between what the LLM thinks it knows and what storage holds.

The diagnostic this graph rests on: [[Agent Runtimes Require Substrate Primitives, Not External Glue]]. The integration complexity is structural, not accidental -- the foundations under today's platforms (relational databases, queues, distributed locks, identity middleware, deploy pipelines) were built for stateless web workloads, not for agent-style multi-author concurrent state. The bugs live in the glue.

Eliminating the impedance mismatch changes the failure model in a way that is hard to replicate incrementally on a substrate that does not already carry the property. The bug classes above do not get patched -- they cease to be possible.

## The architecture

There is a class of runtime where the application's entire state -- code, objects, in-flight operations, accumulated context -- lives in a single persistent image. State does not live in a database that the runtime synchronizes with; the runtime *is* the state. Snapshot the runtime, restore it tomorrow, work continues from where it left off. No marshaling, no separate database, no synchronization layer.

The property has a name: [[Orthogonal Persistence as Foundational Primitive|orthogonal persistence]]. It is the architectural floor. The other seven primitives this graph names derive their value from it -- atomic operations matter because they atomically affect *persistent* state; capability bounds matter because the bounded namespace *persists*; hot reload matters because the *running state survives* the reload; sandboxed code load matters because the loaded code and any objects it creates are persistent artifacts, not ephemeral process state. Without orthogonal persistence, the others are local-process concerns with no continuity across the agent's lifetime; with it, they are substrate-scope guarantees that survive restart indefinitely.

The eight primitives:

1. [[Runtime State Is Persistent by Default, Not by Application Discipline|Orthogonal persistence]] *(foundational)* -- every object, variable, and reference persists automatically across process restarts as a single durable image. The runtime owns the heap. Application code does not save or load.

2. [[Agent Operations Commit Wholly or Roll Back Wholly|Atomic operations]] -- every operation runs as a transaction over the in-memory state. If anything in the operation fails, the entire in-memory state reverts -- not just database rows, but every object that was created, mutated, or referenced during the failed attempt.

3. [[Capability Boundaries Are Runtime-Enforced, Not Policy-Checked|Capability separation]] -- each piece of code runs as a privileged identity with explicit capabilities defining what it can read, modify, or invoke. Out-of-capability operations do not return error codes; they fail at runtime and the operation's atomic boundary rolls back the partial work.

4. [[Multiple Agents See Coherent State Without User-Land Coordination|Coherent multi-agent semantics]] -- concurrent operations see the same state at the same logical time. The runtime serializes conflicting writes deterministically. There is no eventual consistency, no leader election, no distributed-lock dance.

5. [[Hot Reload Is a Runtime Operation, Not a Deployment Event|Hot logic update]] -- source code can be modified, recompiled, and merged into the live runtime while operations are in flight. In-progress operations finish with the old logic; subsequent operations use the new. No restart, no state loss, no warmup.

6. [[Code Load Compiles Into the Live Runtime, Bounded by Capability Tiers|Sandboxed code load]] -- new code can be authored at runtime, compiled by the runtime, and merged into the same persistent image as everything else. The capability layer enforces what newly-loaded code is allowed to do; the persistence layer ensures it stays loaded across restarts.

7. [[Event Notification Is Atomic With State Change, Not Polled or Queued|Asynchronous events]] -- when state changes that other code cares about, the runtime synchronously notifies registered listeners within the same atomic operation that caused the change. Subscribers do not poll, do not race, do not miss events because of delivery-versus-write ordering.

8. [[Runtime State Is Queryable Directly, Not Through a Synthesized API|State introspection]] -- the runtime's live state graph is directly queryable -- by application code, by humans, by other LLMs. The data model is the API.

The leverage is in the combination -- eight primitives, in one runtime, with the same operational semantics across all eight. Pieces of each primitive exist in scattered places across modern infrastructure: some in functional databases, some in actor frameworks, some in capability languages, some in transactional memory research. The combination, in one runtime, is rare. One member of the class has run production services for nearly three decades.

## The architectural inversion

Conventional pattern: an agent harness orchestrates LLM calls, treats LLMs as tools (alongside file read, web search, code execution), and rebuilds state, atomicity, identity, and event coordination from external infrastructure -- a database for state, a queue for atomicity, IAM middleware for identity, distributed locks for coordination, webhooks for notifications, deploy-time tooling for logic updates.

Inverted pattern: [[Agent Harnesses Drive the Runtime, Not the Reverse|the harness uses the runtime as a tool]], the same way it uses LLMs. The harness sends operations to the runtime; the runtime returns state and events. State, mutation safety, multi-agent coordination, identity boundaries, and event notification all arrive as the runtime's natural output.

| Property | LLM-as-tool | Runtime-as-tool |
|---|---|---|
| State across calls | None | Persistent shared graph |
| Mutation safety | None | Atomic call-tree rollback |
| Multi-agent coordination | External | Coherent runtime enforces |
| Identity boundaries | None | Capability-separated |
| Event notifications | None | Native asynchronous |
| Context window | Fixed tokens | Arbitrary state, queryable as needed |
| Observability | Opaque | Object introspection, event log |

LLMs and the runtime sit at the same architectural level in the harness's tool surface, distinguished by cadence and primitive set rather than by rank. The harness's authority over orchestration is preserved; what the runtime adds is the substrate-primitive set LLMs structurally cannot provide.

## Five-axis containment for LLM-authored code

LLMs make mistakes. Code an agent (or an LLM) loads into the runtime sits inside [[Agent Code Containment Stacks Five Axes, Not One|five independent containment mechanisms]], each bounding a different attack surface:

1. **Language constraint.** The DSL agents write in cannot express dangerous operations -- no raw memory access, no escape to the host language, no direct system-call surface.

2. **Location constraint.** Agent code lives only in agent-owned objects, never in privileged runtime layers. The kernel and system tiers are inaccessible regardless of what the language permits.

3. **Invocation constraint.** Agent code is only entered through the event system, not by direct calls from arbitrary code. An attacker who has not subscribed to events cannot reach the code.

4. **Capability separation.** What agent code can reach when it does run is mediated by the privilege layer.

5. **Atomic rollback.** Any error in agent code reverts the entire operation. No partially-applied state, no manual cleanup, no half-corrupted state for the next agent to reconcile.

To break out, agent code would have to defeat all five mechanisms simultaneously. Stacked containment changes the cost calculus: defeating language puts the attacker in a location they cannot run from; defeating location puts them in front of an invocation constraint they cannot enter through; defeating invocation puts them inside a capability layer that bounds reach; defeating capability still leaves them inside an atomic envelope that rolls back partial state.

| Platform | Axes covered |
|---|---|
| WebAssembly + WASI | 2 *(sandbox + capability)* |
| Lua embedded in game engines | 1 *(language)* |
| Erlang processes | 2 *(location + supervision-restart)* |
| This substrate | 5 |

For LLM-generated code specifically, this is the structural safety the workload requires. The runtime contains the mistakes -- not the developer, not the prompt-injection detector, not the human-in-the-loop reviewer.

## Lineage

The architecture has run production services for nearly three decades. It powered iChat -- the technology behind the [[iChat Production Pedigree|first Yahoo! Chatrooms]] in the late 1990s. Production deployments in the same lineage have run continuously for over twenty years. The codebase is open-source, actively maintained by its original author, and current as of 2026.

[[The Capability-OS Tradition]] -- KeyKOS in the 1980s at Tymshare, EROS in the 1990s at Penn, CapROS, Coyotos -- plus Smalltalk and Lisp images, plus mainframe single-level-store designs -- are the architectural ancestors. These systems explicitly used [[Orthogonal Persistence as Foundational Primitive|orthogonal persistence]] as the architectural property. The whole category fell out of fashion when *stateless services + relational database* became dominant in the 1990s.

The active member of the class is [[DGD as the Living Member of the Lineage|Felix Croes's DGD]] (the Dworkin Game Driver), the runtime behind iChat, Castle Marrach, and other long-running narrative-MUD productions. Twenty-five-plus years of operational soak on a [[Adopt Single-Coherence-Domain Architecture|single coherence domain]], with the same architectural primitives modern agent infrastructure is being asked to provide.

eOS Continuum's approach is to take the lineage's substrate and shape it for the contemporary agent-infrastructure audience, rather than reinventing the substrate from scratch on a stack that does not carry orthogonal persistence as a property. The first iteration is being built in [[eos-harness MVA|eos-harness]] (a sibling repository) which validates the substrate's behavior end-to-end before the broader surface is built.

## What becomes possible

Three shapes of customer problem the substrate's primitives change the engineering math for. None is hypothetical; the substrate has run shapes structurally similar to these for over two decades.

**[[Customer-Authored Automation in a SaaS Product]].** Customers want to extend a SaaS product with real logic -- not just webhooks, not just expression-language formulas, but their own rules, calculations, integrations, conditional workflows. Today: ship a limited expression language (Notion formulas), let them write per-tenant cloud functions (operational complexity), or accept that extensibility is the customer-driving feature you keep deferring. With this substrate: customer-authored code compiles into a capability-bounded namespace inside the runtime; the namespace persists across restarts; isolation is a primitive, not a Docker tax. Salesforce Apex without the Salesforce, Notion formulas with teeth.

**[[Long-Running Stateful Workflows]].** Order fulfillment, loan applications, hiring pipelines, multi-step customer onboarding -- processes that run for days or weeks across many possible paths. Today: pick Temporal, AWS Step Functions, or roll a workflow engine on database + queue + retries; reconcile inconsistent half-completed processes when something fails mid-stream. With this substrate: the workflow IS the persistent runtime state. Each step runs atomically; failure rolls back, no half-completed processes leaving inconsistent records. Hot reload fixes bugs in workflows that are mid-flight without losing the customer's accumulated progress.

**[[AI-Authored Tools and Durable Agent Memory]].** Customers want AI to do real work on their data -- generate reports, refactor code, run analyses, drive multi-step actions across their systems. The agent has to write and execute code as part of its reasoning, and it has to remember what it learned. Today: limited tool calls, slow Docker-isolated sandboxes that warm up per session, weak isolation if you go local, agent state that resets every conversation. With this substrate: agent-authored code compiles into a capability-bounded namespace at near-native speed, persists for the agent to reuse across sessions, and cannot escape its boundary. The customer experience changes from "the AI ran for thirty seconds in a sandboxed timeout" to "the AI built me a custom tool that's still here next week."

## Where this fits in the agent ecosystem

This is a substrate, not an agent framework. It [[The Substrate Composes Additively With the Agent Ecosystem|composes with]] the tools the audience already uses:

- **LangChain / LlamaIndex / DSPy / similar reasoning frameworks** -- the substrate is the runtime your agents run on top of. These frameworks remain useful for prompt-shape and reasoning-pattern abstraction.
- **MCP / A2A / agent-to-agent protocols** -- the substrate's HTTP and event primitives implement these protocols natively. The runtime can be both an MCP server (exposing tools to external agents) and an MCP client (calling external tools from inside).
- **Vector databases (Pinecone, Weaviate, Chroma, pgvector)** -- still useful for *fuzzy* retrieval over large unstructured corpora. The substrate handles *exact* memory of structured agent state. Both can coexist.
- **Workflow orchestrators (Temporal, AWS Step Functions, Inngest)** -- the substrate handles small-to-medium-scale durable workflows natively. Temporal remains the right tool for cross-machine workflow durability at large scale.
- **Sandboxed code execution (E2B, Modal, Replit Agents, Daytona)** -- the substrate makes sandboxed code-execution a runtime primitive rather than a per-call infrastructure choice. For one-off cloud-scale code execution, those tools remain appropriate.

The composition story is deliberately additive: the runtime fills the substrate gap that current platforms paper over, without asking adopters to rewrite the parts that already work. Migration is incremental -- start with one workflow, validate the substrate's behavior, add more.

## Where this is wrong

Use a different substrate if any of the following apply:

- **[[Stateless Workloads Do Not Need This Substrate|Stateless workloads]].** Pure RAG queries -- input prompt, retrieve, answer, forget -- get no benefit from persistence overhead. A stateless function-calling pattern on top of an LLM provider is the right choice.
- **[[Embarrassingly Parallel Inference]].** Cloud-scale parallel LLM calls (batch inference over millions of documents) want a different shape than a single coherence domain offers.
- **[[Five-Nines Availability Workloads]].** Single-machine architecture inherits single-machine failure modes. Multi-region active-active distributed systems are the right substrate for that requirement; they trade the atomicity guarantees this runtime provides for the availability they need.
- **[[Workloads That Need Distributed Coherence]].** Global ledgers, planet-scale chat, content delivery -- the substrate's [[Adopt Single-Coherence-Domain Architecture|single-coherence-domain]] commitment is the wrong fit at the architecture level.
- **[[Existing-Stack Inertia]].** Teams deep in existing orchestration code whose current platform's pain is not severe -- wait until the substrate pain is felt before paying migration cost.
- **[[Managed-Cloud-Only Operational Models]].** Self-hosting is first-class here; managed-service offerings are downstream.

The structural rule: [[The Substrate Is the Wrong Choice Without Substrate-Pain|the substrate is for workloads where the primitives reduce real complexity in your application code]]. If the application does not fight the substrate problems the runtime solves, the substrate adds overhead without benefit.

## The demonstration

The eOS Continuum project's demonstration target is [[Passkey-Protected Sandboxed Web REPL|a passkey-protected sandboxed Web REPL]] -- five minutes in a browser tab to see what the substrate carries.

An authenticated user (or agent, or human acting on behalf of an agent) authenticates via Passkey -- Touch ID, Face ID, or hardware key. The browser drops them into a code editor running against a bounded namespace inside the runtime: their workspace, where they build tools, materialize objects, accumulate state. The capability layer prevents the workspace's code from touching anyone else's namespace, the runtime kernel, or the host operating system.

Kill the runtime process. Restart it. Log back in via Passkey. The workspace is exactly as it was left. Every tool built, every object materialized, every accumulated piece of context, intact -- not because anything was serialized to a database between sessions, but because the runtime is the state and orthogonal persistence keeps the entire image durable across restarts.

Seven of the eight primitives are exercised by this single artifact: orthogonal persistence (kill/restart preserves state), atomic operations (each REPL evaluation as an atomic envelope), capability separation (bounded namespace), coherent multi-agent semantics (multi-tenant Web REPL), hot reload (REPL recompiles without restart), sandboxed code load (the REPL's own evaluator), state introspection (queryable namespace). Only asynchronous events is unrepresented, and that primitive lights up as soon as multiple workspaces interact.

## Recent supporting evidence

The substrate-shaped requirement is no longer an idiosyncratic claim. Four independent research lineages have arrived at the same diagnosis from different starting points:

- [[Recursive Language Models (Zhang et al., 2025)]] (arXiv 2512.24601) treats the prompt as an environment the LM navigates programmatically, calling itself recursively over snippets in a Python REPL with state in named variables. A microcosm of the harness-as-tool inversion at single-recursion scale; the limitations the paper names (no async, no orthogonal persistence, no capability bounds) are exactly what this substrate provides as primitives.
- [[Self-Reflective Language Models (Alizadeh et al., 2026)]] (arXiv 2603.15653) extends RLM with uncertainty-aware trajectory selection in the same Python REPL environment; 22% accuracy improvement over RLM under identical wall-clock budgets.
- [[ClawVM Harness-Managed Virtual Memory (Rafique and Bindschaedler, 2026)]] (arXiv 2604.10352) is the closest external cousin to this graph's thesis, arrived at independently. It argues that "when a runtime manages a fast, scarce tier alongside slow, durable storage, the answer is virtual memory, not best-effort heuristics," and enforces atomicity, persistence, and capability boundaries at the harness layer. eOS Continuum extends the same diagnosis to the substrate layer.
- [[MemGPT Towards LLMs as Operating Systems (Packer et al., 2023)]] (arXiv 2310.08560) is the foundational framing of agent memory as an OS-shaped concern. Successors -- [[A-MEM Agentic Memory (Xu et al., 2025)]], [[Mem0 Production Memory (Chhikara et al., 2025)]], [[MemMachine Ground-Truth-Preserving Memory (Wang et al., 2026)]], [[Memoria Modular Memory Framework (Sarin et al., 2025)]], [[EverMemOS Self-Organizing Memory (2026)]] -- elaborate on the metaphor in user-space; orthogonal persistence as a primitive makes much of their work either trivial or unnecessary.
- [[Compound AI Systems (Zaharia et al., 2024)]] is the Berkeley framing for orchestration-over-multiple-LLMs-and-tools as a graph of operations. The [[Compound AI Systems Optimization Survey (Lee et al., 2025)]] surveys the recent literature; [[Towards Resource-Efficient Compound AI Systems (Chaudhry et al., 2025)]] proposes a runtime-shaped answer that arrives close to the substrate-vs-glue diagnostic without naming the substrate primitives. Compound AI Systems are the harness-as-driver pattern at higher abstraction; the literature assumes a substrate but rarely names what makes the substrate well-formed.

The [[DSPy Compiling Declarative Language Model Calls (Khattab et al., 2023)|DSPy paper]] and the public [[Why I Built DSPy Agent Skills (codeandcontext.ai, 2025)]] post sit in the same Khattab axis as RLM and SRLM -- the "writing programs that compile down to prompts" framing requires the substrate properties this graph names. The [[Recursive Language Models Paradigm of 2026 (Prime Intellect, 2026)|Prime Intellect blog post]] frames RLM as "the paradigm of 2026" and explicitly targets long-horizon agent tasks spanning weeks to months -- a workload class where orthogonal persistence stops being a stretch goal and becomes a baseline.

The agentic-runtime literature has converged on a substrate-shaped requirement that this graph's [[Agent Runtimes Require Substrate Primitives, Not External Glue]] Conviction names. eOS Continuum's substrate-LAYER position goes deeper than the harness-LAYER answers in the literature. The literature validates the direction; the depth (orthogonal persistence as foundational, capability-OS-tradition lineage, single-coherence-domain by design) is this project's specific architectural commitment.

## License, sovereignty, self-hosting

The license posture is part of the position, not an afterthought:

- [[Adopt BSD-2-Clause-Patent License|Permissively licensed]] where the team has freedom to choose. Code the team writes from scratch is suitable for downstream use, including in commercial proprietary products.
- **Self-hostable as a primary deployment model.** Run the runtime on your own hardware, in your own cloud account, behind your own network. No mandatory cloud-side dependency, no telemetry-by-default, no per-call usage fees.
- **Auditable.** The substrate is small enough that one careful engineer can read and understand it. The kernel layer that enforces capability boundaries is the security-critical surface; it is intentionally minimal.
- **Forkable.** If the team's direction diverges from yours, fork. If the project goes dormant, fork. The license and architecture together mean your agent infrastructure is not dependent on the team's continued existence.
- [[Data Exit Is a First-Class Feature|Data exit is a first-class feature]]. Snapshots are documented, versioned, and self-describing. Tools to export the state graph in a portable format ship with the runtime.

These commitments reflect a posture: the runtime is infrastructure for builders, and builders need [[Builders Own the Substrate They Depend On|sovereignty]] over their infrastructure to commit to it for serious work.

## What this site is for

A common reference for the small team and early collaborators. A starting point for the documentation introduction, the technical posts, the conversations with future contributors. The argument is intentionally framed for the small-team / community / audience-of-builders model.

What this site is not:

- **Not a marketing document.** No product naming sales pitch.
- **Not a fundraising pitch.** A separate document would be required for an investor audience; the argument here is intentionally framed for builders, not capital allocators.
- **Not a technical specification.** Primitives are described at the level of "what they do and why they matter," not "what the API looks like." Structural rules live in the [[Markdown Node Contract|Form Contracts under nodes/Contracts/]].
- **Not a product requirements document.** The work being done is architectural-depth-over-feature-breadth; PRDs belong to a downstream phase.
- **Not a competitive analysis.** No specific platforms named as adversaries. The argument is structural; any platform built on the wrong substrate has the same weaknesses, regardless of branding.

What this site is:

- A reference for the small team.
- A starting point for collaboration with the contemporary agent-infrastructure audience.
- A test of the architectural claim. If a sophisticated builder reads this and the value proposition lands, the architecture is right. If they shrug, either the audience targeting is wrong or the substrate is genuinely not different enough -- and that is information worth getting early.

## Reading paths

Where to go from here, depending on what brought you:

- **Curious about the diagnostic.** Read [[Agent Runtimes Require Substrate Primitives, Not External Glue]] when authored. Until then, the value-proposition section above and the agentic-runtime concept brief in [[eos-harness MVA|eos-harness]] carry the same argument in longer form.
- **Curious about the eight primitives.** Each will be authored as a Conviction node under `nodes/Convictions/`. They are listed above with ghost links; the per-primitive Conviction texts already live in [[eos-harness MVA|eos-harness]]'s graph and will migrate or scion here as the work proceeds.
- **Evaluating against your workload.** The "Where this is wrong" section is the fast filter -- if your workload matches one of the seven cases there, save yourself the further reading. Otherwise the [[Builders Own the Substrate They Depend On|sovereignty]] section names what commitment looks like.
- **Considering contributing.** Read [`AGENTS.md`](AGENTS.md) for the agent-orientation framing and graph conventions, then `nodes/Contracts/` for the structural rules each node form satisfies, then `nodes/Skills/` for the agent-invocable workflows. The active implementation work happens in [[eos-harness MVA|eos-harness]]; this graph is the architectural argument that work tests.

The graph is pre-content as of this writing. Most of the wikilinks above are ghost links to forthcoming nodes -- each represents a claim the project is committed to articulating in its own typed-node form. The pace of authoring is set by the work in [[eos-harness MVA|eos-harness]] and by the conversations with early collaborators that the small-team-of-builders model depends on.
