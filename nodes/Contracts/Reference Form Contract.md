---
tagline: An external source pointer with an Adopted / Not adopted (yet) split and publication metadata; cite-by-wikilink rather than cite-by-URL
---

- conforms_to::[[Contract Form Contract]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Reference Form Contract

A Reference is a node that captures an external authoritative source the graph draws from — a gist, a paper, a repository, a published article, a lecture. It records what the source is, what role it plays in this graph's reasoning, what this project has adopted from it, and what this project has deliberately declined to adopt. The external URL lives in the Reference node; downstream nodes cite the Reference by wikilink rather than by URL.

A Reference is not a Gloss (which defines an internal term), not a Contract (which specifies structural obligations), and not a Decision (which records a commitment made by this project). A Reference points outward: it says "this graph draws on that source," with enough context that a reader understands the role the source plays here without having to re-read the source to find out.

**Before authoring a Reference node, ask the form-fit question first**: is this artifact actually an external authoritative source the graph draws from, with a canonical address resolvable to readers other than the author? Structural compliance with the Requirements below is necessary but not sufficient -- a node carrying a citation parenthetical filename, a `serves_as::` edge, and an Adopted / Not adopted body split can still fail to be a Reference if the URL is not resolvable to readers other than the author. The URL resolvability Requirement enforces this mechanically, but asking the form-fit question at authoring time saves the work of writing a node that fails validation. If the artifact is internal to this project's authors, or its canonical location is non-public (sibling-project local paths, private cloud-storage URLs, internal-only intranet addresses), the artifact does not yet warrant a Reference node; load-bearing content from such an artifact extracts directly into the appropriate destination form (Aspiration / Conviction / Decision / Observation) with prose-level inline citation in the destination node's body or `## Sources` subsection.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- The requirements below are additions or refinements, not overrides.

### Filename pattern

Enforces [[Embed Citation Parenthetical in Reference Filenames]] and [[Disambiguate Reference Artifacts from Traditions]].

- The filename MUST match the wikilink target exactly (with `.md`), without a `--` separator.
- The filename MUST carry a `(<Author>, <Year>)` citation parenthetical suffix: `<Artifact Name> (<Author>, <Year>).md`.
- The **author** component uses the human-readable display form matching the `authored_by::[[X]]↗` target (without the `↗` marker). Two authors: `(Author One & Author Two, Year)`. Three or more: `(Author One et al., Year)`; the full author set remains enumerated in `authored_by::` predicates. Organizational publications use the organization name.
- The **year** component refers to the source's publication or last substantive revision, NOT the node file's creation date. `(<Author>, <OrigYear>, rev. <RevYear>)` is acceptable for revision-worthy histories. When no year is discoverable, omit it rather than guessing: `(<Author>)`.
- When multiple external artifacts from the same tradition are captured as separate References, the filename MUST carry a disambiguator (`<Name> Gist`, `<Name> Paper`, `<Name> Repository`) before the citation parenthetical.

### Identity predicate block

Enforces [[Reserve Predicate Vocabularies to Specific Forms]].

- The identity block above the H1 MUST include `conforms_to::[[Reference Form Contract]]`.
- The identity block MUST include `serves_as::[[<Target>]]` — a multi-word wikilink naming what this source serves as in this graph.
- The identity block MAY include `under_license::[[<License>]]↗` when the source's license is load-bearing.
- The identity block SHOULD include `in_domain::[[<Domain>]]`.
- The identity block MAY include `authored_by::`, `has_lifecycle::`, and `has_curation::` as for any Markdown Node.

### H1

- The H1 MUST match the filename exactly (minus the `.md` extension).

### URL preservation

Enforces [[Keep URLs as Scalar Metadata, Not Predicates]].

- The Reference node MUST preserve the external URL of the artifact verbatim.
- The URL MUST appear either as a `URL:` line in the body (preferred for a single canonical URL) or inside a `## Sources` section (when multiple URLs are material).
- URLs MUST NOT be encoded as named-edge predicate values.

### URL resolvability

Enforces [[Reference Targets Must Be Resolvable to Other Readers]].

- The URL recorded for a Reference MUST be resolvable to readers other than the author.
- Public web URLs (`https://`, repository URLs, paper DOIs, public gist URLs), registered DNS names, and other addresses anyone with read access to the source can resolve satisfy this Requirement.
- Non-public sibling-project local paths (e.g., `~/Workspace/<project>/...`), private cloud-storage URLs, internal-only intranet addresses, and other addresses requiring author-specific access fail this Requirement.
- An artifact whose canonical address is not yet public does not warrant a Reference node. Load-bearing content from such an artifact MUST be extracted directly into the appropriate destination form (Aspiration / Conviction / Decision / Observation) with prose-level source attribution citing the path inline in the destination node's body or `## Sources` subsection.
- Promoting a non-public-path citation to a Reference node when the artifact later becomes public is the corrective move; until then, prose-level inline citation in extracted nodes' bodies is the canonical form.

### Body shape

Enforces [[Distinguish Adopted from Not-Adopted in References]].

- The body MUST state what the source contributes to this graph — not a summary of the source, but a targeted account of what this project draws from it.
- The body MUST distinguish **what is adopted** from **what is deliberately not adopted**. When both are present, they MAY appear under explicit sub-headings (`### Adopted`, `### Not adopted`) or as prose paragraphs whose role is clear from context.
- The body MAY include a **key moves** or **patterns to remember** list when the source carries several discrete ideas this graph wants to carry forward.
- The body SHOULD NOT re-derive the source's argument.

### Relations section

- The Relations section follows the base Markdown Node Contract.
- A Reference MAY carry these reference-specific or broadly-useful edges:
  - `informs_downstream::[[Downstream Node]]` — a decision, contract, or node this source informs.
  - `contrasts_with::[[Sibling Reference]]` — when two sources occupy adjacent territory.
  - `supersedes::[[Older Reference]]` — when a newer version replaces an older one the graph previously cited.
  - `serves_as::[[<Target>]]` — also valid in the identity block.

### Optional scalar metadata

- YAML frontmatter MAY include `created:` (ISO date of node file creation, not the source's publication date), `tagline:`, and `brief_summary:`.
- YAML is OPTIONAL for References.

### When to split or consolidate

Enforces [[Restrict References to Tight Artifact Clusters]].

- A Reference MAY capture one artifact or a tight cluster of artifacts (e.g., a primary gist and its two immediate follow-ups). It MUST NOT catalog an entire ecosystem.
- Two sources that play distinct roles MUST be split into separate References, even when the same author produced both. Role separation is the primary splitting criterion; authorship is secondary.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds the `serves_as::` identity predicate, the URL-preservation requirement, and the adopted-vs-not-adopted body structure.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- contrasts_with::[[Gloss Form Contract]]
  - A Gloss defines a term used inside this graph; a Reference captures an external artifact this graph draws from. Both may be short, but they face opposite directions.

- contrasts_with::[[Decision Form Contract]]
  - A Decision records a commitment this project has made; a Reference records a source this project has drawn from.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The decision that makes `serves_as::`, `informs_downstream::`, and `under_license::` first-class named edges.

- grounded_in::[[Embed Citation Parenthetical in Reference Filenames]]
  - Grounds the (Author, Year) parenthetical rule in the Filename pattern Requirement.

- grounded_in::[[Disambiguate Reference Artifacts from Traditions]]
  - Grounds the artifact-descriptor rule in the Filename pattern Requirement.

- grounded_in::[[Keep URLs as Scalar Metadata, Not Predicates]]
  - Grounds the URL preservation Requirement.

- grounded_in::[[Reference Targets Must Be Resolvable to Other Readers]]
  - Grounds the URL resolvability Requirement. Authored 2026-04-26 in response to the eos-harness MVA workstream's FX-6 misstep, where two Reference nodes were authored against non-public sibling-project paths (`~/Workspace/skotos-dev/deliverables/...`) before the URL-resolvability test was applied. The Decision node is currently a ghost link; it will be authored when the project's first Decision-form node lands (likely #R-4's foundation tradeoff Decision is the natural pairing for that authoring session). Until then, the Requirement's RFC 2119 keywords (MUST) carry the binding force; the grounding Decision provides the reasoning chain when authored.

- grounded_in::[[Distinguish Adopted from Not-Adopted in References]]
  - Grounds the Body shape Requirement's adopted-vs-not-adopted discipline.

- grounded_in::[[Restrict References to Tight Artifact Clusters]]
  - Grounds the When to split or consolidate Requirement.

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - Grounds the `serves_as::` reservation in the identity predicate block Requirement.
