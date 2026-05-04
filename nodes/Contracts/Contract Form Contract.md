---
tagline: The meta-contract: how a Contract node in this project is named, structured, declares inheritance, and conforms to itself
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Contract Form Contract

The meta-contract. It specifies what a Contract node in this project looks like: how it is named, how its requirements are structured so a validator can read them, how inheritance between contracts is declared, and how a contract conforms to itself.

A Contract describes structural obligations on nodes that claim conformance. A node's `conforms_to::[[X Form Contract]]` predicate is the public assertion that it satisfies the requirements named in X. A build-time or curation-time validator can read the Requirements section of a contract and check conforming nodes against it.

The Contract Form Contract's self-conformance — its own `conforms_to::[[Contract Form Contract]]` edge — is a structural bootstrap invariant, not a revisitable commitment. Exempting the meta-contract from conformance would create a privileged one-off that undermines the form system's universality; the only other move is an infinite meta-meta regress. Self-conformance is what makes the form system internally consistent, and it does not admit viable alternatives. The Self-conformance Requirement below states the rule; no grounding Decision is needed because no choice with alternatives is being made.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- Contracts are Markdown Nodes; the requirements below are additions for the Contract form specifically.

### Filename pattern

- The filename MUST end with ` Contract.md`.
- The preferred form is `<Concept> Form Contract.md` (e.g., `Gloss Form Contract.md`, `Reference Form Contract.md`).
- `<Concept> Contract.md` is permitted when "Form" would be awkward (e.g., `Markdown Node Contract.md` — the node is not a form).
- The filename MUST NOT carry a definition in the `<Concept> -- <definition>` pattern; contracts are self-describing through their Requirements section.

### Self-conformance

- Every Contract MUST include `conforms_to::[[Contract Form Contract]]` in its identity predicate block.
- Contract Form Contract itself declares `conforms_to::[[Contract Form Contract]]` — the meta-contract is self-conforming.

### Inheritance

- A Contract that specializes another Contract MUST declare `extends_contract::[[Parent Contract]]` in its identity predicate block.
- When a Contract extends a parent, it MUST NOT silently override parent requirements. It MAY add requirements, and it MAY refine a parent requirement by naming it and stating the refinement.
- A conforming node satisfies the parent contract's requirements AND the child contract's requirements.

### Requirements section

Enforces [[Decisions/Use RFC 2119 Keywords in Contract Requirements]]↗.

- The body MUST contain a top-level section headed `## Requirements`.
- Each requirement MUST be a subsection headed `### <short name>` — a human-readable phrase, not a numeric identifier.
- The body of each requirement MUST use RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) to state the obligation.
- When the order of requirements carries meaning (e.g., the order in which sections appear in a conforming file), that ordering SHOULD be stated in prose rather than encoded in heading numbers.

### Body precedes Requirements

Enforces [[Decisions/Require Explanatory Prose Before Contract Requirements]]↗.

- A Contract MUST include prose body between the H1 and the `## Requirements` section that explains the purpose of the contract and when it is used.
- The prose body MUST NOT restate the Requirements normatively; it provides orientation, not a second source of truth.

### YAML frontmatter

- A Contract's lead file SHOULD carry YAML frontmatter including `tagline` as a one-line summary of the form the Contract specifies. The Contracts taxonomy index page surfaces each Contract's tagline as the row summary for readers browsing the list of forms; without it, the index row is silent — the Contract appears as a bare wikilink with no orientation to what shape the form carries. Contracts are the forms readers reach for when orienting to the graph, and a silent row at the orientation surface defeats the purpose of the index.
- Optional scalar keys follow `Markdown Node Contract`: `created`, `brief_summary`.
- YAML MUST NOT carry named-edge predicates per the base contract.

### Relations

- A Contract MAY declare `extended_by::[[Child Contract]]` for each known child, so the inheritance graph is traversable in both directions. This edge is added as children come into existence and is not required ahead of them.
- A Contract MAY declare `contrasts_with::[[Sibling Contract]]` to clarify the boundary with peer contracts.

### Vocabulary introduction

- A Contract MAY introduce new local predicates as part of its requirements.
- When it does, the new predicate MUST be named and defined within the Requirements section, and SHOULD be seeded as a Predicate node in `nodes/Predicates/` to register it in the local vocabulary.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - A Contract is a Markdown Node with additional structural obligations — notably the parseable `## Requirements` section and the inheritance pattern.

- grounded_in::[[References/Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]↗
  - The underlying convention that makes `conforms_to::[[X]]` a first-class classification edge rather than a tag.

- grounded_in::[[Decisions/Use RFC 2119 Keywords in Contract Requirements]]↗
  - Grounds the RFC 2119 keyword requirement in the Requirements section Requirement.

- grounded_in::[[Decisions/Require Explanatory Prose Before Contract Requirements]]↗
  - Grounds the prose-before-Requirements rule in the Body precedes Requirements Requirement.

- contends_with::[[Glosses/Convention Overhead vs Graph Quality]]↗
  - Every contract added raises the bar for contribution. Contracts SHOULD be introduced only when two or three concrete nodes already want the same shape.
