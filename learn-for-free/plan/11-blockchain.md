# Vol. 11 – Blockchain (Solidity) – Study Plan

- Source site: https://cryptozombies.io
- Fetched: 2026-10-10
- Access: js-only (direct fetches returned transport errors on every attempt, incl. `/`, `/en/solidity`, `/en/lesson/1`; site is a client-side React SPA, free to use in a browser)
- Notes: Free, no login required for the core Solidity course in a browser; lesson/chapter TOC below was recovered from the site's indexed pages via web search, not a live fetch (inferred, not fabricated).

## Learning path (source order)

Course 1 — "Solidity: Beginner to Intermediate Smart Contracts" (6 lessons):

1. **Making the Zombie Factory** — contracts, state variables, structs, arrays, functions, events, Web3.js basics — https://cryptozombies.io/en/solidity
2. **Zombies Attack Their Victims** — mappings, `require`, ownership/`msg.sender`, inheritance, imports, storage vs memory — https://cryptozombies.io/en/solidity
3. **Advanced Solidity Concepts** — internal/external visibility, gas costs, code optimization, security intro, `view`/`pure` — https://cryptozombies.io/en/solidity
4. **Zombie Battle System** — `payable` functions, randomness caveats, cooldowns, combining learned concepts — https://cryptozombies.io/en/solidity
5. **ERC721 & Crypto-Collectibles** — token standards, ERC721, OpenZeppelin, trading collectibles — https://cryptozombies.io/en/solidity
6. **App Front-ends & Web3.js** — calling contracts from JS, MetaMask, front-end for a DApp — https://cryptozombies.io/en/solidity

Course 2 — "Advanced Solidity: Get In-depth Knowledge":

7. **Deploying DApps with Truffle** — Truffle workflow and project structure for deploying contracts — https://cryptozombies.io/en/course
8. **Testing Smart Contracts with Truffle** — unit tests with Truffle, Ganache, Mocha, Chai, ERC721 transfer scenarios — https://cryptozombies.io/en/course
9. **How to Build an Oracle (Part 1)** — why contracts can't make HTTP calls; oracle architecture — https://cryptozombies.io/en/course
10. **How to Build an Oracle (Part 2)** — JavaScript/Node.js oracle component — https://cryptozombies.io/en/course
11. **How to Build an Oracle (Part 3)** — deploying and running the full oracle stack — https://cryptozombies.io/en/course

Course 3 — "Beyond Ethereum: Explore the Blockchain Ecosystem":

12. **Intro to zkSync** — ZK-rollup development basics — https://cryptozombies.io/en/course
13. **Advanced zkSync Concepts** — deeper zkSync patterns — https://cryptozombies.io/en/course
14. **Data Feeds and Computation** — Chainlink-style external data and computation — https://cryptozombies.io/en/course
15. **Deploying to TRON** — smart contracts on the TRON network — https://cryptozombies.io/en/course
16. **Intro to Smart Contract Development in Neo** — contracts on the Neo blockchain — https://cryptozombies.io/en/course
17. **Testing and Deploying Your Smart Contracts / Contract Deployment** — deployment topics for alt-chains (plus MultiversX/Polkadot/Optimism tracks on the site) — https://cryptozombies.io/en/course

Total TOC items found: 17 lessons (6 + 5 + 6), covering 3 named courses.

## Planned chapters for the volume

1. **Blockchain and Ethereum fundamentals** (covers source items: prerequisites of item 1 — accounts, gas, nodes, wallets)
2. **Your first smart contract** (covers source item 1 — contracts, state variables, integers, math)
3. **Data structures: structs and arrays** (covers source item 1 — structs, arrays, working with them)
4. **Functions, visibility and events** (covers source items 1, 3 — declarations, private/public, events)
5. **Ownership, mappings and security basics** (covers source items 2, 3 — msg.sender, require, gas and security)
6. **Inheritance, interfaces and imports** (covers source item 2 — code organization)
7. **Tokens and the ERC721 standard** (covers source item 5 — token standards, OpenZeppelin)
8. **A payable game economy** (covers source item 4 — payable functions, randomness, cooldowns)
9. **Front-ends and Web3.js** (covers source item 6 — MetaMask, calling contracts from JS)
10. **Tooling: Truffle, Ganache and deployment** (covers source items 7, 17)
11. **Testing smart contracts** (covers source item 8 — Mocha/Chai patterns)
12. **Oracles and external data** (covers source items 9–11, 14 — oracle pattern, Chainlink data feeds)
13. **The L2 and multi-chain landscape** (covers source items 12–13, 15–16 — zkSync, TRON, Neo, Optimism/Polkadot overview)
14. **Capstone: zombie-battle DApp** (covers all items — integrate contract + tests + front-end)

## Flags / issues

- Direct fetching of cryptozombies.io failed with transport errors on 4 URL variants; TOC above was reconstructed from search-engine-indexed copies of the site's own pages — treat lesson order as verified-by-index, not live-fetch.
- Site is a JS-heavy SPA; content is only fully rendered in a browser.
- Course content and artwork are © Loom Network; do not copy prose, code samples, or the zombie narrative into the volume — references and short topic names only.
