# PHIL 452 — Modal Logic

Lecture notes, slides, and problem sets for PHIL 452. Mirrors the structure of
the [220](https://github.com/gabriel-uzquiano/220) repository.

Published at <https://gabriel-uzquiano.github.io/452/>.
Course page: <https://gabriel-uzquiano.github.io/courses/452>.
Textbook: <https://gabriel-uzquiano.github.io/modal-logic/>.

## Layout

| Folder | Contents |
|---|---|
| `notes/` | Lecture notes in markdown. Built to HTML automatically. |
| `slides/` | Quarto revealjs decks (`.qmd`). Rendered locally. |
| `problems/` | Problem sets for the six problem sessions. |
| `solutions/` | Solutions. **Git-ignored — never committed.** |
| `scripts/` | `convert_notes.sh`, the pandoc template, the Carnap transformer. |
| `shared/` | CSS shared by the notes pages. |

## Editing notes

Write markdown in `notes/`. On push to `main`, the
`Build lecture notes` action runs `scripts/convert_notes.sh`, which converts each
`notes/*.md` to `notes/*.html` with pandoc and the Tufte template, then commits
the HTML back.

To build locally instead:

```bash
bash scripts/convert_notes.sh
```

## Editing slides

Open the `.Rproj` in RStudio, open a file in `slides/`, click **Render**.

Keep `.qmd` files in **Source** mode, not Visual.

Quarto ships inside RStudio. For terminal use:

```bash
export PATH="/Applications/RStudio.app/Contents/Resources/app/quarto/bin:$PATH"
quarto render slides/1.1-relations-slides.qmd
```

Rendering produces `slides/<name>.html` plus a `slides/<name>_files/` folder.
The `_files` folders are git-ignored; commit the HTML if you want the deck online.

## Publishing

`.nojekyll` is present, so GitHub Pages serves the HTML untouched rather than
running it through Jekyll.

## Solutions

`solutions/` is in `.gitignore` because this repository is public.

The problem and solution files each carry a JavaScript `prompt()` gate with the
password `MHP102`. That is **not** access control: the password sits in the page
source, and the content is in the DOM before the check runs. Treat those files as
fully public once pushed.
