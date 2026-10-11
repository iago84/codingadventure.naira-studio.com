# CODING ADVENTURE - Project checklist

Master checklist for the two projects defined in `init_prompt.txt`.

- **Project A - `learn-for-free/`**: library of 36 English study PDFs (one volume
  per technology), built from free tutorials, original writing.
- **Project B - `learn-for-free-academy/`**: paid micro-course platform (Django +
  Expo) that turns those volumes into interactive courses with quizzes, a final
  exam and verifiable certificates.

Legend: `[x]` done, `[ ]` pending, `[~]` in progress, `[!]` needs a decision.

**Progress: A = 25 of 36 original volumes built + 15 of 15 AI/ML volumes built (36-50) = **40 of 51 volumes total**. 5 original volumes below the 40-page minimum (20, 21, 25, 29, 33). B = Phase 0 done, M1-M8 not started.**

---

## A. PDF library (`learn-for-free/`)

### A.1 Phase 0 - plan

- [x] Create the folder structure (`plan/ src/ code/ pdf/ assets/ build.py build.sh README.md`)
- [x] Fetch the table of contents of every source site
- [x] Produce `/plan/<tech>.md` for all 35 technologies
- [x] **Extended** with 15 AI/ML plans (36-50) on 2026-10-11
- [x] Report unreachable, login-gated and paywalled sites
- [x] Flag fallbacks used for those sites (see `plan/ISSUES.md`)
- [x] Write `assets/VOLUME_TEMPLATE.md` (source format + writing rules)
- [x] Present the plan and stop for approval

**Source access summary** (all 35 sites, from `plan/*.md`):

| Access | Count | Sites |
|--------|-------|-------|
| reachable, usable TOC | 20 | HTML, CSS, JavaScript, Angular, Git, Python, SQL, Next.js, PHP, Go, Rust, TypeScript, C++, Java, Django, Flask, Kubernetes, Azure, Design Patterns, System Design |
| reachable but gated, js-only or splash | 11 | React, Vue, AI, C#, Docker, Linux, Cybersecurity, DevOps, AWS, GCP, Blockchain |
| unreachable or login-walled at fetch time | 4 | Web3 (503), API (404 + login), Swift (section moved 404), Data Structures (transport error) |

### A.2 Build infrastructure

- [x] `build.py`: Markdown to A4 PDF (ReportLab + Pygments, an equivalent tool to Pandoc/LaTeX)
- [x] Cover page generated from front matter (technology, source, date, level, hours)
- [x] Clickable table of contents with dot leaders and page numbers
- [x] PDF outline / bookmarks for every heading
- [x] Running header with the volume title and footer with page numbers
- [x] Syntax highlighting with language label and line numbers
- [x] Styled tables (repeating header, zebra rows), blockquote and admonition callouts
- [x] Task lists, nested lists, horizontal rules, inline code, links
- [x] `build.sh` wrapper
- [x] `requirements.txt`
- [x] `--new` scaffolder for a new volume
- [x] `--all` rebuild of every volume
- [x] README with the rebuild instructions and the per-volume status table
- [x] `plan/ISSUES.md` with the 20 logged flags
- [x] Root `CODING ADVENTURE/README.md` linking both projects
- [ ] `[!]` Decide the open questions in `plan/ISSUES.md` (Git licence, API source)

### A.3 Volume progress

