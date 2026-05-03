---
tagline: Strict inheritance between form contracts
---

- conforms_to::[[Predicate Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# extends_contract

A predicate declaring that the subject Form Contract inherits all Requirements of the object Form Contract — the inheritance is strict and structural, not merely naming or analogy. The subject may add Requirements or refine inherited ones, but it does not weaken or remove them. The edge places the subject Contract on a named extension chain whose root is the Markdown Node Contract.

The edge lands both in the identity block (declaring inheritance as an identity claim alongside `conforms_to::[[Contract Form Contract]]`) and in the Relations section (declaring inheritance as a typed edge with an annotation explaining what the subject adds to the parent).

## Carries

The predicate names structural inheritance between Form Contracts: the subject Contract carries every Requirement of the object Contract, applies to every node form that conforms to the object Contract, and may extend the object's specification with additional or refined Requirements. The inheritance is not nominal — the subject does not merely reference the object and pick what to borrow; the subject inherits the full set and any divergence is an explicit refinement documented in the subject Contract's own Requirements section.

The web of associations the predicate activates is the Contract hierarchy. A reader traversing `extends_contract::` edges from a Contract back to Markdown Node Contract reads the full stack of Requirements that apply to any node conforming to the subject — the extension chain is what makes Requirements composable across forms.

## Crescent

### Against [[conforms_to -- compliance with a specification]]

`conforms_to::` is an instance-to-specification relationship: any node declares compliance with a Form Contract it satisfies. `extends_contract::` is a specification-to-specification relationship: one Form Contract inherits another Form Contract's Requirements and refines them. The two predicates operate at different layers of the form hierarchy and on different subject types — `conforms_to::` on any node; `extends_contract::` only between Form Contracts. The distinction matters because a single Form Contract typically carries both: the Gloss Form Contract `conforms_to::[[Contract Form Contract]]` (it is itself a Contract subject to the meta-Contract's rules) and `extends_contract::[[Markdown Node Contract]]` (it inherits the base file-form Requirements and adds gloss-specific ones).

### Against [[has_component -- mereological relation where the subject contains the object as a component]]

Containment is whole-to-part — the subject contains the object as a structural component of itself. Extension is specialization-to-generalization — the subject inherits the object and specializes it. The two are different structural shapes: a compound node `has_component::` its constituent nodes carries the constituents as parts; a Form Contract `extends_contract::` another Form Contract carries the parent's Requirements as inherited structure, not as parts the child contains. (The previous `composed_of::` predicate that had carried this contrast was consolidated into `has_component::` when the mereological axis collapsed to one predicate.)

## Typing

- **Subject:** A Form Contract node. Only Form Contracts participate in the extension chain.
- **Object:** A Form Contract node. The object MUST be the parent Contract whose Requirements the subject inherits.

## Instances

- `prototype/nodes/Contracts/Gloss Form Contract.md` carries `extends_contract::[[Markdown Node Contract]]` — the Gloss Form Contract inherits every Markdown Node Contract Requirement (filename rules, identity block, Relations section, named-edge syntax) and adds gloss-specific Requirements (filename-carries-definition pattern, body-shape rules).
- `prototype/nodes/Contracts/Predicate Form Contract.md` carries `extends_contract::[[Gloss Form Contract]]` — the Predicate Form Contract inherits everything Gloss Form Contract specifies and adds the Carries, Crescent, and Typing Requirements that make a predicate Gloss a Predicate node.

## Relations

- contrasts_with::[[conforms_to -- compliance with a specification]]
  - Different layers of the form hierarchy: `conforms_to::` is instance-to-specification compliance; `extends_contract::` is contract-to-contract inheritance.

- contrasts_with::[[has_component -- mereological relation where the subject contains the object as a component]]
  - The Crescent names the distinction between whole-to-part composition and specialization-to-generalization extension. `has_component` absorbed the previously-separate `composed_of` predicate when the mereological axis was consolidated.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes naming the inheritance-vs-composition distinction load-bearing. Both shapes get their own predicate rather than collapsing to a generic structural-relation term.
