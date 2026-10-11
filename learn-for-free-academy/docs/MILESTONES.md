# Milestone checklists

Each milestone ends with: tests passing, migrations clean, docs updated and a
short demo script (`docs/demo-M{n}.md`). Work one milestone at a time.

Status values: `planned` | `in-progress` | `done` | `blocked`

| Milestone | Status | Notes |
|-----------|--------|-------|
| M1 Foundation | planned | |
| M2 Content import + catalog + lessons | planned | |
| M3 Quizzes + final exam | planned | |
| M4 Payments + entitlements | planned | |
| M5 Certificates + verification | planned | |
| M6 Gamification + notifications | planned | |
| M7 Android app (Expo) | planned | |
| M8 Hardening, legal, analytics, release | planned | |

---

## M1 - Foundation

- [ ] Django 5 project with split settings (`base/dev/prod`), `django-environ`, `.env.example`
- [ ] Custom `User` model with email login (no username)
- [ ] PostgreSQL 16 + Redis 7 services
- [ ] Celery app + beat schedule stub
- [ ] Docker Compose: `web`, `db`, `redis`, `worker`, `beat`, `nginx`
- [ ] `docker compose up` works from a clean clone
- [ ] GitHub Actions CI: ruff, black, pytest, coverage
- [ ] `pre-commit` config (ruff, black, trailing whitespace, end-of-file)
- [ ] Email/password registration with verification email
- [ ] Password reset flow
- [ ] Social login (Google, Apple) via allauth
- [ ] SimpleJWT with rotation + blacklist for the API
- [ ] `/api/schema/` and `/api/docs/` served by drf-spectacular
- [ ] i18n: `gettext` with EN + ES, locale middleware, language switcher
- [ ] Base Tailwind + HTMX layout, dark mode, accessible nav
- [ ] `GET /healthz` health check
- [ ] Sentry SDK wired (DSK from env), structlog JSON logging
- [ ] Tests: auth flows, i18n, settings sanity
- [ ] README: setup in 5 commands + status table
- [ ] `docs/demo-M1.md`

**Definition of done:** `docker compose up` works, tests pass, README setup in
5 commands.

## M2 - Content import, catalog, lessons

- [ ] Models: `Course`, `Chapter`, `Lesson` (draft/published, `version`)
- [ ] Management command `import_volume <path.md>` (idempotent, re-runnable)
- [ ] Extracts: course metadata, chapters, lessons, mini-test questions
- [ ] Catalog list: search, filters (level, category), pagination
- [ ] Course detail: syllabus + one free preview lesson + reviews
- [ ] Lesson page: markdown render + syntax highlight, prev/next
- [ ] Progress tracking, resume point, bookmarks, personal notes
- [ ] Customised Django admin for content
- [ ] REST endpoints + OpenAPI for catalog and lessons
- [ ] Locked lessons never exposed to non-entitled users
- [ ] Tests: importer on 2 sample volumes, progress logic, permissions
- [ ] README status updated + `docs/demo-M2.md`

## M3 - Quizzes and final exam

- [ ] Models: `Question`, `Choice`, `QuizAttempt`, `ExamAttempt`, `AttemptAnswer`
- [ ] Question types: mcq, true/false, short answer, code output
- [ ] Importer extension: mini tests per chapter + final-test pool + explanations
- [ ] Lesson quiz: instant feedback, explanations, unlimited retries, best score
- [ ] Final exam: random draw from pool, shuffled order/options
- [ ] Timer with server-set `started_at`/`expires_at`
- [ ] Pass mark 70%, max 3 attempts per 24h
- [ ] Answer review after finishing
- [ ] Grading server-side; no answer leakage in API responses
- [ ] Admin question analytics (difficulty, most missed)
- [ ] Tests: grading edge cases, attempt limits, timer expiry, no leakage
- [ ] README status updated + `docs/demo-M3.md`

## M4 - Payments and entitlements

- [ ] Price per course (default ~2 EUR, configurable), optional bundle
- [ ] Promo codes (percent/amount, expiry, max redemptions)
- [ ] Stripe Checkout (web) + Stripe Tax
- [ ] Idempotent webhooks with provider-ref unique constraint
- [ ] Receipts by email, refunds from admin
- [ ] `Entitlement` created only by verified payment events
- [ ] `Order`/`Payment` audit log
- [ ] Google Play Billing endpoint: token validation, acknowledge, restore
- [ ] EU digital-content consent checkbox + refund policy page
- [ ] Locked/unlocked states across catalog, lessons and exam
- [ ] Tests: webhook replay, failed/refunded payments, revocation, price changes
- [ ] README status updated + `docs/demo-M4.md`

## M5 - Certificates and verification

- [ ] `Certificate` issued on passing (unique ID, score, date, course version)
- [ ] PDF via WeasyPrint: name, course, score, date, ID, QR
- [ ] EN/ES templates
- [ ] Name editable once before issuance
- [ ] Public `/verify/<id>` page (no private data) + Open Graph preview
- [ ] LinkedIn "Add to profile" link
- [ ] Revocation from admin
- [ ] Disclaimer: completion certificate, not an official vendor certification
- [ ] Tests: issuance only after pass, duplicate prevention, verify/revoked/unknown
- [ ] README status updated + `docs/demo-M5.md`

## M6 - Gamification and notifications

- [ ] XP events (lesson, quiz, exam, streak), levels
- [ ] Daily streaks with user timezone, daily goals
- [ ] Badges/achievements, opt-in weekly leaderboard
- [ ] XP only once per lesson/quiz milestone (idempotency key)
- [ ] Profile page with stats, badges, streak calendar
- [ ] In-app inbox, transactional email, FCM push (`DeviceToken`)
- [ ] Streak reminders via Celery beat, user preferences
- [ ] Confetti on pass/level up respecting `prefers-reduced-motion`
- [ ] Tests: streak timezones/DST, XP idempotency, leaderboard privacy
- [ ] README status updated + `docs/demo-M6.md`

## M7 - Android app (Expo)

- [ ] Expo + TypeScript app consuming the REST API
- [ ] Auth (email + Google), catalog, course detail, lessons, quizzes, exam
- [ ] Certificates view/share PDF, profile, gamification
- [ ] i18next EN/ES, dark mode, accessibility labels
- [ ] Secure token storage, automatic refresh
- [ ] Offline cache of purchased lessons + progress sync
- [ ] Google Play Billing with server validation against M4 endpoints
- [ ] FCM push, deep links to lessons and `/verify`
- [ ] EAS Build config for internal testing track
- [ ] Component tests + Maestro smoke flow (login -> buy test product -> lesson -> quiz)
- [ ] README status updated + `docs/demo-M7.md`

## M8 - Hardening, legal, analytics, release

- [ ] Security review vs OWASP top 10: rate limiting, CORS/CSRF, secrets, deps
- [ ] Audit logs for payments and certificates
- [ ] GDPR: data export, account deletion, cookie consent
- [ ] Privacy Policy, Terms, refund policy pages (EN/ES)
- [ ] Query optimisation, caching, CDN config, Lighthouse >= 90
- [ ] Load test of exam endpoints
- [ ] Accessibility pass (WCAG 2.1 AA) web + mobile
- [ ] Analytics (PostHog or Plausible): visit -> purchase -> completion -> certificate
- [ ] Revenue dashboard
- [ ] Backups, migrations strategy, production deployment guide
- [ ] Google Play checklist: data safety form, screenshots, EN/ES listing
- [ ] `docs/RELEASE_CHECKLIST.md` with pass/fail per item
- [ ] Stop for owner review
