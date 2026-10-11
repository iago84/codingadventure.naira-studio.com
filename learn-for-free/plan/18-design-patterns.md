# Vol. 18 – Design Patterns – Study Plan

- Source site: https://refactoring.guru
- Fetched: 2026-10-10
- Access: reachable (partially paywalled)
- Notes: Freemium site: pattern/refactoring descriptions, catalogs and multi-language code examples are public and free, but the downloadable eBook and the refactoring course are paid (Premium Content / store) and a login exists for buyers. The site publishes a Content Usage Policy (all rights reserved, illustrations by Dmitry Zhart) — no prose or images may be reproduced; only topic names and structure may inform original writing.

## Learning path (source order)

Foundations (What is a Pattern):
1. **What's a design pattern?** — Definition and anatomy of a pattern — https://refactoring.guru/design-patterns/what-is-pattern
2. **History of patterns** — From architecture (Alexander) to GoF and beyond — https://refactoring.guru/design-patterns/history
3. **Why should I learn patterns?** — Value and shared vocabulary — https://refactoring.guru/design-patterns/why-learn
4. **Criticism of patterns** — Common objections and overuse warnings — https://refactoring.guru/design-patterns/criticism
5. **Classification of patterns** — Creational, structural, behavioral grouping — https://refactoring.guru/design-patterns/classification
6. **Catalog** — Index of all 23 GoF patterns with intent summaries — https://refactoring.guru/design-patterns/catalog

Creational patterns:
7. **Factory Method** — Defer instantiation to subclasses via a creation interface — https://refactoring.guru/design-patterns/factory-method
8. **Abstract Factory** — Create families of related objects without concrete classes — https://refactoring.guru/design-patterns/abstract-factory
9. **Builder** — Step-by-step construction of complex objects — https://refactoring.guru/design-patterns/builder
10. **Prototype** — Clone objects instead of constructing them — https://refactoring.guru/design-patterns/prototype
11. **Singleton** — One instance with global access — https://refactoring.guru/design-patterns/singleton

Structural patterns:
12. **Adapter** — Wrap an incompatible interface behind a expected one — https://refactoring.guru/design-patterns/adapter
13. **Bridge** — Separate abstraction from implementation — https://refactoring.guru/design-patterns/bridge
14. **Composite** — Treat trees of objects uniformly — https://refactoring.guru/design-patterns/composite
15. **Decorator** — Add behavior dynamically by wrapping — https://refactoring.guru/design-patterns/decorator
16. **Facade** — Simplified entry point to a subsystem — https://refactoring.guru/design-patterns/facade
17. **Flyweight** — Share fine-grained state to save memory — https://refactoring.guru/design-patterns/flyweight
18. **Proxy** — Placeholder controlling access to another object — https://refactoring.guru/design-patterns/proxy

Behavioral patterns:
19. **Chain of Responsibility** — Pass a request along a handler chain — https://refactoring.guru/design-patterns/chain-of-responsibility
20. **Command** — Encapsulate a request as an object — https://refactoring.guru/design-patterns/command
21. **Iterator** — Traverse a collection without exposing its structure — https://refactoring.guru/design-patterns/iterator
22. **Mediator** — Centralise complex communication between objects — https://refactoring.guru/design-patterns/mediator
23. **Memento** — Capture and restore object state — https://refactoring.guru/design-patterns/memento
24. **Observer** — Notify dependents of state changes — https://refactoring.guru/design-patterns/observer
25. **State** — Alter behavior when internal state changes — https://refactoring.guru/design-patterns/state
26. **Strategy** — Swap interchangeable algorithms at runtime — https://refactoring.guru/design-patterns/strategy
27. **Template Method** — Fix an algorithm skeleton, defer steps to subclasses — https://refactoring.guru/design-patterns/template-method
28. **Visitor** — Add operations to a structure without changing its classes — https://refactoring.guru/design-patterns/visitor

Code examples by language (same catalog rendered in 10 languages):
29. **Code Examples index** — C#, C++, Go, Java, PHP, Python, Ruby, Rust, Swift, TypeScript — https://refactoring.guru/design-patterns/examples

Adjacent refactoring section (source order, summarised):
30. **What is Refactoring** — Clean code, technical debt, when and how to refactor — https://refactoring.guru/refactoring
31. **Code Smells catalog** — 22 smells in 6 groups (bloaters, OO abusers, change preventers, dispensables, couplers, other) — https://refactoring.guru/refactoring/smells
32. **Refactorings catalog** — 66 techniques in 6 groups (composing methods, moving features, organizing data, simplifying conditionals, simplifying method calls, dealing with generalization) — https://refactoring.guru/refactoring/techniques

## Planned chapters for the volume
1. What a design pattern is (covers source items: 1-6) — definition, history, motivation, criticism, classification
2. Design principles behind patterns (inferred from standard curriculum; SOLID and general OO design principles are standard companions to this catalog) — SRP, OCP, LSP, ISP, DIP, composition over inheritance
3. Creational patterns I: Factory Method and Abstract Factory (covers source items: 7-8)
4. Creational patterns II: Builder, Prototype, Singleton (covers source items: 9-11)
5. Structural patterns I: Adapter, Bridge, Composite (covers source items: 12-14)
6. Structural patterns II: Decorator, Facade, Flyweight, Proxy (covers source items: 15-18)
7. Behavioral patterns I: Chain of Responsibility, Command, Iterator (covers source items: 19-21)
8. Behavioral patterns II: Mediator, Memento, Observer (covers source items: 22-24)
9. Behavioral patterns III: State, Strategy, Template Method, Visitor (covers source items: 25-28)
10. Patterns across languages (covers source items: 29 + Go/Rust/TypeScript volumes of this library) — idiomatic expression of the catalog in different paradigms, including where the pattern is unnecessary
11. Code smells and when to refactor (covers source items: 30-31)
12. Core refactoring techniques (covers source item: 32 + inferred selection from the 66-entry catalog) — extract method/class, move method, replace conditional with polymorphism, introduce parameter object, pull up/push down, replace inheritance with delegation
13. Refactoring safely (inferred) — tests as a safety net, characterisation tests, small commits, IDE-assisted refactorings
14. Case study and capstone (inferred) — recognise smells in a legacy-style codebase, then apply patterns and refactorings to clean it up

## Flags / issues
- Site is reachable and the pattern content itself is free to read; however the eBook and the refactoring course are paid, and any login-gated or premium pages must not be used as a source of copied text.
- Copyright is explicit: "All rights reserved", illustrations licensed to the author, and a dedicated Content Usage Policy. Only short topic names may be taken; every explanation, example and diagram must be original.
- Pattern pages exist in many languages (site translations) — keep the volume consistent with one language set and cite the site's own multi-language examples as further reading rather than transcribing them.
- Two chapters (design principles/SOLID, and refactoring-safety) are inferred from standard curriculum knowledge: SOLID was not present in the fetched navigation of this page.
- Some listed patterns (Singleton especially) are widely criticised as anti-patterns in modern languages; the chapter on criticism should be honoured, not buried.
