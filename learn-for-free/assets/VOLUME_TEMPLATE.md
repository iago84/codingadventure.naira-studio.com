# Volume source format (Markdown -> PDF)

Every volume is a single Markdown file in `src/`. `build.py` converts it to an A4
PDF in `pdf/` with a cover page, clickable table of contents, PDF bookmarks,
running headers, page numbers, syntax-highlighted code and styled tables.

## Front matter

The file must start with a YAML-ish block between `---` lines:

```markdown
---
title: Vol. 01 - HTML
technology: HTML
vol: 01
source: html.com
date: 2026-10-10
level: Beginner to intermediate
hours: 20
subtitle: Structure, content and semantics for the web
---
```

| Key | Meaning | Used for |
|-----|---------|----------|
| `title` | full volume title | PDF metadata, header, cover |
| `technology` | short name | cover page main title |
| `vol` | volume number | cover "VOL. NN" label |
| `source` | source site | cover metadata table |
| `date` | generation date | cover + metadata |
| `level` | audience level | cover metadata table |
| `hours` | estimated study time | cover metadata table |
| `subtitle` | one-line description | cover subtitle |

## Structure of a volume

```markdown
# How to use this volume        <- chapter 1 (h1)
...

# Chapter N - Title             <- chapter (h1), appears in TOC level 0
## Summary                      <- section (h2), TOC level 1
- 5 to 10 bullet points

## Concepts                     <- section
Explanation, tables, diagrams.

## Examples                     <- section
```python
# code
```

## Common mistakes and best practices

## Practice exercises

### Solutions

## Mini test

### Answer key and explanations

# Cheat sheet                  <- final chapter
# Final test                   <- final chapter
## Final test answers
# Sources                      <- final chapter
```

Rules:

- `#` = chapter (TOC level 0 + bookmark), `##` = section (TOC level 1 +
  bookmark), `###`/`####` = sub-heading (bookmark only).
- Chapter sections are auto-numbered as `N.M` (Chapter N, Section M).
- Section names above are the convention, but any name works.

## Markdown supported

| Feature | Syntax | Result |
|---------|--------|--------|
| Bold | `**text**` | bold |
| Italic | `*text*` | italic |
| Inline code | `` `code` `` | monospace, muted colour |
| Links | `[label](https://...)` | clickable link |
| Lists | `- item` / `1. item` | bullets / numbers (2-level nesting by indent) |
| Task lists | `- [x] done` / `- [ ] todo` | checkbox glyphs |
| Tables | `\| a \| b \|` with `\|---\|---\|` | styled table, repeating header |
| Code | ` ```lang ` fenced blocks | highlighted, line numbers, language label |
| Quotes | `> text` | yellow callout with left bar |
| Admonitions | `> [!TIP]`, `[!NOTE]`, `[!WARNING]`, `[!IMPORTANT]`, `[!CAUTION]` | coloured callout |
| Rule | `---` | horizontal rule |
| Headings | `#` .. `####` | chapter / section / subsection |

Code language aliases understood by the highlighter: `html`, `css`, `js`,
`javascript`, `ts`, `typescript`, `jsx`, `tsx`, `py`, `python`, `java`, `c`,
`cpp`, `cs`, `go`, `rust`, `php`, `sql`, `json`, `yaml`, `bash`, `sh`, `console`,
`diff`, `http`, `vue`, `swift`, `kotlin`, `solidity`, `graphql`, `ini`,
`dockerfile`, `makefile`, `nginx`, `powershell`, `text` (no highlighting).

## Writing style rules

1. English only, beginner-to-intermediate.
2. Original writing. Paraphrase the source; never copy passages, images or full
   code blocks. Short attributed snippets only when unavoidable.
3. Every code example must actually run (or compile). Show the expected output.
4. Every question must have an answer with a brief explanation.
5. Cite every consulted page in `# Sources`.

## Build

```bash
python build.py 01-html      # one volume
python build.py --all        # every volume in src/
python build.py --new 42 fable js example.com
./build.sh 01-html           # wrapper (git-bash / WSL)
```
