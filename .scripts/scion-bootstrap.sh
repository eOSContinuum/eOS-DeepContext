#!/bin/sh
# Orchestrates the Scion Bootstrap ceremony that turns a cloned DeepContext
# graph into a scion with its own Open Integrity inception commit and DID.
#
# Prerequisites the script checks for but does not install (the invoking
# skill walks a missing-prereq user through brew/gh/ssh-keygen install):
#   - git config user.name, user.email, user.signingkey
#   - signing key file readable at user.signingkey
#   - ssh-keygen on PATH
#   - The current directory contains a cloned DeepContext graph
#     (.scion-identity.yml present, .git present).
#
# Ceremony the script performs:
#   1. Reads the template's this_did from .scion-identity.yml
#   2. Removes the cloned .git directory (discards template history)
#   3. Runs .scripts/scion-inception.sh . to produce a fresh empty
#      OI-signed root commit (the scion's new inception)
#   4. Updates .scion-identity.yml: this_did becomes the scion's new DID,
#      scion_of becomes the template's former this_did
#   5. Stages all working-tree content and commits it as the scion's
#      initial content commit (signed by the first steward)
#
# Partial-run recovery:
#   If a previous run removed .git but exited before completing inception,
#   .scion-identity.yml is still in template state (scion_of: null). The
#   script detects this case and resumes from step 3 rather than failing.
#   If .git is missing but scion_of is set (a bootstrapped scion lost its
#   .git), the script reports that re-clone from the remote is required.
#
# Usage:
#   .scripts/scion-bootstrap.sh           # Bootstrap in the current directory
#   .scripts/scion-bootstrap.sh --help    # Print usage and exit

set -eu

show_help() {
    sed -n '2,32p' "$0" | sed 's/^# \{0,1\}//'
}

case "${1:-}" in
    -h|--help)
        show_help
        exit 0
        ;;
esac

REPO_ROOT="$(pwd)"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- Prerequisites ---

if [ ! -f "$REPO_ROOT/.scion-identity.yml" ]; then
    printf 'Error: .scion-identity.yml not found at %s\n' "$REPO_ROOT" >&2
    printf 'Run this script from the root of a cloned DeepContext graph.\n' >&2
    exit 66
fi

partial_resume=0
if [ ! -d "$REPO_ROOT/.git" ]; then
    # Distinguish two missing-.git states:
    #   (a) Partial-run recovery: a previous Bootstrap removed .git but exited
    #       before completing inception. .scion-identity.yml is unchanged
    #       (scion_of: null), so this_did still records the template's DID
    #       and we can resume from the inception step.
    #   (b) Bootstrapped-scion lost .git: scion_of is set, meaning Bootstrap
    #       previously completed. The scion's history lives only on its
    #       remote at this point and cannot be reconstructed by this script.
    scion_of_value="$(sed -n 's/^scion_of:[[:space:]]*//p' "$REPO_ROOT/.scion-identity.yml" | head -n 1)"
    case "$scion_of_value" in
        null|"")
            printf 'Detected partial-run state: no .git, .scion-identity.yml unchanged.\n'
            printf 'Resuming Bootstrap from the inception step.\n\n'
            partial_resume=1
            ;;
        *)
            printf 'Error: no .git directory at %s\n' "$REPO_ROOT" >&2
            printf '  scion_of: %s\n' "$scion_of_value" >&2
            printf '\n' >&2
            printf 'This directory carries a bootstrapped scion identity (scion_of is set)\n' >&2
            printf 'but its .git is missing. The scion'\''s commit history lives only on its\n' >&2
            printf 'remote at this point and cannot be reconstructed by Bootstrap. Re-clone\n' >&2
            printf 'the scion'\''s repository into a fresh directory and resume work there:\n' >&2
            printf '\n' >&2
            printf '  git clone <scion-repo-url> <fresh-dir>\n' >&2
            printf '\n' >&2
            printf 'Bootstrap re-roots a fresh clone of a template; it does not reconstruct\n' >&2
            printf 'an already-bootstrapped scion'\''s lost .git.\n' >&2
            exit 66
            ;;
    esac
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
    printf 'Configure all three, then re-run. The invoking Scion Bootstrap skill\n' >&2
    printf 'walks a missing-prereq user through the brew/gh/ssh-keygen install chain.\n' >&2
    exit 78
fi

if [ ! -r "$SIGNING_KEY" ]; then
    printf 'Error: signing key not readable at %s\n' "$SIGNING_KEY" >&2
    exit 66
fi

# --- Read template DID ---

template_did="$(sed -n 's/^this_did:[[:space:]]*//p' "$REPO_ROOT/.scion-identity.yml" | head -n 1)"
if [ -z "$template_did" ]; then
    printf 'Error: could not read this_did from .scion-identity.yml\n' >&2
    exit 65
fi

printf 'Template DID: %s\n' "$template_did"

# --- Remove .git ---

if [ "$partial_resume" -eq 0 ]; then
    printf 'Removing %s/.git (discarding template history)...\n' "$REPO_ROOT"
    rm -rf "$REPO_ROOT/.git"
else
    printf 'Skipping .git removal (already absent from prior partial run).\n'
fi

# --- Run OI inception ---

printf 'Running Open Integrity inception ceremony...\n'
"$SCRIPT_DIR/scion-inception.sh" "$REPO_ROOT"

new_did="did:repo:$(git -C "$REPO_ROOT" rev-parse HEAD)"
printf 'Scion DID: %s\n' "$new_did"

# --- Update .scion-identity.yml ---
#
# Portable in-place edit: write to a temp file, then replace.
printf 'Updating .scion-identity.yml...\n'

awk -v new_did="$new_did" -v scion_of="$template_did" '
    /^this_did:/ { print "this_did: " new_did; next }
    /^scion_of:/ { print "scion_of: " scion_of; next }
    { print }
' "$REPO_ROOT/.scion-identity.yml" > "$REPO_ROOT/.scion-identity.yml.new"
mv "$REPO_ROOT/.scion-identity.yml.new" "$REPO_ROOT/.scion-identity.yml"

# --- Stage and commit content ---

printf 'Staging scion content and committing as initial content commit...\n'
git -C "$REPO_ROOT" add .

git -C "$REPO_ROOT" \
    -c gpg.format=ssh \
    -c user.signingkey="$SIGNING_KEY" \
    commit --gpg-sign --signoff \
    -m "Initialize scion content from template" \
    -m "Template DID: $template_did" \
    -m "Scion DID:    $new_did"

printf '\nScion Bootstrap complete.\n'
printf '  Scion DID:    %s\n' "$new_did"
printf '  scion_of:     %s\n' "$template_did"
printf '\nNext steps:\n'
printf '  1. Create a new GitHub repository under your account:\n'
printf '       gh repo create <scion-name> --public --source=. --push\n'
printf '     (or use the GitHub web UI, then add the remote and push).\n'
printf '  2. In Settings -> Actions -> General, allow Actions to run.\n'
printf '  3. In Settings -> Pages, set Source = GitHub Actions.\n'
printf '  4. Subsequent pushes will build and deploy your Pages site.\n'
