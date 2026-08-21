#!/usr/bin/env bash
# Convert .md files in notes/ and problems/ to .html using pandoc + Carnap→MC transformer.
# Usage: bash scripts/convert_notes.sh
set -e

TEMPLATE="scripts/tufte-template.html"
TRANSFORMER="scripts/carnap_to_mc.py"
DIRS=(notes problems)

shopt -s nullglob

for dir in "${DIRS[@]}"; do
  [ -d "$dir" ] || continue

  for src in "$dir"/*.md; do
    base=$(basename "$src" .md)
    tmp="/tmp/${base}-raw.html"
    dst="$dir/${base}.html"

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
done

echo "All markdown converted."
