---
name: graph-load-audit
description: |
  Surveys node integration depth -- which nodes pull weight in the graph's reasoning, which are dormant. Counts inbound wikilinks and predicate edge-usage per node, identifies orphans, distinguishes structurally-thin-by-design forms from under-pulling ones, surfaces recommendations (cascade missing edges, flag meta-category candidates, low-usage Predicates). Complements Graph Audit by asking the orthogonal integration question.

  WHEN: user asks which nodes pull weight, which are orphaned, which are under-integrated; user says "load audit", "integration audit", "graph density", "dormant nodes", "/graph-load-audit"; before deprecating, merging, promoting, or elaborating a node; before a curation pass.

  WHEN NOT: looking for drift, ghost links, vocabulary inconsistency (use Graph Audit); validating one node (use Node Validate); graph is small enough that depth is obvious by hand; periodic re-audit within the same session (wastes context).
---
- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Graph Load Audit

Surveys the graph at integration-depth scale. The audit answers a different question from Graph Audit: where Graph Audit asks "is the graph correct" (drift, ghosts, vocabulary, orphans, un-annotated edges), this audit asks "which nodes are pulling weight." A node may be structurally valid (passes its Form Contract, has annotated edges, no ghosts) and still be load-bearing or dormant; integration depth is what the audit measures.

The skill produces a tier-based report. True orphans (zero inbound across both wikilink and prose) sit at the top because they are the clearest signal of misintegration. Wikilink-orphans whose concept is saturated in prose (meta-category candidates) sit next, because their fix is a small wikilinking pass rather than a structural decision. Recently-seeded nodes get their own tier because their latency is by-design rather than misintegration. Low-usage Predicates and structurally-thin-by-design nodes (Aspirations, narrow Decisions) are reported but not flagged as findings.

The audit's purpose is to inform the project's discipline against premature commitment ([[Decisions/Adopt Minimum-Viable-Architecture Stance]]↗) and the convergence-evidence test ([[Patterns/Convergent Motivation as Load-Bearing Signal]]↗). A node with five inbound references has accumulated independent motivation; a node with zero has not yet earned its place. The audit makes that question answerable.

## Steps

### Step 1: Determine scope

Ask the user whether the audit covers the full graph or a scoped subset. Common scopes:

- **Full graph** -- the default; surveys every node under `nodes/`.
- **Single taxonomy** -- e.g., only Glosses, only Predicates. Useful when one form's integration is in question.
- **Recently added nodes** -- e.g., nodes added in the last N commits. Useful for checking whether a recent seed has earned its keep.
- **Specific named nodes** -- e.g., "is the AI Agency Reference pulling its weight yet?"

A full-graph audit is appropriate at curation pass cadence; scoped audits are appropriate when checking specific suspicions.

### Step 2: Count inbound wikilink references per node

For each node in scope, count how many other nodes mention it via a wikilink. The pattern matches three reference shapes:

- `[[Concept]]` -- bare-concept reference (Glosses and Predicates with the ` -- ` separator are not addressable this way; they require either the full filename or pipe form)
- `[[Concept -- ...]]` -- full-filename reference (the structural-context form for Glosses and Predicates)
- `[[Concept|...]]` -- pipe-form reference (the prose-context form for ` -- `-suffixed targets)

The node's own file is excluded from its own count. The result is a per-node integer: the number of OTHER nodes that wikilink to it.

A regex shape that matches all three forms for a given concept name C:

```
\[\[<C>(\]\]|\s*--\s|\|)
```

Where `<C>` is the regex-escaped concept (the part of the filename stem before any ` -- ` separator).

### Step 3: Count predicate edge-usage for Predicate nodes

For Predicate nodes specifically, the inbound-wikilink count undercounts their actual load-bearing. Predicates are used as edge predicates (`predicate::[[Target]]`) far more often than as wikilink targets, and the edge-usage form is what makes them load-bearing.

