#!/usr/bin/env bash
# Convert all .md files in notes/ to .html using pandoc + Carnap→MC transformer.
# Usage: bash scripts/convert_notes.sh
set -e

TEMPLATE="scripts/tufte-template.html"
TRANSFORMER="scripts/carnap_to_mc.py"
NOTES_DIR="notes"

for src in "$NOTES_DIR"/*.md; do
  base=$(basename "$src" .md)
  tmp="/tmp/${base}-raw.html"
  dst="$NOTES_DIR/${base}.html"

  echo "Converting $src → $dst"

  pandoc \
    --from markdown+definition_lists+smart+tex_math_dollars \
    --to html5 \
    --template "$TEMPLATE" \
    --mathjax \
    --no-highlight \
    "$src" -o "$tmp"

  python3 "$TRANSFORMER" "$tmp" "$dst"
done

echo "All notes converted."
