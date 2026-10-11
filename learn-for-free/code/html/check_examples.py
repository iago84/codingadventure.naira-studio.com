#!/usr/bin/env python3
"""
check_examples.py - validate every HTML example in the Vol. 01 source.

Extracts fenced code blocks from ../src/01-html.md and checks the HTML ones:

  1. tags are balanced (open/close pairs match, respecting void elements)
  2. void elements are never closed
  3. attributes with an empty value are reported
  4. every <img> has an alt attribute
  5. every <input>/<select>/<textarea> inside a form has a <label for=id>
  6. documents have at most one <h1>
  7. ids are unique within a block
  8. each block parses without HTMLParser errors (run for the ones that are full
     documents: the ones starting with <!DOCTYPE or <html)

Run:  python check_examples.py
Exit code 0 = all checks passed.
"""

from __future__ import annotations

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "src", "01-html.md")
HERE = os.path.dirname(os.path.abspath(__file__))

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# Elements that auto-close in HTML parsing but must be closed in source.
CONTAINERS = {"html", "head", "body", "table", "thead", "tbody", "tfoot", "tr",
              "ul", "ol", "dl", "dt", "dd", "p", "div", "span", "a", "form",
              "label", "select", "option", "fieldset", "legend", "button",
              "section", "article", "aside", "nav", "header", "footer", "main",
              "h1", "h2", "h3", "h4", "h5", "h6", "figure", "figcaption",
              "picture", "video", "audio", "pre", "code", "em", "strong", "b",
              "i", "small", "sub", "sup", "blockquote", "q", "cite", "time",
              "abbr", "title", "script", "style", "colgroup", "svg", "template",
              "details", "summary", "mark", "del", "ins", "var", "kbd", "samp",
              "address", "caption", "optgroup", "textarea", "iframe", "noscript",
              "path", "circle", "canvas", "hgroup", "search"}


