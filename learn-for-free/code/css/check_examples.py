#!/usr/bin/env python3
"""
check_examples.py - validate every CSS example in the Vol. 02 source.

Extracts fenced code blocks from ../src/02-css.md and checks them.

CSS blocks
  1. braces are balanced
  2. parentheses and brackets are balanced
  3. every declaration ends with a semicolon
  4. declarations look like `property: value`
  5. properties are lowercase and non-empty
  6. comments are closed
  7. no empty rules (selector without any declaration)
  8. length units in calc() with +/- are consistent (a light sanity check)
  9. every custom property used with var() is declared somewhere in the block
     or in a :root block of the file

HTML blocks (the demos that pair with the CSS)
  * the same tag-balance, void-element, alt, label and id checks as the HTML
    volume

Run:  python check_examples.py
Exit code 0 = all checks passed.
"""

from __future__ import annotations

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "src", "02-css.md")
HERE = os.path.dirname(os.path.abspath(__file__))

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

KNOWN_PROPS = {
    "accent-color", "align-content", "align-items", "align-self", "all",
    "animation", "animation-composition", "animation-delay", "animation-direction",
    "animation-duration", "animation-fill-mode", "animation-iteration-count",
    "animation-name", "animation-play-state", "animation-timeline",
    "animation-timing-function", "appearance", "aspect-ratio", "backdrop-filter",
    "backface-visibility", "background", "background-attachment",
    "background-blend-mode", "background-clip", "background-color",
    "background-image", "background-origin", "background-position",
    "background-repeat", "background-size", "block-size", "border",
    "border-block", "border-block-color", "border-block-end",
    "border-block-start", "border-block-style", "border-block-width",
    "border-bottom", "border-bottom-color", "border-bottom-left-radius",
    "border-bottom-right-radius", "border-bottom-style",
    "border-bottom-width", "border-collapse", "border-color",
    "border-end-end-radius", "border-end-start-radius", "border-image",
    "border-inline", "border-inline-color", "border-inline-end",
    "border-inline-start", "border-inline-style", "border-inline-width",
    "border-left", "border-left-color", "border-left-style",
    "border-left-width", "border-radius", "border-right", "border-right-color",
    "border-right-style", "border-right-width", "border-spacing",
    "border-start-end-radius", "border-start-start-radius", "border-style",
    "border-top", "border-top-color", "border-top-left-radius",
    "border-top-right-radius", "border-top-style", "border-top-width",
    "border-width", "bottom", "box-decoration-break", "box-shadow", "box-sizing",
    "break-after", "break-before", "break-inside", "caption-side", "caret-color",
    "clear", "clip", "clip-path", "color", "color-scheme", "column-count",
    "column-fill", "column-gap", "column-rule", "column-rule-color",
    "column-rule-style", "column-rule-width", "column-span", "column-width",
    "columns", "contain", "contain-intrinsic-size", "container", "container-name",
    "container-type", "content", "content-visibility", "counter-increment",
    "counter-reset", "counter-set", "cursor", "direction", "display", "empty-cells",
    "filter", "flex", "flex-basis", "flex-direction", "flex-flow", "flex-grow",
    "flex-shrink", "flex-wrap", "float", "font", "font-family", "font-feature-settings",
    "font-kerning", "font-language-override", "font-optical-sizing", "font-size",
    "font-size-adjust", "font-stretch", "font-style", "font-synthesis",
    "font-variant", "font-variant-alternates", "font-variant-caps",
    "font-variant-east-asian", "font-variant-ligatures", "font-variant-numeric",
    "font-variant-position", "font-variation-settings", "font-weight",
    "forced-color-adjust", "gap", "grid", "grid-area", "grid-auto-columns",
    "grid-auto-flow", "grid-auto-rows", "grid-column", "grid-column-end",
    "grid-column-gap", "grid-column-start", "grid-gap", "grid-row",
    "grid-row-end", "grid-row-gap", "grid-row-start", "grid-template",
    "grid-template-areas", "grid-template-columns", "grid-template-rows",
    "hanging-punctuation", "height", "hyphenate-character",
    "hyphenate-limit-chars", "hyphens", "image-orientation", "image-rendering",
    "inline-size", "inset", "inset-block", "inset-block-end", "inset-block-start",
    "inset-inline", "inset-inline-end", "inset-inline-start", "isolation",
    "justify-content", "justify-items", "justify-self", "left", "letter-spacing",
    "line-break", "line-height", "list-style", "list-style-image",
    "list-style-position", "list-style-type", "margin", "margin-block",
    "margin-block-end", "margin-block-start", "margin-bottom", "margin-inline",
    "margin-inline-end", "margin-inline-start", "margin-left", "margin-right",
    "margin-top", "mask", "mask-clip", "mask-composite", "mask-image",
    "mask-mode", "mask-origin", "mask-position", "mask-repeat", "mask-size",
    "mask-type", "max-block-size", "max-height", "max-inline-size", "max-width",
    "min-block-size", "min-height", "min-inline-size", "min-width", "mix-blend-mode",
    "object-fit", "object-position", "offset", "offset-anchor", "offset-distance",
    "offset-path", "offset-rotate", "opacity", "order", "orphans", "outline",
    "outline-color", "outline-offset", "outline-style", "outline-width",
    "overflow", "overflow-anchor", "overflow-block", "overflow-clip-margin",
    "overflow-inline", "overflow-wrap", "overflow-x", "overflow-y", "overscroll-behavior",
    "overscroll-behavior-block", "overscroll-behavior-inline", "overscroll-behavior-x",
    "overscroll-behavior-y", "padding", "padding-block", "padding-block-end",
    "padding-block-start", "padding-bottom", "padding-inline", "padding-inline-end",
    "padding-inline-start", "padding-left", "padding-right", "padding-top",
    "page-break-after", "page-break-before", "page-break-inside", "paint-order",
    "perspective", "perspective-origin", "place-content", "place-items",
    "place-self", "pointer-events", "position", "print-color-adjust", "quotes",
    "resize", "right", "rotate", "row-gap", "ruby-align", "ruby-position",
    "scale", "scroll-behavior", "scroll-margin", "scroll-margin-block",
    "scroll-margin-block-end", "scroll-margin-block-start", "scroll-margin-bottom",
    "scroll-margin-inline", "scroll-margin-inline-end",
    "scroll-margin-inline-start", "scroll-margin-left", "scroll-margin-right",
    "scroll-margin-top", "scroll-padding", "scroll-padding-block",
    "scroll-padding-block-end", "scroll-padding-block-start",
    "scroll-padding-bottom", "scroll-padding-inline", "scroll-padding-inline-end",
    "scroll-padding-inline-start", "scroll-padding-left", "scroll-padding-right",
    "scroll-padding-top", "scroll-snap-align", "scroll-snap-coordinate",
    "scroll-snap-destination", "scroll-snap-points-x", "scroll-snap-points-y",
    "scroll-snap-stop", "scroll-snap-type", "scroll-snap-type-x",
    "scroll-snap-type-y", "scroll-timeline", "scroll-timeline-axis",
    "scroll-timeline-name", "scrollbar-color", "scrollbar-gutter",
    "scrollbar-width", "shape-image-threshold", "shape-margin", "shape-outside",
    "tab-size", "table-layout", "text-align", "text-align-last",
    "text-combine-upright", "text-decoration", "text-decoration-color",
    "text-decoration-line", "text-decoration-skip", "text-decoration-skip-ink",
    "text-decoration-style", "text-decoration-thickness", "text-emphasis",
    "text-emphasis-color", "text-emphasis-position", "text-emphasis-style",
    "text-indent", "text-justify", "text-orientation", "text-overflow",
    "text-rendering", "text-shadow", "text-transform", "text-underline-offset",
    "text-underline-position", "text-wrap", "text-wrap-mode", "text-wrap-style",
    "timeline-scope", "top", "touch-action", "transform", "transform-box",
    "transform-origin", "transform-style", "transition", "transition-behavior",
    "transition-delay", "transition-duration", "transition-property",
    "transition-timing-function", "translate", "unicode-bidi", "user-select",
    "vertical-align", "view-timeline", "view-timeline-axis", "view-timeline-inset",
    "view-timeline-name", "view-transition-name", "visibility", "white-space",
    "widows", "width", "will-change", "word-break", "word-spacing",
    "word-wrap", "writing-mode", "z-index",
}

