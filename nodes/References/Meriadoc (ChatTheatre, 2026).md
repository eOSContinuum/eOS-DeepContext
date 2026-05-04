---
tagline: The refererence implementation's sandboxed code-load DSL: source-as-property in the persistent image, multi-phase signal-triggered execution, decoration-and-compile over a denylisted kernel; all five axes of code containment enforced by substrate, in continuous production over twenty-five years
created: 2026-05-04
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Foundational Reference Implementation of Sandboxed Code-Load]]
- in_practice_domain::[[eOS Continuum]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# Meriadoc (ChatTheatre, 2026)

Meriadoc -- formally *Mediated Execution Registry Involving A Dialect Of C*, conversationally "Merry" -- is the reference implementation with operational evidence that sandboxed code-load on a property graph works at production scale. The implementation has run in continuous production deployment for over twenty-five years, carrying all five axes of code containment (language, location, invocation, capability, atomic rollback) as substrate primitives rather than as review-time discipline.

The pattern: source lives as a property on objects in the persistent state graph; setting the property compiles the source into the live runtime image; execution happens only when a named signal is dispatched to the storing object. The dispatch model is multi-phase (pre / prime / post), and the dispatcher walks the property's data-inheritance chain (the refererence implementation's "ur-parent" chain, distinct from any host-language class inheritance) to find the matching handler under the host's atomic-call envelope. The handler runs in a constrained vocabulary -- a fixed grammar plus a host-defined function library -- over a denylisted host kernel. The deployment-specific function vocabulary the implementation ships with is a dialect choice that another deployment would adapt to its own object model.

In an eOS workspace, this means an LM-driven agent can author durable handlers directly on workspace objects. When a sub-call commits a result into the namespace, a `meriadoc:react:result_committed` handler can propagate a constant-size metadata summary upward to the parent reasoning context -- the architectural property [[Recursive Language Models (Zhang et al., 2025)|RLM]] proposes at user-space Python scale, realized here at substrate scale. Tools an agent authors are written as properties on workspace objects; the property-set hook compiles them into the live image, and they remain available across process restarts because they live in the orthogonally persistent state graph rather than as ephemeral functions in a Python REPL whose state evaporates on process death. And because handlers themselves live as properties, the same signal mechanism applies to handler authorship: handlers can witness handlers being authored, validated, or revised, making meta-programming a first-class composition surface rather than a meta-layer bolted on top.

### Signal-system shape

The pattern requires a host signal system that supports **multi-phase dispatch** for any operation interesting enough to want hooks around. Three phases generalize cleanly to any reactive substrate; a fourth phase exists in the original text-environment domain and is not part of the pattern.

**Pre** -- early veto. Fires after the substrate sanity-checks the operation's arguments but before any state mutates. Handlers may inspect the operation's parameters and abort it. Runs inside the triggering operation's atomic envelope -- a pre-handler error reverts the entire operation. Use for state-aware argument validation ("can this principal even attempt this operation?").

**Prime** -- late veto. Fires when the substrate believes the operation should proceed (preconditions satisfied, no early veto fired). Last opportunity to abort, with the operation's full intent visible to the handler. Runs inside the same atomic envelope as pre -- a prime-handler veto rolls back not only the prime work but the work the operation has already done. Use for veto that depends on state the early phase could not yet decide ("the workspace compiled the LM-authored expression cleanly, but its closure references a capability the principal does not hold; abort before the expression executes").

**Post** -- react. Fires after the operation has committed. Most common phase to bind to. Runs in a new atomic envelope of its own, so a post-handler error does not retroactively roll back the triggering operation -- post handlers see committed state and react to it; they cannot veto. Use for side-effect cascades ("after a sub-LM call commits its result to a workspace variable, propagate a constant-size metadata summary upward to the parent reasoning context").

A fourth phase, **desc**, exists in the implementation's hosting domain to compile observer-specific output for varying viewers of the same operation; it is a domain-specific rendering concern, not a generalizable phase of the pattern, and explicitly not part of this reference implemenation's adoption.

