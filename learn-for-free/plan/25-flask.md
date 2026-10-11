# Vol. 25 – Flask – Study Plan

- Source site: https://flask.palletsprojects.com/tutorial/
- Fetched: 2026-10-10
- Access: reachable
- Notes: Pallets' official Flask docs (Flask 3.1.x) — Sphinx-generated, full ordered TOC rendered server-side. Free, open (BSD-3-Clause code, docs CC); still write original prose, no verbatim copying. Tutorial builds the "Flaskr" blog app.

## Learning path (source order)
1. **Project Layout** — Recommended directory structure for Flaskr — https://flask.palletsprojects.com/en/stable/tutorial/layout/
2. **Application Setup** — Creating the app object, config, blueprint/web structure — https://flask.palletsprojects.com/en/stable/tutorial/factory/
3. **Define and Access the Database** — SQLite, schema, connection handling, query execution — https://flask.palletsprojects.com/en/stable/tutorial/database/
4. **Blueprints and Views** — Organising routes into blueprints, auth Blueprint basics — https://flask.palletsprojects.com/en/stable/tutorial/views/
5. **Templates** — Jinja2 templates, base layout, auth templates, context passing — https://flask.palletsprojects.com/en/stable/tutorial/templates/
6. **Static Files** — Serving CSS/static assets, overriding app factory — https://flask.palletsprojects.com/en/stable/tutorial/static/
7. **Blog Blueprint** — Full blog feature: list/detail/create/update/delete views and templates — https://flask.palletsprojects.com/en/stable/tutorial/blog/
8. **Make the Project Installable** — Packaging so the project can be installed — https://flask.palletsprojects.com/en/stable/tutorial/install/
9. **Test Coverage** — pytest fixtures, factories, testing routes and auth — https://flask.palletsprojects.com/en/stable/tutorial/tests/
10. **Deploy to Production** — Building distributions, deploying, hosting configuration — https://flask.palletsprojects.com/en/stable/tutorial/deploy/
11. **Keep Developing!** — Next steps and pointers into the wider docs — https://flask.palletsprojects.com/en/stable/tutorial/next/

## Planned chapters for the volume
1. Python Refresher and Flask Intro (covers source items: tutorial preface/assumptions)
2. Project Layout for a Flask App (covers source items: 1, 2)
3. Application Factories and Configuration (covers source items: 2, 6)
4. Routing, Views and Blueprints (covers source items: 4, 7)
5. Working with SQLite and the DB Layer (covers source items: 3)
6. User Registration and Authentication (covers source items: 4, 5, 7)
7. Templates with Jinja2 (covers source items: 5)
8. Static Files and Styling (covers source items: 6)
9. Blog CRUD: Views, Forms and Templates (covers source items: 7)
10. Making the App Installable (covers source items: 8)
11. Testing Flask Apps with pytest (covers source items: 9)
12. Deploying Flask to Production (covers source items: 10)
13. Beyond the Tutorial: Extensions and Next Steps (covers source items: 11 + docs extensions overview)

## Flags / issues
- Source fully reachable; no login/paywall. Content versioned as 3.1.x — note "stable" drift.
- Pallets content is BSD-3-Clause/CC licensed but copyrighted: use topic names only; no copied prose or code listings.
- Flask itself is a micro framework; the tutorial deliberately does not cover extensions (e.g. SQLAlchemy, WTForms, Flask-Login) — plan notes this gap for optional chapters.
