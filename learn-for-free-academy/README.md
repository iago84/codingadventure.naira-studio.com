# Learn for Free Academy

Paid micro-course platform (web + Android): one course per technology, ~2 EUR,
lesson quizzes, a final exam and a **verifiable completion certificate**.

| | |
|---|---|
| Phase | **Phase 0 (plan) - awaiting approval** |
| Content source | [`../learn-for-free/src`](../learn-for-free/src) (51 volumes: tech + AI/ML) |
| Architecture | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Milestone checklists | [`docs/MILESTONES.md`](docs/MILESTONES.md) |
| Open issues | [`docs/ISSUES.md`](docs/ISSUES.md) |

## Setup (5 commands)

```bash
git clone <repo> learn-for-free-academy && cd learn-for-free-academy
cp .env.example .env && make env          # or: docker compose --env-file .env up -d db redis
docker compose up -d db redis             # 1. start Postgres + Redis
docker compose run --rm web python manage.py migrate   # 2. migrations
docker compose run --rm web python manage.py import_volume ../learn-for-free/src/01-html.md  # 3. import a course
docker compose up -d web worker beat nginx # 4. start everything  ->  http://localhost
```

Tests and lint:

```bash
docker compose run --rm web pytest -q      # backend tests
docker compose run --rm web ruff check .   # lint
docker compose run --rm web black --check .# format
```

(The commands above describe the M1 outcome; the backend is not implemented yet.)

## Milestone status

| Milestone | Scope | Status |
|-----------|-------|--------|
| M1 | Foundation (auth, i18n, CI, Docker) | planned |
| M2 | Content import + catalog + lessons | planned |
| M3 | Quizzes + final exam | planned |
| M4 | Payments + entitlements | planned |
| M5 | Certificates + verification | planned |
| M6 | Gamification + notifications | planned |
| M7 | Android app (Expo) | planned |
| M8 | Hardening, legal, analytics, release | planned |

## Layout

```
learn-for-free-academy/
  backend/          Django project + apps
    apps/ accounts catalog learning assessment payments
             certificates gamification notifications content_import
  mobile/           Expo app (React Native + TypeScript)
  docs/             ARCHITECTURE, MILESTONES, ISSUES, RELEASE_CHECKLIST
  infra/            docker-compose, nginx, CI
  .env.example      all settings, documented
  README.md         this file
```

## Content import

`python manage.py import_volume ../learn-for-free/src/01-html.md` turns a
Markdown volume into `Course -> Chapters -> Lessons -> Question pool` (mini tests
per chapter + final exam pool), idempotently and re-runnably. PDFs are attached
to each course as a downloadable bonus after purchase.

## Legal notes

- All course content is original writing (see the PDF library's per-volume
  Sources lists). No source-site logos, names as brand, or copied passages.
- Certificates are certificates of **course completion** issued by Learn for Free
  Academy. They are not accredited and not official vendor certifications.
- Europe: 14-day refund rule applies to digital content; explicit consent is
  captured at checkout and stated on the refund policy page.
- Android: Google Play Billing is required for digital content (15-30% fee), so
  the 2 EUR price point is only viable with a bundle or subscription.
