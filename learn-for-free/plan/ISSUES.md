# ISSUES

Blockers and flags found in Phase 0. None of these stop the work; the affected
volume uses the listed fallback. Items marked **DECISION** need the owner's call.

| Vol | Technology | Issue | Fallback used |
|-----|-----------|-------|---------------|
| 04 | React | reactplay.io is a client-rendered SPA, its lesson list cannot be fetched | Official free React docs (react.dev/learn) as the learning path; ReactPlay's public project list only for exercise ideas |
| 05 | Vue | learnvue.co is pay-what-you-want; quizzes and coding challenges are paid tiers | Free tier-1 videos + official Vue docs |
| 07 | Git | Pro Git book is CC BY-NC-SA 3.0 (non-commercial, share-alike) | Paraphrase with attribution. **DECISION needed:** this volume may not be used inside the paid academy |
| 08 | Web3 | learnweb3.io returned HTTP 503 for /, /degrees and /sitemap | Plan marked INFERRED and anchored to free official docs (ethereum.org, Solidity, Hardhat/Foundry, viem). Re-verify next phase |
| 10 | SQL | w3schools.com/sql is "all rights reserved" and mixes MySQL/SQL Server/MS Access dialects | Original writing only, normalise to a single dialect (PostgreSQL) in the volume |
| 20 | C++ | cplusplus.com tutorial covers only up to C++11 | Volume covers C++11 per the source and adds a modern C++ (17/20) chapter from cppreference |
| 22 | C# | dotnet.microsoft.com/learn/csharp is JS-rendered | Official Microsoft Learn paths + C# docs; TOC marked inferred |
| 23 | Swift | swift.org/learn returns 404 (section moved) and the book needs JS | Official Swift book chapter list from the open-source sources; marked inferred |
| 26 | Docker | docker.com/get-started is a marketing splash with no TOC | Free docs.docker.com/get-started used as the learning path |
| 28 | Linux | linuxjourney.com redirects to the LabEx-hosted Linux Journey | Free Linux Journey courses used; paid LabEx labs ignored |
| 29 | Cybersecurity | tryhackme.com outlines require login; much content is subscription-gated | Free paths (Pre Security, Cyber Security 101) + free references (OWASP, MITRE ATT&CK, NIST) |
| 30 | DevOps | roadmap.sh/devops graph is JS-rendered | Standard DevOps track, marked inferred |
| 31-33 | Clouds | AWS/GCP/Azure training portals require login and are JS-heavy | Free public documentation (AWS Docs, Google Cloud docs, Microsoft Learn) |
| 34 | Data Structures | visualgo.net is an interactive visualiser with no lesson text | Standard DS&A curriculum with visualgo topics as the checklist |
| 11 | Blockchain | cryptozombies.io is a JS-only SPA; fetches returned transport errors | TOC reconstructed from search-indexed copies of the site's own pages (flagged inferred) and anchored to free official Solidity docs; artwork and narrative never copied |
| 12 | Next.js | none blocking; course text is (c) Vercel | Full 20-item TOC fetched live; original writing only |
| 13 | AI (basics) | course platform is JS-only and exercises need a free account | TOC inferred from secondary indexing (Univ. of Helsinki, EU EDIH listings); flagged inferred |
| 14 | PHP | none blocking; it is a best-practices reference, not a strict course | Full 19-section TOC fetched live; paraphrased only |
| 15 | API | **rapidapi.com/learn 404s and shows a login wall; the site was rebranded to "Nokia API Hub"** | Path marked INFERRED; plan anchored to official free docs (MDN HTTP, the OpenAPI Specification, RFC 9110). Re-check the URL before publishing |
| 18 | Design Patterns | refactoring.guru eBook and refactoring course are paid; content is "all rights reserved" with licensed illustrations | Topic names only; all explanations, diagrams and code written from scratch; no illustrations reused |
| 35 | System Design | systemdesign.one is partly paywalled | Free articles used as the syllabus; system-design fundamentals written from scratch |
| 36-37 | Python for AI, Data Science | kaggle.com/learn requires a free account; course pages are behind a login wall | All notes written as original, self-contained tutorials using plain Python + pandas + scikit-learn; no Kaggle notebooks reproduced |
| 38-39 | Machine Learning, Deep Learning | kaggle.com/learn/intro-to-ml and /intro-to-deep-learning are login-gated | Original writing from first principles using scikit-learn and TensorFlow; Kaggle's syllabus used as topic guide only |
| 43 | Generative AI | kaggle.com/learn/generative-ai is login-gated | OpenAI API and Python examples written from scratch; Kaggle syllabus used as topic guide only |
| 44 | LLMs | huggingface.co/learn/llm-course is free and public | No fallback needed |
| 45 | Prompt Engineering | learnprompting.org is free and public | No fallback needed |
| 46 | OpenAI API | platform.openai.com/docs is free and public | No fallback needed |
| 47-48 | Hugging Face, Fine-tuning | huggingface.co/docs is free and public | No fallback needed |
| 49 | AI Agents | huggingface.co/learn/agents-course is free and public | No fallback needed |
| 50 | LangChain | python.langchain.com/docs is free and public | No fallback needed |

## Rules applied

1. Every volume's notes are original writing (summaries, explanations,
   exercises, tests, code).
2. Short attributed snippets only when unavoidable, never full pages, images or
   wholesale code blocks.
3. Every consulted URL is listed in the volume's Sources chapter.
4. When a source is unreachable, login-gated or paywalled, the plan says so
   explicitly and names the fallback used.