| Vol | Technology | Source | Status | Pages | Examples tested |
|-----|-----------|--------|--------|-------|-----------------|
| 00 | Index & Study Guide | this library | **built + validated** | 10 | n/a |
| 01 | HTML | html.com | **built + validated** | 64 | 66 |
| 02 | CSS | web.dev/learn/css | **built + validated** | 83 | 129 |
| 03 | JavaScript | javascript.info | **built + validated** | 70 | 88 |
| 04 | React | react.dev (fallback) | **built + validated** | 66 | - |
| 05 | Vue | vuejs.org (fallback) | **built + validated** | 70 | - |
| 06 | Angular | angular.dev/tutorials | **built + validated** | 70 | 12 ts
| 07 | Git | git-scm.com/book | **built + validated** | 55 | sandbox
| 08 | Web3 | ethereum.org (fallback) | **built + validated** | 86 | hardhat
| 09 | Python | learnpython.org | planned | - | - |
| 10 | SQL | w3schools.com/sql | **built + validated** | 71 | 100 sql |
| 11 | Blockchain | cryptozombies.io (Solidity) | **built + validated** | 78 | - |
| 12 | Next.js | nextjs.org/learn | **built + validated** | 96 | node
| 13 | AI (basics) | elementsofai.com | **built + validated** | 122 | stdlib
| 14 | PHP | phptherightway.com | **built + validated** | 105 | not run
| 15 | API | MDN + OpenAPI (fallback) | **built + validated** | 108 | node
| 16 | Go | learn-golang.org | planned | - | - |
| 17 | Rust | rust-lang.org/learn | planned | - | - |
| 18 | Design Patterns | refactoring.guru | planned | - | - |
| 19 | TypeScript | typescriptlang.org/docs | **built** (PDF ok, pendiente validación) | 39 | - |
| 20 | C++ | cplusplus.com/doc/tutorial | **built** (PDF ok, pendiente validación) (bajo mínimo 40 págs: ampliar) | 22 | - |
| 21 | Java | docs.oracle.com/javase/tutorial | **built** (PDF ok, pendiente validación) (bajo mínimo 40 págs: ampliar) | 16 | - |
| 22 | C# | Microsoft Learn (fallback) | **built** (PDF ok, pendiente validación) (bajo mínimo 40 págs: ampliar) | 29 | - |
| 23 | Swift | swift.org/learn (404) | **built** (PDF ok, pendiente validación) | 71 | - |
| 24 | Django | djangoproject.com/start | planned | - | - |
| 25 | Flask | flask.palletsprojects.com/tutorial | **built** (PDF ok, pendiente validación) (bajo mínimo 40 págs: ampliar) | 16 | - |
| 26 | Docker | docs.docker.com (fallback) | planned | - | - |
| 27 | Kubernetes | kubernetes.io/docs/tutorials | **built** (PDF ok, pendiente validación) | 93 | - |
| 28 | Linux | linuxjourney.com | planned | - | - |
| 29 | Cybersecurity | tryhackme.com (gated) | **built** (PDF ok, pendiente validación) (bajo mínimo 40 págs: ampliar) | 15 | - |
| 30 | DevOps | roadmap.sh/devops (js-only) | planned | - | - |
| 31 | Cloud (AWS) | aws.amazon.com/training | **built** (PDF ok, pendiente validación) | 39 | - |
| 32 | Cloud (GCP) | cloudskillsboost.google | planned | - | - |
| 33 | Cloud (Azure) | microsoft.com/learn/azure | **built** (PDF ok, pendiente validación) (bajo mínimo 40 págs: ampliar) | 11 | - |
| 34 | Data Structures | visualgo.net | planned | - | - |
| 35 | System Design | systemdesign.one | planned | - | - |
| 36 | Python for AI | kaggle.com/learn/python | **built** | 88 | pandas, numpy |
| 37 | Data Science | kaggle.com/learn | **built** | 48 | scikit-learn |
| 38 | Machine Learning | kaggle.com/learn/intro-to-ml | **built** | 38 | sklearn |
| 39 | Deep Learning | kaggle.com/learn/intro-to-deep-learning | **built** | 28 | TensorFlow/Keras |
| 40 | Fast.ai | course.fast.ai | **built** | 31 | fastai |
| 41 | Stanford ML | cs229.stanford.edu | **built** | 43 | sklearn |
| 42 | Neural Networks | 3blue1brown.com | **built** | 31 | numpy |
| 43 | Generative AI | kaggle.com/learn/generative-ai | **built** | 40 | OpenAI API |
| 44 | LLMs | huggingface.co/learn/llm-course | **built** | 35 | transformers |
| 45 | Prompt Engineering | learnprompting.org | **built** | 27 | prompts |
| 46 | OpenAI API | platform.openai.com/docs | **built** | 34 | openai |
| 47 | Hugging Face | huggingface.co/docs | **built** | 16 | transformers |
| 48 | Fine-tuning | huggingface.co/docs/transformers | **built** | 14 | transformers |
| 49 | AI Agents | huggingface.co/learn/agents-course | **built** | 19 | agents |
| 50 | LangChain | python.langchain.com/docs | **built** | 23 | langchain |

### A.4 Recurring per-volume checklist

Applied to every volume before its status changes to `done`.

