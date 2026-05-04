---
tagline: A thesis-driven investigation node carrying a research question, current state, and open questions, with predicate vocabulary deferred to practice
created: 2026-04-25
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Christopher Allen]]
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Inquiry Form Contract

An Inquiry is a node that captures a thesis-driven investigation — a research question the graph is working on, the current state of evidence, and the open questions that still need answering. Its core question is "What should we think about X, and how would we find out?" An Inquiry differs from an Observation (which carries an empirically-grounded claim), from a Decision (which records a committed choice), and from an Aspiration (which states a directional target). An Inquiry holds the question open. When the question resolves, the Inquiry produces one of the other forms and links to it.

The Inquiry Form Contract is drafted speculatively, ahead of any Inquiry nodes existing, because the workstream's research phases (#R-1 through #R-3) generate questions the existing form palette has no clean home for. The cloud-server license question — "is `dworkin/cloud-server` AGPL-3 or not?" — is a representative example: a question that lived without a node, was resolved by direct verification of the LICENSE file, and produced a downstream cascade of corrections. Authoring the Contract before the first Inquiry node lets subsequent Inquiries land into a structural home rather than as ad-hoc prose. The lifecycle marker `has_lifecycle::[[Glosses/Seed Stage]]↗` reflects that no Inquiry node has yet exercised this Contract; advancement to Growth Stage waits on three or more Inquiries running through the form and the predicate vocabulary settling out of practice.

This Contract is intentionally sparse on predicate vocabulary. The obsidian-pkm precursor (`Inquiry Form` in `~/Workspace/obsidian-pkm/garden/forms/`) carries `directed_at::`, `extracted_from::`, and several relational predicates. None are required here. The predicate set is deferred to the first Inquiry nodes — they propose the vocabulary that practice actually demands, and the Contract is revised once two or three Inquiries want the same predicate.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- Inquiries are Markdown Nodes; the requirements below are additions for the Inquiry form specifically.

### Filename pattern

- The filename MUST be `<Scope of Investigation> <What is Being Determined>.md` — naming heuristic: the scope of the question plus what the Inquiry is trying to determine. Examples (illustrative, not yet authored): `Cloud Server License Posture.md`, `Foundation Layer Tradeoff Analysis.md`, `Wiztool Adoption Boundary.md`.
- The filename MUST NOT carry a `<Concept> -- <definition>` suffix; that pattern is reserved to Glosses per [[Gloss Form Contract]].
- The filename MUST NOT carry a `(<Author>, <Year>)` parenthetical; that pattern is reserved to References per [[Reference Form Contract]].

### Identity predicate block

- The body MUST begin with a bullet list of identity predicates before the H1 per [[Markdown Node Contract]].
- This block MUST include `conforms_to::[[Inquiry Form Contract]]`.
- This block SHOULD include `in_domain::[[<Domain>]]`.
- This block MAY include `has_lifecycle::`, `has_curation::`, and `authored_by::` per the base contract.
- This block MUST NOT include `has_commitment::` or `decided_on::`; an Inquiry is not a Decision and MUST NOT carry Decision-form predicates.
- This block MUST NOT include `has_epistemic_status::`; an Inquiry is not an Observation and MUST NOT carry Observation-form predicates.

### H1

- The file MUST contain exactly one H1.
- The H1 MUST match the filename minus `.md`.

### Body: Research Question

- The body between the H1 and the next H2 MUST state the research question the Inquiry is investigating.
- The Research Question MUST be specific enough to recognize a resolution. Vague wonderings fail this requirement; "is cloud-server AGPL-3 or some other license?" passes; "what about cloud-server?" does not.
- The Research Question MAY appear under a labeled `## Research Question` heading, or as the opening prose under the H1 if a single paragraph suffices. Headed form is preferred when other body sections follow.

### Body: Current State

- The body MUST include a section headed `## Current State` (or equivalent — `## What is Known`, `## State of Evidence`).
- The Current State section MUST summarize what is known, what hypotheses exist, and what evidence has been gathered so far.
- When the Current State is "nothing yet beyond the question itself," the section MUST say so explicitly rather than be omitted.

### Body: Open Questions

- The body MUST include a section headed `## Open Questions`.
- The Open Questions section MUST enumerate specific, answerable sub-questions whose resolution would advance the Inquiry. Each sub-question MUST be answerable in principle, not a re-statement of the top-level Research Question.
- An Inquiry with zero open questions has resolved; the resolution MUST be captured per the Resolution Requirement below, and the Open Questions section MUST say "All resolved; see Resolution."

### Body: Resolution

