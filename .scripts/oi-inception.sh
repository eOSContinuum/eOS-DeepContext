#!/bin/sh
# Create an Open Integrity Project inception commit in a fresh repository.
#
# Portable POSIX-sh equivalent of z_Create_Inception_Repository in Blockchain
# Commons' _Z_Utils.zsh library (the authoritative implementation used by
# ~/.bin/setup_git_inception_repo.sh and by DeepContext.com's own root commit).
#
# The two -m commit-message lines plus the --signoff trailer produce the
# canonical OI inception message: subject, canonical body, Signed-off-by
# trailer carrying the committer's SSH-key SHA256 fingerprint. Given the
# same author, committer key, and commit timestamp, this script and the
# zsh authoritative implementation produce byte-identical commit bytes
# and therefore identical did:repo:<sha1> values.
#
# Usage:
#   .scripts/oi-inception.sh                      # creates ./new_open_integrity_repo/
#   .scripts/oi-inception.sh ./my-graph-dir        # creates at the named path
#   .scripts/oi-inception.sh --force ./existing   # overwrite check: refuses unless --force
#
# Prerequisites (checked at runtime):
#   - git config user.name
#   - git config user.email
#   - git config user.signingkey pointing at an SSH private or public key
#   - ssh-keygen, git, awk, date in PATH

set -eu

force=0
target=""

while [ $# -gt 0 ]; do
    case "$1" in
        -f|--force)
            force=1
            shift
            ;;
        -h|--help)
            sed -n '3,25p' "$0" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        -*)
            printf 'Error: unknown option: %s\n' "$1" >&2
            exit 64
            ;;
        *)
            if [ -z "$target" ]; then
                target="$1"
                shift
            else
                printf 'Error: unexpected argument: %s\n' "$1" >&2
                exit 64
            fi
            ;;
    esac
done

: "${target:=$(pwd)/new_open_integrity_repo}"

case "$target" in
    /*) ;;
    *) target="$(pwd)/$target" ;;
esac

if [ -d "$target/.git" ] && [ "$force" -ne 1 ]; then
    printf 'Error: repository already exists at %s (use --force to proceed anyway)\n' "$target" >&2
    exit 73
fi

SIGNING_KEY="$(git config user.signingkey || true)"
GIT_AUTHOR_NAME="$(git config user.name || true)"
GIT_AUTHOR_EMAIL="$(git config user.email || true)"

if [ -z "$SIGNING_KEY" ]; then
    printf 'Error: git config user.signingkey is not set\n' >&2
    exit 78
fi
if [ -z "$GIT_AUTHOR_NAME" ] || [ -z "$GIT_AUTHOR_EMAIL" ]; then
    printf 'Error: git config user.name or user.email is not set\n' >&2
    exit 78
fi
if [ ! -r "$SIGNING_KEY" ]; then
    printf 'Error: signing key not readable at %s\n' "$SIGNING_KEY" >&2
    exit 66
fi

GIT_COMMITTER_NAME="$(ssh-keygen -E sha256 -lf "$SIGNING_KEY" 2>/dev/null | awk '{print $2}')"
if [ -z "$GIT_COMMITTER_NAME" ]; then
    printf 'Error: failed to extract SHA256 fingerprint from %s\n' "$SIGNING_KEY" >&2
    exit 78
fi

GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
GIT_AUTHOR_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"

export GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL GIT_AUTHOR_DATE GIT_COMMITTER_DATE

mkdir -p "$target"
git -C "$target" init --quiet

git -C "$target" \
    -c gpg.format=ssh \
    -c user.signingkey="$SIGNING_KEY" \
    commit --allow-empty --no-edit --gpg-sign --signoff \
    -m "Initialize repository and establish a SHA-1 root of trust" \
    -m "This key also certifies future commits' integrity and origin. Other keys can be authorized to add additional commits via the creation of a ./.repo/config/verification/allowed_commit_signers file. This file must initially be signed by this repo's inception key, granting these keys the authority to add future commits to this repo, including the potential to remove the authority of this inception key for future commits. Once established, any changes to ./.repo/config/verification/allowed_commit_signers must be authorized by one of the previously approved signers."

commit_sha="$(git -C "$target" rev-parse HEAD)"
printf 'Inception commit created at %s\n' "$target"
printf 'did:repo:%s\n' "$commit_sha"