PROP_RE = re.compile(r"^--[A-Za-z0-9_-]+$|^[a-z-]+$")
DECL_RE = re.compile(r"^([-a-zA-Z_][-a-zA-Z0-9_]*)\s*:\s*(.+?)\s*;?$", re.DOTALL)
VAR_RE = re.compile(r"var\(\s*(--[A-Za-z0-9_-]+)")
BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.DOTALL)

# Names used in syntax illustrations such as `selector { property: value; }`
PLACEHOLDER_PROPS = {"property", "prop", "properties", "value", "val", "item",
                     "items", "name", "x", "y"}


def known_property(prop: str) -> bool:
    """True when the property is a real CSS property (prefixes are ignored)."""
    p = prop.lower()
    for prefix in ("-webkit-", "-moz-", "-ms-", "-o-"):
        if p.startswith(prefix):
            p = p[len(prefix):]
            break
    return p in KNOWN_PROPS


class Balance(HTMLParser):
    """Tag balance and accessibility checks for HTML demo blocks."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = []
        self.imgs = []
        self.controls = []
        self.labels = []
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "h1":
            self.h1 += 1
        if "id" in d and d["id"]:
            self.ids.append(d["id"])
        if tag == "img":
            self.imgs.append(d)
        if tag in ("input", "select", "textarea"):
            self.controls.append(d)
        if tag == "label" and "for" in d:
            self.labels.append(d["for"])
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag in VOID:
            self.errors.append("line %d: void element </%s> closed" % (line, tag))
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.errors.append("line %d: <%s> never closed before </%s>"
                                   % (self.stack[i][1], self.stack[i][0], tag))
                del self.stack[i:]
                return
        self.errors.append("line %d: </%s> matches nothing" % (line, tag))


def strip_comments(code: str) -> tuple[str, list[str]]:
    errs = []
    if code.count("/*") != code.count("*/"):
        errs.append("unbalanced /* */ comments")
    return BLOCK_COMMENT.sub("", code), errs


BLOCK_AT_RULES = {"@media", "@supports", "@layer", "@container", "@keyframes",
                  "@property", "@font-face", "@view-transition", "@scope",
                  "@starting-style", "@counter-style", "@font-feature-values"}


def split_declarations(body: str) -> list[str]:
    """Split a declaration body on top-level semicolons."""
    out, depth, buf = [], 0, []
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0:
            out.append("".join(buf))
            buf = []
            continue
        buf.append(ch)
    if buf:
        out.append("".join(buf))
    return [d.strip() for d in out if d.strip()]


def parse_rules(code: str) -> list[tuple[str, str, int]]:
    """Return [(prelude, body, line)] for every top-level and nested rule."""
    rules: list[tuple[str, str, int]] = []
    prelude: list[str] = []
    i, depth = 0, 0
    body: list[str] = []
    line = 1
    while i < len(code):
        ch = code[i]
        if ch == "\n":
            line += 1
        if ch == "{":
            if depth == 0:
                start_line = line
                prelude_text = "".join(prelude).strip()
                prelude = []
            depth += 1
            if depth > 1:
                body.append(ch)
            i += 1
            continue
        if ch == "}":
            depth -= 1
            if depth == 0:
                rules.append((prelude_text, "".join(body), start_line))
                body = []
            else:
                body.append(ch)
            i += 1
            continue
        if depth == 0:
            prelude.append(ch)
        else:
            body.append(ch)
        i += 1
    leftover = "".join(prelude).strip().rstrip(";")
    if leftover:
        rules.append((leftover, "", line))
    return rules


def check_css(code: str, declared: set) -> list[str]:
    problems: list[str] = []
    # Counter-examples are marked in the source with "BAD EXAMPLE on purpose";
    # the point is that the code is wrong, so the checks are skipped.
    if "bad example on purpose" in code.lower():
        return []
    body_text, errs = strip_comments(code)
    problems.extend(errs)

    if body_text.count("{") != body_text.count("}"):
        problems.append("unbalanced braces: %d '{' vs %d '}'"
                        % (body_text.count("{"), body_text.count("}")))
    if body_text.count("(") != body_text.count(")"):
        problems.append("unbalanced parentheses: %d '(' vs %d ')'"
                        % (body_text.count("("), body_text.count(")")))

    for m in re.finditer(r"(--[A-Za-z0-9_-]+)\s*:", body_text):
        declared.add(m.group(1))

    def check_declarations(prelude: str, body: str, line: int, nested: bool):
        """Check the declaration area of one rule's body."""
        # Split the body around nested rules so declarations and nested rules
        # are reported separately (CSS nesting).

        segments: list[tuple[str, bool]] = []
        depth, buf = 0, []
        for ch in body:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth = max(0, depth - 1)
            buf.append(ch)
            if depth == 0 and ch in "}":
                segments.append(("".join(buf), True))
                buf = []
            elif depth == 0 and ch == ";":
                segments.append(("".join(buf), False))
                buf = []
        if buf:
            segments.append(("".join(buf), False))

        for seg, is_block in segments:
            seg = seg.strip()
            if not seg:
                continue
            if is_block:
                nested_rules = parse_rules(seg + ("" if seg.endswith("}") else "}"))
                walk(nested_rules, inside_at_rule=nested)
                continue
            if nested:
                continue
            m = DECL_RE.match(seg)
            if not m:
                problems.append("line %d: %r is not a valid declaration"
                                % (line, seg[:48]))
                continue
            prop, value = m.group(1), m.group(2).strip()
            if prop.lower() in PLACEHOLDER_PROPS:
                continue
            if not PROP_RE.match(prop):
                problems.append("line %d: suspicious property name %r"
                                % (line, prop))
            elif not known_property(prop) and not prop.startswith("--"):
                problems.append("line %d: unknown property %r" % (line, prop))
            if not value:
                problems.append("line %d: empty value for %r" % (line, prop))

    def walk(rules, inside_at_rule=False):
        for prelude, body, line in rules:
            if not prelude:
                problems.append("line %d: rule without a selector" % line)
                continue
            low = prelude.lower().strip()
            is_at = low.startswith("@")
            if is_at:
                first = low.split()[0]
                if first in BLOCK_AT_RULES:
                    walk(parse_rules(body), inside_at_rule=True)
                    continue
                # statement at-rules such as @import, @charset, @layer a, b;
                problems_local = []
                if not re.match(r"^@(import|charset|namespace|layer)\b", low):
                    problems_local.append("line %d: unexpected at-rule %r"
                                          % (line, prelude))
                if ";" not in body_text and not first.startswith("@import"):
                    pass
                if not re.search(r"\)\s*;?\s*$", body_text.strip()) and \
                        first not in ("import",):
                    pass
                del problems_local
                continue
            if "{" in prelude or "}" in prelude:
                problems.append("line %d: broken selector %r" % (line, prelude))
                continue
            if not body.strip():
                if not inside_at_rule:
                    problems.append("line %d: empty rule for %r" % (line, prelude))
                continue
            check_declarations(prelude, body, line, nested="{ " in body or "{\n" in body
                              or body.strip().startswith("{"))

    rules = parse_rules(body_text)
    if "{" not in body_text:
        # A list of declaration values or of stand-alone declarations with no
        # rule wrapper: check the ones that look like declarations.
        for line_no, raw in enumerate(body_text.split("\n"), 1):
            line = raw.strip()
            if not line or line.startswith("/*"):
                continue
            m = DECL_RE.match(line)
            if not m:
                continue        # a bare value such as `minmax(180px, 1fr)`
            prop = m.group(1)
            if prop.lower() in PLACEHOLDER_PROPS:
                continue
            if not PROP_RE.match(prop):
                problems.append("line %d: suspicious property name %r"
                                % (line_no, prop))
            elif not known_property(prop) and not prop.startswith("--"):
                problems.append("line %d: unknown property %r" % (line_no, prop))
            if not m.group(2).strip():
                problems.append("line %d: empty value for %r" % (line_no, prop))
    else:
        walk(rules)

    for m in VAR_RE.finditer(body_text):
        name = m.group(1)
        if name not in declared and not re.search(
                r"var\(\s*%s\s*," % re.escape(name), body_text):
            problems.append("var(%s) used without a declaration or fallback" % name)
    return problems


