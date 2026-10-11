#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py - Learn for Free PDF pipeline.

Converts the Markdown volumes in ./src into A4 PDFs in ./pdf using ReportLab
(an equivalent, dependency-free alternative to Pandoc+LaTeX).

Features
--------
* Cover page generated from YAML-ish front matter
* Clickable table of contents + PDF outline/bookmarks
* Running header (volume title) and footer (page numbers)
* Syntax-highlighted code blocks (Pygments) with language label and line numbers
* Styled tables, blockquote callouts, task lists, horizontal rules
* Escaping of Markdown inline formatting (bold, italic, inline code, links)

Usage
-----
    python build.py 01-html              # build one volume
    python build.py 01-html --out x.pdf  # custom output
    python build.py --all                # build every volume in src/
    python build.py --new 42-foo         # scaffold a new volume from the template

Markdown source conventions (see assets/VOLUME_TEMPLATE.md)
-----------------------------------------------------------
    ---
    title: Vol. 01 - HTML
    technology: HTML
    source: html.com
    date: 2026-10-10
    level: Beginner
    hours: 25
    ---

    # Chapter 1 - Title        -> TOC level 0 + bookmark
    ## Section 1.1             -> TOC level 1 + bookmark
    ### Subsection             -> TOC level 2 (no TOC line, bookmark only)
    ```lang ... ```            -> highlighted code
    | a | b |                  -> table
    > text                     -> callout box