For each Predicate node, additionally count occurrences of `<predicate>::` across all nodes (excluding the Predicate's own file). A regex shape:

```
\b<predicate>::
```

The result is a per-Predicate integer: how many edges across the graph use this Predicate as their named relation. A Predicate with two edge-uses is genuinely under-pulling; a Predicate with two hundred is heavily load-bearing regardless of its wikilink-inbound count.

### Step 4: Identify orphans and verify

A node with zero inbound wikilink references is an apparent orphan. Before reporting it as a true orphan, verify by also searching for prose mentions of the concept across the graph:

- **True orphan** -- zero wikilink inbound AND zero prose mentions outside the node's own file. The node is genuinely not referenced anywhere.
- **Wikilink-orphan, prose-saturated** -- zero wikilink inbound but the concept appears extensively in prose. The node is conceptually load-bearing as a category-anchor but the wikilink target is dormant.
- **Wikilink-orphan, prose-rare** -- zero wikilink inbound and only a handful of prose mentions. Borderline; depends on whether the node's claim is exercised structurally elsewhere.

The distinction matters because the recommendations differ. A true orphan needs structural attention (cascade, deprecate, or accept-as-latent). A wikilink-orphan-prose-saturated needs a wikilinking sweep. A wikilink-orphan-prose-rare may be premature.

### Step 5: Decompose prose mentions for meta-category candidates

When a node's wikilink-inbound count is low but its concept appears frequently in prose, decompose the prose mentions:

- **Wikilinks to specific instances** -- e.g., for the bare concept "Form Contract", count `[[Decision Form Contract]]`, `[[Conviction Form Contract]]`, etc. These are specific-Contract references and do not need to wikilink to the meta-category.
- **Prose mentions of named instances** -- e.g., "the Decision Form Contract..." in prose without `[[ ]]`. These could be wikilinked but each refers to a specific Contract, not the meta-category.
- **Prose mentions of the bare concept** -- e.g., "a Form Contract or other specification node" using "Form Contract" as a meta-category term. These are the legitimate wikilink targets for the meta-category Gloss.

Only the third category is a candidate for wikilinking to the meta-category node. A meta-category node may have hundreds of total prose mentions and only a handful of legitimate-target prose mentions; the decomposition surfaces the true gap.

### Step 6: Categorize by structural baseline

Some forms have a structurally-low inbound baseline. Reporting a low count for these as a "finding" is noise. Categorize accordingly:

- **Aspirations** -- forward-looking by form; 1-2 inbound is the baseline rather than a problem.
- **`Require X` Decisions** -- each grounds exactly one Contract Requirement; 1 inbound is structurally proportionate.
- **Recently-seeded nodes** -- nodes added in the last few commits whose latency is by-design; report but do not flag.
- **Skill nodes** -- user-invocable; their load-bearing is in being invokable rather than in being graph-referenced.
- **External-marker References** (`↗` targets that point at adjacent graphs) -- low inbound is the norm because the graph references them sparingly by design.

For these categories, report the count but classify as "structurally appropriate" rather than as "under-pulling."

### Step 7: Identify low-usage Predicates

For Predicate nodes, the load-bearing measure is edge-usage from Step 3, not wikilink-inbound from Step 2. A Predicate with edge-usage below ~10 is a candidate for either-find-it-work or merge-with-adjacent. Specifically:

- **Edge-usage 0-2** -- the Predicate is registered in vocabulary but not exercised. Either the Predicate is premature (defined before use surfaces) or the use cases it should cover are not being authored. Worth flagging.
- **Edge-usage 3-9** -- the Predicate is exercised but narrowly. Not a finding by itself; depends on whether the Predicate's distinction against adjacent Predicates is load-bearing (the Crescent section's content). If the Crescent does not name a structural distinction the graph commits to, the Predicate may want consolidation.
- **Edge-usage 10+** -- working as intended; no finding.

Recently-seeded Predicates (e.g., `scion_of` shortly after the Self-Sovereign Graph Publication Decision was adopted) are expected to grow and should be classified per Step 6.

### Step 8: Produce the tier-based report

Group findings by tier:

- **Tier 1 -- True orphans (zero inbound and zero prose mentions).** Highest concern. For each, name the node, its outbound edges (if any), and recommend: (a) cascade missing reciprocal edges back from the targets it claims to inform, (b) absorb the node's content into an adjacent existing node, or (c) defer until use surfaces.
- **Tier 2 -- Wikilink-orphans, prose-saturated meta-category nodes.** For each, report the prose-decomposition from Step 5 and recommend either (a) accept as a meta-category whose load is implicit (the prose mentions are sufficient) or (b) sweep the legitimate-target prose mentions and add `[[ ]]` wikilinks.
- **Tier 3 -- Recently seeded, latent-by-design.** Report inbound counts; recommend re-evaluation after the next session that exercises the cluster the seed belongs to.
- **Tier 4 -- Low-usage Predicates.** List Predicates with edge-usage below the threshold; for each, recommend find-it-work, consolidate-with-adjacent, or accept-as-defined-but-narrow.
- **Tier 5 -- Low inbound but structurally appropriate.** Aspirations, narrow Decisions, Skills, external-marker References. Reported with their counts; no finding.

For each Tier 1 and Tier 4 finding, name the specific recommended action and what would change it (e.g., "cascade reciprocal `informed_by::` edges from Vocabulary Diversity Is a Feature and Translation Over Convergence to Synpraxis Spectrum -- both Convictions are claimed downstream by the Gloss but neither documents the back-edge").

### Step 9: Stop

Do not edit nodes. Do not stage or commit. The audit produces findings; acting on them is a separate authoring pass (typically using Node Create for new nodes, direct Edit for cascades, or Predicate Propose for vocabulary changes).

If the user wants a follow-up action committed in the same session, surface the specific edits the audit recommends and let the user authorize them per finding. The audit's role is to surface the gaps; the user decides which are worth closing now.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements -- YAML frontmatter carrying `name` and Anthropic `description`, compound-node layout, numbered Steps, Relations grounded in the Decisions and Convictions the skill realizes.

- composes_with::[[Graph Audit]]
  - The two skills are graph-scope hygiene audits at orthogonal angles. Graph Audit asks "is the graph correct" (drift, ghosts, vocabulary, orphans, un-annotated edges, forbidden predicates). This skill asks "which nodes are pulling weight." A node can pass Graph Audit and still be dormant; a node can be heavily integrated and still have drift. The two together produce a fuller picture of graph health.

- composes_with::[[Node Validate]]
  - Node Validate operates at single-node scope and verifies form-contract conformance. This skill operates at graph scope and verifies integration depth. A node validated by Node Validate may still be a true orphan flagged by this skill; the two checks are independent.

- composes_with::[[Node Read]]
  - When this skill flags a node as under-pulling, the natural follow-up is to read the node and the nodes it claims to inform, to decide whether the under-pulling reflects a structural gap (cascade missing) or a content gap (the node's claim hasn't been exercised). Node Read is the orientation skill that closes that loop.

- grounded_in::[[Decisions/Adopt Wikilinks and Named Edges]]↗
  - The spine commitment this skill measures. The audit counts wikilink references and named-edge predicate usage; both metrics rest on the graph being committed to author-declared edges in the first place. Without the substrate Decision, neither metric would be meaningful.

- grounded_in::[[Decisions/Adopt Minimum-Viable-Architecture Stance]]↗
  - The Minimum Viable Architecture stance defers capabilities until use surfaces them. This skill is the survey that tells the project which seeded nodes have accumulated use and which have not. A node flagged as a true orphan after several sessions is a candidate for the Minimum Viable Architecture discipline's "is this load-bearing yet?" question.

- informs_downstream::[[Patterns/Convergent Motivation as Load-Bearing Signal]]↗
  - The Pattern's convergence test asks whether four or more independent motivations have accumulated on a proposed structural commitment. This skill produces the evidence the test consumes -- inbound reference count is one direct measure of motivation accumulation. The Pattern is the discipline; this skill is the measurement that makes the discipline operational at the graph layer.