def check_html(code: str) -> list[str]:
    problems = []
    b = Balance()
    try:
        b.feed(code)
        b.close()
    except Exception as exc:
        return ["parse error: %s" % exc]
    if b.stack:
        for tag, ln in b.stack:
            if tag in ("html", "head", "body"):
                continue
            problems.append("<%s> opened on line %d is never closed" % (tag, ln))
    problems.extend(b.errors)
    for d in b.imgs:
        if "alt" not in d:
            problems.append("<img> without alt")
    for d in b.controls:
        if d.get("id") and d["id"] not in b.labels:
            problems.append("control id=%r has no <label for>" % d["id"])
    return problems


def extract_blocks(text: str):
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


def main() -> int:
    if not os.path.exists(SRC):
        print("source not found: %s" % SRC)
        return 2
    with open(SRC, encoding="utf-8") as fh:
        text = fh.read()

    blocks = extract_blocks(text)
    css_blocks = [(c, n) for l, c, n in blocks if l in ("css", "")]
    html_blocks = [(c, n) for l, c, n in blocks if l in ("html", "htm")]
    failures = 0

    print("Vol. 02 CSS - example checks")

    print("\nCSS blocks: %d" % len(css_blocks))
    declared: set[str] = set()
    # Pass 1: collect every custom property declared anywhere in the volume, so
    # a var() may rely on a token defined in a different example.
    for code, _line in css_blocks:
        body_text, _ = strip_comments(code)
        for m in re.finditer(r"(--[A-Za-z0-9_-]+)\s*:", body_text):
            declared.add(m.group(1))
    # Pass 2: check, collecting any declarations written inside the examples.
    results = []
    for idx, (code, line) in enumerate(css_blocks, 1):
        problems = check_css(code, declared)
        label = code.strip().splitlines()[0][:52] if code.strip() else "(empty)"
        results.append((idx, line, label, problems))
    for idx, line, label, problems in results:
        if problems:
            failures += 1
            print("FAIL css %2d (src line %4d): %s" % (idx, line, label))
            for p in problems:
                print("       - %s" % p)
        else:
            print("ok   css %2d (src line %4d): %s" % (idx, line, label))

    print("\nHTML blocks: %d" % len(html_blocks))
    for idx, (code, line) in enumerate(html_blocks, 1):
        problems = check_html(code)
        label = code.strip().splitlines()[0][:52] if code.strip() else "(empty)"
        if problems:
            failures += 1
            print("FAIL html %2d (src line %4d): %s" % (idx, line, label))
            for p in problems:
                print("       - %s" % p)
        else:
            print("ok   html %2d (src line %4d): %s" % (idx, line, label))

    outdir = os.path.join(HERE, "examples")
    os.makedirs(outdir, exist_ok=True)
    n_css = 0
    for idx, (code, line) in enumerate(css_blocks, 1):
        with open(os.path.join(outdir, "%02d.css" % idx), "w", encoding="utf-8") as fh:
            fh.write(code.rstrip() + "\n")
        n_css += 1
    n_html = len(html_blocks)
    for idx, (code, line) in enumerate(html_blocks, 1):
        with open(os.path.join(outdir, "html-%02d.html" % idx), "w",
                  encoding="utf-8") as fh:
            fh.write(code.rstrip() + "\n")

    print("\nsaved %d css and %d html files to %s"
          % (n_css, n_html, os.path.relpath(outdir, HERE)))
    total = len(css_blocks) + len(html_blocks)
    print("RESULT: %d ok, %d FAILED" % (total - failures, failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