A handler binds to a `<phase>:<signal>` pair on an object. The dispatcher resolves a signal at dispatch time by walking the storing object's data-inheritance chain, so a child object that has not overridden a parent's handler still picks up the parent's behavior. **Exactly one handler runs per phase per dispatch** -- the first match in the data-inheritance walk, with the child's override taking precedence over its parents' bindings. This is method dispatch, not event-bus fan-out: there is no implicit chaining, no observer-list aggregation, and no subscription-order dependency. Behavior is deterministic in the resolution order. This is what makes "fork an object's behavior by overriding one phase of one signal" the dominant authoring pattern -- and what differentiates Meriadoc from systems where hooks are registered globally rather than carried by the object that owns them.

The foundational signal source in an eOS workspace is the property write itself. The 2004 design document names the primitive directly: "Setting a property on an object fires an event ... this allows developers to hook complicated [scripts] up to react to changes in properties." When any property changes on an object, the substrate fires the change through the same pre / prime / post protocol any other operation uses; handlers register interest by binding to a property key (or a namespace prefix), and they receive the proposed value, the principal performing the write, and the operation's atomic envelope. This collapses what other systems treat as separate concerns -- property setters, observer hooks, schema-validation hooks, change-emit events -- into a single substrate primitive. Operations from the broader operation flow (sub-call dispatch, capability extension, recursion-step transitions, tool invocation) layer on top of the same protocol; pre / prime / post phases are the substrate's atomic-call envelope made dispatchable.

### Property-system minimum

The pattern's substrate floor is more than just "an object has properties." Four capabilities are required:

- **Keyed property map per object.** Each object carries a string-keyed map; values are any host-supported type, including source text. Typical key shape: `<dsl-prefix>:<phase>:<signal>` (e.g., `meriadoc:react:result_committed`, `meriadoc:pre:capability_requested`). The namespace is convention, not primitive -- the substrate sees an opaque key.
- **Set-time hook.** Writing a property fires a substrate event the DSL's daemon can react to. This is what makes property-write the trigger for compiling the source into the live image. Compilation failures surface at edit time -- the substrate's compile pass is wired to the property write, so a broken handler is caught when it is authored, not on the path that first dispatches it. There is no separate deploy step; code becomes live as part of state mutation, atomically with the property write that introduced it.
- **Data-object inheritance on read.** A property read on a child object falls back through a chain to the parent. Without it, every script must be set on every instance; with it, libraries and inherited behavior become first-class. The refererence implementation calls this "ur-parent" inheritance, and it is a runtime mechanism distinct from any class or code inheritance the host language provides (elaborated in "Data inheritance, not code inheritance" below).
- **Persistent property storage.** Property writes survive runtime restart by virtue of the substrate's orthogonal-persistence primitive. Without persistence, the script-as-property model collapses into normal load-from-disk modules, and the pattern's hot-reload story degrades to deploy-time.

Two further capabilities are commonly used but not strictly required:

- **Virtual (computed) properties.** A property's read may run host code rather than fetch a stored value. Useful for derived state (a workspace's accumulated token cost as a sum of its sub-calls' costs; a namespace's effective capability set as the intersection of its parent's set and the principal's authorized scope; a reasoning trace's current recursion depth). Not strictly needed for the code-load pattern, but the refererence implementation uses virtual properties pervasively in adjacent surfaces, and any deployment carrying the pattern will likely want them too.
- **Property-write capability tier.** Writes to script-bearing namespaces should be gated by the same capability layer that gates other writes. Required for security; the pattern itself does not define the policy -- the substrate's capability primitive does.

A property system that supplies the four required capabilities (keyed map, set-time hook, data-object inheritance, persistence) is sufficient to host the pattern. eOS Continuum's substrate carries all four as primitives.

### Data inheritance, not code inheritance

The refererence implementation's substrate provides two distinct inheritance systems, and Meriadoc handlers compose through one of them, not the other.

**Code inheritance** is the host language's compile-time class inheritance (LPC's `inherit` directive). It composes the substrate's own implementation: the dispatch object that runs Meriadoc handlers inherits from a curated set of host libraries; system services inherit from kernel libraries; the runtime's structure is built through code inheritance the same way any host-language program is.

**Data inheritance** is a separate runtime mechanism that operates on data objects through the property system. A data object names another data object as its parent ("ur-parent"); property reads on the child cascade through the chain, and the child may override individual properties. Crucially, in the refererence implementation's design, all data objects are clones of the same underlying host class -- their behavior differs entirely through their data-inheritance chain, not through programmatic class. The compositional surface for authoring (world authoring in the refererence implementation; tool authoring in an eOS workspace) is the data graph, not the class graph.

