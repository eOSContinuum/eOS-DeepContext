---
tagline: The base file-form every node inherits: encoding, filename rules, YAML scope, identity predicate block above the H1, Relations section, and named-edge syntax
---

- conforms_to::[[Contract Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Markdown Node Contract

The base contract every Markdown Node in this project conforms to. It specifies the file-level form: encoding, filename rules, YAML frontmatter scope, the predicate block above the H1, the Relations section, and the named-edge syntax. More specific contracts (Gloss, Contract, Reference, Decision, Pattern, Observation, Conviction, Aspiration Form Contracts) extend this one by adding structural requirements on top of the base form.

The Requirements below are thin enforcement clauses; their reasoning, alternatives, and revisit conditions live in the Decisions they ground in. The grounding edges are named in each Requirement and listed in the Relations section.

## Requirements

### File form

Enforces [[Decisions/Use ASCII Dashes in Filenames]]↗.

- The file MUST be UTF-8 markdown with `.md` extension.
- The filename MUST NOT contain em-dashes (`—`) or en-dashes (`–`). Use ASCII hyphens.
- Where a visual dash is needed in a filename, the form MUST be a double ASCII hyphen `--`.
- The filename MUST be either `<wikilink target>.md` or `<wikilink target> -- <description>.md` (the latter reserved for Gloss Form per its own contract).
- Referencing this file from another node depends on whether the filename carries a ` -- <description>` suffix. When the filename has no suffix, other nodes reference it using the bare wikilink `[[<filename>]]`. When the filename has a ` -- <description>` suffix, references in prose flow MUST use the pipe form `[[<full filename>|<concept>]]` per [[Decisions/Use Pipe Wikilinks for Display-Target Divergence]]↗. In structural contexts — `## Relations` edges, subsection headings, and other locations where readers scan a structured index rather than read running prose — the bare full filename `[[<full filename>]]` is permitted, because the ` -- <description>` suffix carries the target's working definition to the reader at the edge site. The bare concept form `[[<concept>]]` is never permitted for a ` -- `-suffixed target, because it does not resolve in standard wiki tooling.

### Node atomicity

Enforces [[Decisions/Adopt Node Atomicity]]↗.

- A file MUST address exactly one concept. One node names one concept, and one concept has one node.
- A file whose body would legibly split into two independent sections serving two different concepts MUST be split into two files, each naming one concept.
- Compound nodes follow node atomicity: a compound names one concept; its sub-files are supporting material, not sub-concepts or facets. A sub-file that reads as a node in its own right — cited by other nodes under its own name, carrying its own identity predicates — MUST be promoted to an atomic node, and the compound split.
- Decisions MAY bundle multiple logically-related commitments under the narrow conditions in [[Decision Form Contract]]. A bundled Decision still names ONE concept — the bundle itself.

### YAML frontmatter

Enforces [[Decisions/Restrict YAML to Scalar Metadata]]↗.

- YAML frontmatter is OPTIONAL as a structural matter, but every node SHOULD carry at minimum a `tagline:` (see below); a node with no YAML at all is permitted by the Contract but undermines the taxonomy index pages that surface taglines as row summaries.
- When present, YAML MUST contain only scalar metadata (e.g., `created`, `tagline`, `brief_summary`).
- Every node SHOULD carry `tagline:` — a single-line summary that the build pipeline surfaces on the node's taxonomy index row. Without it, the index renders the node as a bare wikilink with no orientation to what the node carries; the index becomes silent on the form's question (what does *this* one specifically claim?). Form-specific Contracts may strengthen this to MUST when the form's role makes the absence load-bearing (Contracts and Skills are the canonical cases).
- A node MAY carry `brief_summary:` — a paragraph-length restatement when one is genuinely additive over the body's restate-and-elaborate opening. Short Glosses, terse Predicate definitions, and other concise forms typically do not need a `brief_summary:`; longer Decisions and Convictions often benefit from one.
- A node MAY carry `created:` — an ISO date marking when the node file was first authored. Form-specific Contracts may add additional optional or required scalars (e.g., `is_home:` and `hide_identity_block:` on Touch Point; `serves_as:`, `url:`, `this_did:` on Reference).
- YAML keys for Deep Context-specific scalars MUST be multi-word `snake_case`, matching named-edge predicate discipline. Two classes of exception: tool-reserved or convention-respecting fields (`aliases`, `tags`, `created`) keep their established names, and fused compound words (`tagline`, `wikilink`) operate as single concepts.
- Named-edge predicates MUST NOT live in YAML. This applies to graph-participating predicates and to their scalar mirrors.
- An `aliases:` field MAY appear as a tool-level convenience; it is graph-non-participating.

### Identity predicate block

Enforces [[Decisions/Adopt Layered Node Structure]]↗.

- The body MUST begin with a bullet list of identity predicates before the H1.
- This block MUST include `conforms_to::[[<Form> Contract]]` or `conforms_to::[[<Form> Form Contract]]`.
- This block SHOULD include `in_practice_domain::[[<Practice Domain>]]`.
- This block MAY include `has_lifecycle::[[<X> Stage]]`, `has_curation::[[<descriptive phrase>]]`, and `authored_by::[[<Person>]]`.
- Identity predicates describe what the node IS; they do not describe its relationships to other nodes.

### H1

- The file MUST contain exactly one H1.
- The H1 MUST be the concept name — not the full filename, not a definition, not a sentence.

### Body

- Prose body follows the H1.
- Prose MAY contain inline wikilinks; inline links are readable references, not structural edges.

### Layered structure

Enforces [[Decisions/Adopt Layered Node Structure]]↗.

- A node MUST be arranged in layers that differ in cost to read, and each layer MUST be complete at its own scale.
- The minimum layering is: (a) the identity predicate block above the H1 (cheap, structural, machine-readable), (b) the H1 and its opening prose — or the opening designated section such as a Heart — stating the node's claim at card scale, (c) the elaboration body carrying reasoning, consequences, or instances, and (d) the Relations section (cheap, structural, machine-readable). Specific form contracts MAY extend or refine this shape; they MUST NOT collapse it below the minimum.
- Each layer MUST carry what its scale claims to carry. A claim layer MUST state the claim, not tease it; a structural layer MUST carry authoritative data, not preview text; an elaboration layer MUST reason about the claim, not re-introduce it.
- The cheapest structural layer MUST appear before the expensive prose.

### Relations section

Enforces [[Decisions/Annotate Edges With Why-They-Matter]]↗ and [[Decisions/No Generic relates_to Predicate]]↗.

- If the node has relational edges, they MUST appear in a section headed `## Relations` after the body.
- Each relational edge MUST be a top-level bullet in the form `- predicate::[[Target]]` or `- predicate::[[Target]]↗`.
- Each relational edge SHOULD carry an indented sub-bullet annotation explaining why the relationship matters.
- The `relates_to::` predicate MUST NOT be used. Choose a specific predicate (`extends_contract::`, `has_component::`, `grounded_in::`, `built_on::`, `informed_by::`, `informs_downstream::`, `contrasts_with::`, `contends_with::`, and so on) or add one to the local vocabulary.

### Named-edge syntax

Enforces [[Decisions/Adopt Wikilinks and Named Edges]]↗.

- Predicates MUST be multi-word, lower-case, joined by underscores (`has_component::`, not `includes::`).
- Named-edge values MUST take one of two shapes: a wikilink target (`- predicate::[[Target]]` or `- predicate::[[Target]]↗`) or a structural scalar introduced by a form-specific Contract.
- A form-specific Contract MAY introduce a scalar-valued predicate when the scalar carries structural content (e.g., `decided_on::YYYY-MM-DD` introduced by [[Decision Form Contract]]). The introducing Contract MUST name the value shape and MUST reserve the predicate to the form it belongs to via [[Decisions/Reserve Predicate Vocabularies to Specific Forms]]↗. Scalar-valued predicates inherit every other Requirement in this section (naming discipline, form-specific reservation).
- Wikilink targets MUST be multi-word. Single-word targets are not permitted (`[[Wikilink Syntax]]`, not `[[Wikilink]]`).
- A target whose referent belongs to a different wiki or to an external tradition MUST be marked with a trailing `↗`. The `↗` marks the referent's provenance, not a URL. URLs, when recorded, live in a stub node under `sources/`.
- Ghost links (wikilinks to targets that do not yet exist) are permitted and signal intended future nodes.

### Image embeds

Enforces [[Decisions/Embed Images via Obsidian Wikilink Syntax]]↗.

- Image embeds MUST use Obsidian's wikilink-embed syntax: `![[path/to/image.ext]]`. The pipe form `![[path|alt text]]` overrides the default alt text (otherwise derived from the filename stem).
- Recognized image extensions are `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`. Embeds whose target has another extension pass through the render pipeline unchanged, reserving the syntax for future non-image uses.
- Attachment files MUST live in an `Attachments/` folder co-located with the referring note: at the repository root for root-level notes (`landing.md`, and similar), and as a sibling subdirectory for compound nodes (`nodes/<Tax>/<Folder>/Attachments/`).
- The render pipeline MUST translate each embed into a standard markdown image reference with a site-root-relative URL and MUST copy every `Attachments/` tree into the build output so those URLs resolve at request time.

### Predicate atomicity

Enforces [[Decisions/Adopt Predicate Atomicity]]↗.

- Each predicate MUST answer exactly one question — one axis of distinction, not multiple.
- A predicate's values MAY span many points along that one axis. What MUST NOT occur is values that cluster into subgroups answering different questions.
- When a predicate is found carrying two or more axes, the remedy MUST be a predicate family — each member a single-axis predicate — not a revised but still-overloaded name. The recurring craft move is [[Patterns/Refactor the Predicate's Axes]]↗.
- A new axis of distinction MUST earn a new predicate; retrofitting existing predicates to carry a new axis is forbidden.

## Relations

- built_on::[[CommonMark Markdown]]↗
  - A node conforming to this contract is valid CommonMark; the contract adds reading and authoring discipline on top of the file format.

- grounded_in::[[References/Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]↗
  - The canonical reference for the underlying wikilinks-plus-named-edges convention this contract specializes.

- grounded_in::[[Decisions/Adopt Wikilinks and Named Edges]]↗
  - The project-level Decision that commits to the wikilinks-and-named-edges spine. Node atomicity, predicate atomicity, and layered structure all presuppose this Decision.

- grounded_in::[[Decisions/Adopt Node Atomicity]]↗
  - The Decision grounding the node-atomicity Requirement.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - The Decision grounding the predicate-atomicity Requirement.

- grounded_in::[[Decisions/Adopt Layered Node Structure]]↗
  - The Decision grounding the layered-structure Requirement and the identity-predicate-block placement.

- grounded_in::[[Decisions/Restrict YAML to Scalar Metadata]]↗
  - The Decision grounding the YAML-frontmatter Requirement.

- grounded_in::[[Decisions/Use ASCII Dashes in Filenames]]↗
  - The Decision grounding the filename-dash rules in the File form Requirement.

- grounded_in::[[Decisions/Annotate Edges With Why-They-Matter]]↗
  - The Decision grounding the Relations-section annotation requirement.

- grounded_in::[[Decisions/No Generic relates_to Predicate]]↗
  - The Decision grounding the `relates_to::` prohibition in the Relations-section Requirement.

- grounded_in::[[Decisions/Embed Images via Obsidian Wikilink Syntax]]↗
  - The Decision grounding the Image embeds Requirement. The Contract states the rule (`![[path]]` syntax, `Attachments/` folder colocation, site-root URL resolution, pipeline copy step); the Decision records the reasoning and revisit conditions.

- extended_by::[[Gloss Form Contract]]
  - Gloss Form Contract extends this contract with filename-carries-definition and body-shape allowances.

- extended_by::[[Contract Form Contract]]
  - Contract Form Contract extends this contract with requirements for parseable `## Requirements` sections and the self-conformance pattern.

- informs_downstream::[[Glosses/Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]↗
  - The compound-node pattern realizes node atomicity for concepts whose supporting material warrants its own sub-files: the compound names one concept, the sub-files are supporting material, and the node-atomicity Requirement's split criterion is what tells the author whether a prospective sub-file is supporting material (stays compound) or an independent concept (promote to atomic).

- informs_downstream::[[Patterns/Progressive Summary Before Substance]]↗
  - The Pattern that realizes the layered-structure Requirement in the prototype's specific vocabulary. The Requirement states the standing structural rule; the Pattern names the move an author makes composing a node in practice.

- informs_downstream::[[Patterns/Refactor the Predicate's Axes]]↗
  - The Pattern that realizes or restores predicate atomicity when a predicate is found carrying multiple axes. The Requirement states the rule; the Pattern names the craft applied when the rule is violated in the wild.

- informed_by::[[Decisions/Use Pipe Wikilinks for Display-Target Divergence]]↗
  - Bare `[[Concept]]` does not resolve to a file whose name carries a ` -- <description>` suffix; the pipe form Decision specifies the canonical way to reference gloss nodes and other disambiguated filenames from both prose and named edges.
