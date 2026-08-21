#!/usr/bin/env bash
# Convert .md files in notes/ and problems/ to .html using pandoc + Carnap→MC transformer.
# notes/    -> Tufte template
# problems/ -> minimal template matching the course pages
# Usage: bash scripts/convert_notes.sh
set -e

TRANSFORMER="scripts/carnap_to_mc.py"

shopt -s nullglob

for dir in notes problems; do
  [ -d "$dir" ] || continue

  case "$dir" in
    notes)    TEMPLATE="scripts/tufte-template.html" ;;
    problems) TEMPLATE="scripts/minimal-template.html" ;;
  esac

  for src in "$dir"/*.md; do
    base=$(basename "$src" .md)
    tmp="/tmp/${base}-raw.html"
    dst="$dir/${base}.html"

    echo "Converting $src → $dst  (${TEMPLATE##*/})"

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
