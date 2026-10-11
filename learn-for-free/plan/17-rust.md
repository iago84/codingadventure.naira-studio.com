# Vol. 17 – Rust – Study Plan

- Source site: https://www.rust-lang.org/learn
- Fetched: 2026-10-10
- Access: reachable
- Notes: The `/learn` page is a curated index of official resources rather than an ordered course; it links to The Rust Programming Language (the canonical chapter-ordered path, 21 chapters + 7 appendices), Rust by Example, Rustlings and the reference books. Everything linked is free and open (MIT/Apache-2.0 licensed docs); `/learn` itself is JS-free static HTML.

## Learning path (source order)

Entry points listed on `/learn` (source order):
1. **The Rust Programming Language ("the book")** — Concept chapters plus three project chapters, the canonical first read — https://doc.rust-lang.org/book/
2. **Rust by Example** — Code-first alternative to the book, runnable examples with exercises — https://doc.rust-lang.org/rust-by-example/
3. **Rustlings** — Command-line course teaching Rust syntax in your own toolchain — https://github.com/rust-lang/rustlings/
4. **The standard library** — API reference for std — https://doc.rust-lang.org/std/index.html
5. **Edition Guide** — Migration and differences between Rust editions — https://doc.rust-lang.org/edition-guide/index.html
6. **Cargo Book** — Rust's package manager and build system — https://doc.rust-lang.org/cargo/index.html
7. **rustdoc Book** — Writing documentation for crates — https://doc.rust-lang.org/rustdoc/index.html
8. **rustc Book** — Compiler options and behaviour — https://doc.rust-lang.org/rustc/index.html
9. **Compiler Error Index** — Explanations of every rustc error code — https://doc.rust-lang.org/error-index.html
10. **Command Line Book** — Building CLI applications in Rust — https://rust-cli.github.io/book/index.html
11. **Embedded Book** — Rust for microcontrollers and embedded systems — https://doc.rust-lang.org/embedded-book
12. **The Reference** — More detailed than the book, not a formal spec — https://doc.rust-lang.org/reference/index.html
13. **The Rustonomicon** — Advanced and unsafe Rust — https://doc.rust-lang.org/nomicon/index.html
14. **The Unstable Book** — Nightly-only features — https://doc.rust-lang.org/nightly/unstable-book/index.html

Ordered chapter path inside the primary resource (The Rust Programming Language, doc.rust-lang.org/book):
1. **Getting Started** — Installation via rustup, "Hello, world!", Cargo basics — https://doc.rust-lang.org/book/ch01-00-getting-started.html
2. **Programming a Guessing Game** — Project chapter: let, match, methods, external crates — https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html
3. **Common Programming Concepts** — Variables, mutability, data types, functions, comments, control flow — https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html
4. **Understanding Ownership** — Ownership, references and borrowing, the slice type — https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html
5. **Using Structs to Structure Related Data** — Structs, methods, associated functions — https://doc.rust-lang.org/book/ch05-00-structs.html
6. **Enums and Pattern Matching** — Enums, `match`, `if let`, `let...else` — https://doc.rust-lang.org/book/ch06-00-enums.html
7. **Managing Growing Projects with Packages, Crates and Modules** — Module system, paths, privacy, `use` — https://doc.rust-lang.org/book/ch07-00-managing-growing-projects-with-packages-crates-and-modules.html
8. **Common Collections** — Vectors, strings, hash maps — https://doc.rust-lang.org/book/ch08-00-common-collections.html
9. **Error Handling** — `panic!`, `Result`, `?` operator, propagation — https://doc.rust-lang.org/book/ch09-00-error-handling.html
10. **Generic Types, Traits and Lifetimes** — Generics, trait bounds, lifetimes — https://doc.rust-lang.org/book/ch10-00-generics.html
11. **Writing Automated Tests** — Unit tests, integration tests, organisation — https://doc.rust-lang.org/book/ch11-00-testing.html
12. **An I/O Project: Building a Command Line Program** — Project chapter: a mini grep — https://doc.rust-lang.org/book/ch12-00-an-io-project.html
13. **Functional Language Features: Iterators and Closures** — Closures, iterator adapters, performance — https://doc.rust-lang.org/book/ch13-00-functional-features.html
14. **More About Cargo and Crates.io** — Workspaces, publishing, custom commands — https://doc.rust-lang.org/book/ch14-00-more-about-cargo.html
15. **Smart Pointers** — Box, Rc, RefCell, reference cycles, Deref/Drop — https://doc.rust-lang.org/book/ch15-00-smart-pointers.html
16. **Fearless Concurrency** — Threads, message passing, shared state, Sync/Send — https://doc.rust-lang.org/book/ch16-00-concurrency.html
17. **Fundamentals of Asynchronous Programming: Async, Await, Futures and Streams** — Async runtime model, tasks, futures — https://doc.rust-lang.org/book/ch17-00-async-await.html
18. **Object Oriented Programming Features of Rust** — OOP concepts expressed with traits and enums — https://doc.rust-lang.org/book/ch18-00-oop.html
19. **Patterns and Matching** — Pattern syntax, refutability, all pattern uses — https://doc.rust-lang.org/book/ch19-00-patterns.html
20. **Advanced Features** — Unsafe Rust, macros, lifetimes and traits deep-dive — https://doc.rust-lang.org/book/ch20-00-advanced-features.html
21. **Final Project: Building a Multithreaded Web Server** — Project chapter: TCP, threads, graceful shutdown — https://doc.rust-lang.org/book/ch21-00-final-project-a-web-server.html
22. **Appendix A: Keywords** — Reserved identifiers — https://doc.rust-lang.org/book/appendix-01-keywords.html
23. **Appendix B: Operators and Symbols** — Operator reference — https://doc.rust-lang.org/book/appendix-02-operators.html
24. **Appendix C: Derivable Traits** — Std traits you can derive — https://doc.rust-lang.org/book/appendix-03-derivable-traits.html
25. **Appendix D: Useful Development Tools** — rustfmt, clippy, rust-analyzer, rustup — https://doc.rust-lang.org/book/appendix-04-useful-development-tools.html
26. **Appendix E: Editions** — Rust 2015/2018/2021/2024 editions — https://doc.rust-lang.org/book/appendix-05-editions.html
27. **Appendix F: Translations of the Book** — Community translations — https://doc.rust-lang.org/book/appendix-06-translation.html
28. **Appendix G: How Rust is Made and Nightly Rust** — Release process and nightly — https://doc.rust-lang.org/book/appendix-07-nightly.html

