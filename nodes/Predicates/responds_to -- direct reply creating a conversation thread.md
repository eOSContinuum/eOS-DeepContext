---
tagline: Direct reply creating a conversation thread
---

- conforms_to::[[Predicate Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗

# responds_to

A predicate declaring that the subject is a direct reply to the object, establishing a thread a reader can trace. The reply has a specific target at a specific moment — not a diffuse influence, not a generic connection, but a pointed response that the graph carries as conversation structure.

The edge lands in Relations on nodes that are themselves replies — meeting notes replying to prior notes, proposals replying to specific prompts, decision records replying to particular antecedent questions. The temporal and referential specificity is what distinguishes the predicate from broader provenance predicates.

## Carries

The predicate names a direct-reply-within-thread relationship: the subject is authored as a response to the object, and the two together form a conversation thread the reader can traverse forward from object to subject or backward from subject to object. The response has a specific referent (the subject points at *this* target, not a general context) and a short temporal distance (the subject is authored in the conversational window where the object is still live). The web of associations the predicate activates is the graph's conversation structure — the explicit threads that contributors are in with each other.

Conversation threading is itself structural content the graph commits to preserving. A Decision authored as a direct reply to an open question retains its conversational provenance when `responds_to::` points at the question; without the predicate, the reply structure collapses into generic provenance and the thread becomes unreadable.

## Crescent

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` names diffuse influence at any temporal distance, with no requirement that the subject be a reply to the object. `responds_to::` names a direct reply with specific target and short temporal distance. A node `informed_by::` a gist written years earlier is shaped by the gist across a long distance with no reply structure; a meeting note `responds_to::` a specific proposal document creates a thread with a short temporal distance and a specific referent. Both are provenance predicates, but they preserve different structures — influence preserves shape-over-time; response preserves conversation.

### Against [[relates_to]]

Ghost link; `relates_to::` is prohibited in this graph and actively used in some adjacent vocabularies. The distinction is load-bearing across vocabularies: `relates_to::` names a generic connection without direction or specificity — the subject and object are related, but the kind and direction of relation are not specified. `responds_to::` is directional and specific: the subject replies to the object, the direction is pointed, and the referent is named. Cross-vocabulary authors working in corpora that use `relates_to::` freely have sometimes surfaced the distinction in practice and adopted a separate directional-reply predicate; naming it as its own predicate is translation-not-convergence at the predicate layer.

## Typing

- **Subject:** Any node that is itself a reply — a meeting note, a response document, a decision record authored to address a specific antecedent question.
- **Object:** The specific target being replied to. The object is typically a single named node with clear referential identity.

## Instances

- A decision record authored as a direct reply to an antecedent open question carries `responds_to::[[X Open Question]]`. A reader tracing the decision's conversational origin follows the edge back to the question; a reader at the question traverses forward to see how it was addressed.
- A note written as a direct reply to a specific proposal document carries `responds_to::[[Y Proposal]]`. The reply structure preserves the pairing: the proposal and the response together are a thread, and the graph makes the thread visible rather than flattening the two into co-occurrence.

## Relations

- contrasts_with::[[informed_by -- weaker influence than grounded_in]]
  - Both are provenance predicates; they preserve different structures. Influence names shape-without-thread-structure; response names direct-reply-within-thread.

- contrasts_with::[[relates_to]]
  - Ghost link; target is prohibited in this graph and used in adjacent vocabularies. Directional-specific vs generic-undirected.

- grounded_in::[[Convictions/Translation Over Convergence]]↗
  - The Conviction that makes adopting this predicate load-bearing. The direct-reply-vs-generic-connection distinction is observed in adjacent plural-contributor corpora; adopting it here is translation-not-convergence at the predicate layer rather than folding it into existing provenance predicates.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The substrate Conviction. Conversation structure is one kind of relation; influence is another; treating them as the same predicate would flatten a distinction the graph commits to preserving.