"""

from __future__ import annotations

import argparse
import html as _html
import os
import re
import sys
from datetime import date

# --------------------------------------------------------------------------- #
# Optional heavy imports (kept late so --new / --help stay fast)
# --------------------------------------------------------------------------- #

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT, "src")
PDF_DIR = os.path.join(ROOT, "pdf")
ASSETS_DIR = os.path.join(ROOT, "assets")

# Page geometry (kept in sync with make_doc margins)
PAGE_MARGIN = 20  # mm
CONTENT_W = None  # set lazily in make_table/first use


def content_width() -> float:
    """Usable content width in points (A4 minus both margins)."""
    global CONTENT_W
    if CONTENT_W is None:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        CONTENT_W = A4[0] - 2 * PAGE_MARGIN * mm
    return CONTENT_W

# --------------------------------------------------------------------------- #
# Fonts
# --------------------------------------------------------------------------- #

FONT_CANDIDATES = {
    "body": [
        ("DejaVuSans", "C:/Windows/Fonts/DejaVuSans.ttf"),
        ("DejaVuSans-Bold", "C:/Windows/Fonts/DejaVuSans-Bold.ttf"),
        ("DejaVuSans-Oblique", "C:/Windows/Fonts/DejaVuSans-Oblique.ttf"),
        ("DejaVuSans-BoldOblique", "C:/Windows/Fonts/DejaVuSans-BoldOblique.ttf"),
    ],
    "mono": [
        ("DejaVuSansMono", "C:/Windows/Fonts/DejaVuSansMono.ttf"),
        ("DejaVuSansMono-Bold", "C:/Windows/Fonts/DejaVuSansMono-Bold.ttf"),
        ("DejaVuSansMono-Oblique", "C:/Windows/Fonts/DejaVuSansMono-Oblique.ttf"),
        ("Consolas", "C:/Windows/Fonts/consola.ttf"),
    ],
}


def register_fonts() -> tuple[str, str, str, str, str]:
    """Register TTF fonts, falling back to the built-in Helvetica family."""
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    body, body_bold, body_italic, body_bold_italic = (
        "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique")
    for name, path in FONT_CANDIDATES["body"]:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
            except Exception:
                continue
    reg = {f for f in pdfmetrics.getRegisteredFontNames()}
    if "DejaVuSans" in reg:
        body, body_bold = "DejaVuSans", "DejaVuSans-Bold"
        body_italic = "DejaVuSans-Oblique" if "DejaVuSans-Oblique" in reg else body
        body_bold_italic = ("DejaVuSans-BoldOblique"
                            if "DejaVuSans-BoldOblique" in reg else body_bold)

    mono, mono_bold, mono_italic = "Courier", "Courier-Bold", "Courier-Oblique"
    for name, path in FONT_CANDIDATES["mono"]:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
            except Exception:
                continue
    if "DejaVuSansMono" in reg or "DejaVuSansMono" in pdfmetrics.getRegisteredFontNames():
        mono = "DejaVuSansMono"
        mono_bold = ("DejaVuSansMono-Bold"
                     if "DejaVuSansMono-Bold" in pdfmetrics.getRegisteredFontNames() else mono)
        mono_italic = ("DejaVuSansMono-Oblique"
                       if "DejaVuSansMono-Oblique" in pdfmetrics.getRegisteredFontNames() else mono)
    return body, body_bold, body_italic, body_bold_italic, mono


# --------------------------------------------------------------------------- #
# Colour palette (GitHub-light inspired)
# --------------------------------------------------------------------------- #

C = {
    "ink": "#1f2328",
    "muted": "#57606a",
    "faint": "#8c959f",
    "accent": "#0969da",
    "accent_soft": "#ddf4ff",
    "rule": "#d8dee4",
    "code_bg": "#f6f8fa",
    "quote_bg": "#fff8c5",
    "quote_bar": "#d4a72c",
    "tip_bg": "#dafbe1",
    "tip_bar": "#1a7f37",
    "thead": "#f6f8fa",
    "zebra": "#fbfcfd",
}

TOKEN_COLORS = {
    "comment": "#6e7781",
    "keyword": "#cf222e",
    "keyword_const": "#0550ae",
    "string": "#0a3069",
    "number": "#0550ae",
    "func": "#8250df",
    "cls": "#953800",
    "builtin": "#0550ae",
    "op": "#cf222e",
    "tag": "#116329",
    "punct": "#24292f",
    "deleted": "#82071e",
    "inserted": "#116329",
    "generic": "#24292f",
}

# Languages we highlight (aliases handled by Pygments)
LANG_LABELS = {
    "": "code", "text": "output", "txt": "output", "console": "shell",
    "bash": "shell", "sh": "shell", "shell": "shell", "zsh": "shell",
    "html": "HTML", "css": "CSS", "js": "JavaScript", "javascript": "JavaScript",
    "ts": "TypeScript", "typescript": "TypeScript", "jsx": "JSX", "tsx": "TSX",
    "py": "Python", "python": "Python", "java": "Java", "c": "C", "cpp": "C++",
    "cs": "C#", "csharp": "C#", "go": "Go", "rust": "Rust", "rs": "Rust",
    "php": "PHP", "rb": "Ruby", "ruby": "Ruby", "sql": "SQL", "json": "JSON",
    "yaml": "YAML", "yml": "YAML", "toml": "TOML", "xml": "XML", "md": "Markdown",
    "dockerfile": "Dockerfile", "diff": "diff", "http": "HTTP", "vue": "Vue",
    "svelte": "Svelte", "swift": "Swift", "kt": "Kotlin", "kotlin": "Kotlin",
    "dart": "Dart", "lua": "Lua", "r": "R", "perl": "Perl", "scala": "Scala",
    "haskell": "Haskell", "elixir": "Elixir", "erlang": "Erlang", "sol": "Solidity",
    "solidity": "Solidity", "graphql": "GraphQL", "ini": "INI", "env": "shell",
    "makefile": "Makefile", "nginx": "Nginx", "apache": "Apache",
    "powershell": "PowerShell", "ps1": "PowerShell", "cmd": "Shell",
    "plain": "code", "output": "output", "none": "code",
}

LANG_ALIASES = {
    "js": "javascript", "javascript": "javascript", "jsref": "javascript",
    "ts": "typescript", "typescript": "typescript", "jsx": "jsx", "tsx": "tsx",
    "py": "python", "python": "python", "rs": "rust", "kt": "kotlin",
    "yml": "yaml", "sh": "bash", "zsh": "bash", "console": "bash",
    "shell": "bash", "env": "bash", "cmd": "bash", "ps1": "powershell",
    "cs": "csharp", "cpp": "cpp", "c++": "cpp", "sol": "solidity",
    "txt": "text", "plain": "text", "output": "text", "none": "text",
    "": "text", "json": "json", "yaml": "yaml", "bash": "bash", "sql": "sql",
    "html": "html", "css": "css", "java": "java", "c": "c", "go": "go",
    "rust": "rust", "php": "php", "ruby": "ruby", "diff": "diff",
    "http": "http", "vue": "vue", "svelte": "svelte", "swift": "swift",
    "kotlin": "kotlin", "dart": "dart", "lua": "lua", "r": "r",
    "perl": "perl", "scala": "scala", "haskell": "haskell",
    "elixir": "elixir", "erlang": "erlang", "solidity": "solidity",
    "graphql": "graphql", "ini": "ini", "makefile": "makefile",
    "nginx": "nginx", "apache": "apache", "powershell": "powershell",
    "dockerfile": "dockerfile", "md": "markdown", "toml": "toml", "xml": "xml",
    "text": "text", "mjs": "javascript", "cjs": "javascript", "mts": "typescript",
}


# --------------------------------------------------------------------------- #
# Markdown block parser
# --------------------------------------------------------------------------- #

def _append_continuation(items, line):
    """Attach a wrapped continuation line to the last list item."""
    kind, flag, txt = items[-1][1]
    items[-1] = (items[-1][0], (kind, flag, (txt + " " + line.strip()).strip()))
    return items


FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FENCE_RE = re.compile(r"^\s*```([A-Za-z0-9_+#.-]*)\s*$")
HEADING_RE = re.compile(r"^(#{1,4})\s+(.*?)\s*$")
UL_RE = re.compile(r"^(\s*)[-*+]\s+(.*)$")
OL_RE = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
TASK_RE = re.compile(r"^\[([ xX])\]\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$")
HR_RE = re.compile(r"^\s*([-*_])\s*(\1\s*){2,}$")
BLOCKQUOTE_RE = re.compile(r"^\s*>\s?(.*)$")
ADMONITION_RE = re.compile(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.I)


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip().lower()] = v.strip().strip('"').strip("'")
    return meta, text[m.end():]


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


class Block:
    """A parsed markdown block."""
    __slots__ = ("kind", "text", "extra")

    def __init__(self, kind: str, text: str = "", extra=None):
        self.kind = kind
        self.text = text
        self.extra = extra or {}

    def __repr__(self):  # pragma: no cover - debugging helper
        return f"<{self.kind} {self.text[:40]!r}>"


def parse_blocks(md: str) -> list[Block]:
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    blocks: list[Block] = []
    i, n = 0, len(lines)
    para_buf: list[str] = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            blocks.append(Block("para", " ".join(x.strip() for x in para_buf).strip()))
            para_buf = []

    while i < n:
        line = lines[i]

        if not line.strip():
            flush_para()
            i += 1
            continue

        # fenced code
        m = FENCE_RE.match(line)
        if m:
            flush_para()
            lang = (m.group(1) or "").lower()
            buf = []
            i += 1
            while i < n and not FENCE_RE.match(lines[i]):
                buf.append(lines[i])
                i += 1
            i += 1  # closing fence
            while buf and not buf[-1].strip():
                buf.pop()
            blocks.append(Block("code", "\n".join(buf), {"lang": lang}))
            continue

        # heading
        m = HEADING_RE.match(line)
        if m:
            flush_para()
            level = len(m.group(1))
            txt = m.group(2).strip()
            if level == 1:
                blocks.append(Block("h1", txt))
            elif level == 2:
                blocks.append(Block("h2", txt))
            elif level == 3:
                blocks.append(Block("h3", txt))
            else:
                blocks.append(Block("h4", txt))
            i += 1
            continue

        # horizontal rule (must be checked before lists since --- / *** look similar)
        if HR_RE.match(line) and len(line.strip()) >= 3 and not TABLE_SEP_RE.match(line):
            flush_para()
            blocks.append(Block("hr"))
            i += 1
            continue

        # table (header + separator)
        if i + 1 < n and "|" in line and TABLE_SEP_RE.match(lines[i + 1]):
            flush_para()
            rows = [split_row(line)]
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            blocks.append(Block("table", "", {"rows": rows}))
            continue

        # blockquote / admonition
        if BLOCKQUOTE_RE.match(line):
            flush_para()
            qbuf = []
            admon = None
            while i < n:
                mm = BLOCKQUOTE_RE.match(lines[i])
                if not mm:
                    if lines[i].strip() and qbuf:
                        qbuf.append(lines[i].strip())
                        i += 1
                        continue
                    break
                body = mm.group(1).strip()
                am = ADMONITION_RE.match(body)
                if am and not qbuf:
                    admon = am.group(1).upper()
                else:
                    qbuf.append(body)
                i += 1
            blocks.append(Block("quote", "\n".join(qbuf).strip(), {"admon": admon}))
            continue

        # unordered list
        if UL_RE.match(line):
            flush_para()
            items = []
            while i < n:
                mm = UL_RE.match(lines[i])
                if not mm:
                    if items and lines[i].startswith(("  ", "\t")):
                        _append_continuation(items, lines[i])
                        i += 1
                        continue
                    break
                indent = len(mm.group(1).expandtabs(4))
                task = TASK_RE.match(mm.group(2))
                if task:
                    items.append((indent, ("task", task.group(1).lower() == "x", task.group(2))))
                else:
                    items.append((indent, ("item", None, mm.group(2))))
                i += 1
            blocks.append(Block("ul", "", {"items": items}))
            continue

        # ordered list
        if OL_RE.match(line):
            flush_para()
            items = []
            start = None
            while i < n:
                mm = OL_RE.match(lines[i])
                if not mm:
                    if items and lines[i].startswith(("  ", "\t")):
                        _append_continuation(items, lines[i])
                        i += 1
                        continue
                    break
                if start is None:
                    start = int(mm.group(2))
                task = TASK_RE.match(mm.group(3))
                if task:
                    items.append((len(mm.group(1)), ("task", task.group(1).lower() == "x", task.group(2))))
                else:
                    items.append((len(mm.group(1)), ("item", None, mm.group(3))))
                i += 1
            blocks.append(Block("ol", "", {"items": items, "start": start or 1}))
            continue

        # plain paragraph
        para_buf.append(line)
        i += 1

    flush_para()
    return blocks


# --------------------------------------------------------------------------- #
# Inline markdown -> Paragraph XML
# --------------------------------------------------------------------------- #

INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*|__([^_]+)__")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)|(?<!_)_([^_\n]+)_(?!_)")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def inline(text: str) -> str:
    """Convert inline markdown to ReportLab paragraph XML.

    Handles inline code, **bold**, *italic*, [links](url) and escapes the rest.
    Callers replace the MONO_FONT placeholder with the monospace font name.
    """
    out = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "`":
            j = text.find("`", i + 1)
            if j == -1:
                out.append(_html.escape(ch))
                i += 1
                continue
            code = text[i + 1:j]
            out.append('<font face="MONO_FONT" size="8.6" color="#%s">%s</font>'
                       % (C["muted"].lstrip("#"), _html.escape(code)))
            i = j + 1
            continue
        if text[i:i + 2] == "**":
            j = text.find("**", i + 2)
            if j != -1:
                out.append("<b>%s</b>" % _esc(text[i + 2:j]))
                i = j + 2
                continue
        if ch == "*" and not text[i + 1:i + 2].isspace():
            j = text.find("*", i + 1)
            if j != -1 and "\n" not in text[i + 1:j]:
                out.append("<i>%s</i>" % _esc(text[i + 1:j]))
                i = j + 1
                continue
        if ch == "[":
            m = LINK_RE.match(text, i)
            if m:
                label, url = m.group(1), m.group(2)
                out.append('<link href="%s" color="#%s"><u>%s</u></link>'
                           % (_html.escape(url, quote=True),
                              C["accent"].lstrip("#"), _esc(label)))
                i = m.end()
                continue
        out.append(_html.escape(ch))
        i += 1
    return "".join(out)


def _esc(text: str) -> str:
    """Escape a span that will be wrapped in a tag (no further recursion)."""
    return _html.escape(text)


# --------------------------------------------------------------------------- #
# Syntax highlighting
# --------------------------------------------------------------------------- #

def _token_color(tok) -> str:
    from pygments import token as T
    if tok in T.Comment or tok in T.Comment.Preproc:
        return TOKEN_COLORS["comment"]
    if tok in T.Keyword:
        if tok in T.Keyword.Constant:
            return TOKEN_COLORS["keyword_const"]
        return TOKEN_COLORS["keyword"]
    if tok in T.String or tok in T.String.Escape:
        return TOKEN_COLORS["string"]
    if tok in T.Number:
        return TOKEN_COLORS["number"]
    if tok in T.Operator or tok in T.Operator.Word:
        return TOKEN_COLORS["op"]
    if tok in T.Name.Function or tok in T.Name.Function.Magic:
        return TOKEN_COLORS["func"]
    if tok in T.Name.Class:
        return TOKEN_COLORS["cls"]
    if tok in T.Name.Builtin or tok in T.Name.Builtin.Pseudo:
        return TOKEN_COLORS["builtin"]
    if tok in T.Name.Tag or tok in T.Name.Attribute:
        return TOKEN_COLORS["tag"]
    if tok in T.Name.Variable or tok in T.Name.Constant:
        return TOKEN_COLORS["tag"]
    if tok in T.Generic.Deleted:
        return TOKEN_COLORS["deleted"]
    if tok in T.Generic.Inserted:
        return TOKEN_COLORS["inserted"]
    return TOKEN_COLORS["punct"]


def highlight(code: str, lang: str) -> list[str]:
    """Return a list of marked-up lines (XML for XPreformatted)."""
    try:
        from pygments import lex
        from pygments.lexers import get_lexer_by_name
        from pygments.util import ClassNotFound
        alias = LANG_ALIASES.get(lang, lang)
        if alias in ("text", ""):
            lexer = None
        else:
            try:
                lexer = get_lexer_by_name(alias, stripnl=False, ensurenl=False)
            except ClassNotFound:
                lexer = None
    except Exception:
        lexer = None

    if lexer is None:
        return [_html.escape(ln) for ln in code.split("\n")]

    from pygments import lex as _lex
    lines: list[list[str]] = [[]]
    for tok, val in _lex(code, lexer):
        color = _token_color(tok)
        parts = val.split("\n")
        for k, part in enumerate(parts):
            if k:
                lines.append([])
            if not part:
                continue
            esc = _html.escape(part)
            if color == TOKEN_COLORS["punct"]:
                lines[-1].append(esc)
            else:
                lines[-1].append('<font color="%s">%s</font>' % (color, esc))
    return ["".join(x) if x else " " for x in lines]


# --------------------------------------------------------------------------- #
# Document template
# --------------------------------------------------------------------------- #

def build_styles(fonts):
    body, body_b, body_i, body_bi, mono = fonts
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER

    ss = {}
    ss["body"] = ParagraphStyle("body", fontName=body, fontSize=10.2, leading=14.4,
                                textColor=C["ink"], alignment=TA_LEFT, spaceAfter=6)
    ss["lead"] = ParagraphStyle("lead", parent=ss["body"], fontSize=10.8, leading=15.6,
                                textColor=C["muted"], spaceAfter=10)
    ss["h1"] = ParagraphStyle("h1", fontName=body_b, fontSize=20, leading=24,
                              textColor=C["ink"], spaceBefore=6, spaceAfter=14)
    ss["h2"] = ParagraphStyle("h2", fontName=body_b, fontSize=14.5, leading=19,
                              textColor=C["ink"], spaceBefore=14, spaceAfter=7)
    ss["h3"] = ParagraphStyle("h3", fontName=body_b, fontSize=11.6, leading=15,
                              textColor=C["muted"], spaceBefore=10, spaceAfter=5)
    ss["h4"] = ParagraphStyle("h4", fontName=body_b, fontSize=10.4, leading=14,
                              textColor=C["muted"], spaceBefore=8, spaceAfter=4)
    ss["bullet"] = ParagraphStyle("bullet", parent=ss["body"], leftIndent=14,
                                  bulletIndent=3, spaceAfter=3)
    ss["numbered"] = ParagraphStyle("numbered", parent=ss["body"], leftIndent=19,
                                    bulletIndent=3, spaceAfter=3)
    ss["td"] = ParagraphStyle("td", parent=ss["body"], fontSize=9.2, leading=12.4,
                              spaceAfter=0)
    ss["th"] = ParagraphStyle("th", parent=ss["td"], fontName=body_b)
    ss["quote"] = ParagraphStyle("quote", parent=ss["body"], fontSize=9.8,
                                 leading=13.6, spaceAfter=0)
    ss["code"] = ParagraphStyle("code", fontName=mono, fontSize=8.1, leading=10.6,
                                textColor=C["ink"], spaceAfter=0)
    ss["code_label"] = ParagraphStyle("code_label", fontName=body_b, fontSize=7.6,
                                      leading=9.6, textColor=C["muted"], spaceAfter=2)
    ss["toc0"] = ParagraphStyle("toc0", fontName=body_b, fontSize=10.4, leading=15.5,
                                textColor=C["ink"])
    ss["toc1"] = ParagraphStyle("toc1", fontName=body, fontSize=9.6, leading=13.6,
                                textColor=C["muted"], leftIndent=14)
    ss["toc2"] = ParagraphStyle("toc2", fontName=body, fontSize=9.2, leading=13,
                                textColor=C["faint"], leftIndent=28)
    ss["cover_title"] = ParagraphStyle("cover_title", fontName=body_b, fontSize=31,
                                       leading=37, textColor=C["ink"])
    ss["cover_sub"] = ParagraphStyle("cover_sub", fontName=body, fontSize=13.5,
                                     leading=19, textColor=C["muted"])
    ss["cover_meta"] = ParagraphStyle("cover_meta", fontName=body, fontSize=10,
                                      leading=15, textColor=C["muted"])
    ss["footer"] = ParagraphStyle("footer", fontName=body, fontSize=8,
                                  textColor=C["faint"])
    return ss


class VolumeDoc:
    """Holds everything the renderer needs for one volume."""

    def __init__(self, meta: dict, blocks: list[Block], fonts):
        from reportlab.lib.styles import ParagraphStyle
        self.meta = meta
        self.blocks = blocks
        self.fonts = fonts
        self.S = build_styles(fonts)
        body, body_b, body_i, body_bi, mono = fonts
        self.body, self.mono = body, mono

        self.vol_no = meta.get("vol", "").strip()
        self.technology = meta.get("technology", meta.get("title", "Volume"))
        self.title = meta.get("title", f"Vol. {self.vol_no} - {self.technology}")
        self.source = meta.get("source", "")
        self.date = meta.get("date") or date.today().isoformat()
        self.level = meta.get("level", "Beginner to intermediate")
        self.hours = meta.get("hours", "")
        self.subtitle = meta.get("subtitle", "Original study notes, examples and tests")
        self.brand = "Learn for Free"


# --------------------------------------------------------------------------- #
# Flowable builders
# --------------------------------------------------------------------------- #

def hr() -> "object":
    from reportlab.platypus import HRFlowable
    from reportlab.lib import colors
    return HRFlowable(width="100%", thickness=0.7, color=colors.HexColor(C["rule"]),
                      spaceBefore=10, spaceAfter=10)


def make_table(rows, styles, fonts, avail=None):
    """Build a styled table. `avail` is the content width in points."""
    from reportlab.platypus import Table, TableStyle, Paragraph
    from reportlab.lib import colors
    avail = avail or content_width()
    ncols = max(len(r) for r in rows)
    norm = [r + [""] * (ncols - len(r)) for r in rows]
    data = []
    for ri, row in enumerate(norm):
        st = styles["th"] if ri == 0 else styles["td"]
        data.append([Paragraph(inline(c).replace("MONO_FONT", fonts[4]), st) for c in row])

    # Column widths: heuristic from the longest cell in each column, clamped so
    # no column collapses or hogs the page.
    weights = []
    for ci in range(ncols):
        longest = max((len(norm[ri][ci]) for ri in range(len(norm))), default=1)
        weights.append(max(6, min(longest, 60)))
    total = sum(weights) or 1
    col_w = [avail * (0.86 * w / total + 0.14 / ncols) for w in weights]

    t = Table(data, colWidths=col_w, repeatRows=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(C["thead"])),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor(C["rule"])),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, colors.HexColor(C["rule"])),
        ("LINEABOVE", (0, 0), (-1, 0), 0.8, colors.HexColor(C["rule"])),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    for r in range(1, len(norm)):
        if r % 2 == 0:
            cmds.append(("BACKGROUND", (0, r), (-1, r), colors.HexColor(C["zebra"])))
    t.setStyle(TableStyle(cmds))
    return t


def make_quote(text, styles, fonts, admon=None):
    from reportlab.platypus import Table, TableStyle, Paragraph
    from reportlab.lib import colors
    if admon in ("TIP", "IMPORTANT"):
        bg, bar = C["tip_bg"], C["tip_bar"]
    elif admon in ("WARNING", "CAUTION"):
        bg, bar = "#ffebe9", "#cf222e"
    else:
        bg, bar = C["quote_bg"], C["quote_bar"]
    label = {"NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important",
             "WARNING": "Warning", "CAUTION": "Caution"}.get(admon)
    if label:
        from reportlab.platypus import Paragraph as P
        text = f"<b>{label}.</b> " + text
    para = Paragraph(inline(text).replace("MONO_FONT", fonts[4]), styles["quote"])
    t = Table([[para]], colWidths=["100%"], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, colors.HexColor(bar)),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def make_code(code, lang, styles, fonts, first_line_no=1):
    from reportlab.platypus import Table, TableStyle, XPreformatted, Paragraph
    from reportlab.lib import colors
    mono = fonts[4]
    lines = highlight(code, lang)
    label = LANG_LABELS.get(lang, lang.upper() if lang else "code")
    numbered = []
    for idx, ln in enumerate(lines, start=first_line_no):
        numbered.append('<font color="#%s">%4d</font>  %s'
                        % (C["faint"].lstrip("#"), idx, ln))
    # A block taller than the A4 body frame (683 pt at 10.6 leading, minus the
    # label and padding) cannot be laid out as one table, so split it into
    # page-sized chunks that keep the line numbering continuous.
    chunk = 56
    tables = []
    for start in range(0, len(numbered), chunk):
        piece = numbered[start:start + chunk]
        if start == 0 and label and label != "code":
            head = Paragraph(label, styles["code_label"])
        elif start > 0:
            head = Paragraph("%s (continued)" % (label or "code"),
                             styles["code_label"])
        else:
            head = None
        pre = XPreformatted("\n".join(piece), styles["code"])
        t = Table([[pre]], colWidths=["100%"], hAlign="LEFT")
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(C["code_bg"])),
            ("LINEBEFORE", (0, 0), (0, -1), 2.0, colors.HexColor(C["accent"])),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]))
        tables.extend([head, t] if head is not None else [t])
    return tables


def build_list_flow(items, styles, fonts, ordered, start):
    from reportlab.platypus import Paragraph
    from reportlab.lib.styles import ParagraphStyle
    mono = fonts[4]
    flows = []
    counter = start
    for indent, payload in items:
        kind, flag, text = payload
        depth = indent // 2 if indent < 8 else (1 if indent < 16 else 2)
        st = ParagraphStyle("li%d" % depth, parent=styles["bullet"],
                            leftIndent=14 + depth * 16, bulletIndent=2 + depth * 16,
                            spaceAfter=3.5)
        if kind == "task":
            glyph = "[x]" if flag else "[ ]"
            p = Paragraph('<font face="%s" size="8.6" color="#%s">%s</font>&nbsp;&nbsp;%s'
                          % (mono, C["muted"].lstrip("#"), glyph,
                             inline(text).replace("MONO_FONT", mono)), st)
        elif ordered:
            p = Paragraph(inline(text).replace("MONO_FONT", mono), st)
            p.bulletText = "%d." % counter
            counter += 1
        else:
            p = Paragraph(inline(text).replace("MONO_FONT", mono), st)
            p.bulletText = "\u2022"
        flows.append(p)
    return flows


# --------------------------------------------------------------------------- #
# Page templates
# --------------------------------------------------------------------------- #

def make_doc(path, doc: VolumeDoc):
    from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, NextPageTemplate
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors

    M = 20 * mm
    PAGE_W, PAGE_H = A4
    frame = Frame(M, M + 8 * mm, PAGE_W - 2 * M, PAGE_H - 2 * M - 16 * mm,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="body")

    class Doc(BaseDocTemplate):
        def afterFlowable(self, flowable):
            key = getattr(flowable, "_toc_key", None)
            if key is None:
                return
            level = flowable._toc_level
            text = flowable._toc_text
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level, closed=(level > 0))
            self.notify("TOCEntry", (level, text, self.page, key))

    d = Doc(path, pagesize=A4, leftMargin=M, rightMargin=M,
            topMargin=M + 8 * mm, bottomMargin=M + 8 * mm,
            title=doc.title, author=doc.brand, subject=doc.source,
            creator="learn-for-free build.py")
    d.vol = doc

    def cover_page(canv, _d):
        canv.saveState()
        canv.setFillColor(colors.HexColor(C["accent"]))
        canv.rect(0, PAGE_H - 14 * mm, PAGE_W, 14 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.white)
        canv.setFont(doc.fonts[1], 10)
        canv.drawString(M, PAGE_H - 9.2 * mm, doc.brand.upper())
        canv.setFont(doc.fonts[0], 9)
        canv.drawRightString(PAGE_W - M, PAGE_H - 9.2 * mm, doc.date)
        canv.setStrokeColor(colors.HexColor(C["rule"]))
        canv.setLineWidth(0.7)
        canv.line(M, M + 10 * mm, PAGE_W - M, M + 10 * mm)
        canv.setFillColor(colors.HexColor(C["faint"]))
        canv.setFont(doc.fonts[0], 8.4)
        canv.drawCentredString(PAGE_W / 2, M + 5 * mm,
                               "Personal study material - original notes, not affiliated with the source site")
        canv.restoreState()

    def normal_page(canv, _d):
        canv.saveState()
        canv.setFont(doc.fonts[0], 8.4)
        canv.setFillColor(colors.HexColor(C["faint"]))
        canv.drawString(M, PAGE_H - M + 2 * mm, doc.title)
        canv.setStrokeColor(colors.HexColor(C["rule"]))
        canv.setLineWidth(0.6)
        canv.line(M, PAGE_H - M - 0.5 * mm, PAGE_W - M, PAGE_H - M - 0.5 * mm)
        canv.line(M, M - 1 * mm, PAGE_W - M, M - 1 * mm)
        canv.setFont(doc.fonts[0], 8.4)
        canv.drawRightString(PAGE_W - M, M - 6 * mm, "%d" % canv.getPageNumber())
        canv.drawString(M, M - 6 * mm, doc.brand)
        canv.restoreState()

    d.addPageTemplates([
        PageTemplate(id="cover", frames=[frame], onPage=cover_page),
        PageTemplate(id="normal", frames=[frame], onPage=normal_page),
    ])
    return d


# --------------------------------------------------------------------------- #
# Cover + TOC flowables
# --------------------------------------------------------------------------- #

def cover_flowables(doc: VolumeDoc):
    from reportlab.platypus import (Spacer, Paragraph, PageBreak, NextPageTemplate,
                                    Table, TableStyle, KeepTogether)
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    S = doc.S
    fl = []
    fl.append(Spacer(1, 26 * mm))
    if doc.vol_no:
        fl.append(Paragraph('<font color="#%s">VOL. %s</font>'
                            % (C["accent"].lstrip("#"), doc.vol_no), S["cover_sub"]))
        fl.append(Spacer(1, 3 * mm))
    fl.append(Paragraph(_html.escape(doc.technology), S["cover_title"]))
    fl.append(Spacer(1, 4 * mm))
    fl.append(Paragraph(_html.escape(doc.subtitle), S["cover_sub"]))
    fl.append(Spacer(1, 10 * mm))
    fl.append(hr())
    meta_rows = [
        ["Source", doc.source or "-"],
        ["Generated", doc.date],
        ["Level", doc.level],
        ["Estimated study time", ("%s hours" % doc.hours) if doc.hours else "-"],
        ["Language", "English"],
        ["Volume", doc.title],
    ]
    from reportlab.platypus import Paragraph as P
    data = [[P("<b>%s</b>" % _html.escape(k), S["cover_meta"]),
             P(_html.escape(str(v)), S["cover_meta"])] for k, v in meta_rows]
    t = Table(data, colWidths=[46 * mm, 104 * mm], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, colors.HexColor(C["rule"])),
    ]))
    fl.append(t)
    fl.append(Spacer(1, 8 * mm))
    fl.append(Paragraph(
        "This volume is personal study material. The notes, examples, exercises and "
        "tests were written from scratch while following the source site's learning "
        "path. No content is affiliated with, endorsed by, or copied from the source "
        "site or the technology's owner.", S["footer"]))
    fl.append(NextPageTemplate("normal"))
    fl.append(PageBreak())
    return fl


def toc_flowables(doc: VolumeDoc):
    from reportlab.platypus import Paragraph, Spacer, PageBreak
    from reportlab.platypus.tableofcontents import TableOfContents
    S = doc.S
    fl = []
    fl.append(Paragraph("Table of contents", S["h1"]))
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"], S["toc2"]]
    toc.dotsMinLevel = 0
    fl.append(toc)
    fl.append(PageBreak())
    return fl


# --------------------------------------------------------------------------- #
# Render
# --------------------------------------------------------------------------- #

_section_counter = {"h2": 0}


def render_blocks(doc: VolumeDoc, story: list):
    from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether
    S = doc.S
    fonts = doc.fonts
    mono = fonts[4]

    chapter_no = 0
    section_no = 0
    for bi, blk in enumerate(doc.blocks):
        k = blk.kind

        if k == "h1":
            chapter_no += 1
            section_no = 0
            # The front matter chapter ("How to use this volume") is chapter 0:
            # its sections stay unnumbered, the real chapters start at 1.
            if "how to use" in blk.text.lower():
                chapter_no = 0
            p = Paragraph(_html.escape(blk.text), S["h1"])
            p._toc_text = blk.text
            p._toc_level = 0
            p._toc_key = "ch%d" % bi
            story.append(p)
            story.append(hr())

        elif k == "h2":
            section_no += 1
            label = blk.text if chapter_no == 0 else "%d.%d  %s" % (chapter_no, section_no, blk.text)
            p = Paragraph(_html.escape(label), S["h2"])
            p._toc_text = label
            p._toc_level = 1
            p._toc_key = "sec%d" % bi
            story.append(p)

        elif k == "h3":
            p = Paragraph(_html.escape(blk.text), S["h3"])
            p._toc_text = blk.text
            p._toc_level = 2
            p._toc_key = "sub%d" % bi
            story.append(p)

        elif k == "h4":
            story.append(Paragraph(_html.escape(blk.text), S["h4"]))

        elif k == "para":
            if blk.text.strip():
                story.append(Paragraph(inline(blk.text).replace("MONO_FONT", mono), S["body"]))

        elif k == "code":
            story.append(Spacer(1, 3))
            story.extend(make_code(blk.text, blk.extra.get("lang", ""), S, fonts))
            story.append(Spacer(1, 7))

        elif k == "table":
            story.append(Spacer(1, 3))
            story.append(make_table(blk.extra["rows"], S, fonts))
            story.append(Spacer(1, 8))

        elif k == "quote":
            story.append(Spacer(1, 3))
            story.append(make_quote(blk.text, S, fonts, blk.extra.get("admon")))
            story.append(Spacer(1, 8))

        elif k in ("ul", "ol"):
            story.extend(build_list_flow(blk.extra["items"], S, fonts,
                                         ordered=(k == "ol"),
                                         start=blk.extra.get("start", 1)))
            story.append(Spacer(1, 4))

        elif k == "hr":
            story.append(hr())


def volume_pdf(meta: dict, md_body: str, out_path: str) -> str:
    fonts = register_fonts()
    blocks = parse_blocks(md_body)
    doc = VolumeDoc(meta, blocks, fonts)
    d = make_doc(out_path, doc)
    story = []
    story.extend(cover_flowables(doc))
    story.extend(toc_flowables(doc))
    render_blocks(doc, story)
    d.multiBuild(story)
    return out_path


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

VOLUME_TEMPLATE = """---
title: Vol. {nn} - {name}
technology: {name}
source: {source}
date: {date}
level: Beginner to intermediate
hours: 20
---

