# Vol. 06 – Angular – Study Plan

- Source site: https://angular.dev/tutorials
- Fetched: 2026-10-10
- Access: reachable
- Notes: Official open-source Angular documentation (source in the `angular/angular` GitHub repo); no login; tutorial hub lists 5 interactive tutorials with free in-browser playground, plus an AI-Tutor/MCP option.

## Learning path (source order)
1. **Learn Angular (in your browser)** — interactive, step-by-step intro to Angular's building blocks via the playground — https://angular.dev/tutorials/learn-angular
2. **Build your first Angular app (locally, via npm/Angular CLI)** — 14-lesson project tutorial building a home-rentals listing app — https://angular.dev/tutorials/first-app
3. **Learn signals** — the signals API: computed/linked signals, async data, effects, model signals, signal queries — https://angular.dev/tutorials/signals
4. **Deferrable views** — lazy-loading parts of a template with `@defer`, loading/placeholder/error states, defer triggers — https://angular.dev/tutorials/deferrable-views
5. **Learn signal forms (signal-based forms)** — new signal-based form model: setup, binding, validation, errors, submission — https://angular.dev/tutorials/signal-forms
6. **Angular AI Tutor (MCP server)** — optional AI-tutoring setup for the tutorials — https://angular.dev/ai/ai-tutor

Tutorial sub-lesson inventory extracted from the tutorial pages / site sitemap (source order):
- Learn Angular: 25 steps — components, component class, composing components, control flow (`@if`, `@for`), property binding, event handling, `input()`, `output()`, deferrable views, optimizing images, routing setup, route definitions, `routerLink`, forms, form-control values, reactive forms, validation, injectable services, `inject()`-based DI, pipes (formatting data, custom pipe), next steps (numbering in the source jumps from step 20 to step 22) — https://angular.dev/tutorials/learn-angular/1-components-in-angular
- First app: 14 lessons — hello world, home feature, app-housing-location details, interfaces, inputs, property binding, dynamic values, `@for` lists, services, routing basics, detail page, forms, search, HTTP data — https://angular.dev/tutorials/first-app/01-hello-world
- Signals: 11 steps — first signal, computed, linked signals, async data, component communication, model signals, signals with services/directives, signal queries, `effect`, next steps — https://angular.dev/tutorials/signals/1-creating-your-first-signal
- Deferrable views: 3 steps — what are deferrable views, loading/error/placeholder, defer triggers — https://angular.dev/tutorials/deferrable-views/1-what-are-deferrable-views
- Signal forms: 6 steps — form model, template connection, validation, error display, submission, next steps — https://angular.dev/tutorials/signal-forms/1-set-up-form-model

## Planned chapters for the volume
1. What is Angular and the Angular CLI setup (covers source items: first-app intro prerequisites)
2. Components and the component class (covers source items: learn-angular steps 1–2, first-app lessons 1–2)
3. Composing components and data flow: `input()`, `output()`, property binding, event handling (covers source items: learn-angular steps 3, 6–9, first-app lessons 4–7)
4. Templates and control flow (`@if`, `@for`, dynamic template values) (covers source items: learn-angular steps 4–5, first-app lessons 7–8)
5. Dependency injection and services (`providedIn`, `inject()`) (covers source items: learn-angular steps 19–20, first-app lesson 9)
6. Routing and navigation (covers source items: learn-angular steps 12–14, first-app lessons 10–11)
7. Forms: template-driven basics and reactive forms with validation (covers source items: learn-angular steps 15–18, first-app lessons 12–13)
8. HTTP client and async data access (covers source items: first-app lesson 14)
9. Signals: state, computed, linked, effects, model signals, signal queries (covers source items: signals tutorial steps 1–11)
10. Performance: deferrable views and image optimization (covers source items: deferrable-views tutorial, learn-angular steps 10–11)
11. Pipes and data formatting, plus custom pipes (covers source items: learn-angular steps 22–24)
12. Signal-based forms (covers source items: signal-forms tutorial steps 1–6)

## Flags / issues
- Site fully reachable, no login or paywall for tutorials; embedded playground requires JavaScript (fetched via server-rendered docs pages).
- Do not copy tutorial prose verbatim — write original explanations, reference only short topic names and link back.
- "Learn-angular" step numbering skips 21 in the published path (step 21 page not present in the sitemap listing) — noted, not an error in this plan.
- Angular version pins on the site move (docs showed v22); verify CLI/Node requirements before publishing the volume.