Meriadoc handlers compose through data inheritance because they are properties on data objects. To specialize a handler, an agent clones a parent object and overrides one property; the clone inherits every other handler, shares the host class, and differs only in its property store. There is no new class, no recompilation, no separate code unit. Code inheritance and data inheritance evolve on different timescales -- code on substrate-source-change (with hot-reload to merge updates), data on principal-authored-property-change -- and the substrate's machinery for managing data inheritance does not require code recompilation. The two systems coexist without interfering: substrate maintainers extend the runtime through code inheritance, and agents extend their workspace through data inheritance, and neither path can substitute for the other.

This distinction is not cosmetic. The refererence implementation's design choice -- many data-object instances of one host class, distinguished by ur-parent state, rather than many host classes with one instance each -- is precisely what makes the code-as-state principle workable at the workspace scale an LM-driven agent will exercise. Class-based composition would force every tool variant to be a new class; data-based composition lets variants exist as cloned property bundles, persistable and inheritable through the substrate's existing primitives.

### Reflexive composition

Because Meriadoc handlers themselves live as properties, the property-write signal mechanism applies to handler authorship too. Writing a handler to `meriadoc:react:<signal>` is itself a property write that fires its own pre / prime / post protocol; other handlers can witness it. The pattern is reflexive: handlers and the things handlers witness are the same kind of substrate object.

This is the structural consequence of the code-as-state principle. Worked examples relevant to an eOS workspace:

- A meta-handler bound pre to writes in the `meriadoc:` namespace can validate proposed handlers before they compile -- gate authorship by capability tier, refuse handlers that exceed a token-budget heuristic, reject handlers whose closure references capabilities the principal does not hold. Capability gating on script authorship is a script that witnesses script-property writes.
- A meta-handler bound post to writes in the `meriadoc:` namespace can index the handler population, persist an audit trail of authorship and revision, or notify subscribers that a new tool is available in the workspace. The agent's tool registry is naturally implemented as a handler that subscribes to its own namespace's writes -- no separate registry service, no external observer process, no out-of-band synchronization.
- A learning loop watching how an LM-driven agent's tool population evolves over sessions is a handler bound post to the `meriadoc:` namespace, persisting summaries to a sibling property that downstream agents inherit through the ur-parent chain. The substrate primitives -- persistence, data inheritance, atomic envelope -- carry the learning loop's state without an external store.

Meta-programming is a first-class composition surface, not a meta-layer bolted on top of a fixed event schema. This is what differentiates the pattern from systems where hooks are second-class additions, and from systems where the script population is opaque to the scripts themselves.

### Limitations of modern "safe" languages

Modern language-level safety -- memory-safe languages (Rust), sandboxed runtimes (WebAssembly + WASI, V8 isolates, Lua interpreters), capability-typed embeddings -- addresses real problems and gets things right that Meriadoc does not. Modern safe languages have superior tooling, broader audience familiarity, sophisticated type systems, near-native compute performance, and decades of investment in cross-platform portability. For workloads where the safety question is "can untrusted code crash the host process or escape the FFI boundary," any of them is a reasonable answer.

The structural gap, relative to what an LM-driven agent workspace needs, is that none of them addresses **state-substrate concerns**. Their containment story stops at the language boundary; the substrate they run on does not natively carry the properties an agent's persistent reasoning surface requires. Concretely:

- **Atomic rollback over host state.** A Wasm trap aborts computation but does not roll back the host-state mutations performed before trapping; the host owns cleanup. Meriadoc handlers run inside the substrate's atomic envelope -- a trap reverts every property write the handler performed, automatically.
- **Orthogonal persistence of the sandboxed code itself.** Wasm modules, Lua scripts, V8 contexts, container images all load from filesystem or registry on each host startup; the sandboxed code is not part of the substrate's persistent image. Meriadoc handlers persist as properties in the orthogonally persistent state graph; restart finds them where they were, with no separate load step.
- **Reflexive composition between sandboxed modules.** Wasm modules call each other through host-managed FFI but cannot witness each other being authored or revised through the same primitive that watches host data change. Meriadoc handlers witness handler authorship through the same property-write signal mechanism that watches any other property change.
- **Data-object inheritance of sandboxed code.** No modern safe-language sandbox carries runtime data-object inheritance for code units. To fork a code unit's behavior by overriding one handler, the host must roll its own composition layer outside the sandbox, in a separate data model. Meriadoc handlers inherit through the substrate's ur-parent chain the same way data does, because they are data.
- **Multi-phase dispatch as substrate primitive.** Wasm has no pre / prime / post phases; Lua hooks are per-engine conventions; JS event listeners are single-phase and uncontainable. Meriadoc's pre / prime / post protocol is a property of the dispatch envelope, not an application-layer convention.

