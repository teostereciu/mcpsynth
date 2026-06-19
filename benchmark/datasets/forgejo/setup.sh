#!/usr/bin/env bash
# Clone the Forgejo source repo at the pinned commit into ./source/
# Run this once before synthesis. The source/ directory is gitignored.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$SCRIPT_DIR/source"
COMMIT="$(cat "$SCRIPT_DIR/FORGEJO_COMMIT")"

if [ -d "$TARGET/.git" ]; then
    echo "source/ already exists. To re-fetch, delete it first."
    exit 0
fi

echo "Cloning forgejo/forgejo at $COMMIT..."
git clone --no-checkout https://codeberg.org/forgejo/forgejo.git "$TARGET"
cd "$TARGET"
git checkout "$COMMIT"
echo "Done. Forgejo source tree is at $TARGET"
