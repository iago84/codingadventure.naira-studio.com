# ISSUES

Blockers logged during the project. Each item says what, impact, and the current
workaround. Nothing here stops work; we continue with the next item.

## Content source issues (from Phase 0 of the PDF library)

| Tech | Issue | Impact | Workaround |
|------|-------|--------|------------|
| React (04) | reactplay.io is a client-rendered SPA; its lesson list cannot be fetched statically | plan could not follow the site's own order | Learning path anchored to the free official React docs (react.dev/learn); ReactPlay's public project list used only for exercise ideas |
| Vue (05) | learnvue.co courses are pay-what-you-want; quizzes/challenges are paid tiers ($10/$25) | the full quiz set is not free | Free tier-1 videos + official Vue docs form the learning path |
| Web3 (08) | learnweb3.io returned HTTP 503 for /, /degrees and /sitemap at fetch time | no verified syllabus | Plan explicitly marked INFERRED, anchored to free official docs (ethereum.org, Solidity, Hardhat/Foundry, viem); re-verify next phase |
| Cybersecurity (29) | tryhackme.com path outlines render only for logged-in users; much content is subscription-gated | no free full syllabus | Free paths (Pre Security, Cyber Security 101) + free references (OWASP, MITRE ATT&CK, NIST) |
| DevOps (30) | roadmap.sh/devops graph is JS-rendered; TOC could not be scraped | no verified order | Plan marked inferred from standard DevOps track |
| Cloud AWS/GCP/Azure (31-33) | training portals require login and are JS-heavy | no verified lesson list | Plans anchored to free public docs (AWS Docs, Google Cloud docs, Microsoft Learn) |
| Data Structures (34) | visualgo.net is an interactive visualiser with no lesson text | no readable TOC | Standard DS&A curriculum used, with visualgo topics as the checklist |
| Git (07) | Pro Git book is CC BY-NC-SA 3.0 (non-commercial, share-alike) | **licence conflict with selling courses** | Paraphrase with attribution; **flag for owner decision**: either keep the PDF volume free/personal-only or replace the syllabus with a permissively licensed source |
| Blockchain (11) | cryptozombies.io is a JS-only SPA that refused fetches | no live syllabus | TOC reconstructed from indexed copies of the site's own pages (flagged inferred); anchored to free official Solidity docs |
| Next.js (12) | course text is (c) Vercel | copying risk | TOC fetched live; original writing only |
| AI (13) | course platform is JS-only; exercises need a free account | no live chapter TOC | TOC inferred from secondary indexing and flagged as inferred |
| API (15) | **rapidapi.com/learn 404s and is behind a login wall (rebranded to "Nokia API Hub")** | source disappeared | Path inferred; plan anchored to MDN HTTP, the OpenAPI spec and RFC 9110. Re-check before publishing |
| C# (22), Swift (23) | microsoft.com/learn and swift.org/learn are JS-rendered / moved | no verified order | Plans anchored to Microsoft Learn and the official Swift book, marked inferred where noted |
| w3schools SQL (10), cplusplus (20), refactoring.guru (18) | "All rights reserved" sites | copying risk | Original writing only; topic names and exercise prompts written from scratch |

## Open questions for the owner

1. **Git volume licence (CC BY-NC-SA 3.0):** sell academy courses derived from it?
2. **API source disappeared:** rapidapi.com/learn now 404s behind a login wall. Approve using MDN + the OpenAPI Specification + RFC 9110 as the source for Vol. 15?
3. **Pricing:** 2 EUR per course with the Play fee makes little margin - enable the
   "all courses" bundle at launch?
4. **Content language:** volumes are English; UI is EN + ES. Confirm the volume
   content stays English at launch.