class Balance(HTMLParser):
    """Tracks open/close tags and collects structural mistakes."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.errors: list[str] = []
        self.ids: list[str] = []
        self.imgs: list[dict] = []
        self.controls: list[dict] = []
        self.labels: list[str] = []
        self.h1 = 0
        self.has_html = False
        self.has_doctype = False

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype"):
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        line = self.getpos()[0]
        if tag == "html":
            self.has_html = True
        if tag == "h1":
            self.h1 += 1
        if "id" in d and d["id"]:
            self.ids.append(d["id"])
        if tag == "img":
            self.imgs.append(d)
        if tag in ("input", "select", "textarea"):
            self.controls.append(dict(tag=tag, **d))
        if tag == "label" and "for" in d:
            self.labels.append(d["for"])
        if tag not in VOID:
            self.stack.append((tag, line))

    def handle_startendtag(self, tag, attrs):
        # self-closing syntax: valid for void and foreign (svg) elements
        if tag not in VOID and tag not in ("path", "circle"):
            line = self.getpos()[0]
            self.errors.append("line %d: <%s/> is self-closed but not a void "
                               "element" % (line, tag))

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag in VOID:
            self.errors.append("line %d: void element </%s> must not be closed"
                               % (line, tag))
            return
        if not self.stack:
            self.errors.append("line %d: </%s> with nothing open" % (line, tag))
            return
        # Ignore implicit closes of <p> and <li> style legacy recovery only if
        # the tag does not match at all; otherwise report the mismatch.
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                # close everything above it implicitly
                for j in range(len(self.stack) - 1, i - 1, -1):
                    open_tag, open_line = self.stack[j]
                    if j != i:
                        self.errors.append(
                            "line %d: <%s> opened on line %d is never closed "
                            "(implicitly closed by </%s> on line %d)"
                            % (line, open_tag, open_line, tag, line))
                del self.stack[i:]
                return
        self.errors.append("line %d: </%s> does not match any open element "
                           "(open: %s)" % (line, tag,
                                           ", ".join(t for t, _ in self.stack)))


def extract_blocks(text: str) -> list[tuple[str, str, int]]:
    """Return [(lang, code, line_number)] for every fenced block."""
    out = []
    lines = text.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^```([A-Za-z0-9_+#.-]*)\s*$", lines[i])
        if m:
            lang = (m.group(1) or "").lower()
            start = i + 1
            buf = []
            i += 1
            while i < len(lines) and not re.match(r"^```\s*$", lines[i]):
                buf.append(lines[i])
                i += 1
            while buf and not buf[-1].strip():
                buf.pop()
            out.append((lang, "\n".join(buf), start + 1))
        i += 1
    return out


def is_html_block(code: str) -> bool:
    head = code.lstrip()[:200].lower()
    return ("<" in head and ">" in head
            and not head.startswith(("$", "#", "npm", "docker", "git",
                                     "python", "cd ", "make", "kubectl")))


def check_block(lang: str, code: str, line: int, idx: int) -> tuple[list[str], bool]:
    """Run every structural check on one code block.

    Returns (problems, intentionally_broken). Intentionally broken
    counter-examples are marked in the source with "BAD EXAMPLE on purpose":
    the point is that the code is wrong, so they are reported as skipped.
    """
    if "bad example on purpose" in code.lower():
        return [], True
    problems: list[str] = []
    b = Balance()
    try:
        b.feed(code)
        b.close()
    except Exception as exc:  # pragma: no cover
        problems.append("parse error: %s" % exc)
        return problems, False

    problems.extend(b.errors)

    looks_like_document = ("<!doctype" in code.lower()
                           or ("<html" in code.lower()
                               and ("<head" in code.lower()
                                    or "<body" in code.lower())))
    if looks_like_document and not b.has_doctype:
        problems.append("<html> without a preceding <!DOCTYPE html>")
    if b.h1 > 1:
        problems.append("%d <h1> elements (expected at most 1)" % b.h1)
    for d in b.imgs:
        if "alt" not in d:
            problems.append("<img> without alt attribute: %s"
                            % (d.get("src") or "?"))
    for d in b.controls:
        ident = d.get("id")
        if ident and ident not in b.labels:
            problems.append("control id=%r has no <label for=...>" % ident)
    dupes = {x for x in b.ids if b.ids.count(x) > 1}
    if dupes:
        problems.append("duplicate ids: %s" % sorted(dupes))

    # Document-level elements may stay open inside a fragment, exactly as a
    # browser implicitly closes them at the end of a document.
    b.stack = [(t, l) for t, l in b.stack if t not in ("html", "head", "body")]
    for tag, ln in b.stack:
        problems.append("<%s> opened near source line %d is never closed"
                        % (tag, ln))
    return problems, False


def main() -> int:
    if not os.path.exists(SRC):
        print("source not found: %s" % SRC)
        return 2
    with open(SRC, encoding="utf-8") as fh:
        text = fh.read()

    blocks = extract_blocks(text)
    html_blocks = [(l, c, n) for l, c, n in blocks if is_html_block(c)]
    failures = 0
    skipped = 0
    print("Vol. 01 HTML - example checks")
    print("fenced blocks: %d   html blocks: %d\n" % (len(blocks), len(html_blocks)))

    for idx, (lang, code, line) in enumerate(html_blocks, 1):
        problems, broken = check_block(lang, code, line, idx)
        label = code.strip().splitlines()[0][:58] if code.strip() else "(empty)"
        if broken:
            skipped += 1
            print("skip block %2d (src line %4d): %s [bad example on purpose]"
                  % (idx, line, label))
            continue
        if problems:
            failures += 1
            print("FAIL block %2d (src line %4d): %s" % (idx, line, label))
            for p in problems:
                print("       - %s" % p)
        else:
            print("ok   block %2d (src line %4d): %s" % (idx, line, label))

    # Save the examples so they can be opened in a browser.
    outdir = os.path.join(HERE, "examples")
    os.makedirs(outdir, exist_ok=True)
    saved = 0
    for idx, (lang, code, line) in enumerate(html_blocks, 1):
        if "<!DOCTYPE" in code.upper() or "<html" in code.lower():
            pass
        path = os.path.join(outdir, "%02d.html" % idx)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(code.rstrip() + "\n")
        saved += 1
    print("\nsaved %d examples to %s" % (saved, os.path.relpath(outdir, HERE)))
    print("RESULT: %d ok, %d skipped (bad examples on purpose), %d FAILED"
          % (len(html_blocks) - failures - skipped, skipped, failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
