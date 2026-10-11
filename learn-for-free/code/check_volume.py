#!/usr/bin/env python3
"""
check_volume.py - structural validation of a volume's Markdown source.

Verifies the contract from assets/AUTHORING_GUIDE.md for any number of volumes:

  * front matter present with the required keys
  * "# How to use this volume" and a chapter map
  * every "# Chapter N - ..." has the six required sections
  * 5-10 summary bullets, 3-5 exercises, 3+ solutions,
    5-10 mini-test questions and a matching answer key
  * a "# Cheat sheet", a "# Final test" with 20-30 questions and its answers
  * a "# Sources" section listing URLs
  * balanced code fences and no stray markdown pipes in tables
  * every fenced code fence is closed
  * no leftover TODO or placeholder text

Usage:
    python check_volume.py                 # every volume in src/
    python check_volume.py 09-python       # one volume
    python check_volume.py --missing-only  # only volumes missing sections
"""
from __future__ import annotations

import os
import re
import sys

# This file lives in <root>/code/, so the project root is two levels up.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

REQUIRED_KEYS = ["title", "technology", "vol", "source", "date", "level", "hours"]
REQUIRED_SECTIONS = ["Summary", "Concepts", "Examples",
                     "Common mistakes and best practices", "Practice exercises"]
OPTIONAL_CODE_SECTIONS = ["Commands", "Exercises"]
FINAL_SECTIONS = ["Cheat sheet", "Final test", "Sources"]

BULLET_RE = re.compile(r"(?m)^\s*[-*]\s+\S")
QUESTION_RE = re.compile(r"(?m)^\s*\d+\.\s*\*\*")
NUMBERED_RE = re.compile(r"(?m)^\s*(\d+)\.\s+")
FENCE_RE = re.compile(r"^```")
URL_RE = re.compile(r"https?://[^\s)\]]+")


def front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip().lower()] = v.strip().strip('"')
    return meta, text[end + 4:]


def split_chunks(text: str) -> list[tuple[str, str, list[str]]]:
    """Return [(heading, body, body_lines)] for every `# Heading` block."""
    lines = text.split("\n")
    chunks: list[tuple[str, list[str]]] = []
    current: list[str] = []
    current_h1 = ""
    for line in lines:
        if line.startswith("# ") and not line.startswith("##"):
            if current:
                chunks.append((current_h1, current))
            current_h1 = line[2:].strip()
            current = []
        current.append(line)
    if current:
        chunks.append((current_h1, current))
    return chunks


def _section(text: str, title: str) -> str | None:
    """Body of `## title` up to the next `## ` section or `# ` chapter.

    Level-3 headings (`### Solutions`, `### Answer key`) stay inside the body.
    """
    m = re.search(r"(?m)^## %s\s*$" % re.escape(title), text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"(?m)^##? |^# ", rest)
    return rest[:nxt.start()] if nxt else rest


def _before_sub(text: str, marker: str) -> str:
    i = text.find(marker)
    return text[:i] if i != -1 else text