- The body MAY include a section headed `## Resolution` capturing what the Inquiry produced when resolved.
- When present, the Resolution section MUST name the resolving node(s) — typically an Observation, Decision, or Aspiration — and SHOULD include a `resolved_into::[[Target Node]]` edge in the Relations section pointing to each resolving node.
- An Inquiry MAY remain open indefinitely; absence of a Resolution section is permitted and signals an active research thread.

### Body: Sources

- The body MAY include a section headed `## Sources` listing References, gists, papers, repositories, or other authoritative material the Inquiry draws on.
- When the evidence is captured via `grounded_in::[[Reference Node]]` edges in the Relations section, a separate Sources section MAY be omitted.
- Inline URLs in Sources MUST follow [[Reference Form Contract]]'s URL preservation and URL resolvability Requirements: links to artifacts that pass the URL resolvability test (resolvable to readers other than the author) and warrant their own node SHOULD be promoted to Reference nodes rather than left as inline URLs. Non-public-path citations (sibling-project local paths, private cloud-storage URLs, internal-only intranet addresses) MUST stay as inline citations in this Sources subsection rather than being promoted to Reference nodes; they are descriptive provenance, not graph-level targets.

### Predicate vocabulary

- This Contract introduces no required form-specific predicates beyond `conforms_to::[[Inquiry Form Contract]]`.
- The predicate vocabulary for Inquiry nodes is provisional. The first two or three Inquiry nodes authored against this Contract are expected to propose predicates via `/predicate-propose` (see [[Predicate Propose]]). Likely candidates include `directed_at::[[Person]]` (for questions requiring a specific human's judgment, mirroring the obsidian-pkm Inquiry Form's marker), `bound_to_workstream::[[Workstream]]` (binding the Inquiry to its owning workstream), and `resolved_into::[[Target Node]]` (capturing the resolution target).
- When two or three Inquiry nodes want the same predicate, this Contract MUST be revised to either require it (MUST), recommend it (SHOULD), or permit it (MAY) explicitly. Until that revision lands, predicates remain ad-hoc and cite-by-name.

### YAML frontmatter

- The lead file SHOULD carry YAML frontmatter including `tagline` as a one-line summary of the Inquiry's question and scope.
- Optional scalar keys follow [[Markdown Node Contract]]: `created`, `brief_summary`.
- YAML MUST NOT carry named-edge predicates per the base contract.

### Relations section

- The Relations section follows [[Markdown Node Contract]].
- An Inquiry SHOULD declare `grounded_in::[[Reference]]` edges for evidence the Current State or Open Questions cite.
- An Inquiry MAY declare `resolved_into::[[Target Node]]` for each resolving node when the Inquiry has resolved.
- An Inquiry MAY declare `bound_to_workstream::[[Workstream Name]]` to mark the workstream that owns progress on the Inquiry. The eos-harness graph does not yet have first-class Workstream nodes; until it does, this edge is a ghost link to a future node and the wikilink target SHOULD match the workstream's directory-relative name (e.g., `feature/mva-foundation-bootstrap`).

## Relations

- extends_contract::[[Markdown Node Contract]]
  - An Inquiry is a Markdown Node with additional structural obligations: a stated Research Question, a Current State summary, and an enumerated Open Questions section. The base contract's file form, identity predicate block, and Relations section all apply.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like (filename, self-conformance, parseable Requirements section with RFC 2119 keywords, prose body before Requirements).

- contrasts_with::[[Observation Form Contract]]
  - An Observation carries an empirically-grounded claim with a matched epistemic status; an Inquiry carries an open question that may resolve into an Observation but is not itself one. The distinction is load-bearing: writing as an Observation a claim that has not been verified collapses the inquiry stage and produces false authority.

- contrasts_with::[[Decision Form Contract]]
  - A Decision records a committed choice with `decided_on::` and `has_commitment::`; an Inquiry holds open the question whose answer would inform the choice. The same situation may move from Inquiry to Decision over time, with the Inquiry's `resolved_into::` edge pointing at the Decision.

- contrasts_with::[[Aspiration Form Contract]]
  - An Aspiration states a directional target the project is working toward; an Inquiry asks whether and how a target should be set. An Inquiry whose resolution clarifies that a target is appropriate produces an Aspiration via `resolved_into::`.

- contends_with::[[Glosses/Convention Overhead vs Graph Quality]]↗
  - Introducing a Contract ahead of two or three conforming nodes raises the bar speculatively. Authoring the first Inquiry node into this Contract is expected to surface revisions; the predicate-vocabulary section names that expectation explicitly. The Skill Form Contract's Seed-to-Growth progression is the precedent for this move.
