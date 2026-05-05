---
name: graph-audit
description: |
  Sweeps the graph (or a scoped subset) for drift Node Validate cannot catch at single-node scope: vocabulary drift, ghost-link inventory, orphan nodes, un-annotated edges, forbidden predicates, non-ASCII filenames. Aggregates findings across files and reports by category, so the author sees patterns instead of per-file repetition.

  WHEN: user asks to audit the graph, sweep for drift, check hygiene, find ghost links, list orphans, audit the vocabulary; graph has 10+ nodes and drift is plausible; preparing for a curation pass; a Contract or Decision was recently revised.

  WHEN NOT: a single node needs checking (use Node Validate); graph is small enough that by-hand survey is faster; task is writing new content; periodic hygiene on a recently-audited graph (re-auditing wastes context).
---
- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Graph Audit

Sweeps the graph looking for drift and violations at scales Node Validate cannot reach. Node Validate checks one node against its Form Contract and reports findings local to that node; Graph Audit walks the corpus, aggregates findings across files, and reports patterns — vocabularies accreting without documentation, ghost links accumulating into planning debt, edges that never got their annotation, predicates that forbid themselves appearing at scale.

The skill's output is not a comprehensive list of every small violation. It is a compressed audit report grouped by category, naming the scale of each finding and the remediation path. A scion author reading the report decides which categories warrant a cleanup pass now, which deserve their own follow-up work, and which are acceptable drift for the current stage.

The audit is intentionally read-only. Graph Audit does not fix violations, does not delete stale nodes, and does not propose edits. Fixing is the work that follows the audit — usually direct editing, sometimes Node Validate per flagged node, sometimes Predicate Propose for a vocabulary gap the audit surfaced.

## Steps

### Step 1: Scope the audit

Ask the user the scope unless one is already named. Common scopes:

- **Whole graph** — every file under `nodes/`. Default when a scion author has just arrived.
- **One taxonomy** — `nodes/Decisions/`, `nodes/Predicates/`, etc. Useful after seeding a taxonomy with new nodes.
- **One predicate** — every edge using a specific predicate. Useful when a predicate's semantics shifted and a sweep should check downstream uses.
- **Since a commit or date** — files touched since a reference point. Useful after a contract revision that might have cascade effects.

Report the scope back to the user before running the sweep. A broad scope costs more context; narrow scopes are often what the user actually wanted.

### Step 2: Mechanical sweep

Run mechanical checks with `rg` via Bash. These are fast, deterministic, and catch clear violations.

**Filename rules** — em-dashes and en-dashes forbidden in filenames:

```sh
find nodes -name '*—*' -o -name '*–*' 2>/dev/null
```

**Forbidden predicate** — `relates_to::` is prohibited per `No Generic relates_to Predicate`. Anchor the pattern to `^-` so prose discussions (which frequently mention the forbidden predicate in backticks) are excluded:

```sh
rg -n -I -- '^- relates_to::' nodes/
```

**Identity block presence** — every `.md` node under `nodes/` should have a `conforms_to::` line. Use `find -print0 | while IFS= read -r -d ''` so filenames with spaces (Gloss and Predicate filenames use ` -- ` separators) survive the loop intact:

```sh
find nodes -type f -name '*.md' -print0 | while IFS= read -r -d '' file; do
  grep -q '^- conforms_to::' "$file" || echo "missing conforms_to: $file"
done
```

**YAML basics** — per `Markdown Node Contract`, every node SHOULD carry `tagline:` in its YAML frontmatter; the build pipeline surfaces it as the row summary on each taxonomy's index page, and a missing tagline renders the row silent. `brief_summary:` is genuinely optional; report presence as an informational stat rather than a Shortfall.

```sh
find nodes -type f -name '*.md' -print0 | while IFS= read -r -d '' file; do
  awk '/^---$/{c++; next} c==1 && /^tagline:/{print "yes"; exit} c>=2{exit}' "$file" \
    | grep -q yes || echo "missing tagline: $file"
done
```

Report missing-tagline hits as Shortfall (SHOULD violation, not Violation). Form-specific Contracts MAY strengthen `tagline:` to MUST when the form's role makes the absence load-bearing — Contracts and Skills are the canonical cases; for those forms, missing-tagline becomes Violation.

