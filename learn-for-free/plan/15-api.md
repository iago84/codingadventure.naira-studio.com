# Vol. 15 – API – Study Plan

- Source site: https://rapidapi.com/learn
- Fetched: 2026-10-10
- Access: requires-login (hub itself 404s; individual learn pages such as `/learn/rest` return a login wall / empty body to the fetcher; RapidAPI has been rebranded "Nokia API Hub")
- Notes: The Learn hub TOC could not be retrieved; the learning path below is inferred from RapidAPI's previously published free REST curriculum fragments surfaced in search results, cross-checked against the free public official docs that replace it: MDN Web Docs (HTTP), the OpenAPI Specification, and RFC 9110 (HTTP semantics). Inferred — not a fetched TOC.

## Learning path (source order — inferred)

1. **Introduction to APIs** — what an API is, client/server model, why APIs exist — https://rapidapi.com/learn
2. **REST API fundamentals** — the six REST constraints, resources, representations — https://rapidapi.com/learn/rest
3. **Resource naming and URI design** — nouns vs verbs, path structure best practices — https://rapidapi.com/learn/rest
4. **HTTP methods** — correct use of GET, POST, PUT, PATCH, DELETE — https://rapidapi.com/learn/rest
5. **Status codes and error handling** — 2xx/3xx/4xx/5xx semantics, error payloads — https://rapidapi.com/learn/rest
6. **Request and response formats** — JSON conventions, content types, headers — https://rapidapi.com/learn/rest
7. **Query parameters, filtering and sorting** — designing queryable collections — https://rapidapi.com/learn/rest
8. **Pagination strategies** — offset/limit vs cursor pagination — https://rapidapi.com/learn/rest
9. **Authentication** — API keys, JWT basics, OAuth 2.0 overview — https://rapidapi.com/learn/rest
10. **API documentation** — OpenAPI/Swagger documentation basics — https://rapidapi.com/learn/rest
11. **Versioning strategies** — URI vs header versioning, handling breaking changes — https://rapidapi.com/learn/rest
12. **Rate limiting and security** — throttling, quotas, CORS, security headers — https://rapidapi.com/learn/rest
13. **API testing** — manual and automated API testing with test suites — https://rapidapi.com/learn/rest
14. **Consuming APIs as a client** — using API marketplaces/hubs, keys, playgrounds — https://rapidapi.com/learn

Replacement free public documentation (official, no login):

15. **MDN Web Docs — HTTP** — protocol, methods, headers, status codes — https://developer.mozilla.org/en-US/docs/Web/HTTP
16. **OpenAPI Specification** — describing RESTful APIs — https://spec.openapis.org/oas/latest.html
17. **RFC 9110 – HTTP Semantics** — authoritative HTTP semantics — https://www.rfc-editor.org/rfc/rfc9110

Total TOC items found: 0 fetched (hub unreachable/login-gated); 14 inferred path items + 3 official free documentation anchors named above.

## Planned chapters for the volume

1. **What an API is** (covers source item 1)
2. **REST principles and constraints** (covers source items 2, 15–17)
3. **Designing resources and URIs** (covers source item 3)
4. **HTTP methods done right** (covers source item 4)
5. **Status codes and error payloads** (covers source item 5)
6. **Requests, responses and JSON hygiene** (covers source item 6)
7. **Filtering, sorting and query design** (covers source item 7)
8. **Pagination** (covers source item 8)
9. **Authentication and authorization** (covers source item 9 — keys, JWT, OAuth 2.0)
10. **Documenting with OpenAPI** (covers source items 10, 16)
11. **Versioning and change management** (covers source item 11)
12. **Rate limiting and cross-origin security** (covers source item 12 — CORS, headers, throttling)
13. **Testing APIs** (covers source item 13)
14. **Consuming third-party APIs** (covers source item 14)
15. **Capstone: design, document and deploy a public API** (integrates all items)

## Flags / issues

- Source hub unreachable via fetcher: `/learn` returns 404 and `/learn/rest` is login-gated — the entire path above is INFERRED from search snippets of RapidAPI's own course pages plus standard curriculum knowledge, not a live fetch.
- RapidAPI rebrand ("Nokia API Hub") — URL structure may change again; re-check before publishing.
- Plan therefore leans on the free official documentation (MDN HTTP, OpenAPI Spec, RFC 9110) named above instead of RapidAPI's gated material.
