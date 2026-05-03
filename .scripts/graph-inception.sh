#!/bin/sh
# Orchestrates the Graph Inception ceremony that turns a cloned Deep Context
# graph (or a fresh-init directory) into a new graph with its own Open
# Integrity inception commit and DID. The new graph may optionally claim
# scion-of lineage from the donor; default behavior is to leave scion_of
# null (the graph is its own thing, not a scion).
#
# Prerequisites the script checks for but does not install (the invoking
# skill walks a missing-prereq user through brew/gh/ssh-keygen install):
#   - git config user.name, user.email, user.signingkey
#   - signing key file readable at user.signingkey
#   - ssh-keygen on PATH
#   - The current directory contains a cloned Deep Context graph
#     (.deep-context-identity.yml present, .git present).
#
# Ceremony the script performs:
#   1. Reads the donor's this_did from .deep-context-identity.yml
#   2. Touches .deep-context-inception-in-progress as the partial-resume flag
#   3. Removes the cloned .git directory (discards donor history)
#   4. Runs .scripts/oi-inception.sh . to produce a fresh empty
#      OI-signed root commit (the new graph's inception)
#   5. Updates .deep-context-identity.yml: this_did becomes the new graph's
#      own DID. If --claim-scion-of was passed, scion_of becomes the donor's
#      former this_did; otherwise scion_of is set to null. Most graphs are
#      not scions: they grafted content from a donor without intending to
#      track the donor as upstream, and the lineage claim does not apply.
#      Pass --claim-scion-of only when the new graph is intentionally a
#      parallel-fork-tracking scion.
#   6. Stages all working-tree content and commits it as the graph's
#      initial content commit (signed by the first steward)
#   7. Removes the partial-resume flag file
#
# Partial-run recovery:
#   The presence of .deep-context-inception-in-progress (created at step 2,
#   removed at step 7) signals that a previous run did not complete. If the
#   flag exists and .git is missing, the script resumes from step 4 (re-runs
#   inception). If the flag exists and .git is present, the script reports
#   the inconsistent state and refuses to proceed; the user can either
#   remove the flag manually after verifying state, or restart from a fresh
#   clone. If the flag does not exist and .git is missing, the directory
#   carries a previously-incepted graph whose .git was lost; this script
#   cannot reconstruct it (the commit history lives only on the remote at
#   that point) and reports the unrecoverable state.
#
# Usage:
#   .scripts/graph-inception.sh                       # Inception in current directory, scion_of: null
#   .scripts/graph-inception.sh --claim-scion-of      # Inception with scion-of lineage claim
#   .scripts/graph-inception.sh --help                # Print usage and exit

set -eu

show_help() {
    sed -n '2,46p' "$0" | sed 's/^# \{0,1\}//'
}

claim_scion_of=0
for arg in "$@"; do
    case "$arg" in
        -h|--help)
            show_help
            exit 0
            ;;
        --claim-scion-of)
            claim_scion_of=1
            ;;
        *)
            printf 'Error: unrecognized argument: %s\n' "$arg" >&2
            printf 'Run --help for usage.\n' >&2
            exit 64
            ;;
    esac
done

REPO_ROOT="$(pwd)"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
FLAG_FILE="$REPO_ROOT/.deep-context-inception-in-progress"

# --- Prerequisites ---

if [ ! -f "$REPO_ROOT/.deep-context-identity.yml" ]; then
    printf 'Error: .deep-context-identity.yml not found at %s\n' "$REPO_ROOT" >&2
    printf 'Run this script from the root of a cloned Deep Context graph.\n' >&2
    exit 66
fi

# --- Partial-resume detection (flag-file based) ---

partial_resume=0
flag_present=0
if [ -f "$FLAG_FILE" ]; then
    flag_present=1
fi

if [ ! -d "$REPO_ROOT/.git" ]; then
    if [ "$flag_present" -eq 1 ]; then
        printf 'Detected partial-run state: no .git, inception-in-progress flag present.\n'
        printf 'Resuming Inception from the OI-inception step.\n\n'
        partial_resume=1
    else
        printf 'Error: no .git directory at %s\n' "$REPO_ROOT" >&2
        printf '\n' >&2
        printf 'No inception-in-progress flag is present, so this is not a partial-run\n' >&2
        printf 'state from this script. The directory may carry a previously-incepted\n' >&2
        printf 'graph whose .git was lost; in that case the commit history lives only\n' >&2
        printf 'on the remote and cannot be reconstructed by Inception. Re-clone the\n' >&2
        printf 'graph'\''s repository into a fresh directory and resume work there:\n' >&2
        printf '\n' >&2
        printf '  git clone <graph-repo-url> <fresh-dir>\n' >&2
        printf '\n' >&2
        printf 'Inception re-roots a fresh clone of a donor; it does not reconstruct\n' >&2
        printf 'a previously-incepted graph'\''s lost .git.\n' >&2
        exit 66
    fi