# How to use this volume

**Prerequisites:** ...

**Estimated study time:** ...

**How the chapters work:** every chapter ends with practice exercises (with
solutions) and a mini test with an answer key. Code blocks are numbered so the
explanations and the tests can refer to specific lines.

## Chapter map

| # | Chapter | You will learn |
|---|---------|----------------|
| 1 | ... | ... |

# Chapter 1 - Getting started

## Summary

- point 1
- point 2
- point 3
- point 4
- point 5

## Concepts

Explain the idea in simple terms here. Keep paragraphs short.

| Concept | Meaning |
|---------|---------|
| A | ... |

## Examples

```{lang}
// code here
```

Expected output:

```text
output here
```

## Common mistakes and best practices

- Mistake -> fix

## Practice exercises

1. Exercise text
2. Exercise text
3. Exercise text

### Solutions

1. Solution text
2. Solution text
3. Solution text

## Mini test

1. **Question text?**
   - a) option
   - b) option
   - c) option
   - d) option
2. **True or false:** statement.
3. **What is the output?**

```{lang}
// snippet
```

### Answer key and explanations

1. **b** - because ...

# Cheat sheet

| Item | Syntax | Notes |
|------|--------|-------|
| ... | ... | ... |

# Final test

1. **Question...**
   - a) ...
   - b) ...