Count `brief_summary:` presence per taxonomy as an informational stat — useful for noticing when a taxonomy's nodes have drifted away from the form's typical body shape (e.g., Decision nodes typically benefit from `brief_summary:` because their bodies are long; if many Decisions lack it, the form's authoring habit may have drifted). The audit does not flag absence as a finding.

Report any hits as Violations or Shortfalls per the categories above.

### Step 2.5: Currency drift candidates

Currency cannot be checked mechanically — whether a tagline still describes the node's current claim is semantic judgment, not regex work. Word-overlap heuristics between tagline and H1 produce mostly false positives because taglines *describe* what the H1 *names* using deliberately complementary vocabulary; a Form Contract whose H1 is "Decision Form Contract" will have a tagline that talks about commitments, choices, and alternatives without the word "decision," and that is the tagline doing its job.

What the audit can flag mechanically is **staleness relative to body edits** — a tagline that hasn't been touched in months while the body has been substantially rewritten. The signal is direct: if the body's framing has shifted, the tagline that hasn't moved with it is a candidate for review.

**Tagline staleness via git-blame** — find the timestamp of the last edit to each node's `tagline:` line and compare against the timestamp of the node's most recent body-affecting commit. A gap larger than N months (start at 3 months) is a candidate.

```sh
# Implementation pattern: per-file git blame on the tagline line, compared to
# the file's last commit. Threshold-based candidate flagging.
find nodes -type f -name '*.md' -print0 | while IFS= read -r -d '' file; do
  tagline_line=$(awk '/^---$/{c++; next} c==1 && /^tagline:/{print NR; exit}' "$file")
  [ -z "$tagline_line" ] && continue
  tagline_date=$(git log -L "${tagline_line},${tagline_line}:$file" --format='%cs' -n 1 -- "$file" 2>/dev/null | head -1)
  body_date=$(git log -1 --format='%cs' -- "$file" 2>/dev/null)
  # Flag when body_date - tagline_date exceeds threshold (date math via Python).
  python3 -c "
from datetime import date
import sys
t='$tagline_date'; b='$body_date'
if t and b and t<b:
    td=date.fromisoformat(t); bd=date.fromisoformat(b)
    days=(bd-td).days
    if days > 90:
        print(f'  stale {days}d: $file (tagline {t}, body {b})')
" 2>/dev/null
done
```

**Stale `decided_on::` for Decisions** — a Decision's `decided_on::` date is its commitment timestamp. When the body has been substantially edited months later, the rendered Decision may carry framing that no longer matches what was decided. Flag when most-recent-body-commit minus `decided_on::` exceeds N months (start at 6 months for Decisions, since their bodies legitimately evolve).

Report any flagged candidates as a separate "Currency drift candidates" section in Step 8's aggregate report — distinct from Violations and Shortfalls, and distinct from automated findings. Each candidate is "consider reviewing this node's tagline / brief_summary"; the scion author decides whether each is real drift, acceptable evolution, or evidence the body itself has moved past what the surrounding metadata still claims. The audit does NOT classify these as failures.

If a more sophisticated semantic check is desired, that work belongs in `/node-validate` per node (where the full Form Contract context applies) or in a domain-aware reading pass, not in this graph-scope sweep. Word-overlap, sentiment analysis, or LLM-classifier approaches at graph scale produce noise too high to act on.

### Step 3: Vocabulary audit

List every predicate in use across the graph, count occurrences, and identify which have backing Predicate nodes:

```sh
rg -o -I -- '^- [a-z_]+::' nodes/ | sort | uniq -c | sort -rn
```

Cross-reference against the backing nodes:

```sh
ls nodes/Predicates/
```

Split the vocabulary into three tiers:

- **Backed** — predicate has a `nodes/Predicates/<predicate> -- <sense>.md` node. These are the definitional vocabulary.
- **Provisional** — predicate is in use but has no backing node. This is drift; report the list.
- **Base-contract** — predicates introduced by `Markdown Node Contract` or form-specific Contracts without a Predicate node (`conforms_to`, `authored_by`, `has_lifecycle`, `has_curation`, `has_commitment`, `decided_on`, `has_epistemic_status`, `serves_as`, `under_license`, `extends_contract`, `extended_by`). These are defined structurally in Contracts rather than in Predicate nodes; not drift.

Report provisional predicates as candidates for `/predicate-propose` work — each is either drift to consolidate or vocabulary to codify.

### Step 4: Ghost-link inventory

Extract every wikilink target and compare against the set of existing files. The difference is the ghost-link list.

```sh
rg -o -I -- '\[\[[^|\]]+\]\]' nodes/ | sort -u > /tmp/graph-audit-targets.txt
find nodes -name '*.md' -type f -exec basename {} .md \; | sort -u > /tmp/graph-audit-files.txt
```

For each target in the targets file that does not match a file stem (or the concept side of a `-- `-suffixed file), it is a candidate ghost link.

Filter out template-token false positives before reporting. Contract bodies and skill bodies use `[[X]]`, `[[<Domain>]]`, `[[Target]]`, `[[Editor]]`, `[[Principal]]`, `[[Downstream Node]]`, `[[X Form Contract]]`, `[[<placeholder>]]`, and similar as syntactic placeholders in examples — these are documentation shapes, not intended wikilinks. A candidate whose target is a single uppercase letter, contains `<` or `>`, matches `X Form Contract`, or appears inside backtick-fenced content in its source is a false positive. Filter them out before producing the ghost-link list, or name them as "template-token false positives" in a separate bucket so the scion author knows to skip them.

Ghost links are not violations — they are planning signals per `Markdown Node Contract`'s Named-edge syntax Requirement. Not every ghost is equal, though; four buckets sharpen the signal:

**Deliberate ghosts** — bare wikilinks in Predicate Crescent H3 headings (`### Against [[predicate]]`) and the paired `contrasts_with::[[predicate]]` edges in Relations, targeting predicates that deliberately don't have Predicate nodes. Categories include prohibited predicates (`relates_to`, `is_a` — forbidden by Decision, so no node will ever exist), base-contract predicates (`authored_by`, `has_lifecycle`, `has_commitment` and similar — introduced by Contracts rather than by Predicate nodes), and adjacent-graph vocabulary (`derived_from`, `contradicts` — predicates used in other graphs the Crescent is contrasting against). Deliberate ghosts are NOT drift; the `contrasts_with::` edge annotations typically acknowledge them explicitly ("Ghost link; target is prohibited..."). Report them as informational — no action needed.

**Drift ghosts** — bare wikilinks to what looks like a node that should exist and doesn't. Usually arises from a file rename that didn't update incoming references, or from a reference to a planned node that was never created. These are actionable: fix the reference, create the target, or explicitly demote the reference to deliberate-ghost status with an annotation.

**Vocabulary-value ghosts** — identity-predicate values (`[[Glosses/Seed Stage]]↗`, `[[Glosses/Working Draft]]↗`, `[[Glosses/Provisional Commitment]]↗`, `[[Glosses/Empirical Observation]]↗`, etc.) that every node points to via `has_lifecycle::`, `has_curation::`, `has_commitment::`, or `has_epistemic_status::` but which have no corresponding Gloss. These carry the highest-inbound-count ghosts in a new graph and represent the largest self-documentation gap. A healthy graph seeds Glosses for them early; an unhealthy graph accumulates identity predicates pointing to undefined values.

**Planning-surface ghosts** — single- or low-count bare wikilinks to genuinely-unfinished concepts (`[[Glosses/Convention Overhead vs Graph Quality]]↗`, a person's Gloss, a future Decision). These are the scion author's to-write list.

Report each bucket separately, with the bucket name in the report. Deliberate and template-token buckets are informational; vocabulary-value and drift buckets are actionable; planning-surface is curation. A ghost whose targets appears in MORE than one bucket (e.g., a predicate-name bare wikilink that's also a provisional predicate) counts as Drift until the author promotes it to a Predicate node, at which point it resolves.

### Step 5: Un-annotated edge sweep

Every top-level bullet under `## Relations` should be followed by an indented sub-bullet annotation per `Annotate Edges With Why-They-Matter`. An un-annotated edge is tag spaghetti.

The check pattern: within the `## Relations` section of each node, for every top-level bullet matching `^- [a-z_]+::`, the following non-blank line MUST begin with `  -` (two-space indent then hyphen). Implementations vary — awk with `getline`, a short Python script over `Path.read_text().split("\n")`, or a two-line rg over the section's range are all reasonable. Choose what the agent can ship reliably.

Report un-annotated edges as Shortfall findings, grouped by file. If the count is large enough that the fix is a dedicated curation pass rather than quick edits, flag the scale in the summary rather than listing every instance.

### Step 6: Reciprocal-edge sweep

When a node carries a forward edge like `informs_downstream::[[X]]` in its Relations, the target X typically carries a reciprocal edge back. Bidirectional edges are the convention across Decisions, References, Contracts, and Predicates; missing reciprocals are cascade failures — a forward edge was added without the back-edge being wired on the target.

The conventional pairs:

| Forward edge | Reciprocal on target |
|--------------|---------------------|
| `informs_downstream::[[X]]` | X has `informed_by::` or `grounded_in::` back |
| `grounded_in::[[X]]` | X has `informs_downstream::` back |
| `informed_by::[[X]]` | X has `informs_downstream::` back |
| `extends_contract::[[X]]` | X has `extended_by::` back |
| `supersedes::[[X]]` | X has `superseded_by::` back |
| `contrasts_with::[[X]]` | X has `contrasts_with::` back (symmetric) |

The check pattern: for each forward edge in every node's `## Relations` section, resolve the target to its file, and search that file for the corresponding reciprocal pointing back at the source node. Implementations vary; an `rg` sweep for forward edges piped into a per-target check is one pattern. Some forward edges are legitimately one-directional — an external reference marked with `↗` does not live in the graph, and a ghost link's target does not yet exist; skip externals and ghost-link targets.

Report missing reciprocals as Shortfall findings, grouped by the source node. Most missing reciprocals are quick Edit fixes — add the reciprocal on the target with an annotation explaining the relationship.

The sweep catches a specific failure pattern: when a new node is added and its forward edges are wired, it is easy to miss wiring the corresponding back-edges on older, established target nodes. The sweep makes the gap visible at graph scope rather than relying on per-node validation to notice.

### Step 7: Orphan detection

An orphan node has no incoming edges from any other node. Some orphans are intentional (the landing page; founding documents that are only linked-to from outside the graph). Others are drift (a node that was written but never wired into the graph).

For each node, search for incoming references:

```sh
for file in $(find nodes -name '*.md' -type f); do
  stem=$(basename "$file" .md)
  concept=$(echo "$stem" | sed 's/ -- .*//')
  count=$(rg -c -I -- "\[\[$stem\]\]|\[\[$concept" nodes/ 2>/dev/null | wc -l)
  if [ "$count" -eq 0 ]; then
    echo "orphan: $file"
  fi
done
```

Report orphans with their form (from `conforms_to::`) and lifecycle stage. A Seed Stage orphan is usually a work-in-progress; an Evergreen orphan is a candidate for either promotion (adding incoming edges) or demotion (stepping back the lifecycle).

### Step 8: Aggregate and report

Group findings by category, not by file. The report structure:

- **Violations** — hits from Step 2 (filename rules, `relates_to::` sightings, missing `conforms_to::`, missing `tagline:` on a form whose Contract specifies MUST). Each requires a fix before the graph meets its own Contract.
- **Shortfalls** — SHOULD-violations from Step 2 (missing `tagline:` on forms whose Contract specifies SHOULD). Each is a quick Edit fix; the graph functions without them but the index pages render silent rows.
- **YAML stats** — informational counts from Step 2: `brief_summary:` presence per taxonomy, optional scalar coverage. Not findings; useful for noticing when a form's authoring habit has drifted.
- **Currency drift candidates** — from Step 2.5: tagline-vs-H1 word divergence; stale `decided_on::` relative to recent body edits. Heuristic-flagged candidates the scion author reviews to decide whether the tagline, brief_summary, or body needs revision.
- **Vocabulary drift** — provisional predicates from Step 3. Each is a candidate for Predicate-node creation or consolidation into an existing predicate.
- **Planning surface** — ghost-link inventory from Step 4, grouped by inbound-edge count. High-count ghost links are the graph's most-wanted future nodes.
- **Un-annotated edges** — from Step 5, grouped by file. Shortfalls; the `Annotate Edges With Why-They-Matter` Decision asks for annotations but allows nodes to exist without them; flagged for curation.
- **Missing reciprocals** — from Step 6, grouped by source node. Shortfalls; most are quick Edit fixes once surfaced.
- **Orphans** — from Step 7, with form and lifecycle. Signals: intentional isolation (often fine), work-in-progress (fine), drift (fix).

Report each category compressed. Do not dump every finding; sample representative cases per category and name the total count. A scion owner wants to know "there are 40 ghost links, the top five are…" — not 40 individual list items.

### Step 9: Name the follow-ups

End the report by naming which follow-up skills or operations would address which categories:

- Violations → direct Edit per file.
- Shortfalls (missing tagline) → direct Edit per file; author a one-line tagline that reads as the row summary on the form's index page.
- YAML stats → no immediate action; revisit if a form's `brief_summary:` coverage falls below typical for that form.
- Currency drift candidates → review per node; rewrite tagline or brief_summary if stale, dismiss if acceptable lag, escalate to body revision if the framing itself is out of date.
- Vocabulary drift → `/predicate-propose` per provisional predicate, or edit-and-consolidate when two provisional predicates overlap.
- Ghost links → `/node-create` for the high-count targets; ignore the rest until they accumulate more incoming edges.
- Un-annotated edges → direct Edit per file, or `/node-validate` per file to get the full Form Contract check while fixing.
- Missing reciprocals → direct Edit per target file to add the reciprocal back-edge with annotation.
- Orphans → case-by-case; no single skill covers them.

The follow-up naming lets the scion author route the audit's findings without re-deriving what each category asks for.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements. Along with Node Validate, it forms the validation surface: Node Validate at node scope, Graph Audit at graph scope. The two compose as single-target and sweep modes of the same underlying discipline.

- composes_with::[[Node Validate]]
  - Node Validate operates at node scope; this skill operates at graph scope. An audit that flags a specific node can hand that node to Node Validate for the full Form Contract check. Each skill defers its out-of-scope concerns to the other.

- composes_with::[[Graph Load Audit]]
  - Graph Load Audit checks render-pipeline invariants (slug collisions, broken external wikilinks, unresolved donor proxies); this skill checks structural invariants (Form Contract compliance, predicate vocabulary, ghost links, reciprocals). Both sweep at graph scope but along orthogonal axes — one ensures the graph builds; the other ensures it coheres.

- grounded_in::[[Decisions/Adopt Wikilinks and Named Edges]]↗
  - The spine commitment this skill audits at graph scale. Every check in Steps 2 through 7 traces back to a named-edge or wikilink Requirement.

- grounded_in::[[Decisions/No Generic relates_to Predicate]]↗
  - Step 2's `relates_to::` sweep enforces this Decision across the whole graph. A single `relates_to::` hit is an architectural breach; the sweep exists to catch it even when per-node validation did not run.

- grounded_in::[[Decisions/Annotate Edges With Why-They-Matter]]↗
  - Step 5's un-annotated-edge sweep enforces this Decision. Annotations are the graph's mechanism for making edges legible to contributors scanning rather than just to agents traversing; un-annotated edges accumulating at scale signal drift.

- grounded_in::[[Decisions/Use ASCII Dashes in Filenames]]↗
  - Step 2's filename sweep enforces this Decision. Em-dash and en-dash drift in filenames is cheap to detect and cheap to fix but invisible without a sweep.

- grounded_in::[[Decisions/Adopt Predicate Atomicity]]↗
  - Step 3's vocabulary audit is the graph-wide expression of predicate atomicity. Provisional predicates accumulating without backing Predicate nodes mean the vocabulary is accreting without each predicate's distinction being documented.

- grounded_in::[[Markdown Node Contract]]
  - Step 2's YAML basics check enforces MNC's SHOULD requirement that every node carry `tagline:`. The base Contract is the source of truth for what every node looks like at the structural layer; this skill surveys the corpus for compliance with that source.

- informs_downstream::[[Markdown Node Contract]]
  - The base Contract specifies the structural shape this skill surveys. Graph Audit's aggregate findings surface where the graph has drifted from the Contract at scale; single-node validation surfaces where one specific node has drifted.

- composes_with::[[Node Create]]
  - Node Create's Step 10 wires reciprocal back-edges at authoring time; this skill's Step 6 sweeps for missing reciprocals at audit time. Same logic, different time-points: authoring-time keeps the graph consistent moment-by-moment; audit-time catches whatever authoring missed.
