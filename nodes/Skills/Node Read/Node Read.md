---
runtime_name: node-read
tagline: Reads a node progressively by layer (identity, H1, opening, Relations), letting an agent spend a finite context budget on the layer its task needs
description: |
  Reads a single node using progressive disclosure: identity predicate block, H1, opening card-scale prose, and annotated Relations section first; the full elaboration body is loaded only when the cheaper layers do not satisfy the agent's reason for reading. Lets an agent spend a finite context budget deliberately on the layers most worth reading.

  WHEN: the user asks the agent to read a node, open a node, summarize a node at card scale, orient to a node before editing, or report what a node says; the agent is about to follow an edge and needs to read the target; the agent is building context across multiple nodes and reading each in full would exceed the context budget.

  WHEN NOT: editing the node (read directly with the Read tool; this skill is for orientation, not modification); building multi-hop research across many nodes (use Node Research once it exists; for now, invoke Node Read per node in the traversal); the agent needs to read the full body for verbatim citation or validation.
---

- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Node Read

Reads a single node in cost-graded layers so the agent spends context budget deliberately. The node graph is authored to be read this way: the identity predicate block above the H1 is cheap and structural, the H1 and opening prose carry the node's claim at card scale, the Relations section with its indented annotations names the edges worth following and why, and only the elaboration body carries the full reasoning at full cost. Reading from cheap to expensive lets the agent stop early when the cheaper layers already answer the question.

An agent invokes this skill when it has a reason to read a node but does not yet know whether the full body is worth the cost. The skill's output is a compressed representation of what the node carries, not a verbatim dump — the agent reports what the layers revealed and names which edges were most worth following.

## Steps

### Step 1: Load the node

Read the node file with the Read tool. The file may be:

- A single-file node at `nodes/<Taxonomy>/<Name>.md`.
- A compound-node lead at `nodes/<Taxonomy>/<Name>/<Name>.md`.
- A Skill lead at `nodes/Skills/<Folder>/<Folder>.md` (same shape as any compound node).

If the target is a folder rather than a file, the lead file matches the folder name — read `<Folder>/<Folder>.md`.

### Step 2: Read the identity predicate block

The identity block is the bullet list above the H1. It carries the node's form (`conforms_to::`), its lifecycle (`has_lifecycle::`), curation state (`has_curation::`), domain (`in_practice_domain::`), authorship (`authored_by::`), and any form-specific identity predicates the form owns (`has_commitment::` and `decided_on::` for Decisions, `has_epistemic_status::` for Observations, `serves_as::` for References).

From the identity block alone, the agent already knows:

- What kind of node this is, and therefore what body shape to expect.
- How mature and settled it is (Seed vs Evergreen; Working Draft vs Canonical).
- Which domain it belongs to.
- For Decisions: whether the commitment is Provisional or Firm, and when it was made.
- For Observations: the epistemic status that must match the Grounds section.

Report the identity block's content as the first layer of the reading.

### Step 3: Read the H1 and opening

Read the H1 (the concept name) and the prose between the H1 and the first H2 subsection — the card-scale claim layer per `Adopt Layered Node Structure` and `Progressive Summary Before Substance`.

The opening states the node's claim. For Decisions it names the commitment; for Convictions it states the held stance; for Observations it names the claim and its epistemic status; for Glosses it restates and elaborates the filename definition; for Predicates it opens the positive sense of the edge; for Patterns it opens the Heart.

After Step 3, the agent has a card-scale understanding of what the node carries. If that is enough for the agent's purpose, stop here — the expensive body layer is not needed.

### Step 4: Read the Relations section

Scroll to `## Relations` and read the edges with their indented annotations. Each annotation is the author's statement of why the edge matters — what a reader should expect to find if they follow it.

Use the Relations section to answer two questions:

- What does this node ground in, inform, contrast with, compose with? These are the node's outgoing structural commitments.
- Which edges are worth following next? The annotations say what the target carries; the agent decides per edge whether the target is worth the reading cost.

Report the Relations edges and their annotations as the third layer of the reading.

### Step 5: Decide whether to read the body

Stop at Step 4 when the identity block, opening, and Relations together satisfy the reason for reading. Examples where stopping is appropriate:

- The agent is building context across many nodes and needs only the card-scale claim of each.
- The agent is choosing which edge to follow and the annotations already name the distinction.
- The node's claim is stable enough and old enough (Evergreen / Canonical) that the body is unlikely to carry surprises.

Proceed to Step 6 when the cheaper layers are insufficient. Examples where the body is needed:

- The agent needs a specific Why, Alternative, or Grounds paragraph verbatim.
- The card-scale claim is ambiguous or the agent expects the body carries a distinction the opening did not name.
- The agent is about to edit the node and needs the full context to change it coherently.

Name which condition triggered the body read; stopping decisions and continuation decisions are both data the user benefits from hearing.

### Step 6: Read the body

Read the elaboration body — the H2 and H3 subsections between the opening and `## Relations`. Each form has its own body sections:

- `Decision` — Why, Alternatives Considered, Consequences, What Would Change It.
- `Conviction` — Why It Is Held, Drift Recognition.
- `Observation` — Grounds, What Would Revise It.
- `Pattern` — Heart, Forces, Moves.
- `Predicate` — Carries, Crescent (per adjacent predicate), Typing, Instances.
- `Contract` — Requirements (with RFC 2119 keywords), per-Requirement body.
- `Reference` — Adopted, Not adopted (yet), Key moves.
- `Gloss` — restate-and-elaborate opening, elaboration paragraphs, optional distinguishing paragraph.
- `Aspiration` — Gap, Work, Progress Recognition.
- `Skill` — opening, Steps, Scripts (when present).

Report the sections that carry the content the agent needs. Do not report the full body when a subset answers the question — the agent's job is to translate the body's reasoning into what the user needs to hear, not to relay it verbatim.

### Step 7: Report in layer order

When reporting to the user, order the output from cheapest layer to most expensive: identity block → H1 and opening → Relations → body excerpts (only if loaded). Name which edges are most worth following next, quoting each annotation. The layered report lets the user follow the same cost-graded path the skill followed and decide independently whether to drill further.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill is itself a Skill node and declares compliance with the Skill Form Contract's Requirements — YAML frontmatter carrying `runtime_name` and Anthropic `description`, compound-node layout, numbered Steps, Relations grounded in the Decisions the skill realizes.

- grounded_in::[[Decisions/Adopt Layered Node Structure]]↗
  - The Decision this skill realizes on the reading side. The layered structure Requirement specifies the cost-graded arrangement from identity block through Relations; this skill is the agent-side discipline that reads the layers in order and stops when cheaper layers suffice.

- grounded_in::[[Patterns/Progressive Summary Before Substance]]↗
  - The Pattern that names the move the opening paragraph makes. Step 3's card-scale reading depends on authors having realized this Pattern; Step 5's stop-early decision is justified when they have.

- informs_downstream::[[Markdown Node Contract]]
  - The base Contract specifies the structural shape this skill reads. The Contract states the standing structural rule; the skill carries the reading workflow that uses it.

- composes_with::[[Node Create]]
  - Node Create is the write-side companion: when the author wants to model a new node on an existing neighbor, Node Read orients them to the neighbor first; Node Create drafts the new node. Both skills walk the same layered structure, in opposite directions.
