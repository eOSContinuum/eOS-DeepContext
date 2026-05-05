---
name: predicate-propose
tagline: Gates additions to the local predicate vocabulary; each new predicate arrives as a proposal with Carries, Crescent per neighbor, and Typing, not as drift discovered after the fact
description: |
  Gates the addition of a new predicate to the graph's vocabulary. When an author wants to introduce a predicate that does not yet have a backing Predicate node, this skill walks the proposal: establish the axis the predicate answers, check existing vocabulary for fit, identify near-neighbors, draft a Predicate node (Carries / Crescent per neighbor / Typing), and validate against Predicate Form Contract before committing. Prevents silent vocabulary accretion — each new predicate arrives as a proposal the community can accept or refuse, not as drift discovered after the fact.

  WHEN: the user wants to introduce a new predicate; Node Create's Step 7 hits a relation the existing vocabulary does not cleanly express; Graph Audit flags a provisional predicate (in use without a backing Predicate node) as a candidate for codification; the user says "propose a predicate", "add this predicate to the vocabulary", "define X as a new edge type", or "write a Predicate for X".

  WHEN NOT: the relation can be expressed by an existing predicate with a backing node (use the existing predicate — inventing a synonym is the primary mechanism of vocabulary drift); the predicate is form-specific and already reserved by a form Contract (e.g., `has_commitment` is a Decision-form predicate governed by the Decision Form Contract; its values are Glosses, authored via Node Create, not new Predicate nodes); the author is consolidating two provisional predicates into one (that is content editing, not predicate proposal); the predicate is a scalar-valued one a form Contract should introduce (use Markdown Node Contract's scalar-predicate Requirement and the relevant form Contract).
---

- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Predicate Propose

Authors a new Predicate node that codifies a proposed addition to the graph's predicate vocabulary. A predicate used without a backing Predicate node is provisional drift — the author introduced it, but the community has not yet seen the distinctions it carries, the near-neighbors it contrasts with, or the node shapes it connects. This skill is the gate between provisional use and codified vocabulary: walking it produces a Predicate node conforming to `Predicate Form Contract`, which the project can accept into the vocabulary or refuse after review.

The skill is deliberate, not mechanical. `Terms Become Common Through Unanimity, Not Precedent` asks that a term become shared only when the community agrees to it; an agent silently introducing a predicate across several nodes is exactly the failure mode this Conviction guards against. Predicate Propose is slower than silent usage, and the slowness is the point. Each predicate earns its place by having its Carries stated positively, its Crescent drawn against its near-neighbors, its Typing declared, and its contrasts_with edges pointing at the adjacent vocabulary the new predicate does not cover.

## Steps

### Step 1: Establish the axis the predicate answers

Ask the author: what single question is this predicate the answer to? A predicate that answers "how does this relate" is too broad and will fail predicate atomicity. A predicate that answers "is this source-side provenance or dependent-side provenance for a bidirectional substrate edge" is precise.

Name the axis explicitly before drafting. The axis is what `## Carries` will articulate; vague axes produce vague Carries sections. If the author cannot state the axis in one sentence, the predicate is not yet ready to propose — the underlying distinction needs more clarity first.

### Step 2: Check existing vocabulary

Survey the existing predicates: read each Predicate node under `nodes/Predicates/` at identity-block-plus-Carries scale per `Node Read`. For each, ask whether the axis the author named is already covered.

If an existing predicate already covers the axis with a distinction the author can live with, stop — use the existing predicate rather than inventing a synonym. Synonym predicates are the primary mechanism of vocabulary drift per `No Generic relates_to Predicate`'s rationale.

If the axis is close to an existing predicate but carries a distinction the existing predicate does not, continue to Step 3. The new predicate's Crescent against that existing one will carry the distinction explicitly.

Also check the base-contract predicates — `conforms_to`, `authored_by`, `has_lifecycle`, `has_curation`, `has_commitment`, `decided_on`, `has_epistemic_status`, `serves_as`, `extends_contract`, `extended_by` — introduced by Contracts rather than Predicate nodes. A new predicate that duplicates a base-contract predicate's axis should not be proposed as a Predicate node; the form Contract that reserves that predicate is the authority.

### Step 3: Identify near-neighbors

List the predicates whose axis is adjacent to the proposed predicate's axis. A near-neighbor is a predicate whose territory overlaps with the new predicate's territory enough that a reader could plausibly use either — and whose Crescent against the new predicate carries a load-bearing distinction.

For each near-neighbor, name what the proposed predicate carries that the neighbor does not. This will become the `### Against [[neighbor -- sense]]` H3 subsection in the Crescent. If the author cannot name the distinction, the adjacency is not real or the new predicate is actually a synonym — return to Step 2.

A predicate with no near-neighbors is permitted but should carry a sentence in its Carries section noting that no adjacent predicate has yet emerged, per `Predicate Form Contract`'s Crescent Requirement.

### Step 4: Draft the Predicate node

Invoke Node Create with form=Predicate. The filename is `<predicate> -- <one-clause sense>.md`; the concept side is the predicate name without the trailing `::`.

The body requires:
- **`## Carries`** — the positive sense of the predicate, what claim it makes when attached as an edge, what web of associations it activates. Positive, not comparative. Two to four sentences typical.
- **`## Crescent`** — one H3 subsection per near-neighbor, each headed `### Against [[neighbor -- sense]]` using the full-filename bare form per `Markdown Node Contract`'s structural-context refinement. Each subsection states what this predicate carries that the neighbor does not — the distinction the merge would destroy.
- **`## Typing`** — the subject and object shape. If the predicate expects a specific node form as subject or object, name it. If polymorphism is intentional, state it explicitly.
- **`## Instances`** (optional) — concrete examples of the predicate in use in the graph.
- **`## Relations`** — `contrasts_with::[[neighbor -- sense]]` per Crescent subsection (required by `Predicate Form Contract`); `composes_with::` edges for routinely-paired predicates (optional); `grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗` when the Crescent is a direct instance of that Conviction.

### Step 5: Validate against Predicate Form Contract

Invoke `/node-validate` against the draft. The walk covers:
- Filename pattern `<predicate> -- <one-clause sense>.md`.
- H1 is the bare predicate name (no `::`, no definition appended).
- Identity block includes `conforms_to::[[Predicate Form Contract]]`.
- `## Carries` present, positive, non-empty.
- `## Crescent` present with one H3 per `contrasts_with::` edge.
- Each `### Against [[neighbor -- sense]]` heading resolves to a real Predicate node (or is a ghost link marked as such).
- `## Typing` present with subject and object shapes named.
- `## Relations` pairs each Crescent subsection with a `contrasts_with::` edge.

Findings get fixed before proceeding. A Predicate node is a vocabulary commitment; shipping it non-conforming sets a precedent the next author will imitate.

### Step 6: Consider declaring the contrast on the neighbor

Per `Predicate Form Contract`, the Crescent content on two adjacent Predicate nodes is NOT required to be symmetric. The proposing node carries its own account of the distinction; the neighbor may or may not add a mirror account. Offer the author the choice:

- Leave the neighbor's Crescent as-is (asymmetric — the new predicate's Crescent against the neighbor is the only account).
- Add a `### Against [[new predicate -- sense]]` subsection to the neighbor with its own account of what the neighbor carries that the new predicate does not.

