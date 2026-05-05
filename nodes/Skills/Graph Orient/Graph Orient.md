---
runtime_name: graph-orient
tagline: Orients an agent to this graph at first entry by reading AGENTS.md, the landing page, then Contracts, Convictions, and Predicates in a prescribed order
description: |
  Orients an agent to this graph at first entry. Reads AGENTS.md and the landing page for stance, then the Contracts at identity-block scale to learn what forms nodes take, then the Convictions to learn the stances the graph is committed to, then the Predicates to learn the local typed-edge vocabulary. Reports a compressed orientation covering the graph's forms, vocabulary, founding commitments, and live tensions.

  WHEN: the user is new to this graph and has scioned or cloned it locally; the agent has entered the repository for the first time and has not yet read AGENTS.md; the user says "orient me", "what is this graph", "read the repo", "get up to speed", or "where do I start"; at session start before the agent begins a task against the graph.

  WHEN NOT: the agent has already read AGENTS.md and the key Contracts in this session (repeat orientation burns context without adding signal); the task is scoped to a single node (use Node Read); the user wants a deep traversal across many nodes on a specific topic (use Node Research once it exists); the agent is working in a scion and the scion's AGENTS.md already establishes the stance.
---

- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Graph Orient

Orients an agent at first entry to the graph. Entering a new knowledge graph without a curated path is expensive — every node looks equally worth reading, and the cost of reading them all before beginning work exhausts context. This skill walks a deliberately short path through the files that carry the most orientation signal per read: the agents file, the landing page, the Contracts at identity-block scale, the Convictions, and the Predicate vocabulary. After this path, the agent knows what forms the graph uses, what stances it holds, what predicates it speaks, and where the live tensions are.

The skill does not read all nodes, does not summarize individual Decisions or Observations, and does not follow edges into elaboration bodies. Depth on specific nodes is the job of Node Read; cross-topic traversal is the job of Node Research. Graph Orient is the cheapest read that produces enough context to make the later skills land well.

## Steps

### Step 1: Read AGENTS.md

Read the repository-root `AGENTS.md` file first. It carries the project's stance on agent behavior — curate not overwrite, translate not normalize, name features not traditions, treat new common vocabulary as proposal, preserve reasoning in the form, remain authored-by not authoring. These imperatives constrain every subsequent action the agent takes.

If the agent is working on a scion whose `AGENTS.md` differs from the template's, this is the authoritative stance — do not fall back on the template's file.

Report the stance imperatives in one compressed paragraph. The agent will not re-read this file later in the session; the compression is the reference.

### Step 2: Read the landing surface

Read the project's landing surface. The landing surface is one of two shapes: a `landing.md` file at the repository root (older graphs), or a Touch Point node carrying `is_home: true` in its YAML frontmatter (newer graphs that adopted the Touch Point Form Contract). Check for `landing.md` first; if absent, search `nodes/Touch Points/` for the home Touch Point.

The landing surface carries the project's public framing — what the graph is for at card scale, the founding Decision it rests on, the Convictions that ground the founding Decision, and the first-reader entry points.

Report the founding Decision and its grounding Convictions by name. These are the load-bearing commitments; every Decision downstream either composes with them or argues against them. If the landing surface names them as ghost wikilinks rather than resolved internal links, report them as ghost-linked-and-unauthored — a young graph framing its commitments before authoring the load-bearing nodes is a legitimate state, the same way an empty Convictions surface is in Step 4.

### Step 3: Scan the Contracts

List `nodes/Contracts/` and read each Contract's identity predicate block and opening paragraph — the cheapest two layers per Node Read. The Contracts establish the form system: Markdown Node Contract is the base; form-specific Contracts (Gloss, Decision, Conviction, Aspiration, Observation, Pattern, Predicate, Reference, Skill) extend it.

Report the Contracts by name, each with a one-line statement of what form it specifies. The agent does not read the `## Requirements` sections of each Contract here — that cost is deferred to Node Create or Node Validate when an operation actually needs them.

### Step 4: Scan the Convictions