elif [ "$flag_present" -eq 1 ]; then
    printf 'Error: inconsistent state: .git present and inception-in-progress flag present.\n' >&2
    printf '\n' >&2
    printf 'A previous run created the flag but did not complete the ceremony, yet\n' >&2
    printf 'the .git directory still exists. Either:\n' >&2
    printf '  - Remove the flag manually after verifying this state was expected:\n' >&2
    printf '      rm %s\n' "$FLAG_FILE" >&2
    printf '  - Or restart from a fresh clone of the donor graph.\n' >&2
    exit 66
fi

if ! command -v ssh-keygen >/dev/null 2>&1; then
    printf 'Error: ssh-keygen not found on PATH.\n' >&2
    exit 69
fi

SIGNING_KEY="$(git config user.signingkey 2>/dev/null || true)"
AUTHOR_NAME="$(git config user.name 2>/dev/null || true)"
AUTHOR_EMAIL="$(git config user.email 2>/dev/null || true)"

if [ -z "$SIGNING_KEY" ] || [ -z "$AUTHOR_NAME" ] || [ -z "$AUTHOR_EMAIL" ]; then
    printf 'Error: git signing configuration is incomplete.\n' >&2
    printf '  user.signingkey: %s\n' "${SIGNING_KEY:-(unset)}" >&2
    printf '  user.name:       %s\n' "${AUTHOR_NAME:-(unset)}" >&2
    printf '  user.email:      %s\n' "${AUTHOR_EMAIL:-(unset)}" >&2
    printf 'Configure all three, then re-run. The invoking Graph Inception skill\n' >&2
    printf 'walks a missing-prereq user through the brew/gh/ssh-keygen install chain.\n' >&2
    exit 78
fi

if [ ! -r "$SIGNING_KEY" ]; then
    printf 'Error: signing key not readable at %s\n' "$SIGNING_KEY" >&2
    exit 66
fi

# --- Read donor DID ---

donor_did="$(sed -n 's/^this_did:[[:space:]]*//p' "$REPO_ROOT/.deep-context-identity.yml" | head -n 1)"
if [ -z "$donor_did" ]; then
    printf 'Error: could not read this_did from .deep-context-identity.yml\n' >&2
    exit 65
fi

printf 'Donor DID: %s\n' "$donor_did"
if [ "$claim_scion_of" -eq 1 ]; then
    printf 'Scion-of lineage claim: yes (--claim-scion-of)\n'
else
    printf 'Scion-of lineage claim: no (default; pass --claim-scion-of to claim)\n'
fi

# --- Touch the partial-resume flag and remove .git ---

if [ "$partial_resume" -eq 0 ]; then
    : > "$FLAG_FILE"
    printf 'Removing %s/.git (discarding donor history)...\n' "$REPO_ROOT"
    rm -rf "$REPO_ROOT/.git"
else
    printf 'Skipping .git removal (already absent from prior partial run).\n'
fi

# --- Run OI inception ---

printf 'Running Open Integrity inception ceremony...\n'
"$SCRIPT_DIR/oi-inception.sh" "$REPO_ROOT"

new_did="did:repo:$(git -C "$REPO_ROOT" rev-parse HEAD)"
printf 'New graph DID: %s\n' "$new_did"

# --- Update .deep-context-identity.yml ---
#
# Portable in-place edit: write to a temp file, then replace.
printf 'Updating .deep-context-identity.yml...\n'

if [ "$claim_scion_of" -eq 1 ]; then
    scion_of_value="$donor_did"
else
    scion_of_value="null"
fi

awk -v new_did="$new_did" -v scion_of="$scion_of_value" '
    /^this_did:/ { print "this_did: " new_did; next }
    /^scion_of:/ { print "scion_of: " scion_of; next }
    { print }
' "$REPO_ROOT/.deep-context-identity.yml" > "$REPO_ROOT/.deep-context-identity.yml.new"
mv "$REPO_ROOT/.deep-context-identity.yml.new" "$REPO_ROOT/.deep-context-identity.yml"

# --- Stage and commit content ---

if [ "$claim_scion_of" -eq 1 ]; then
    commit_subject="Initialize graph content from donor (scion-of claimed)"
else
    commit_subject="Initialize graph content from donor"
fi

printf 'Staging graph content and committing as initial content commit...\n'
git -C "$REPO_ROOT" add .

git -C "$REPO_ROOT" \
    -c gpg.format=ssh \
    -c user.signingkey="$SIGNING_KEY" \
    commit --gpg-sign --signoff \
    -m "$commit_subject" \
    -m "Donor DID:     $donor_did" \
    -m "New graph DID: $new_did" \
    -m "scion_of:      $scion_of_value"

# --- Clean up partial-resume flag ---

rm -f "$FLAG_FILE"

printf '\nGraph Inception complete.\n'
printf '  New graph DID: %s\n' "$new_did"
printf '  scion_of:      %s\n' "$scion_of_value"
printf '\nNext steps:\n'
printf '  1. Create a new GitHub repository under your account:\n'
printf '       gh repo create <graph-name> --public --source=. --push\n'
printf '     (or use the GitHub web UI, then add the remote and push).\n'
printf '  2. In Settings -> Actions -> General, allow Actions to run.\n'
printf '  3. In Settings -> Pages, set Source = GitHub Actions.\n'
printf '  4. Subsequent pushes will build and deploy your Pages site.\n'
