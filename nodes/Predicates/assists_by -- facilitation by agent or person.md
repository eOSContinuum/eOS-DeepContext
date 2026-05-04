---
tagline: Facilitation by agent or person
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# assists_by

A predicate declaring that the object provided facilitative work on the subject node — editorial support, mediation, scaffolding, or substantive review that shaped the node without being its voice. The edge carries a contribution mode that `authored_by::` flattens and `source_voice::` does not cover: neither writing the words nor originating the ideas, but shaping what the words or ideas became.

The edge lands in Relations when facilitation is a load-bearing part of a node's history — an editor who shaped a document, an agent who scaffolded a draft, a reviewer whose substantive feedback changed the shape of the content. Facilitation differs from authorship in that the facilitator is not the producer, and differs from voice in that the facilitator is not the idea origin.

## Carries

The predicate names a facilitation contribution: shaping work that falls short of authorship, where the object supported the subject's authoring without being the voice. Facilitation can take many shapes — editorial support, mediation between contributors, scaffolding that structured the draft, substantive review that altered the content — and the predicate abstracts over these while preserving the core claim that the object's work mattered to the node's final shape.

The web of associations the predicate activates is the contribution-mode stack under a node. A document `authored_by::[[Writer]]` with `assists_by::[[Editor]]` preserves the writer-editor distinction; `authored_by::[[Agent]]` with `source_voice::[[Principal]]` and `assists_by::[[Facilitator]]` preserves three distinct contribution modes on one node. Leaving facilitation unnamed — folding it into `authored_by::` as co-authorship, or into `source_voice::` as co-voice — loses the distinction that the project holds load-bearing: authorship, voice, and facilitation are different kinds of contribution.

## Crescent

### Against [[authored_by]]

Ghost link; `authored_by::` is in the local vocabulary but not yet seeded as a Predicate node. `authored_by::` names authorship — who produced the node's words. `assists_by::` names facilitation — whose shaping work supported the authoring without being the producer. A node with `authored_by::[[Writer]]` and `assists_by::[[Editor]]` carries both contributions on one artifact: the writer produced, the editor facilitated. The distinction matters because a node can carry multiple `authored_by::` edges for co-authored work — that is not the same as having one author and one facilitator. Co-authorship and facilitation are different kinds of contribution.

### Against [[source_voice -- whose thinking is captured when different from the author]]

`source_voice::` names idea-origin: whose thinking is captured by the node's content. `assists_by::` names shaping-during-authoring: whose work supported the authoring without being the content's voice. The distinction matters when all three modes are present on one node — a principal's thinking (source_voice), an agent's writing (authored_by), and an editor's shaping (assists_by) are separately load-bearing contributions, and collapsing any two loses the specific kind distinction.

## Typing

- **Subject:** Any node where facilitation happened as part of its authoring history.
- **Object:** A person (human or agent) whose facilitative work shaped the subject.

## Instances

- A proposal `authored_by::[[Writer]]` with `assists_by::[[Reviewer]]` preserves the writing-vs-review distinction when the reviewer's substantive feedback changed the shape of the proposal. Without the predicate, the reviewer's contribution is invisible on the final artifact, or must be inflated to co-authorship.
- An agent-authored draft `authored_by::[[Agent]]` with `source_voice::[[Principal]]` and `assists_by::[[Editor]]` preserves three contribution modes on one node — the agent wrote, the principal thought, the editor shaped. Removing any one of the three edges loses a distinct kind of work.

## Relations

- contrasts_with::[[authored_by]]
  - Ghost link; target Predicate not seeded. Facilitation vs authorship — different contribution modes on the same artifact.

- contrasts_with::[[source_voice -- whose thinking is captured when different from the author]]
  - Shaping-during-authoring vs idea-origin. Different relationships to the node's content.

- grounded_in::[[Convictions/Translation Over Convergence]]↗
  - The Conviction that makes adopting this predicate load-bearing. The facilitation-vs-authorship-vs-voice distinction is observed in adjacent plural-contributor corpora; adopting it here is translation-not-convergence at the predicate layer.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The substrate Conviction. Contribution-mode distinctions are the kind of vocabulary diversity the project commits to preserving; folding facilitation into authorship or voice would flatten what the practice kept distinct.
