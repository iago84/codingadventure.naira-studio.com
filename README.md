# CODING ADVENTURE

Two related projects: a **library of original study PDFs** (tech + AI/ML) and the
learning platform that sells them as interactive courses.

```
CODING ADVENTURE/
  learn-for-free/          51 study volumes in PDF (source of the content)
    plan/                  Phase 0 plans, one per technology + ISSUES.md
    src/                   Markdown sources (51 volumes: 00-50)
    code/<tech>/           tested example code
    pdf/                   built PDFs (51 volumes)
    assets/                source format + build rules
    build.py               Markdown -> PDF pipeline (ReportLab + Pygments)
    README.md              status table per volume

  learn-for-free-academy/   Django + Expo micro-course platform
    docs/                  ARCHITECTURE, MILESTONES checklists, ISSUES
    backend/               Django project (not scaffolded yet)
    mobile/                Expo app (not scaffolded yet)
    infra/                 docker-compose, nginx, CI
    README.md              setup in 5 commands + milestone status

  init_prompt.txt          the original master prompts (reference)
```

## Volume catalog

| Range | Category | Source sites |
|-------|----------|-------------|
| 00-08 | Web fundamentals | HTML, CSS, JS, React, Vue, Angular, Git, Web3 |
| 09-15 | Core languages | Python, SQL, Blockchain, Next.js, AI, PHP, API |
| 16-23 | Systems & languages | Go, Rust, Design Patterns, TS, C++, Java, C#, Swift |
| 24-35 | Backend & cloud | Django, Flask, Docker, Kubernetes, Linux, DevOps, AWS, GCP, Azure, Data Structures, System Design |
| 36-37 | AI fundamentals | Python for AI, Data Science (Kaggle) |
| 38-42 | ML & deep learning | ML, Deep Learning, Fast.ai, Stanford CS229, Neural Networks (3Blue1Brown) |
| 43-45 | Generative AI & LLMs | Generative AI, LLMs (HuggingFace), Prompt Engineering |
| 46-50 | APIs & agents | OpenAI API, HuggingFace Docs, Fine-tuning, AI Agents, LangChain |

## Current state

| Project | Phase | State |
|---------|-------|-------|
| learn-for-free | **Phase 0 complete + Vol 00-15 built + Vol 19-23, 25, 27, 29, 31, 33, 36-50 built** | 51 PDFs total (40 built, 11 planned) |
| learn-for-free-academy | **Phase 0 complete** | ARCHITECTURE, ERD, API spec, screens, milestones, risks |

## Roadmap

1. ~~Phase 0 (plans, architecture)~~ **done**
2. ~~Vol. 00 Index~~ and ~~Vol. 01 HTML~~ **built**
3. ~~Vol. 02 CSS~~ **built (83 pages)**
4. ~~Volumes 03-15 (core technologies)~~ **built**
5. ~~Volumes 19-23, 25, 27, 29, 31, 33 (second wave)~~ **built**
6. ~~Volumes 36-50 (AI/ML catalog)~~ **built**
7. Volumes 09, 16-18, 24, 26, 28, 30, 32, 34-35 (remaining 11) one at a time
8. Academy M1-M8, one milestone at a time

## Decisions still open

- Git volume licence (CC BY-NC-SA 3.0) vs selling academy courses
- Pricing: 2 EUR per course is thin after Google Play's fee - bundle at launch?
- Volume content language stays English at launch (UI is EN + ES)