The graph's [[Agent Code Containment Stacks Five Axes, Not One]] table places Wasm + WASI at 2 axes, Lua at 1, Erlang processes at 2. Composing additional axes means stacking technologies (Wasm in a container in a transactional database with a supervisor and an event bus); the composition's boundaries are exactly where bugs live. Meriadoc's 5-of-5 containment is the substrate's natural property, not an externally-stacked composition.

The reference implemenation does not claim modern safe languages should be displaced for workloads where state-substrate concerns are not load-bearing. Pure compute, embedded scripting in non-stateful contexts, sandboxes for untrusted code with clear boundaries -- those workloads do not need orthogonal persistence or reflexive composition, and the modern-safe-language ecosystems serve them well. The narrower claim: for an LM-driven agent workspace where state-substrate properties are exactly the bugs the application keeps fighting, the modern-safe-language path stacks technologies to approximate what Meriadoc's substrate carries natively. The conceptual shift is that instead of making code safe around the system, the substrate is the safety boundary.

### Adopted

The code-as-state principle (Property-system minimum and Data inheritance subsections above carry the substantive treatment). Policy and data live in the same store, under the same data-object (ur-parent) inheritance, in the same atomic envelope, with the same persistence -- the substrate model eOS Continuum names as primitive #6 ([[Code Load Compiles Into the Live Runtime, Bounded by Capability Tiers]]).

The five-axis containment claim, grounded in operational artifact with per-axis citations. The graph's [[Agent Code Containment Stacks Five Axes, Not One]] table places the refererence implementation substrate plus Meriadoc as its DSL surface at 5 of 5 axes covered, each enforced by a specific mechanism in the source:

- **Language** -- `merry.y` refuses dangerous productions at parse time (the `->` operator rejection production; the `rlimits()` rejection production); `merrynode.c` denylists ~30 host kfuns at the dispatch boundary via the `SANDBOX(...)` macro and overrides `call_other` / `new_object` to a tiny allowlist.
- **Location** -- scripts cannot inhabit privileged tiers because they are not a kind of object; they are a property value compiled into a per-script unprivileged object under the merry daemon's namespace (`/usr/SkotOS/merry/<name>`).
- **Invocation** -- scripts are entered only through `merrynode.c`'s `evaluate()` function, called by the substrate's signal dispatcher. There is no path for arbitrary code to call a script directly.
- **Capability** -- the function vocabulary is the capability boundary. The dispatch object's `inherit` directives (`/lib/string`, `/lib/array`, `/lib/date`, `/lib/mapping`, `/lib/propmap`, plus deployment-specific libraries) and its `nomask static` direct functions enumerate exactly what's available; a per-deployment fork of those inheritance lines is how a different deployment narrows or widens the surface.
- **Atomic rollback** -- inherited from the host's atomic-function semantics; a runtime error inside a Meriadoc handler reverts every property write the handler performed before the trap, without application participation.

A reviewer can verify each axis by reading the named files. The 5/5 claim is grounded in current implementation behavior, not aspirational design.

The decoration-and-compile strategy. The implementation has no separate VM. Source is decorated host-language: same control flow, same operators, same types, plus syntactic sugar for property access, object refs, argument refs, inline templating, and a delay statement. A grammar pass rewrites the decorations into pure host-language AST nodes; the host compiles the result with its normal compiler and caches it. Safety is enforced at the host-language level, not by interpretation in a separate runtime -- which is why the implementation runs at host-native speed and inherits the host's atomic-rollback semantics for free.

The pre / prime / post phase model (Signal-system shape subsection above). The three generalizable phases form the application surface of the substrate's atomic-call envelope, essential to the veto / late-veto / react composability the pattern enables.

### Not adopted (yet)

The deployment-specific function vocabulary. The implementation ships with a function library shaped by its specific hosting deployment rather than by a substrate-layer use case. These deployment-specific primitives presuppose an object model and content surface eOS Continuum does not share; the pattern lifts but the dialect does not. eOS Continuum's adoption is at the pattern layer; the function vocabulary the substrate exposes will be shaped by what eOS workspaces actually need -- sub-call coalescing, namespace operations, capability extension, recursion-budget management, tool authoring and indexing, and reasoning-trace introspection.

