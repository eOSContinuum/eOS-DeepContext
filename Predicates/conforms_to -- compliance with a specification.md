---
tagline: Compliance with a specification
---

- conforms_to::[[Predicate Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# conforms_to

A predicate declaring that the subject node satisfies the specification named by the object — a Form Contract or other specification node. The subject-to-specification relationship is compliance rather than identity: multiple `conforms_to::` edges may appear on one node, and the commitment the edge carries is revisable if the specification changes or the node's shape evolves.

The edge lands in the identity block above the H1 when it is declaring what the node is (e.g., `conforms_to::[[Decision Form Contract]]` on every Decision node). It may also appear in Relations when the conformance is itself a load-bearing claim about the node's relationship to a specification.

## Carries

The predicate names that the subject node satisfies the specification the object specifies, without asserting that the subject *is* the specification. Compliance is pluralizable — the same node may carry multiple `conforms_to::` edges, each naming a different specification the node satisfies simultaneously. Compliance is also revisable: the claim is that the node's current shape matches the specification's current Requirements, not that the node's identity is fused with the specification. A node can start conforming, stop conforming, or add new conformances over time without the predicate's semantics changing — each `conforms_to::` edge is an assertion about the present state.

The web of associations the predicate activates is the Form Contract layer of the graph: when a reader sees `conforms_to::[[Decision Form Contract]]`, they know the node carries Decision-specific body sections, Decision-specific identity predicates, and Decision-specific filename shape. The compliance claim is the entry point to those Requirements.

## Crescent

### Against [[is_a]]

`is_a::` is prohibited in this graph and actively used in some adjacent vocabularies; the distinction between `is_a::` and `conforms_to::` is the reason for the prohibition and the reason for this predicate's existence. `is_a::[[X]]` asserts identity — the subject and the named type are one thing at the ontological level, and the subject cannot also be `is_a::[[Y]]` without contradiction. `conforms_to::[[X]]` names compliance with a specification, and a single node may conform to multiple specifications without contradiction because compliance is pluralizable. The distinction is load-bearing for cross-vocabulary collaboration: a node in an adjacent graph carrying both `conforms_to::[[X Form Contract]]` and `conforms_to::[[Adjacent Form Contract]]` holds both compliances without requiring either vocabulary to yield ontological authority.

### Against [[extends_contract]]

`extends_contract::` names strict inheritance between Form Contracts — a contract-to-contract relationship where the subject Contract inherits all Requirements of the object Contract. `conforms_to::` is a different layer: it is an instance-to-specification relationship where the subject is any node (Decision, Conviction, Reference, Gloss, and so on) and the object is a Form Contract the node complies with. The two predicates operate at different tiers of the form hierarchy — `extends_contract::` describes the shape of Contracts relative to each other; `conforms_to::` describes the shape of nodes relative to Contracts.

## Typing

- **Subject:** Any node with an identity predicate block. Compliance is declarable for any node form.
- **Object:** A Form Contract node or other specification node. The object MUST be a node whose purpose is to specify Requirements the subject can satisfy.

## Instances

- `prototype/nodes/Decisions/Adopt Node Atomicity.md` carries `conforms_to::[[Decision Form Contract]]` — the Decision node declares compliance with the Decision Form Contract's Requirements.
- `prototype/nodes/Contracts/Gloss Form Contract.md` carries `conforms_to::[[Contract Form Contract]]` — the Gloss Form Contract is itself a Contract, so it conforms to the meta-contract specifying what Contract nodes look like. A single node (the Gloss Form Contract) holds two relationships to the Contract Form Contract: it conforms to it (via this predicate) and extends Markdown Node Contract (via `extends_contract::`). The coexistence of both edges on one node demonstrates the pluralizability the predicate carries.

## Relations

- contrasts_with::[[is_a]]
  - Ghost link; `is_a::` is prohibited in this graph but actively used in some adjacent vocabularies. The Crescent names the distinction that makes the prohibition load-bearing: `is_a::` asserts identity and forecloses pluralized membership; `conforms_to::` names compliance and stays revisable.

- contrasts_with::[[extends_contract -- strict inheritance between form contracts]]
  - Different layers of the form hierarchy: `extends_contract::` is contract-to-contract inheritance; `conforms_to::` is instance-to-specification compliance.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes the distinction-naming in this Predicate's Crescent sections load-bearing. The `is_a::` vs `conforms_to::` distinction is one the project commits to preserving against the convergence pressure that would flatten them.
