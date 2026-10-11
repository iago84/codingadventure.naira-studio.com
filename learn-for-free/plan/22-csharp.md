# Vol. 22 – C# – Study Plan

- Source site: https://dotnet.microsoft.com/learn/csharp
- Fetched: 2026-10-10
- Access: js-only
- Notes: The learn/csharp hub is a JavaScript-rendered marketing page; the course list (free courses/tutorials/videos) did not appear in static fetch. Plan is based on the free official Microsoft Learn C# beginner learning paths ("Get started with C#" Parts 1-5) plus the official C# documentation TOC (learn.microsoft.com/en-us/dotnet/csharp/).

## Learning path (source order)
**Microsoft Learn "Get started with C#" series (Parts 1-5, in order):**
1. **Part 1: Write your first C# code** — Basic syntax via in-browser code examples — https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/
   - Write your first C# code — https://learn.microsoft.com/en-us/training/modules/csharp-write-first/
   - Store data with variables in C# — https://learn.microsoft.com/en-us/training/modules/csharp-literals-variables/
   - Perform basic operations on numbers in C# — https://learn.microsoft.com/en-us/training/modules/csharp-basic-operations/
   - Add decision logic to your code in C# — https://learn.microsoft.com/en-us/training/modules/csharp-if-elseif-else/
2. **Part 2: Create and run simple C# console applications** — VS Code, loops, arrays/lists, methods, file I/O — https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-2/
   - Install and configure Visual Studio Code — /modules/install-configure-visual-studio-code/
   - Repeat actions with loops in C# — /modules/csharp-repeat-actions-loops/
   - Organize data with arrays and lists in C# — /modules/csharp-arrays-lists/
   - Write reusable code in C# — /modules/csharp-reusable-code/
   - Read and write files in C# — /modules/csharp-read-write-files/
3. **Part 3: Add logic to C# console applications** — Boolean expressions, scope, switch, for/while, guided + challenge projects — https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-3/
   - Evaluate Boolean expressions to make decisions — /modules/csharp-evaluate-boolean-expressions/
   - Control variable scope and logic using code blocks — /modules/csharp-code-blocks/
   - Branch the flow of code using switch-case — /modules/csharp-switch-case/
   - Iterate through a code block using for — /modules/csharp-for/
   - Add looping logic using do-while and while — /modules/csharp-do-while/
   - Guided project: conditional branching and looping — /modules/guided-project-develop-conditional-branching-looping/
   - Challenge project: branching and looping structures — /modules/challenge-project-develop-branching-looping-structures-c-sharp/
4. **Part 4: Work with variable data in C# console applications** — Data types, conversion, array operations, string formatting — https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-4/
   - Choose the correct data type — /modules/csharp-choose-data-type/
   - Convert data types using casting and conversion — /modules/csharp-convert-cast/
   - Perform operations on arrays using helper methods — /modules/csharp-arrays-operations/
   - Format alphanumeric data for presentation — /modules/csharp-format-strings/
   - Modify the content of strings — /modules/csharp-modify-content/
   - Guided project: work with variable data — /modules/guided-project-work-variable-data-c-sharp/
   - Challenge project: work with variable data — /modules/challenge-project-work-variable-data-c-sharp/
5. **Part 5: Create methods in C# console applications** — Methods, parameters, return values, projects — https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-5/
   - Write your first C# method — /modules/write-first-c-sharp-method/
   - Create C# methods with parameters — /modules/create-c-sharp-methods-parameters/
   - Create C# methods that return values — /modules/create-c-sharp-methods-return-values/
   - Guided project: Plan a Petting Zoo Visit — /modules/guided-project-visit-petting-zoo/
   - Challenge project: Create a mini-game — /modules/challenge-project-create-mini-game/
   (A Part 6 "Debug C# console applications" path is listed by Microsoft Learn: https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-6/)

**Official C# documentation structure (learn.microsoft.com/en-us/dotnet/csharp/):**
6. Get started — Beginner tutorials (incl. in-browser Hello world), A tour of C#, language-specific tips (for Java/JS/Python developers), what you can build — https://learn.microsoft.com/en-us/dotnet/csharp/
7. Fundamentals — C# overview/tour, program structure, type system, object-oriented programming, pattern matching, exceptions, coding style, LINQ, async — https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/overview
8. What's new / key concepts — C# 12/13/14 features, records, top-level statements, LINQ and async programming concepts — https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/
9. C# language reference — Keywords, operators and expressions, tokens, full language reference — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/

## Planned chapters for the volume
1. Hello C#: First Program and Program Structure (covers source items: 1a, 6, 7)
2. Variables, Literals and Data Types (covers source items: 1b, 4a)
3. Operators, Arithmetic and Expressions (covers source items: 1c, 4b)
4. Decision Logic and Branching (covers source items: 1d, 3a, 3c)
5. Loops and Iteration (covers source items: 2b, 3d, 3e)
6. Arrays, Lists and Collections (covers source items: 2c, 4c)
7. Strings and Text Formatting (covers source items: 4d, 4e)
8. Methods and Parameters (covers source items: 2d, 5a-5c)
9. Toolchain and File I/O (covers source items: 2a, 2e)
10. Object-Oriented C# (covers source items: 7)
11. Exceptions and Error Handling (covers source items: 7)
12. Pattern Matching and Switch Expressions (covers source items: 7, 8)
13. LINQ and Delegates (covers source items: 7, 8)
14. Async/Await and Concurrency Basics (covers source items: 7, 8)
15. Debugging Visual Studio Code C# Apps (covers source items: Part 6 path)
16. Project Lab: Console Mini-Game / Guided Challenge (covers source items: 3f, 3g, 4f, 4g, 5d, 5e)
17. Modern C#: Records, Top-level Statements, What's New (covers source items: 8)

## Flags / issues
- dotnet.microsoft.com/learn/csharp is JS-only: the ordered course list did not render in fetch; plan anchored on Microsoft Learn official free paths (free, no login for read) + official C# docs.
- Microsoft Learn may require sign-in for progress/achievements; content itself is public.
- All content Microsoft copyright — do not copy text/instructions; only short topic names used above.
- "Part 6" (Debug) TOC not fetched (assumed to exist from the series listing on Parts 1-5 pages).
