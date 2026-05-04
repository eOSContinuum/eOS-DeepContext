---
tagline: Whose thinking is captured when different from the author
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# source_voice

A predicate declaring that the subject node's content represents the object's thinking even though the subject's `authored_by::` names someone else. The edge carries an attribution split observed in practice across plural-contributor corpora: an agent or scribe authors a document that captures another person's thinking, and both the writing-of-it and the thinking-behind-it are separately load-bearing attributions.

The edge lands in Relations alongside `authored_by::` when a node's authorship and its voice diverge. Without the split, the node's attribution is a single fused claim and the distinction — who wrote versus whose ideas — is lost.

## Carries

The predicate names an idea-origin claim that is distinct from the authorship claim. The object is the person (human or agent) whose thinking the node's content carries; the subject's `authored_by::` edge names the person who produced the words. The two may refer to the same person — in which case `source_voice::` adds nothing — but when they differ, each carries a separate kind of attribution: authorship names the producer of the artifact, source voice names the origin of the ideas.

The web of associations the predicate activates is the authorship stack under any document. A meeting note `authored_by::` a scribe who is `source_voice::` for multiple meeting participants preserves the scribal-vs-principal distinction. A document `authored_by::` an agent with `source_voice::` naming the principal whose thinking the agent captured preserves the agent-vs-principal distinction. The predicate is an acknowledgment that some nodes are doubly-authored — one author for the words, another for the ideas — and that the graph commits to keeping both visible.

## Crescent

### Against [[authored_by]]

Ghost link; `authored_by::` is in the local vocabulary but not yet seeded as a Predicate node. `authored_by::` names who wrote the words — the producer of the artifact. `source_voice::` names whose ideas are captured — the origin of the content, when distinct from the writer. The same document can carry both predicates with different referents (the agent authored; the principal thought), and the distinction is load-bearing because collapsing the two would hide either the scribal work or the intellectual work. Authorship and voice are different contributions to the same artifact.

### Against [[assists_by -- facilitation by agent or person]]

`source_voice::` names idea-origin — whose thinking is captured by the node's content. `assists_by::` names facilitation — whose shaping work supported the node's authoring without being the content's voice. The distinction is between the idea-side of a contribution (voice) and the shaping-side of a contribution (facilitation). A document with `source_voice::[[Principal]]` and `assists_by::[[Editor]]` preserves both: the principal's thinking is the content, the editor's work shaped its delivery without being its voice. Merging the two would lose the kind distinction — shaping and voicing are different contribution modes.

## Typing

- **Subject:** Any node whose content carries distinct voice-authoring pairing. Most commonly a meeting note, a summary, a transcription, or an agent-authored document preserving a principal's thinking.
- **Object:** A person (human or agent). The object MUST be a node or wikilink target that identifies a specific contributor whose thinking the subject's content represents.

## Instances

- A meeting summary `authored_by::[[Scribe]]` with `source_voice::[[Speaker]]` preserves the scribal-vs-principal authorship distinction that a single `authored_by::` edge would flatten. The scribe produced the words; the speaker's thinking is the content. Both attributions matter when a reader needs to trace either the writing or the ideas.
- An agent-authored document `authored_by::[[Agent]]` with `source_voice::[[Principal]]` preserves the agent-vs-principal distinction in agent-mediated authoring. The agent generated the text; the principal's thinking is what the text captures. Without the split, the agent appears as the idea source (inflating its authority) or the principal appears as the writer (denying the agent's work).

## Relations

- contrasts_with::[[authored_by]]
  - Ghost link; target Predicate not seeded. Idea-origin vs words-producer — different attributions that may name the same or different contributors.

- contrasts_with::[[assists_by -- facilitation by agent or person]]
  - Different contribution modes: voice is idea-origin; facilitation is shaping-during-authoring.

- grounded_in::[[Convictions/Translation Over Convergence]]↗
  - The Conviction that makes adopting this predicate load-bearing. The source-voice-vs-authorship distinction comes from an adjacent plural-contributor corpus where agent-mediated authoring made the split necessary; adopting the predicate here is translation-not-convergence at the predicate layer.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The substrate Conviction. The distinction the adjacent corpus's practice surfaced is preserved by keeping `source_voice::` as a separate predicate rather than folding it into `authored_by::`.
