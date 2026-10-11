# Vol. 20 – C++ – Study Plan

- Source site: https://cplusplus.com/doc/tutorial/
- Fetched: 2026-10-10
- Access: reachable
- Notes: Complete, free, no-login language tutorial grouped into 7 sections and 25 chapters, with runnable examples in every chapter. Static HTML; the site also hosts a Reference and Articles. Copyright is explicit ("© cplusplus.com, 2000-2026 — All rights reserved") and the site states it is maintained by a single author, so no text may be reproduced — topic names only.

## Learning path (source order)
1. **Compilers** (Introduction) — What a compiler does, setting up a toolchain — https://cplusplus.com/doc/tutorial/introduction/
2. **Structure of a program** — Translation units, functions, comments, basic syntax — https://cplusplus.com/doc/tutorial/program_structure/
3. **Variables and types** — Identifiers, fundamental types, declaration and initialisation — https://cplusplus.com/doc/tutorial/variables/
4. **Constants** — Literals, typed constants, const-qualified values — https://cplusplus.com/doc/tutorial/constants/
5. **Operators** — Arithmetic, relational, logical, assignment, increment, conditional operator — https://cplusplus.com/doc/tutorial/operators/
6. **Basic Input/Output** — `cin`/`cout` streams and simple formatting — https://cplusplus.com/doc/tutorial/basic_io/
7. **Statements and flow control** — Selection statements, iteration, jump statements — https://cplusplus.com/doc/tutorial/control/
8. **Functions** — Definitions, parameters, return values, scope, recursion, prototypes — https://cplusplus.com/doc/tutorial/functions/
9. **Overloads and templates** — Function overloading and function templates — https://cplusplus.com/doc/tutorial/functions2/
10. **Name visibility** — Namespaces, `using`, name lookup — https://cplusplus.com/doc/tutorial/namespaces/
11. **Arrays** — Declaration, initialisation, multidimensional arrays — https://cplusplus.com/doc/tutorial/arrays/
12. **Character sequences** — null-terminated strings and their pitfalls — https://cplusplus.com/doc/tutorial/ntcs/
13. **Pointers** — Address-of, dereference, pointer arithmetic, pointers and arrays — https://cplusplus.com/doc/tutorial/pointers/
14. **Dynamic memory** — `new`/`delete`, allocation and leaks — https://cplusplus.com/doc/tutorial/dynamic/
15. **Data structures** — Aggregating several types into one type — https://cplusplus.com/doc/tutorial/structures/
16. **Other data types** — Type aliases, unions, enumerations, references — https://cplusplus.com/doc/tutorial/other_data_types/
17. **Classes (I)** — Class syntax, members, constructors, access specifiers — https://cplusplus.com/doc/tutorial/classes/
18. **Classes (II)** — Pointers to classes, `this`, static members, const members — https://cplusplus.com/doc/tutorial/templates/
19. **Special members** — Copy constructor, default constructor, destructor, assignment operator, move semantics — https://cplusplus.com/doc/tutorial/classes2/
20. **Friendship and inheritance** — Friend functions/classes, inheritance, access and visibility — https://cplusplus.com/doc/tutorial/inheritance/
21. **Polymorphism** — Virtual functions, abstract classes, dynamic dispatch, multiple inheritance — https://cplusplus.com/doc/tutorial/polymorphism/
22. **Type conversions** — Implicit/explicit conversions, `static_cast`, `dynamic_cast`, `reinterpret_cast`, `const_cast` — https://cplusplus.com/doc/tutorial/typecasting/
23. **Exceptions** — try/catch/throw, exception specifications, standard exceptions — https://cplusplus.com/doc/tutorial/exceptions/
24. **Preprocessor directives** — Macros, conditional compilation, include guards — https://cplusplus.com/doc/tutorial/preprocessor/
25. **Input/output with files** (Standard Library) — File streams, open modes, text and binary I/O — https://cplusplus.com/doc/tutorial/files/

## Planned chapters for the volume
1. Toolchain and first program (covers source items: 1-2) — compilers, build steps, translation units, `main`
2. Variables, constants and types (covers source items: 3-4) — fundamental types, signedness, `const`, `constexpr` (modern note)
3. Operators and basic I/O (covers source items: 5-6) — operator categories and precedence, stream I/O
4. Control flow (covers source item: 7) — selection, loops, jumps, range-based for (modern note)
5. Functions (covers source items: 8) — definitions, overloading basics, scope, recursion, prototypes
6. Overloading and templates (covers source items: 9) — overload resolution, function templates, `auto` return types (modern note)
7. Namespaces and scope (covers source item: 10) — namespaces, `using`, ADL, inline namespaces
8. Compound data I: arrays, character sequences, data structures (covers source items: 11, 12, 15)
9. Compound data II: pointers, references and dynamic memory (covers source items: 13, 14, 16) — plus smart pointers as the modern replacement (supplementary)
10. Classes I: syntax and constructors (covers source items: 17) — encapsulation, member functions, access control
11. Classes II: pointers to classes, `this`, statics (covers source item: 18)
12. Special members and the rule of three/five/zero (covers source item: 19) — copy/move/destroy semantics
13. Friendship and inheritance (covers source item: 20) — base/derived design, access rules
14. Polymorphism (covers source item: 21) — virtual dispatch, abstract classes, `override`/`final` (modern note), multiple inheritance
15. Type conversions and casts (covers source item: 22)
16. Exceptions and error handling (covers source item: 23) — RAII, exception safety guarantees, noexcept
17. Preprocessor, macros and modular compilation (covers source item: 24) — include guards, conditional compilation, modules as a modern alternative (supplementary)
18. File I/O and the standard library (covers source item: 25, supplemented) — fstreams, `<string>`, containers, algorithms, smart pointers
19. Capstone project (inferred; covers the full tutorial) — a console application using classes, inheritance, containers and error handling

## Flags / issues
- Site is reachable, free and needs no login; the chapter list above was fetched directly from https://cplusplus.com/doc/tutorial/.
- The tutorial is explicitly written "up to the newest features introduced by C++11" — C++14/17/20/23 additions (lambdas, smart pointers, `auto`, range-for, structured bindings, concepts, modules, coroutines) are NOT in this TOC and are flagged as supplementary from the site's Reference section and cppreference.com.
- Copyright is explicit ("All rights reserved"); no text or example code may be copied — topic names and chapter ordering only.
- Chapter 18 ("Classes (II)") is served from the URL path `/templates/`, which is a historical mismatch on the source site; it is not about templates — normal templates content lives under "Overloads and templates".
- The tutorial predates the modern "Core Guidelines"/RAII-centric teaching style; chapters on pointers and `new`/`delete` should be presented with their modern safe alternatives (smart pointers, containers, RAII) alongside the classic material, which is how the source itself treats them.
- Some Reference links on the site may require the separate /reference/ tree; only the /doc/tutorial/ tree was fetched for this plan.
