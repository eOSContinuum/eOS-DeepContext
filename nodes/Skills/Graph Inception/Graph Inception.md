---
runtime_name: graph-inception
tagline: Performs the local Open Integrity inception ceremony that stands up a new Deep Context graph with its own SSH-signed root commit and DID
description: |
  Guides a first steward through the local Graph Inception ceremony that re-roots a cloned Deep Context graph (or initializes a fresh one) with a new Open Integrity inception commit signed by the steward's own SSH key, producing the new graph's own `did:repo:<sha1>` DID. Verifies prerequisites, walks a missing-prereq steward through the brew/gh/ssh-keygen install chain, runs `.scripts/graph-inception.sh` for the ceremony proper, and reports next steps for standing up the graph's GitHub repository and Pages site.

  WHEN: the user has cloned a Deep Context graph locally (or initialized a fresh directory) and wants to turn the working directory into a new graph with its own cryptographic identity; the user says "graph inception", "stand up a new graph", "initialize my graph", "/graph-inception"; a fresh working directory contains `.deep-context-identity.yml` with `scion_of: null` and `.git` pointing at the donor's history (or no `.git` at all for a fresh-init case).

  WHEN NOT: the repository is DeepContext.com itself or another existing graph (the ceremony is for new graphs, not for the graph being cloned from); the local repository has already completed Inception (the directory's `.deep-context-identity.yml` `this_did` matches the current root-commit SHA1); the user is exploring an existing graph someone else stood up (use Graph Orient for orientation); a contributor is editing content on an existing graph (direct git edits, not re-Inception).
---

- conforms_to::[[Skill Form Contract]]
- grafted_from::[[DeepContext.com Graph (Allen, 2026)]]
- authored_by::[[Glosses/Deep Context Community]]↗
- has_lifecycle::[[Glosses/Seed Stage]]↗
- has_curation::[[Glosses/Working Draft]]↗
- in_practice_domain::[[Glosses/Deep Context Architecture]]↗

# Graph Inception

Performs the local ceremony that stands up a new Deep Context graph with its own cryptographic identity. The ceremony is local-only because the Open Integrity inception commit must be signed by the first steward's own SSH key; no hosting platform's Actions runner has access to that key, so a single-click "Use this template" path cannot produce an inception with identity sovereignty flowing from the graph owner rather than from the runner's ephemeral token.

The skill runs in two phases. The first phase verifies prerequisites and walks a missing-prereq first steward through the install chain — Homebrew if absent, `gh` via Homebrew, and an SSH signing key generated and registered by `gh auth login -p ssh` (the modern `gh` flow generates a key if none exists and registers it with GitHub for both authentication and signing in one interactive walk), with git configured to use the key for signing. The second phase runs `.scripts/graph-inception.sh`, which reads the donor's DID from `.deep-context-identity.yml`, removes the cloned `.git` directory, produces a fresh Open-Integrity-signed root commit via `.scripts/oi-inception.sh`, commits the new graph's content signed by the first steward, and writes the new graph's DID back into `.deep-context-identity.yml`.

Inception runs once per graph. After it completes, the steward creates a new GitHub repository under their account, pushes, and enables Actions and Pages. The new graph may optionally claim **scion-of lineage** from the donor by recording `scion_of:` in `.deep-context-identity.yml` — but most graphs do not, because scion-of signals upstream-tracking intent (the rare parallel-fork case) rather than mere content adoption. The Decision backing the ceremony's shape is [[Decisions/Adopt Self-Sovereign Graph Publication]]↗.

## Steps

### Step 1: Confirm the user is ready to run Inception

Before touching prerequisites or running any ceremony commands, confirm with the user that they have cloned a Deep Context graph locally (or initialized a fresh directory) and want to turn this working directory into a new graph. Name what the ceremony does at a high level — it discards the donor's git history (in the cloned case), produces a fresh Open-Integrity-signed root commit with the steward's own SSH key, and commits the graph's initial content. Name what it cannot do — it cannot be signed by GitHub Actions, cannot be undone by a simple git command once the content commit lands, and requires an SSH key the user controls.

If the user has not cloned a donor graph yet, walk them through the clone step first: `git clone https://github.com/ChristopherA/DeepContext.com.git <graph-name>` and `cd <graph-name>`. If the user is in DeepContext.com itself rather than a fresh clone, stop — Inception is for new graphs, not for the donor being cloned from.

Also confirm intent on **scion-of lineage**: most new graphs are not scions, even when they began as a clone of a donor. A scion claim signals upstream-tracking intent (a parallel-fork case where vocabulary divergence among contributors needs structural support). If the user does not have that intent, run the script without the `--claim-scion-of` flag; the script will write `scion_of: null` to the identity file. If the user does want the scion claim, run the script with `--claim-scion-of` and the script will write the donor's DID under `scion_of:`.

### Step 2: Verify platform and package manager

Check the platform:

```sh
uname
```

If `Darwin` (macOS), the install chain uses Homebrew. If `Linux`, the install chain uses Homebrew or the distribution's package manager; the instructions below assume Homebrew for consistency, and the steward running on Linux may substitute `apt`/`dnf`/`pacman` for the equivalent packages.

Check whether Homebrew is installed:

```sh
command -v brew
```

If missing, offer to install it. Homebrew's install script requires an admin password and takes several minutes. Do not install without user consent. If consented, run:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After install, ensure the new `brew` shim is on PATH for the current session (the installer prints the two-line `eval "$(...)"` snippet to run).

### Step 3: Verify gh

Check whether `gh` (GitHub CLI) is installed:

```sh
command -v gh
```

If missing, install it:

```sh
brew install gh
```

Then ensure the user is authenticated:

```sh
gh auth status
```

If not authenticated, run `gh auth login` and walk the user through the interactive prompts. Choose HTTPS (for now; SSH auth is orthogonal to the SSH signing key the ceremony uses) and authenticate via web browser.

### Step 4: Verify an SSH signing key

Check whether git has a signing key configured:

```sh
git config user.signingkey
```

If empty, use `gh` to generate and register one. The `gh auth login -p ssh` flow walks an interactive prompt that generates a new SSH key (if none exists on disk), registers the key with GitHub, and in the modern flow offers to register it for **both authentication and signing** in a single walk:

```sh
gh auth login -p ssh
```

Follow the prompts: choose to generate a new SSH key, accept the default filename unless there's a reason not to, pick a passphrase or accept empty, and complete the browser handoff for authentication. When the flow asks about signing key upload, accept it — the generated key is registered as a signing key in the same step.

After `gh` completes, configure git to use the key for commit signing:

```sh
git config --global gpg.format ssh
git config --global user.signingkey "$HOME/.ssh/id_ed25519.pub"
```

(Adjust the path if `gh` placed the key under a different filename — the interactive flow reports the path.)

Verify the key is registered for signing:

```sh
gh ssh-key list
```

The output should show at least one entry with type `signing`. If the modern `gh auth login` flow did not register the key for signing on this user's install, add it explicitly:

```sh
gh ssh-key add ~/.ssh/id_ed25519.pub --type signing --title "Deep Context Graph Inception signing key"
```

### Step 5: Verify git identity

Check that `user.name` and `user.email` are set:

```sh
git config user.name
git config user.email
```

If either is empty, set them globally. The email should match the email on the user's GitHub account so the signing key is associated correctly with commits.

```sh
git config --global user.name "Name"
git config --global user.email "email@example.com"
```

### Step 6: Run the Inception script

With prerequisites satisfied, run (without the flag for the common non-scion case):

```sh
.scripts/graph-inception.sh
```

Or, if the new graph is intentionally claiming scion-of lineage (the rare parallel-fork-tracking case):

```sh
.scripts/graph-inception.sh --claim-scion-of
```

The script:

1. Reads the donor's `this_did` from `.deep-context-identity.yml`.
2. Touches `.deep-context-inception-in-progress` (the partial-resume flag, gitignored).
3. Removes the cloned `.git` directory (discards donor history).
4. Runs `.scripts/oi-inception.sh .` to produce a fresh empty Open-Integrity-signed root commit in the current directory.
5. Captures the new graph's DID from `git rev-parse HEAD`.
6. Updates `.deep-context-identity.yml`: `this_did` becomes the new DID; `scion_of` becomes the donor's DID if `--claim-scion-of` was passed, otherwise `null`.
7. Stages all working-tree content and commits it as the graph's initial content commit, signed by the first steward's SSH key.
8. Removes the partial-resume flag file.

If the script errors, read the error message and return to the appropriate step. The script's errors name which prerequisite is missing or which path is wrong; re-running after the fix is safe. If a previous attempt exited after the script removed `.git` but before the new inception commit landed, the partial-resume flag will still be present; on the next run, the script detects that state (no `.git`, flag present) and resumes from the inception step rather than failing. The unrecoverable case is a previously-incepted graph whose `.git` was lost without the flag present; the script reports that and points at re-cloning from the graph's remote.

### Step 7: Create the graph's GitHub repository

Create a new repository under the steward's GitHub account. Recommended via `gh`:

```sh
gh repo create <graph-name> --public --source=. --push
```

This creates the repository, adds it as `origin`, and pushes in one command. If `--public` is not desired, substitute `--private` (Pages requires a paid plan for private repos on some GitHub accounts; the ceremony does not depend on repository visibility).

Alternatively, create via the GitHub web UI, then:

```sh
git remote add origin https://github.com/<user>/<graph-name>.git
git push -u origin main
```

### Step 8: Enable Actions and Pages

Open the graph's repository settings on GitHub and configure:

- **Settings → Actions → General**: allow Actions to run (the default is often "Allow all actions and reusable workflows").
- **Settings → Pages**: set **Source** to **GitHub Actions**.

### Step 9: Push again to trigger the first build

Make any small content edit (or an empty commit) and push. The build-and-deploy Action runs and publishes the graph's Pages site with its own DID in the footer.

```sh
git commit --allow-empty -m "Trigger first Pages build"
git push
```

Monitor the Action at `https://github.com/<user>/<graph-name>/actions`. When it completes, the graph's site is live at the URL shown under **Settings → Pages**.

### Step 10: Report

Report the graph's identity to the user:

- The graph's DID (the `this_did` value in `.deep-context-identity.yml`).
- The `scion_of` value: either pointing at the donor's DID (if the graph claims scion-of lineage) or `null` (most graphs).
- The graph's GitHub URL and Pages URL.
- Any remaining post-Inception customization the steward plans (a custom domain, edits to `AGENTS.md` for graph-specific agent stance, first content revisions, recording `grafted_from::` edges on grafted nodes if traceability matters).

The graph is now a first-class Deep Context graph with its own cryptographic identity; subsequent work happens through ordinary git operations, not through Inception again.

## Scripts

### `.scripts/graph-inception.sh`

The wrapper script for the ceremony proper. POSIX-sh. Runs from the new graph's directory root. Accepts `--claim-scion-of` flag (default off) to record `scion_of:` in the identity file.

- **Inputs**: the current working directory must contain `.deep-context-identity.yml` and `.git` (a fresh clone of a Deep Context graph). Git signing configuration (`user.name`, `user.email`, `user.signingkey`) must be set and the signing key file must be readable.
- **Outputs**: `.git` rewritten with two signed commits (the Open Integrity inception commit plus the graph's initial content commit); `.deep-context-identity.yml` updated with the new graph's DID under `this_did`; `scion_of` set to the donor's DID if `--claim-scion-of` was passed, else `null`.
- **Failure modes**: missing prerequisite → exits with clear message naming the missing piece; partial run (script exited after removing `.git` but before completing inception) → re-running detects the partial-run state via the `.deep-context-inception-in-progress` flag file (no `.git`, flag present) and resumes from the inception step; previously-incepted graph lost `.git` without the flag present → unrecoverable from this script, re-clone from the graph's remote into a fresh directory; inconsistent state (`.git` present and flag present) → reports the inconsistency and refuses to proceed; signing failure → check that the signing key's public half is in GitHub allowed-signers and that `git config user.signingkey` points at the correct path.

### `.scripts/oi-inception.sh`

The Open Integrity inception primitive this skill's wrapper calls. Produces a fresh empty signed root commit establishing the new graph's `did:repo:<sha1>`. Not normally called directly by a user; the Graph Inception wrapper invokes it with the current directory as the target.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements. Sits alongside Graph Orient and Node Read as first-session skills a new graph's first steward walks through: Inception stands up the graph, Orient reads the inherited graph into context, Node Read drills into specific inherited nodes.

- grounded_in::[[Decisions/Adopt Self-Sovereign Graph Publication]]↗
  - The Decision this skill operationalizes. The Decision names what a Deep Context graph is (a self-sovereign repository with its own Open-Integrity-signed DID), why Inception must be local (Open Integrity signing requires the steward's SSH key, which Actions cannot access), and what file records the identity (`.deep-context-identity.yml` with `this_did` always, optional `scion_of` for the lineage-claim case). This skill is the concrete procedure that makes the Decision's commitments actionable for a first steward.

- grounded_in::[[References/Open Integrity Project (Blockchain Commons, 2025)]]↗
  - The cryptographic specification that makes a graph's DID identity-sovereign rather than hosting-derivative. The inception-commit ceremony, the SHA1-derived DID, the allowed-signers delegation model — all are Open Integrity moves this skill's script composes together.

- informs_downstream::[[scion_of -- content lineage from a template graph]]
  - The Predicate whose value this skill writes into `.deep-context-identity.yml` at step 6 of the script — conditionally on the `--claim-scion-of` flag. Most invocations leave `scion_of: null`; the flag is reserved for the parallel-fork-tracking case where the new graph intends to track the donor as upstream.

- informs_downstream::[[grafted_from -- per-node content provenance from a donor graph]]
  - The Predicate that records per-node content provenance independently of the graph-level scion-of claim. A graph that grafts content from a donor without claiming scion-of records the per-node provenance via `grafted_from::` edges (with the donor proxied by a Reference node in the recipient's `nodes/References/`). Inception sets up the graph's identity; `grafted_from::` edges document what content was carried over.

- composes_with::[[Graph Orient]]
  - Invoked after Inception completes to walk the newly-stood-up graph's content into context. Inception establishes the graph's identity; Orient establishes the graph's content understanding for subsequent work.

- composes_with::[[Node Read]]
  - Invoked alongside Graph Orient in the graph's first session to drill into specific nodes the steward wants to understand in depth. Inception produces the graph; Graph Orient walks the content at breadth; Node Read walks specific nodes at depth. Together the three form the standard first-session triad for a new graph's first steward.
