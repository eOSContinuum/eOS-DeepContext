---
tagline: A typed-edge definition with Carries, Crescent-per-adjacent-predicate, and Typing sections; a specialization of Gloss for predicate names
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Gloss Form Contract]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Predicate Form Contract

A Predicate is a node that defines a typed edge-predicate used elsewhere in the graph. It carries the positive sense of the predicate — the shape of claim it makes when attached as an edge — together with the crescent distinctions that separate it from adjacent predicates and the subject-and-object typing that constrains where it may legitimately attach.

A Predicate is a specialization of Gloss: it defines a term, and that term happens to be a predicate name. It inherits Gloss's filename-carries-definition pattern and restate-and-elaborate body opening. It adds structural obligations specific to predicates — the [[Glosses/Crescent -- the distinction a predicate holds against an adjacent predicate|Crescent]]↗ section that documents what this predicate holds that its near-neighbors don't, and the Typing section that names the node shapes it connects.

The Predicate Form exists because the project holds vocabulary diversity load-bearing: adjacent predicates are not interchangeable, and the distinctions between them are the content the graph is committed to preserving. A Predicate node is the structural home for those distinctions. The Crescent section is required — not optional — because an undocumented crescent is a silent invitation to merge the predicate into a neighbor under later convergence pressure. The term comes from a Venn-diagram picture of two adjacent predicates as overlapping circles: they share an intersection, and each holds a crescent-shaped arc outside the intersection — the `## Crescent` section carries that arc's content as prose.

## Requirements

### Inherits Gloss Form Contract

- All requirements of [[Gloss Form Contract]] apply, including the double-hyphen filename pattern, the bare-concept H1, and the restate-and-elaborate body opening.
- The requirements below are additions or refinements for Predicate nodes specifically.

### Filename pattern

- The filename MUST follow `<predicate> -- <one-clause sense>.md`, inherited from Gloss.
- The concept side MUST be the predicate name without the trailing `::`. Filesystems do not reliably carry `::`, and the predicate's name as a concept (how other nodes wikilink to it) is distinct from its syntactic role as an edge marker.
- The one-clause sense SHOULD name the shape of the claim the predicate makes, not a category label. Prefer `critiques -- principled disagreement with a position` over `critiques -- a disagreement predicate`.

### Identity predicate block

- The identity block above the H1 MUST include `conforms_to::[[Predicate Form Contract]]`.
- The identity block SHOULD include `in_practice_domain::[[<Practice Domain>]]`.

### Body: Carries

Enforces [[Decisions/Require Carries Section in Predicate Nodes]]↗.

- The body MUST include a `## Carries` section stating the positive sense of the predicate — what claim it makes when attached as an edge, what stance it encodes, what web of associations it activates.
- The Carries section MUST be written positively, not comparatively. Comparative content belongs in Crescent.
- Two to four sentences is typical. A Predicate load-bearing enough to earn its own node can usually sustain a longer Carries paragraph.

### Body: Crescent

Enforces [[Decisions/Document Predicate Crescents Against Adjacent Predicates]]↗.

- The body MUST include a `## Crescent` section when the Predicate declares one or more `contrasts_with::` edges.
- Each adjacent predicate MUST have its own H3 subsection headed `### Against [[adjacent predicate -- sense]]` using the adjacent Predicate node's full filename as the wikilink target. The bare full filename is the permitted form here per [[Markdown Node Contract]]'s refinement for structural contexts; the ` -- sense` suffix carries the adjacent predicate's working definition to the reader at the heading. The bare concept form `[[adjacent predicate]]` MUST NOT be used because it does not resolve in standard wiki tooling.
- Each Crescent subsection MUST state what this predicate carries that the adjacent one does not — the distinction that would be destroyed by merging them.
- The Crescent content on two adjacent Predicate nodes is NOT required to be symmetric. `critiques -- ...`'s crescent against `challenges` names what `critiques` holds; `challenges -- ...`'s crescent against `critiques` names what `challenges` holds. Each node carries its own account; the two accounts together are the full pairing.
- A Predicate with no declared `contrasts_with::` edges MAY omit the Crescent section, but SHOULD include a sentence in the Carries section noting that no adjacent predicate has yet emerged.

### Body: Typing

- The body MUST include a `## Typing` section that names the subject and object shape the predicate expects.
- The subject is the node attaching the edge; the object is the wikilink target.
- Either side MAY be polymorphic — if so, state the polymorphism explicitly rather than leaving it undefined.
- If the predicate expects a specific node form (e.g., "the object MUST be a [[Contract Form Contract|Contract]]"), state it here.

### Body: Instances (Optional)

- An `## Instances` section MAY list concrete uses of the predicate in the graph, to ground the Carries and Crescent sections in real edges.
- Each instance SHOULD name the subject node, the object node, and a one-clause gloss of what the edge claims in that context.

### Relations section

- A Predicate MUST include `contrasts_with::[[Adjacent Predicate]]` for every adjacent predicate whose Crescent it documents. The `contrasts_with::` edge is the pairing; the Crescent section is the content. Together they make the near-neighbor relationship structurally visible.
- A Predicate MAY include `composes_with::[[Related Predicate]]` when two predicates are routinely used alongside each other.
- A Predicate SHOULD include `grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗` when its Crescent section is a direct instance of the conviction that vocabulary diversity is load-bearing.

### Vocabulary registration

- A Predicate node's existence IS the project's structural registration of a predicate in the local vocabulary. The graph holds its vocabulary in the Predicate nodes themselves rather than in a separate registry file.
- A predicate used in the graph without a corresponding Predicate node is a drift signal — the vocabulary is accreting without its distinctions being documented.

## Relations

- extends_contract::[[Gloss Form Contract]]
  - Inherits the double-hyphen filename pattern and the restate-and-elaborate body opening; adds the required Carries, Crescent, and Typing sections and the `contrasts_with::` edge for every documented crescent.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- grounded_in::[[Convictions/Vocabulary Diversity Is a Feature]]↗
  - The conviction this contract realizes. The Crescent section is the structural home for the distinctions that conviction holds load-bearing, and the required `contrasts_with::` pairing is what keeps adjacent predicates from being silently merged.

- grounded_in::[[Decisions/Document Predicate Crescents Against Adjacent Predicates]]↗
  - Grounds the Crescent-per-neighbor Requirement.

- grounded_in::[[Decisions/Require Carries Section in Predicate Nodes]]↗
  - Grounds the Carries Requirement and its positive-not-comparative framing.

- contrasts_with::[[Gloss Form Contract]]
  - A Gloss defines any term; a Predicate defines a term used as a typed edge and therefore carries subject-object typing and per-neighbor crescents. A Predicate is a Gloss with stricter body obligations and required adjacency relations.

- informed_by::[[Glosses/Crescent -- the distinction a predicate holds against an adjacent predicate|Crescent]]↗
  - The Gloss that carries the Venn-non-overlap metaphor underwriting the `## Crescent` section's shape. The per-neighbor H3 structure and the asymmetry of crescents across adjacent nodes both follow from the geometric picture.
