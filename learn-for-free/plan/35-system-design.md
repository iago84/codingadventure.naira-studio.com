# Vol. 35 – System Design – Study Plan

- Source site: https://systemdesign.one (plus /categories/, /categories/fundamentals/, /categories/deep-dive/)
- Fetched: 2026-10-10
- Access: reachable (homepage shell is JS-rendered, but the archive/category pages server-render the full article list)
- Notes: Personal blog by Neo Kim (2022–2023 articles) built around a newsletter; content is fully copyrighted — only short topic titles are listed; no article text will be copied. Archive contains two categories: Fundamentals (9 articles) and Deep Dive case studies (8 articles).

## Learning path (source order)
**Fundamentals (1 of 2):**
1. **What Happens When You Type a URL Into Your Browser?** — DNS, TCP/TLS, HTTP request lifecycle end to end — https://systemdesign.one/what-happens-when-you-type-url-into-your-browser/
2. **How to Troubleshoot if You Can't Access a Particular Website?** — Systematic network debugging approach — https://systemdesign.one/how-to-troubleshoot-if-you-cannot-access-a-website/
3. **Consistent Hashing Explained** — Hash rings, virtual nodes, rebalancing — https://systemdesign.one/consistent-hashing-explained/
4. **Bloom Filters Explained** — Probabilistic membership testing, false positives — https://systemdesign.one/bloom-filters-explained/
5. **Quotient Filter Explained** — Compact alternative to bloom filters — https://systemdesign.one/quotient-filter-explained/
6. **Back of the Envelope** — Estimation and capacity planning techniques — https://systemdesign.one/back-of-the-envelope/
7. **What Is Service Discovery?** — Locating services in dynamic environments — https://systemdesign.one/what-is-service-discovery/
8. **Gossip Protocol** — Epidemic-style information dissemination — https://systemdesign.one/gossip-protocol/
9. **Consistency Patterns** — Consistency models in distributed systems — https://systemdesign.one/consistency-patterns/
10. **Hinted Handoff** — Sloppy quorum write hand-off technique — https://systemdesign.one/hinted-handoff/

**Deep Dive case studies (2 of 2):**
11. **URL Shortening System Design** — Designing a URL shortener — https://systemdesign.one/url-shortening-system-design/
12. **System Design Pastebin** — Text-paste service design — https://systemdesign.one/system-design-pastebin/
13. **System Design Interview Cheat Sheet** — Condensed interview reference — https://systemdesign.one/system-design-interview-cheatsheet/
14. **Leaderboard System Design** — Real-time ranking systems — https://systemdesign.one/leaderboard-system-design/
15. **Live Comment System Design** — Live-streaming comment systems — https://systemdesign.one/live-comment-system-design/
16. **Real Time Presence Platform System Design** — Online/offline presence tracking — https://systemdesign.one/real-time-presence-platform-system-design/
17. **Distributed Counter System Design** — Counting at scale — https://systemdesign.one/distributed-counter-system-design/
18. **Slack Architecture** — Slack's high-level architecture — https://systemdesign.one/slack-architecture/

## Planned chapters for the volume
1. Request Lifecycle & Networking Fundamentals (covers source items 1, 2)
2. Back-of-the-Envelope Estimation (covers source item 6)
3. Hashing, Sharding & Consistent Hashing (covers source items 3, 4, 5)
4. Caching, CDNs & Proxies (standard system-design core, complements items 1, 3)
5. Databases, Replication & Sharding (covers source item 9)
6. Distributed Primitives: Service Discovery, Gossip, Hinted Handoff (covers source items 7, 8, 10)
7. Messaging, Eventing & Real-Time Systems (covers source items 14, 15, 16)
8. Capstone Case Study: URL Shortener (covers source items 11, 13)
9. Capstone Case Study: Pastebin & Chat (covers source items 12, 18)
10. Interview Strategy & Cheat Sheet Synthesis (covers source item 13, 17)

## Flags / issues
- Blog content is fully copyrighted (personal site, not open-licensed) — do NOT copy article text; write original explanations of the same concepts.
- Homepage search/listing is JavaScript-rendered; the ordered TOC came from the server-rendered /categories/ archive (18 articles, last updated 2023) — site may have newer newsletter-only material not in the public archive.
- Site footer shows 2022–2025 but archive articles end in 2023; some content may live behind the paid newsletter — treat anything beyond the public archive as unavailable.
