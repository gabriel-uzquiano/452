#!/usr/bin/env bash
# Convert .md files in notes/ and problems/ (plus .qmd files in problems/) to .html using pandoc + Carnap→MC transformer.
# notes/    -> Tufte template
# problems/ -> minimal template matching the course pages
#
# Title handling: a YAML "title:" in the .md wins. If there is none, the first
# level-1/2 heading is promoted to the title and removed from the body, so the
# template's <h1> is never empty.
#
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

  srcs=("$dir"/*.md)
  [ "$dir" = problems ] && srcs+=("$dir"/*.qmd)

  for src in "${srcs[@]}"; do
    base=$(basename "$src"); base="${base%.*}"
    tmp="/tmp/${base}-raw.html"
    dst="$dir/${base}.html"
    input="$src"

    # A title in the YAML block, if the file has one.
    title=""
    if [ "$(head -n 1 "$src")" = "---" ]; then
      title=$(awk 'NR>1 && /^---[[:space:]]*$/ {exit}
                   /^title:[[:space:]]*/ {
                     sub(/^title:[[:space:]]*/, "")
                     gsub(/^"|"$/, "")
                     gsub(/^'"'"'|'"'"'$/, "")
                     print; exit }' "$src")
    fi

    # Otherwise fall back to the first heading, and drop it from the body.
    if [ -z "$title" ]; then
      title=$(grep -m 1 -E '^#{1,2}[[:space:]]+' "$src" 2>/dev/null \
              | sed -E 's/^#{1,2}[[:space:]]+//; s/&nbsp;/ /g; s/[[:space:]]+$//')
      if [ -n "$title" ]; then
        input="/tmp/${base}-body.md"
        awk '!dropped && /^#{1,2}[[:space:]]+/ { dropped = 1; next } { print }' "$src" > "$input"
      fi
    fi

    if [ -n "$title" ]; then
      echo "Converting $src → $dst  (${TEMPLATE##*/})  [$title]"
    else
      echo "Converting $src → $dst  (${TEMPLATE##*/})  [no title found]"
    fi

    pandoc \
      --from markdown+definition_lists+smart+tex_math_dollars \
      --to html5 \
      --template "$TEMPLATE" \
      --metadata title="$title" \
      --mathjax \
      --no-highlight \
      "$input" -o "$tmp"

    python3 "$TRANSFORMER" "$tmp" "$dst"
  done
done

echo "All markdown converted."