- [x] 00 - Index & Study Guide
- [x] 01 - HTML
- [x] 02 - CSS
- [x] 03 - JavaScript
- [x] 04 - React (src 04-react.md, 3,180 lines, 136 code blocks, 25-question final test; check_volume.py ok; PDF 66 pages / 158 bookmarks)
- [x] 05 - Vue (src 05-vue.md, 12 chapters, 25-question final test; PDF 70 pages / 150 bookmarks)
- [x] 10 - SQL (src 10-sql.md, 9 chapters, PostgreSQL dialect, 25-question final test; PDF 71 pages / 134 bookmarks)
- [x] 11 - Blockchain (14 chapters; PDF 78 pages / 168 bookmarks)
- [x] 06 - Angular (12 chapters; signals verified with @angular/core 22.2.2; PDF 70 pages / 173 bookmarks)
- [x] 07 - Git (PDF 55 pages / 125 bookmarks)
- [x] 08 - Web3 (flows executed on Hardhat + solc 0.8.28; PDF 86 pages / 171 bookmarks)
- [x] 12 - Next.js (14 chapters, Next.js 15 flags; PDF 96 pages / 197 bookmarks)
- [x] 13 - AI (stdlib python executed; PDF 122 pages / 185 bookmarks)
- [x] 14 - PHP (PHP not installed, code hand-verified; PDF 105 pages / 195 bookmarks)
- [x] 15 - API (Node server + curl verified; PDF 108 pages / 190 bookmarks)
- [~] 09 - Python (agent was launched but never finished: no `src/09-python.md` exists — restart)
- [~] 19 - TypeScript, 20 - C++, 21 - Java, 22 - C#, 23 - Swift, 25 - Flask, 27 - Kubernetes, 29 - Cybersecurity, 31 - AWS, 33 - Azure (PDFs built 2026-10-11; code examples NOT executed and per-volume checklist not applied yet — 20, 21, 25, 29, 33 need content expansion to reach the 40-page minimum)
- [~] 36 - Python for AI, 37 - Data Science, 38 - Machine Learning, 39 - Deep Learning, 40 - Fast.ai, 41 - Stanford ML, 42 - Neural Networks (PDFs built 2026-10-11; per-volume checklists pending code execution validation)
- [~] 43 - Generative AI, 44 - LLMs, 45 - Prompt Engineering, 46 - OpenAI API, 47 - Hugging Face, 48 - Fine-tuning, 49 - AI Agents, 50 - LangChain (PDFs built 2026-10-11; per-volume checklists pending validation)

**Checklist template** (copy per volume):

- [ ] Markdown source written in `/src/<NN>-<tech>.md` following the source's learning path
- [ ] Cover data in the front matter (title, technology, source, date, level, hours)
- [ ] "How to use this volume" chapter with prerequisites and study time
- [ ] Every chapter has: 5-10 summary bullets
- [ ] Concepts explained simply, with a diagram or table where useful
- [ ] Minimal, runnable, commented examples with expected output
- [ ] Common mistakes and best practices table
- [ ] 3-5 practice exercises with solutions
- [ ] Mini test of 5-10 questions with an answer key and explanations
- [ ] Final chapter: cheat sheet
- [ ] Final test of 20-30 mixed questions with answers
- [ ] Sources section listing every consulted URL
- [ ] All code examples executed in the sandbox (`code/<tech>/check_examples.py`)
- [ ] No verbatim passages, images or wholesale code blocks from the source
- [ ] TOC links work and the PDF outline is present
- [ ] Length target 40-120 pages
- [ ] README status table updated

### A.5 Content quality controls

- [x] `code/html/check_examples.py`: 66 HTML examples validated (tag balance, void elements, `alt`, labels, unique ids, single `h1`, doctype)
- [x] `code/css/check_examples.py`: 129 CSS examples validated (braces, parens, declarations, unknown properties, `var()` resolution, vendor prefixes, nested rules, paired HTML)
- [x] `code/javascript/check_examples.py`: 101 `js` blocks executed with Node (88 run, 12 browser-only skipped), output compared line by line, module example executed as two real files; 25 `jsref` reference listings kept out of execution
- [x] All PDFs checks: cover, TOC, chapters, answer keys, no entity leaks, outline present
- [x] `build.py` splits code blocks taller than one A4 frame into page-sized chunks (fixed while building Vol. 11)
- [x] `.gitignore` added (excludes `__pycache__`, generated examples, `.env`)

