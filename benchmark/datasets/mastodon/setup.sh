#!/usr/bin/env bash
# Clone the Mastodon source repo at the pinned commit into ./source/
# Run this once before synthesis. The source/ directory is gitignored.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$SCRIPT_DIR/source"
COMMIT="$(cat "$SCRIPT_DIR/MASTODON_COMMIT")"

if [ -d "$TARGET/.git" ]; then
    echo "source/ already exists. To re-fetch, delete it first."
    exit 0
fi

echo "Cloning mastodon/mastodon at $COMMIT..."
git clone --no-checkout https://github.com/mastodon/mastodon.git "$TARGET"
cd "$TARGET"
git checkout "$COMMIT"
echo "Done. Mastodon source tree is at $TARGET"