## Final test answers

1. **a** - ...

# Sources

- https://example.com/page
- https://example.com/page2
"""


def cmd_new(slug: str):
    from slugify import slugify  # type: ignore
    raise SystemExit("use --new <NN> <name> <lang> <source>")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build Learn for Free PDF volumes.")
    ap.add_argument("volume", nargs="?", help="volume slug, e.g. 01-html")
    ap.add_argument("--all", action="store_true", help="build every volume in src/")
    ap.add_argument("--out", help="output PDF path (single volume only)")
    ap.add_argument("--src", help="explicit markdown source path")
    ap.add_argument("--new", nargs=4, metavar=("NN", "NAME", "LANG", "SOURCE"),
                    help="scaffold a new volume: --new 42 fable js example.com")
    args = ap.parse_args(argv)

    if args.new:
        nn, name, lang, source = args.new
        slug = ("%s-%s" % (nn, re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")))
        dst = os.path.join(SRC_DIR, slug + ".md")
        os.makedirs(SRC_DIR, exist_ok=True)
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write(VOLUME_TEMPLATE.format(nn=nn, name=name.title(), lang=lang,
                                            source=source, date=date.today().isoformat()))
        print("created %s" % dst)
        return 0

    targets = []
    if args.all:
        targets = sorted(f[:-3] for f in os.listdir(SRC_DIR) if f.endswith(".md"))
    elif args.volume:
        targets = [args.volume]
    else:
        ap.print_help()
        return 2

    os.makedirs(PDF_DIR, exist_ok=True)
    failures = []
    for slug in targets:
        src = args.src or os.path.join(SRC_DIR, slug + ".md")
        if not os.path.exists(src):
            print("!! missing source: %s" % src)
            failures.append(slug)
            continue
        out = args.out or os.path.join(PDF_DIR, slug + ".pdf")
        with open(src, encoding="utf-8") as fh:
            text = fh.read()
        meta, body = parse_front_matter(text)
        meta.setdefault("title", slug)
        try:
            volume_pdf(meta, body, out)
            n_blocks = len(parse_blocks(body))
            print("OK  %-34s -> %s  (%d blocks)" % (slug, os.path.relpath(out, ROOT), n_blocks))
        except Exception as exc:  # pragma: no cover
            print("FAIL %s: %s" % (slug, exc))
            failures.append(slug)
    if failures:
        print("\n%d volume(s) failed: %s" % (len(failures), ", ".join(failures)))
        return 1
    print("\n%d volume(s) built." % len(targets))
    return 0


if __name__ == "__main__":
    sys.exit(main())
