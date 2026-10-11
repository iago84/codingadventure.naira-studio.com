# Vol. 23 – Swift – Study Plan

- Source site: https://www.swift.org/learn/
- Fetched: 2026-10-10
- Access: js-only (source page gone)
- Notes: https://www.swift.org/learn/ returns HTTP 404 — swifts.org restructured its documentation section; the rendered docs at docs.swift.org require JavaScript ("This page requires JavaScript"). Plan is based on the free public official documentation: *The Swift Programming Language* (TSPL), whose source lives in the official swiftlang/swift-book repository. Chapter order below is INFERRED from the book's canonical ordering and the source file names — not from a fetched rendered TOC.

## Learning path (source order)
1. **Guided Tour** — First taste of Swift language and REPL-style walkthrough — https://github.com/swiftlang/swift-book/tree/main/TSPL.docc/GuidedTour
2. **The Basics** — Constants, variables, types, optionals basics — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/TheBasics.md
3. **Basic Operators** — Arithmetic, comparison, logical, range operators — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/BasicOperators.md
4. **Strings and Characters** — String API, character handling, Unicode — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/StringsAndCharacters.md
5. **Collection Types** — Arrays, sets, dictionaries — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/CollectionTypes.md
6. **Control Flow** — Conditionals, loops, defer, guard, early exits — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/ControlFlow.md
7. **Functions** — Parameters, argument labels, variadic/inout, function types — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Functions.md
8. **Closures** — Closure expressions, trailing closures, capturing — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Closures.md
9. **Enumerations** — Raw and associated values, indirect enums — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Enumerations.md
10. **Structures and Classes** — Value vs reference semantics, identity — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/ClassesAndStructures.md
11. **Properties** — Stored, computed, lazy, property observers, wrappers — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Properties.md
12. **Methods** — Instance/type methods, mutating, subscripts basics — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Methods.md
13. **Subscripts** — Custom subscript syntax and usage — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Subscripts.md
14. **Inheritance** — Subclassing, overriding, initializers relation — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Inheritance.md
15. **Initialization** — Designated/convenience init, failable init, required — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Initialization.md
16. **Deinitialization** — deinit and cleanup — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Deinitialization.md
17. **Optional Chaining** — Chained optional member access — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/OptionalChaining.md
18. **Error Handling** — throws/try/catch, throwing functions — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/ErrorHandling.md
19. **Concurrency** — async/await, structured concurrency, actors — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Concurrency.md
20. **Macros** — Freestanding/attached macros, expansion — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Macros.md
21. **Type Casting** — is/as, Any/AnyObject, downcasting — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/TypeCasting.md
22. **Nested Types** — Types nested in types — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/NestedTypes.md
23. **Extensions** — Adding capabilities to existing types — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Extensions.md
24. **Protocols** — Protocol syntax, delegation, conformance — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Protocols.md
25. **Generics** — Generic functions/types, where clauses — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/Generics.md
26. **Opaque Types** — some P and opaque return types — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/OpaqueTypes.md
27. **Automatic Reference Counting** — ARC, retain cycles, weak/unowned — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/AutomaticReferenceCounting.md
28. **Memory Safety** — Conflicting-access rules — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/MemorySafety.md
29. **Access Control** — open/public/internal/fileprivate/private — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/AccessControl.md
30. **Advanced Operators** — Bitwise, overflow, custom operators, precedence — https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/AdvancedOperators.md
31. **Language Reference** — Grammar: lexical structure, types, expressions, statements, declarations — https://github.com/swiftlang/swift-book/tree/main/TSPL.docc/ReferenceManual

## Planned chapters for the volume
1. Swift Tour: Setup and First Look (covers source items: 1)
2. Variables, Constants and Basic Types (covers source items: 2)
3. Operators and Expressions (covers source items: 3, 30)
4. Strings and Characters (covers source items: 4)
5. Collections: Array, Set, Dictionary (covers source items: 5)
6. Control Flow and Optionals Handling (covers source items: 6, 17)
7. Functions and Closures (covers source items: 7, 8)
8. Enumerations and Pattern Matching Basics (covers source items: 9)
9. Structures, Classes and Value vs Reference Types (covers source items: 10)
10. Properties, Methods and Subscripts (covers source items: 11, 12, 13)
11. Inheritance and Initialization (covers source items: 14, 15, 16)
12. Protocols and Delegation (covers source items: 24)
13. Extensions and Type Casting (covers source items: 23, 21, 22)
14. Generics and Opaque Types (covers source items: 25, 26)
15. Error Handling and Result Types (covers source items: 18)
16. Concurrency: async/await, Actors (covers source items: 19)
17. ARC and Memory Safety (covers source items: 27, 28)
18. Access Control and Module Design (covers source items: 29)
19. Macros (covers source items: 20)
20. Language Reference and Advanced Grammar (covers source items: 31)

## Flags / issues
- The URL provided (swift.org/learn/) returns 404 — the /learn section no longer exists; swift.org/documentation/ now redirects to docs.swift.org which is JS-only.
- No rendered TOC could be fetched. The ordered TOC above is INFERRED from the official swift-book source files (GitHub API listing + the book's canonical chapter order). Verify ordering against the rendered Swift book before finalising.
- TSPL is (c) Apple/Swift.org — reference topic names only; do not reproduce prose or code snippets in the volume.