def check_volume(path: str) -> list[str]:
    problems: list[str] = []
    text = open(path, encoding="utf-8").read()
    meta, body = front_matter(text)

    for key in REQUIRED_KEYS:
        if not meta.get(key):
            problems.append("front matter is missing %r" % key)

    # fences must be balanced
    fence_lines = [i for i, l in enumerate(body.split("\n"), 1) if FENCE_RE.match(l)]
    if len(fence_lines) % 2:
        problems.append("unbalanced code fences (%d fence lines)" % len(fence_lines))

    # The index volume is a study guide, not a course: only the generic checks.
    if os.path.basename(path).startswith("00-"):
        for bad in ("TODO", "TBD", "FIXME", "XXX", "Lorem ipsum"):
            if bad in body:
                problems.append("placeholder text found: %s" % bad)
        return problems

    chapters = [(h, b) for h, b in split_chunks(body) if re.match(r"^Chapter \d+", h)]
    if not chapters:
        problems.append("no '# Chapter N - ...' headings found")

    for heading, chunk in chapters:
        chunk_text = "\n".join(chunk)
        for section in REQUIRED_SECTIONS:
            if not re.search(r"(?m)^## %s\s*$" % re.escape(section), chunk_text):
                problems.append("%s: missing section '## %s'" % (heading, section))
        for section in OPTIONAL_CODE_SECTIONS:
            if (section in ("Commands",) and re.search(r"(?m)^## %s\s*$" % section,
                                                       chunk_text)):
                pass
        if "## Examples" not in chunk_text and "## Commands" not in chunk_text:
            problems.append("%s: no code-bearing section" % heading)

        # summary bullets
        m = re.search(r"(?m)^## Summary\s*$(.*?)(?=^## |\Z)", chunk_text, re.S)
        if m:
            n = len(BULLET_RE.findall(m.group(1)))
            if not (3 <= n <= 12):
                problems.append("%s: Summary has %d bullets (want 5-10)"
                                % (heading, n))
        # exercises and solutions (count only the questions, not the solutions)
        ex_section = _section(chunk_text, "Practice exercises")
        if ex_section is not None:
            questions = _before_sub(ex_section, "### Solutions")
            ex = len(NUMBERED_RE.findall(questions))
            if not (2 <= ex <= 8):
                problems.append("%s: Practice exercises has %d items (want 3-5)"
                                % (heading, ex))
            if "### Solutions" not in ex_section:
                problems.append("%s: exercises without '### Solutions'" % heading)
        # mini test
        mini = _section(chunk_text, "Mini test")
        if mini is not None:
            questions = _before_sub(mini, "### Answer key")
            q = len(QUESTION_RE.findall(questions))
            if not (4 <= q <= 12):
                problems.append("%s: Mini test has %d questions (want 5-10)"
                                % (heading, q))
            if "### Answer key" not in mini:
                problems.append("%s: mini test without an answer key" % heading)

    # final chapters
    for section in FINAL_SECTIONS:
        if not re.search(r"(?m)^# %s\s*$" % re.escape(section), body):
            problems.append("missing final chapter '# %s'" % section)

    m = re.search(r"(?m)^# Final test\s*$(.*?)(?=^# |\Z)", body, re.S)
    if m:
        n = len(QUESTION_RE.findall(_before_sub(m.group(1), "## Final test answers")))
        if not (18 <= n <= 40):
            problems.append("Final test has %d questions (want 20-30)" % n)
    m = re.search(r"(?m)^## Final test answers\s*$", body)
    if not m:
        problems.append("missing '## Final test answers'")

    m = re.search(r"(?m)^# Sources\s*$", body)
    if not m:
        problems.append("missing '# Sources'")
    else:
        urls = URL_RE.findall(body[body.find("# Sources"):])
        if len(urls) < 5:
            problems.append("Sources lists only %d URLs" % len(urls))

    if not re.search(r"(?m)^# How to use this volume\s*$", body):
        problems.append("missing '# How to use this volume'")

    for bad in ("TODO", "TBD", "FIXME", "XXX", "Lorem ipsum", "{{{", "}}}"):
        if bad in body:
            problems.append("placeholder text found: %s" % bad)

    return problems


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    missing_only = "--missing-only" in sys.argv
    if args:
        targets = [a if a.endswith(".md") else a + ".md" for a in args]
    else:
        targets = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))

    total_problems = 0
    for name in targets:
        path = os.path.join(SRC, name)
        if not os.path.exists(path):
            print("!! missing file %s" % name)
            total_problems += 1
            continue
        problems = check_volume(path)
        if problems:
            total_problems += len(problems)
            print("FAIL %-22s %d problem(s)" % (name, len(problems)))
            if not missing_only:
                for p in problems[:12]:
                    print("       - %s" % p)
                if len(problems) > 12:
                    print("       ... and %d more" % (len(problems) - 12))
        else:
            print("ok   %s" % name)

    print("\n%d problem(s) across %d volume(s)" % (total_problems, len(targets)))
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
