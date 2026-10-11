# Authoring guide for new volumes

Read this before writing a volume. It is the contract every `src/*.md` file
follows, so all 36 PDFs look and behave the same.

## File and front matter

One file per volume: `src/<NN>-<tech>.md`. It **must** start with:

```markdown
---
title: Vol. 04 - React
technology: React
vol: 04
source: react.dev
date: 2026-10-10
level: Intermediate
hours: 30
subtitle: One line, sentence case, no full stop
---
```

`source` is the site actually used as the syllabus. If the technology's plan file
says the original source is unreachable, login-gated or paywalled, use the
fallback named in `plan/ISSUES.md` and name that here.

## Required skeleton, in this order

```markdown
# How to use this volume
   prerequisites, estimated study time, how the chapters work,
   how to run the code (one bash block)
## Chapter map
   a table: # | Chapter | You will learn

# Chapter 1 - <Title>
## Summary                    5 to 10 bullet points, each one full sentence
## Concepts                   plain explanation + tables or ASCII diagrams
## Examples                   numbered examples, fenced code + expected output
## Common mistakes and best practices
                              a table: Mistake | Why it hurts | Best practice
## Practice exercises         3 to 5 questions
### Solutions                 one solution per exercise
## Mini test                  5 to 10 questions (multiple choice, true/false,
                              short code question)
### Answer key and explanations
                              every answer with a one-line explanation

# Chapter 2 - ...
   ... same six sections ...
   (aim for 8 to 14 content chapters; more only if the plan demands it)

# Cheat sheet                 1 to 2 pages of compact reference tables
# Final test                   20 to 30 mixed questions covering the whole book
## Final test answers          every answer with a short explanation
# Sources                      the URL of every page consulted
```

Section names are fixed: `## Summary`, `## Concepts`, `## Examples`,
`## Common mistakes and best practices`, `## Practice exercises`,
`### Solutions`, `## Mini test`, `### Answer key and explanations`.

## Markdown that the build supports

| Write | Get |
|-------|-----|
| `**bold**`, `*italic*` | bold, italic |
| `` `code` `` | inline monospace |
| `[label](https://...)` | clickable link |
| `- item`, `1. item`, `- [x] done` | bullets, numbers, checkboxes |
| `\| a \| b \|` + `\|---\|---\|` | styled table with a repeating header |
| ` ```lang ` | syntax-highlighted, line-numbered code box |
| `> text`, `> [!TIP]` | callout box |
| `---` | horizontal rule |
| `#`..`####` | chapter / section / subsection |

Language tags understood: `html`, `css`, `js`, `jsref` (reference listing, not
executed), `ts`, `tsx`, `jsx`, `py`, `python`, `java`, `c`, `cpp`, `cs`, `go`,
`rust`, `php`, `rb`, `sql`, `json`, `yaml`, `bash`, `sh`, `console`, `diff`,
`http`, `vue`, `svelte`, `swift`, `kotlin`, `dart`, `solidity`, `graphql`, `ini`,
`dockerfile`, `makefile`, `nginx`, `powershell`, `text`, `toml`, `xml`.

Use `jsref` only for JavaScript API listings that are not runnable programs.

## Content rules

1. **English only**, beginner-to-intermediate, short paragraphs.
2. **Original writing.** Paraphrase the source's topic names only. Never copy
   sentences, images or full code blocks. Short attributed snippets only when
   unavoidable.
3. **Code must be correct.** If the language is installed locally, run it. Always
   show the expected output.
4. Every question must have an answer with a brief explanation.
5. Cite every consulted URL in `# Sources`.
6. Do not invent APIs, syntax or output. When unsure, write less and say what the
   behaviour depends on.

## Length targets

| Technology size | Chapters | Pages |
|-----------------|----------|-------|
| small (Git, Flask, API) | 6-9 | 40-55 |
| medium (HTML, SQL, Python) | 10-14 | 55-80 |
| large (CSS, JavaScript, Rust) | 12-16 | 70-110 |

## Checklist before handing the file back

- [ ] Front matter complete, `source` names the site actually used
- [ ] `# How to use this volume` and `## Chapter map` present
- [ ] Every chapter has all six required sections with the exact names
- [ ] Every chapter has 5-10 summary bullets
- [ ] 3-5 exercises with solutions and 5-10 mini questions with an answer key
- [ ] Cheat sheet, final test (20-30 questions) with answers, and Sources
- [ ] Code examples correct, with expected output
- [ ] No verbatim passages from the source
- [ ] Tables use pipes and have a header row