The second is usually more complete but adds authoring cost on a neighbor the author may not feel empowered to modify. If unsure, leave asymmetric; the graph tolerates it, and later contributors can add the mirror account.

### Step 7: Commit and note the vocabulary addition

Commit the new Predicate node as its own commit. The commit message names the predicate, the axis it answers, and the near-neighbors its Crescent is drawn against. The commit is the public act by which the proposal enters the graph's vocabulary.

The Predicate node's existence in `nodes/Predicates/` is the registration — this graph holds its vocabulary in the Predicate nodes themselves rather than in a separate registry file.

Note: committing is not unilateral acceptance. A Predicate node at Seed Stage / Working Draft is a proposal; subsequent use (or non-use) by the community is the actual test of whether the predicate joins the vocabulary. A Predicate node with zero edges using it after multiple sessions is a signal that the proposal did not meet a live need — demotion, revision, or removal may be appropriate.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements. Forms a vocabulary-authoring counterpart to Node Create — where Node Create covers most forms, Predicate Propose walks the specific protocol Predicate Form Contract requires for vocabulary additions.

- composes_with::[[Node Create]]
  - Step 4 invokes Node Create with form=Predicate. Node Create handles the Gloss-inheriting filename and identity-block drafting; this skill walks the Carries / Crescent / Typing protocol Node Create's form-Predicate branch would otherwise under-specify.

- composes_with::[[Node Validate]]
  - Step 5 invokes Node Validate against the draft. The inheritance chain Node Validate walks — Predicate Form Contract extends Gloss Form Contract extends Markdown Node Contract — is where the form-specific compliance checks happen.

- composes_with::[[Graph Audit]]
  - Graph Audit surfaces provisional predicates (in use without a backing Predicate node) as candidates for this skill. Running Graph Audit periodically and then invoking Predicate Propose against each provisional predicate is the cleanup path for vocabulary drift.

- grounded_in::[[Convictions/Terms Become Common Through Unanimity, Not Precedent]]↗
  - The Conviction that asks new vocabulary to arrive as proposal rather than precedent. This skill realizes that Conviction operationally: silent predicate use across multiple nodes is exactly what the Conviction guards against; walking the proposal is the alternative.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The Conviction that makes distinction-preservation load-bearing. A Crescent section is the structural home for distinctions the new predicate carries that its near-neighbors do not; this skill is the write-time workflow that produces those distinctions.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - The Decision that requires each predicate to answer one axis. Step 1's axis-naming enforces atomicity at proposal time; a predicate that cannot state its axis in one sentence fails atomicity before drafting begins.

- grounded_in::[[Decisions/No Generic relates_to Predicate]]↗
  - The Decision that prohibits catch-all predicates. Step 2's vocabulary check against existing predicates enforces this Decision by refusing to let a new predicate be proposed as a synonym when a specific predicate already exists.

- informs_downstream::[[Predicate Form Contract]]
  - The Contract this skill realizes at write time. The Contract states the standing structural rule for Predicate nodes; this skill carries the authoring workflow that satisfies the Contract deliberately rather than mechanically.
