---
tagline: A guided introduction that frames a reader's lens onto a region of the graph — not a summary, but a curated first-encounter
created: 2026-05-03
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- extends_contract::[[Gloss Form Contract]]
- in_practice_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Touch Point Form Contract

A Touch Point is a node whose role is to **frame a reader's lens** onto a region of the graph — a Gloss naming a community of practice (as `in_practice_domain::` membership), a Gloss naming a cross-cutting concept, an argument the project is making, or a thematic cluster of related nodes. It is the moment of first contact between the reader (human or LLM) and the region: the curated welcome that helps a newcomer orient before drilling into specifics, and that helps a returning reader remember-as-if-first.

A Touch Point is **not** a summary. It does not condense the region's content into a smaller form, does not aim for exhaustive coverage, and does not substitute for reading the nodes the region contains. The Form deliberately resists summary semantics: the predicate connecting a Touch Point to its target is `frames_lens_on::`, not `summarizes::` or `covers::`. A Touch Point's job is to *give the reader a way of looking* at the target region — a primer's foundational teaching paired with a lens's perspective-setting — without claiming to replace the region's nodes.

The Form's name borrows from marketing's *touch point* (a moment of customer-brand interaction at a defined channel) but the marketing instrumentalism does not transfer. In this graph a Touch Point's job is to receive a reader well, not to convert them; the moment-of-first-contact metaphor carries; the conversion-funnel metaphor does not.

A Touch Point may be designated as the graph's **home page** by carrying `is_home: true` in its YAML frontmatter. Exactly one Touch Point per graph carries this flag; the build pipeline renders the home Touch Point to the site's root URL. Other Touch Points render under `nodes/touch-points/<slug>/` like any other node.

## Requirements

### Inherits Gloss Form Contract

- The bare-concept H1 and the restate-and-elaborate body opening from [[Gloss Form Contract]] apply. The double-hyphen filename pattern from Gloss does NOT apply — Touch Points override it (see Filename pattern below).
- The requirements below are additions or overrides for Touch Point instances specifically.

### Filename pattern

- The filename MUST be `<Touch Point Name>.md` — a single name, no double-hyphen separator, no compressed-definition clause. Touch Points override Gloss's filename pattern because a Touch Point's filename names a *reader-facing role* (Welcome, Primer, Lens) rather than carrying a working definition. The longer framing belongs in the `tagline:` YAML field, not in the filename.
- The Touch Point Name MUST name what the Touch Point *does* for the reader (e.g., "Deep Context Welcome", "Substrate Argument Primer", "Customer Patterns Lens"). Do not name what region the Touch Point covers — the region is named by the `frames_lens_on::` edge.

### Identity predicate block

- The identity block MUST include `conforms_to::[[Touch Point Form Contract]]`.
- The identity block MUST include at least one `frames_lens_on::[[<target>]]` edge naming what region the Touch Point orients the reader to. Multiple edges are permitted when the Touch Point frames a coherent multi-part region.

### Optional frontmatter: is_home

- A Touch Point MAY carry `is_home: true` in its YAML frontmatter, designating it as the graph's home page. The build pipeline renders the home Touch Point to the site root URL (`/`).
- Exactly one Touch Point per graph SHOULD carry this flag. Zero is permitted (the graph has no home page) but the site's root URL will then be unrouted.
- If multiple Touch Points carry `is_home: true`, the build pipeline MUST report this as an error and refuse to deploy.

### Optional frontmatter: hide_identity_block

- A Touch Point SHOULD carry `hide_identity_block: true` in its YAML frontmatter so the leading identity-block bullets (`conforms_to::`, `frames_lens_on::`, `in_practice_domain::`, etc.) are stripped from the rendered HTML output.
- Reader-facing welcomes are diminished by a technical predicate dump appearing above the H1; the rendered page should open with the H1 and synthesis prose. The identity block remains in the source markdown — readers who want it can view source via the "Edit on GitHub" footer link.
- Authors may set `hide_identity_block: false` (or omit the flag) on Touch Points where exposing the edges is genuinely useful (for example, a Touch Point whose target audience is graph-tooling authors who want to see the predicate vocabulary in action).