The fourth signal phase, "desc". The implementation dispatches a fourth phase per signal to compile observer-specific output for varying viewers of the same operation. This is a domain-specific rendering concern, not a generalizable phase of the pattern, and explicitly not adopted.

The functional-templating sibling. The implementation ships alongside a separate functional templating layer for variable output text. eOS Continuum may need its own content layer or none at all; the templating sibling is not part of the code-load pattern this Reference adopts.

The specific property-namespace conventions and dialect-level idioms. The implementation uses naming patterns like `merry:react:<signal>`, `merry:lib:<name>`, `merry:inherit:<mode>:<signal>`, plus dialect-level constructs (named-reference values, named-object constants, inline-templating literals, label calls between named script-spaces). These are the implementation's specific conventions; eOS workspaces will name and shape their script-properties according to their own conventions.

### Open verification questions

Three determinism properties an LM-driven workspace would benefit from having confirmed, but which are not yet verified by by reading of the reference implemenation source. They are reasonable design properties for a deterministic self-modifying runtime; whether the implementation enforces each (and how strictly) is a source-verification task flagged here as potential future development. Confirming each would strengthen the reference implementation's 5/5 containment claim and the eOS substrate's reflexive-composition guarantee.

- **Re-entrancy detection.** Does the runtime prevent a handler from modifying the property it is reacting to? An eOS workspace benefits from this guarantee because it bounds the cascade implications of property mutations during dispatch and prevents a class of subtle infinite-recursion bugs. Not visible in `merry.y` or the dispatch object's surface structure as read; may be enforced in the merry daemon or in inherited substrate code. Verification task: locate the enforcement point, or confirm absence and characterize the resulting failure mode.
- **Signal-loop detection.** When a handler emits a signal that ultimately causes the same handler to fire again, does the runtime detect and terminate the loop? The host's tick limits will eventually halt any runaway computation, but a more specific loop-detection mechanism would be a stronger guarantee with cleaner failure semantics (named "loop terminated" rather than generic "tick limit exceeded"). Verification task: search for cycle-detection logic in the dispatcher, or confirm reliance on tick limits as the only backstop.
- **Compilation non-reentrancy.** When a handler write triggers compilation, does the substrate prevent that compilation from being reentered -- for example, by a meta-handler bound pre to writes in the same namespace that itself attempts to author another handler? The reflexive-composition story's safety depends on this: without the guarantee, a meta-handler could trap the compiler in a cascade. Verification task: trace the merry daemon's compile path, identify whether nested compilation is permitted, and characterize what happens if it is attempted.

These three are flagged for future development rather than as current limitations. The reference implementation's containment story holds at the level of language, location, invocation, capability, and atomic rollback regardless of how each verification resolves; the determinism story is a separate, sharper claim that would benefit from the verification.

## Sources

- **Grammar**: <https://github.com/ChatTheatre/SkotOS/blob/master/skoot/usr/SkotOS/grammar/merry.y> -- the canonical pattern definition; ~490 lines defining the DSL's lexical structure, types, operators, control flow, and the explicit rejection of dangerous host-language productions.
- **Dispatch object**: <https://github.com/ChatTheatre/SkotOS/blob/master/skoot/usr/SkotOS/lib/merrynode.c> -- the canonical sandbox implementation; defines what is directly exposed (the `nomask static` function set), what host-language libraries the DSL inherits, and the explicit denylist of dangerous host-language kfuns at the dispatch boundary.
- **Period-authentic design context**: <https://github.com/ChatTheatre/eOS/blob/master/historical/Doc%202004-08-29%20Re%3A%20SkotOS%3A%20SkotOS%20on%20the%20brink%20of%20the%20rewrite.md> -- a 2004 technical summary of the refererence implementation at the moment Meriadoc "had emerged as possibly the single most important component"; carries the canonical phrasing of the implementation strategy ("a decorated and sandboxed form of LPC; the decorations are turned into 100% LPC, and the result is compiled") and articulates the pre / prime / post (and domain-specific desc) phase model from period-authentic primary documentation.
- **Date**: pattern established early 2000s; implementation continuously maintained; cited revision year is most recent.
- **Stub note**: Authored 2026-05-04 as the canonical Reference for the refererence implementation's sandboxed code-load DSL. Body to be expanded with per-axis containment-mechanism citations into specific merrynode.c sections, the universal-kernel-vs-dialect split formalized, and an audit checklist for deployments adapting the pattern, in a future authoring session.

