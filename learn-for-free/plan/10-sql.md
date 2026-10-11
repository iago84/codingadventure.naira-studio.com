# Vol. 10 – SQL – Study Plan

- Source site: https://www.w3schools.com/sql/
- Fetched: 2026-10-10
- Access: reachable (optional account; tutorials are free without login)
- Notes: Free SQL tutorial split into a core "SQL Tutorial" section, a "SQL Database" section, references, examples, exercises, and quizzes. Site carries ads and paid options; the tutorial content itself is free. Content © Refsnes Data — all rights reserved.

## Learning path (source order)
### SQL Tutorial (source order)
1. **SQL Intro** — what SQL is, relational database basics — https://www.w3schools.com/sql/sql_intro.asp
2. **SQL Syntax** — statement structure, semicolons, comments — https://www.w3schools.com/sql/sql_syntax.asp
3. **SQL Select** — selecting columns from tables — https://www.w3schools.com/sql/sql_select.asp
4. **SQL Select Distinct** — removing duplicates with DISTINCT — https://www.w3schools.com/sql/sql_distinct.asp
5. **SQL Where / And / Or / Not** — filtering rows, boolean conditions — https://www.w3schools.com/sql/sql_where.asp
6. **SQL Order By** — sorting result sets — https://www.w3schools.com/sql/sql_orderby.asp
7. **SQL Insert Into** — inserting rows — https://www.w3schools.com/sql/sql_insert.asp
8. **SQL Null Values** — NULL semantics — https://www.w3schools.com/sql/sql_null_values.asp
9. **SQL Update / Delete** — modifying and removing rows — https://www.w3schools.com/sql/sql_update.asp
10. **SQL Select Top / Limit** — limiting rows returned — https://www.w3schools.com/sql/sql_top.asp
11. **Aggregate Functions** — MIN, MAX, COUNT, SUM, AVG — https://www.w3schools.com/sql/sql_aggregate_functions.asp
12. **Pattern matching** — LIKE, wildcards, IN, BETWEEN — https://www.w3schools.com/sql/sql_like.asp
13. **Aliases** — renaming columns and tables — https://www.w3schools.com/sql/sql_alias.asp
14. **Joins** — inner, left, right, full, self joins — https://www.w3schools.com/sql/sql_join.asp
15. **Union / Union All** — combining result sets — https://www.w3schools.com/sql/sql_union.asp
16. **Group By / Having** — grouping rows, filtering groups — https://www.w3schools.com/sql/sql_groupby.asp
17. **Exists / Any / All** — subquery existence and quantifiers — https://www.w3schools.com/sql/sql_exists.asp
18. **Select Into / Insert Into Select** — copying data between tables — https://www.w3schools.com/sql/sql_select_into.asp
19. **SQL Case** — conditional expressions — https://www.w3schools.com/sql/sql_case.asp
20. **Null Functions** — IFNULL, ISNULL, COALESCE, NVL — https://www.w3schools.com/sql/sql_isnull.asp
21. **Stored Procedures** — creating and calling procedures — https://www.w3schools.com/sql/sql_stored_procedures.asp
22. **Comments / Operators** — comment syntax, operator reference — https://www.w3schools.com/sql/sql_comments.asp

### SQL Database (source order)
23. **Databases** — CREATE DB, DROP DB, backup DB — https://www.w3schools.com/sql/sql_create_db.asp
24. **Tables** — CREATE TABLE, DROP TABLE, ALTER TABLE — https://www.w3schools.com/sql/sql_create_table.asp
25. **Constraints** — NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT — https://www.w3schools.com/sql/sql_constraints.asp
26. **Indexes / Auto Increment** — CREATE INDEX, auto-increment columns — https://www.w3schools.com/sql/sql_create_index.asp
27. **Dates** — date/time types and functions — https://www.w3schools.com/sql/sql_dates.asp
28. **Views** — creating virtual tables — https://www.w3schools.com/sql/sql_view.asp
29. **Injection** — SQL injection risks and defenses — https://www.w3schools.com/sql/sql_injection.asp
30. **Parameters / Prepared Statements** — parameterized queries — https://www.w3schools.com/sql/sql_parameterized_queries.asp
31. **Hosting** — hosting SQL databases (external-side note) — https://www.w3schools.com/sql/sql_hosting.asp

Reference materials also on the page: keyword reference, data types, functions for MySQL / SQL Server / MS Access, quick reference — https://www.w3schools.com/sql/sql_ref_keywords.asp

## Planned chapters for the volume
1. Relational databases and SQL overview (covers source items: 1)
2. SQL syntax and statement basics (covers source items: 2)
3. Querying one table: SELECT and DISTINCT (covers source items: 3–4)
4. Filtering data: WHERE, AND/OR/NOT, IN, BETWEEN, LIKE, wildcards (covers source items: 5, 12)
5. Sorting and limiting results: ORDER BY, TOP/LIMIT (covers source items: 6, 10)
6. Inserting, updating, and deleting rows (covers source items: 7–9)
7. NULL values and null-handling functions (covers source items: 8, 20)
8. Joins: inner, left, right, full, self (covers source items: 14)
9. Set operations: UNION and UNION ALL (covers source items: 15)
10. Aggregation: MIN, MAX, COUNT, SUM, AVG, GROUP BY, HAVING (covers source items: 11, 16)
11. Subqueries: EXISTS, ANY, ALL, SELECT INTO, INSERT INTO SELECT (covers source items: 17–18)
12. Conditional logic with CASE (covers source items: 19)
13. Table and database management: CREATE/ALTER/DROP, constraints, indexes (covers source items: 23–26)
14. Dates and times in SQL (covers source items: 27)
15. Views and stored procedures (covers source items: 28, 21)
16. SQL security: injection, parameterized queries, prepared statements (covers source items: 29–30)

## Flags / issues
- Copyrighted source: W3Schools content is © Refsnes Data, all rights reserved — do NOT copy tutorial text, examples, or quizzes into the volume; write original explanations and use only short topic names with attribution-style references.
- Site is reachable without login for reading, but progress tracking and some features require an optional account; some linked services (certificates, PLUS) are paid — exclude those from the volume.
- Section ordering in the "SQL Database" part mixes basic and advanced DDL (e.g., Hosting lesson) — skip the Hosting lesson in the volume.
- Examples mix MySQL / SQL Server / MS Access dialects — the volume should pick ANSI-compatible SQL and note dialect differences (e.g., TOP vs LIMIT) rather than mirror the site's dialect switching.