## Planned chapters for the volume
1. Setup, toolchain and first program (covers source items: /learn items 1, 3; book ch. 1) — rustup, rustc, cargo new/build/run/check, project layout
2. Guessing game project (covers source item: book ch. 2) — hands-on use of let, match, methods and crates
3. Language fundamentals (covers source item: book ch. 3) — variables, mutability, scalar/compound types, functions, control flow
4. Ownership, borrowing and slices (covers source item: book ch. 4) — move semantics, references, the borrow checker
5. Structs, methods and enums (covers source items: book ch. 5-6) — custom data types, `match`, `if let`
6. Modules, packages and visibility (covers source item: book ch. 7) — crates, mod tree, `use`, privacy rules
7. Collections in std (covers source item: book ch. 8; /learn item 4) — Vec, String, HashMap; navigating std docs
8. Error handling and testing (covers source items: book ch. 9, 11) — Result, `?`, panic strategy, unit and integration tests
9. Generics, traits and lifetimes (covers source item: book ch. 10; /learn item 12) — abstraction without runtime cost
10. I/O project and Cargo in depth (covers source items: book ch. 12, 14; /learn item 6) — CLI arguments, file I/O, test organisation, workspaces, publishing
11. Smart pointers and functional features (covers source items: book ch. 13, 15) — Box/Rc/RefCell, closures, iterators
12. Concurrency, async and patterns (covers source items: book ch. 16, 17, 19) — threads, channels, Sync/Send, futures, pattern matching
13. Advanced features and OOP in Rust (covers source items: book ch. 18, 20; /learn items 9, 12, 13) — unsafe, macros, Rust's take on OOP, error index, Reference, Nomicon
14. Final project: multithreaded web server (covers source item: book ch. 21) — end-to-end build with graceful shutdown
15. Ecosystem and next steps (covers source items: /learn items 6, 7, 8, 10, 11, 14) — rustdoc, rustc options, CLI and embedded books, nightly workflow

## Flags / issues
- `/learn` is reachable and fully public, but it is an index page, not a chapter list: the ordered learning path had to be taken from the linked official book (doc.rust-lang.org/book), whose chapter list was read from the book's introduction; chapter URLs follow the stable mdbook naming convention and may shift with editions.
- No login, paywall or JS-only gating. The printed book is sold by No Starch Press, but the identical text is free online.
- Rust docs are MIT/Apache-2.0 licensed; still avoid copying prose — use topic names and original explanations only.
- The book assumes prior programming experience and explicitly skips "what is programming" basics; readers new to programming need a separate primer.
- The book's online edition is written against a specific Rust version and edition (2024 idioms); version drift should be re-checked at writing time.