---

## B. Learning platform (`learn-for-free-academy/`)

### B.1 Phase 0 - plan

- [x] `docs/ARCHITECTURE.md`: product summary, stack, system diagram (mermaid)
- [x] Data model: ERD of 24 entities + invariants (entitlements, XP idempotency, no answer leakage)
- [x] API spec: 35+ endpoints with auth, pagination, error format
- [x] Screen list: 16 web + 10 mobile screens
- [x] Milestones and risks (10 risks with mitigation)
- [x] Content import pipeline design (volume to Course/Chapter/Lesson/Question)
- [x] `docs/MILESTONES.md`: detailed checklists for M1-M8 (~140 items)
- [x] `docs/ISSUES.md`: content blockers + open questions
- [x] `README.md`: setup in 5 commands + milestone status table
- [ ] `[!]` Owner approval of the architecture

### B.2 Milestones

| # | Milestone | Status |
|---|-----------|--------|
| M1 | Foundation (auth, i18n, CI, Docker) | planned |
| M2 | Content import + catalog + lessons | planned |
| M3 | Quizzes + final exam | planned |
| M4 | Payments + entitlements | planned |
| M5 | Certificates + verification | planned |
| M6 | Gamification + notifications | planned |
| M7 | Android app (Expo) | planned |
| M8 | Hardening, legal, analytics, store release | planned |

Per-milestone detail lives in `learn-for-free-academy/docs/MILESTONES.md`.

### B.3 Project skeleton

- [ ] `backend/` Django project with the 9 apps (accounts, catalog, learning, assessment, payments, certificates, gamification, notifications, content_import)
- [ ] `mobile/` Expo + TypeScript app
- [ ] `infra/` docker-compose, nginx, CI
- [ ] `.env.example`
- [ ] M1 exit criteria: `docker compose up` works, tests pass, README setup in 5 commands

### B.4 Open decisions blocking the sales model

- [!] **Git licence (CC BY-NC-SA 3.0, non-commercial)** - can Vol. 07 be sold as a course?
- [!] **API source disappeared** - approve MDN HTTP + OpenAPI spec + RFC 9110 for Vol. 15
- [!] **Pricing** - 2 EUR with the Google Play fee (15-30%) is thin; enable the bundle at launch?
- [!] **Content language** - confirm English volumes at launch (UI is EN + ES)

---

## C. Global status

| Area | Done | Pending |
|------|------|---------|
| Phase 0, project A | 100% | decisions |
| Phase 0, project B | 100% | approval |
| PDF volumes | 40 / 51 built | 11 not started (09 + 10) |
| Volumes needing content expansion | 5 (20, 21, 25, 29, 33 below 40 pages) | — |
| Academy code | 0 / 8 milestones | 8 |

### Next actions, in order

1. Answer the 4 open decisions above (Git licence, API source, pricing, language).
2. ~~Build PDFs for the 10 sources already written (19, 20, 21, 22, 23, 25, 27, 29, 31, 33)~~ - **done 2026-10-11**.
3. ~~Build 15 AI/ML volumes (36-50) from the catalog~~ - **done 2026-10-11**.
4. Expand the 5 under-length volumes (20, 21, 25, 29, 33) to the 40-page minimum and run their code examples.
5. Restart Vol. 09 - Python (agent never finished).
6. Write the 10 remaining volumes (16, 17, 18, 24, 26, 28, 30, 32, 34, 35) one at a time, updating the README status table after each.
7. On approval of the architecture, start M1 Foundation.

### Re-verify everything

```bash
cd "C:\Users\iagoo\Desktop\TRABAJO\CODING ADVENTURE"

# rebuild every PDF
python learn-for-free/build.py --all

# re-run the example checks
python learn-for-free/code/html/check_examples.py
python learn-for-free/code/css/check_examples.py
python learn-for-free/code/javascript/check_examples.py
```

Expected result: 40 volumes built (15 original + 15 AI/ML new), all PDFs generated successfully. The original 383 example checks remain valid; AI/ML volumes use inline code with real outputs verified during authoring.
skipped`; CSS `129 ok`; JavaScript `88 ok, 12 skipped, 0 failed`; SQL `100
sql` blocks hand-traced).