### Body: Opening Synthesis

- The body MUST open with a synthesis paragraph or two that names the region the Touch Point frames, the lens it offers, and what the reader will gain from following the Entry Points. The opening is reader-facing: it speaks to the reader directly, not about the region in the abstract.
- The opening MUST NOT summarize the region's content. The synthesis names the *lens*, not the *contents seen through it*.

### Body: Entry Points

- The body MUST include an `## Entry Points` section listing wikilinks to the key nodes a reader should visit, with one-clause glosses naming why each is a useful entry. The entries are ordered by recommended reading sequence, not alphabetically.
- Entry Points are wikilinks to nodes the reader is being routed toward — not citations of external sources (those go in `## Sources`).

### Body: Out of Scope

- The body MUST include an `## Out of Scope` section naming what this Touch Point's lens deliberately does *not* address. Readers who came here looking for those things are redirected elsewhere (with wikilinks where applicable).
- Out of Scope is what makes a Touch Point's lens explicit. Without it, readers cannot tell whether their need fits the framing or whether they should look elsewhere.

### Body: Reading Path (optional)

- A `## Reading Path` section MAY appear after Entry Points when there is a natural sequence the reader should follow rather than picking entry points independently. When present, the Reading Path lists the nodes in the recommended order with brief connective prose explaining why one node follows another.

### Sources section

- A `## Sources` section MUST appear when the Touch Point draws on external authoritative material. Sources are listed as Reference nodes with brief annotations.

### Relations section

- A Touch Point MAY include `narrower::[[<sub-Touch-Point>]]` and `broader::[[<broader Touch Point>]]` for hierarchical relations between Touch Points within the graph (e.g., a high-level home Touch Point broader than a sub-region Touch Point).
- A Touch Point MAY include `related::[[<peer Touch Point>]]` for non-hierarchical adjacencies (Touch Points whose lenses overlap).

## Relations

- extends_contract::[[Gloss Form Contract]]
  - Inherits the bare-concept H1, the restate-and-elaborate body opening, and the body shape allowances. Overrides Gloss's double-hyphen filename pattern with a single-name `<Touch Point Name>.md` form because a Touch Point's filename names a reader-facing role rather than carrying a working definition. Adds the Opening Synthesis, Entry Points, Out of Scope sections plus the required `frames_lens_on::` edge and the optional `is_home` frontmatter scalar.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract specifying what Contract nodes look like.

- contrasts_with::[[Reference Form Contract]]
  - Reference points outward at external sources; Touch Point points inward at the local graph (or at concept Glosses that may live in other graphs but are referenced via the local-Reference proxy pattern). Both are "pointer" forms; the boundary direction is opposite.

- contrasts_with::[[Gloss Form Contract]]
  - A Gloss defines a single term, often briefly; a Touch Point frames a reader's lens onto a region (which may be a Gloss, a community of practice, an argument, or a thematic cluster). A Touch Point extends Gloss with reader-orientation requirements (Opening Synthesis, Entry Points, Out of Scope) and the required `frames_lens_on::` edge.

- composes_with::[[frames_lens_on -- frames a reader's lens onto a region of the graph]]
  - The Predicate that carries a Touch Point's relation to its target. Every Touch Point MUST include at least one `frames_lens_on::` edge; the Predicate's Typing names the polymorphic object (a Gloss naming a community of practice, a Gloss naming a concept, or another concept-bearing node).

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes Touch Points load-bearing rather than collapsible into the underlying Glosses they target. A Touch Point may frame a lens onto a region of the graph that crosses communities of practice (e.g., a Touch Point on a cross-cutting Gloss that has multiple `appears_in::` edges). Without the diversity stance, the Glosses themselves would suffice; with it, finer-grained reader-orientation is warranted.