List `nodes/Convictions/` and read each Conviction's identity block, H1, and opening paragraph. Convictions carry held stances — the normative commitments the project's authors make about what ought to be the case in the domain the graph concerns. The specific Convictions vary per graph; read what the local graph carries, not what an upstream or template graph carried.

If `nodes/Convictions/` does not exist or is empty, report "no Convictions yet authored in this graph" and proceed to Step 5. The skill's structure does not depend on Convictions being present; an empty Convictions surface is a legitimate state for a young or newly-scioned graph.

Report each Conviction's stance in one compressed sentence. A Conviction is the furthest-upstream anchor the agent can cite when a Decision needs grounding.

### Step 5: Scan the Predicate vocabulary

List `nodes/Predicates/` and read each Predicate node's filename and `## Carries` paragraph. The Predicate filenames follow `<predicate> -- <one-clause sense>.md`, so the filename itself carries a compact definition.

Run a frequency audit to see which predicates are actually in use across the graph, regardless of whether they have a backing Predicate node:

```sh
rg -o -I -- '^- [a-z_]+::' nodes/ | sort | uniq -c | sort -rn
```

Report the vocabulary in two columns: predicates with a backing Predicate node (definitional) and predicates in use without a backing node (provisional or drift). The split lets the agent know which edges are load-bearing and which are candidates for predicate-proposal work.

### Step 6: Note the live tensions

Scan for `contends_with::` edges across the graph — each one names a tension the project holds open rather than collapsed:

```sh
rg -I -- 'contends_with::' nodes/ | sort -u
```

Report the tensions by the two sides they name. Live tensions are where the graph is still arguing with itself; the agent should neither take sides nor propose a resolution without explicit invitation.

### Step 7: Report

Produce a compressed orientation covering:

- **Stance** — the agent-behavior imperatives from AGENTS.md, in one paragraph.
- **Founding commitment** — the Decision that established the graph and the Convictions that ground it.
- **Form system** — the Contracts available, one line each.
- **Held stances** — the Convictions, one line each.
- **Vocabulary** — the predicates with backing Predicate nodes, the predicates in use without backing nodes, and the live tensions the graph holds open.

Do not include long quotes. The orientation is the compressed reference the agent uses for the rest of the session; treat it as a card, not a transcript.

### Step 8: Name what was skipped

End the report by naming what this skill deliberately did not read:

- Decision bodies (Whys, Alternatives, What Would Change It) — load these per-Decision when the agent needs them.
- Observation grounds and Pattern hearts — load these when an operation lands on a specific Observation or Pattern.
- Reference bodies — load when the agent cites a Reference.
- Existing Skill bodies — load when the agent invokes a sibling skill or needs to compose with one.

The skipped surfaces are not unimportant; they are load-on-demand. Naming them sets the agent up to fetch them later without re-running Graph Orient.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements. Along with Node Read and Node Create, it forms the first-session triad a scion author walks through before touching the graph.

- grounded_in::[[Decisions/Adopt Layered Node Structure]]↗
  - The layered-structure Decision is what makes this skill possible. Reading identity blocks and opening paragraphs across many nodes is cheap precisely because those layers are authored to be cheap; a graph without layered structure would force the agent to read full bodies to orient.

- grounded_in::[[Patterns/Progressive Summary Before Substance]]↗
  - The Pattern this skill realizes at graph scale. Node Read walks the cost-graded layers within one node; Graph Orient walks the cost-graded nodes within the graph. Both realize the same progressive-disclosure stance, at different scales.

- informs_downstream::[[Markdown Node Contract]]
  - This skill depends on the base Contract being honored across the graph. If a node lacks an identity predicate block, the orientation sweep misses it; the skill's output quality is a function of the graph's compliance with the base Contract.

- composes_with::[[Node Read]]
  - Node Read is how the agent drills into a specific node after orientation flagged it as worth reading at depth. Graph Orient names candidates; Node Read decides what they carry.

- composes_with::[[Node Create]]
  - Graph Orient produces the mental model Node Create needs. An agent drafting a new node after orientation knows which forms exist, which Convictions to potentially ground in, and which predicates are active vocabulary.
