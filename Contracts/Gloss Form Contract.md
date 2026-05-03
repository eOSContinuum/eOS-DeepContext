---
tagline: An interpretive definition whose filename carries the working definition, usable from the filesystem without opening the file
---

- conforms_to::[[Contract Form Contract]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Gloss Form Contract

A Gloss is a node whose purpose is to define a term used elsewhere in the graph. It carries enough body to make the term usable on first encounter and carries its working definition in the filename itself, so that a contributor browsing the filesystem reads the definition without opening the file.

A Gloss is not a Reference (which points to external authoritative source material) and not a Contract (which specifies structural requirements). It is the most compact self-contained node the graph supports, but its body may grow when the term is load-bearing enough to deserve elaboration.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

Enforces [[Use Double-Hyphen Separator for Gloss Definitions]].

- The filename MUST follow `<Concept> -- <one-clause definition>.md`.
- The separator between concept and definition MUST be ` -- ` (space, double hyphen, space).
- The concept side MUST match the wikilink target other nodes use to reference this gloss.
- The definition side MUST be a single clause, no trailing period, no internal `--`.

### H1

- The H1 MUST be the bare concept name only, matching the concept side of the filename.
- The H1 MUST NOT repeat the definition from the filename.

### Body shape

Enforces [[Require Body Elaboration Beyond Filename Definition]].

- The body MAY be a single sentence, a short paragraph, or several paragraphs with H2 subsections. Typical shape is two or three paragraphs: the opening restate-and-elaborate, a paragraph giving concrete elaboration or showing the concept at work, and a paragraph distinguishing the concept from an obvious alternative.
- The first sentence MUST restate the filename definition and elaborate it by one useful clause or contrast — not a verbatim repeat. A body whose only content is the bare definition is not conforming.
- Subsection headings (H2) are permitted when a gloss carries distinct sub-angles that each want their own named section. For a compact gloss, prefer unheaded paragraphs.
- If the content grows beyond what a gloss can comfortably carry (roughly 300 words of body, or more than three sub-sections), consider whether the node wants a different form (Reference, Case Study, Pattern).

### Sources section

- When the gloss draws on external sources, a `## Sources` section MUST appear after the body and before `## Relations`.
- Sources are listed as bulleted URLs with brief annotations. They are not typed edges; the typed edges go in `## Relations`.

### Relations section

- A Gloss MAY omit `## Relations` when it has no non-trivial relational edges.
- When present, relational edges follow the base Markdown Node Contract.

### Identity predicate block

- The identity block above the H1 MUST include `conforms_to::[[Gloss Form Contract]]`.

### Optional scalar metadata

- YAML frontmatter MAY include `created:` (ISO date), `tagline:` (a pithy one-liner), and `brief_summary:` (a paragraph-length summary).
- All three are scalar metadata, not graph-structural. They support human browsing and build-time rendering.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the filename-carries-definition pattern, body-shape allowances, and the standard section order (body → Sources → Relations).

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract, so it conforms to the meta-contract that specifies what Contract nodes look like.

- grounded_in::[[Use Double-Hyphen Separator for Gloss Definitions]]
  - Grounds the filename pattern Requirement.

- grounded_in::[[Require Body Elaboration Beyond Filename Definition]]
  - Grounds the body-shape rule against verbatim repetition of the filename definition.

- contrasts_with::[[Reference Form Contract]]
  - A Gloss defines a term used internally; a Reference points to external authoritative source material. Both may be short, but the purposes are distinct.
