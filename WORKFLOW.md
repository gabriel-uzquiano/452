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

Write or edit a `.qmd` in `slides/` and push (or upload) it to `main`. The
`Build and deploy site` action installs Quarto 1.9.38 and renders every
`slides/*.qmd` to `slides/<name>.html` plus `slides/<name>_files/` before
publishing, so there is no need to render locally or commit the HTML.

Keep `.qmd` files in **Source** mode, not Visual.

To preview locally, open the `.Rproj` in RStudio, open a file in `slides/`, and
click **Render**. Any HTML you commit is overwritten by the fresh render on the
site.

## Publishing

`.nojekyll` is present, so GitHub Pages serves the HTML untouched rather than
running it through Jekyll.

## Solutions

`solutions/` is in `.gitignore` because this repository is public.

The problem and solution files each carry a JavaScript `prompt()` gate with the
password `MHP102`. That is **not** access control: the password sits in the page
source, and the content is in the DOM before the check runs. Treat those files as
fully public once pushed.