## Relations

- conforms_to::[[Reference Form Contract]]
  - The canonical Reference for the refererence implementation's sandboxed code-load DSL; informs the substrate's primitive #6 and the five-axis containment claim.

- informs_downstream::[[Code Load Compiles Into the Live Runtime, Bounded by Capability Tiers]]
  - The implementation's defining principle (code lives as data in the persistent image, compiled into the live runtime at property-set time, capability-bounded at the dispatch boundary) is the refererence implementation source for the eOS substrate's primitive #6. The Conviction will draw its operational evidence from this Reference.

- informs_downstream::[[Agent Code Containment Stacks Five Axes, Not One]]
  - The "5 axes covered" claim in the welcome's containment table is grounded in this implementation: each axis maps to a specific enforcement mechanism (grammar productions, property-tier location, signal-triggered invocation, dispatch-object inheritance graph, host-runtime atomic envelope) cited from the reference implemenation's source files.

- composes_with::[[Orthogonal Persistence Is the Foundational Substrate Primitive]]
  - The implementation's "code as property in the persistent image" model presupposes orthogonal persistence as a substrate primitive. Without #1, the code-load pattern collapses into a normal load-from-disk module system, and the pattern's hot-reload story degrades to deploy-time. This Reference is one of the operational citations for the welcome doc's claim that #1 is foundational to the other seven.

- composes_with::[[Agent Operations Commit Wholly or Roll Back Wholly]]
  - The substrate's atomic-call envelope is invoked throughout this Reference: pre / prime / post handlers run inside it, a runtime error reverts every property write the handler performed, and the 5/5 containment table's atomic-rollback axis maps directly to primitive #2. Adopting Meriadoc-the-pattern presupposes the substrate carries atomic operations as a primitive rather than as application discipline.

- composes_with::[[Capability Boundaries Are Runtime-Enforced, Not Policy-Checked]]
  - The capability axis of the 5/5 containment table is the intersection of three sources: the principal's authorized scope, the object's tier, and the dispatch object's function vocabulary. Handlers can only call what the dispatch object's `inherit` graph exposes; principals can only write properties their tier authorizes; objects can only carry handlers their tier permits. Meriadoc's specific contribution to this intersection is the function-vocabulary axis at the dispatch boundary; the substrate's primitive #3 contributes the principal and object axes.

- composes_with::[[Event Notification Is Atomic With State Change, Not Polled or Queued]]
  - Meriadoc's signal-triggered execution model is the application surface of primitive #7. Scripts run only in response to signals dispatched within the atomic envelope of the state-changing operation; the implementation has no scheduler, no polling, no separate event queue. Adopting the pattern presupposes adopting this primitive.

- composes_with::[[Hot Reload Is a Runtime Operation, Not a Deployment Event]]
  - The pattern's hot-reload story is the property-write itself: writing a `meriadoc:*` property recompiles the script and updates the live runtime; in-flight handlers complete with their old code, subsequent dispatches use the new. The implementation's hot-reload mechanism is the operational citation for primitive #5.

- composes_with::[[DGD as the Living Member of the refererence implementation]]
  - The substrate Reference. DGD provides the host language (LPC), the kfun surface that the sandbox denylists, the atomic operations the dispatch envelope uses, the parse_string grammar facility that the decoration-and-compile strategy relies on, and the orthogonally-persistent runtime image that makes code-as-state coherent. This Reference (Meriadoc as DSL) and the DGD Reference (Meriadoc's substrate) compose to a complete picture.

- composes_with::[[Recursive Language Models (Zhang et al., 2025)]]
  - RLM proposes the architectural inversion (LM as a tool the program calls, not the program calling tools) at user-space Python scale, with the explicit limitation that "REPL state evaporates on process death." Meriadoc realizes the same inversion at substrate scale: handlers, tools, and intermediate sub-call results all live in the orthogonally persistent state graph, so recursion depth, accumulated reasoning context, and authored tools survive process restart by default. The two References compose -- RLM names the technique; Meriadoc is the substrate-layer realization that lifts the limitation.
