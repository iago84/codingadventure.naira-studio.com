#!/usr/bin/env python3
"""
check_examples.py - run every JavaScript example in the Vol. 03 source with Node.

What it does
------------
1. Extracts every fenced ```js block from ../src/03-javascript.md.
2. Checks the syntax with `node --check`.
3. Runs it with Node and captures stdout.
4. If the block is followed by a ```text block, compares the real output with
   the published expectation, line by line.
5. Blocks marked `// DOM EXAMPLE` need a browser, so they are reported as
   skipped (not executed). Blocks marked `// MODULE EXAMPLE` are syntax-checked
   only, because they are multi-file examples.
6. Saves every example to examples/ so it can be run by hand.

Run:  python check_examples.py
Exit code 0 = everything that can run, runs and matches.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "src", "03-javascript.md")
HERE = os.path.dirname(os.path.abspath(__file__))
NODE = "node"

FENCE_RE = re.compile(r"^```([A-Za-z0-9_+#.-]*)\s*$")


def extract_blocks(text: str):
    """Return [(lang, code, start_line)] plus [(js_index, expected_text)]."""
    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if m:
            lang = (m.group(1) or "").lower()
            start = i + 1
            buf = []
            i += 1
            while i < len(lines) and not FENCE_RE.match(lines[i]):
                buf.append(lines[i])
                i += 1
            while buf and not buf[-1].strip():
                buf.pop()
            blocks.append({"lang": lang, "code": "\n".join(buf), "line": start})
            i += 1
            continue
        i += 1

    # pair each js block with the block that follows it
    for idx, blk in enumerate(blocks):
        blk["expected"] = None
        if blk["lang"] != "js":
            continue
        nxt = blocks[idx + 1] if idx + 1 < len(blocks) else None
        if nxt and nxt["lang"] in ("text", "output"):
            # only when there is nothing but a blank line between them
            gap = nxt["line"] - (blk["line"] + blk["code"].count("\n") + 2)
            if gap <= 1:
                blk["expected"] = nxt["code"]
    return blocks


def normalise(text: str) -> list[str]:
    return [ln.rstrip() for ln in text.rstrip("\n").split("\n")]


def module_file_name(code: str) -> str | None:
    """Return the file name declared by a MODULE EXAMPLE marker."""
    m = re.search(r"MODULE EXAMPLE \(syntax\):\s*(\S+\.m?js)", code)
    return m.group(1) if m else None


def run_module_group(names: list[str], code_by_name: dict[str, str],
                     main: str, expected: str | None) -> tuple[int, str]:
    """Write every file of the example into one temp folder and run `main`."""
    folder = tempfile.mkdtemp(prefix="lff-module-")
    try:
        for name in names:
            with open(os.path.join(folder, name), "w", encoding="utf-8") as fh:
                fh.write(code_by_name[name].rstrip() + "\n")
        proc = subprocess.run([NODE, os.path.join(folder, main)],
                              capture_output=True, timeout=30, cwd=folder)
        out = (proc.stdout or b"").decode("utf-8", errors="replace")
        err = (proc.stderr or b"").decode("utf-8", errors="replace")
        if proc.returncode != 0:
            return proc.returncode, err
        if expected is None:
            return 0, out
        return (0, out) if normalise(out) == normalise(expected) else (1, out)
    except subprocess.TimeoutExpired:
        return 124, "timeout"
    except FileNotFoundError:
        return 127, "node executable not found"
    finally:
        import shutil
        shutil.rmtree(folder, ignore_errors=True)


def run_node(code: str, suffix: str, check_only: bool) -> tuple[int, str, str]:
    """Run (or syntax-check) one file with Node and decode its output as UTF-8.

    Node may print Unicode (box drawing for console.table), so the output is
    read as bytes and decoded explicitly: text=True would use the console
    encoding and fail on Windows.
    """
    with tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False,
                                      encoding="utf-8") as fh:
        fh.write(code)
        path = fh.name
    try:
        cmd = [NODE, "--check", path] if check_only else [NODE, path]
        proc = subprocess.run(cmd, capture_output=True, timeout=30)
        out = (proc.stdout or b"").decode("utf-8", errors="replace")
        err = (proc.stderr or b"").decode("utf-8", errors="replace")
        return proc.returncode, out, err
    except subprocess.TimeoutExpired:
        return 124, "", "timeout after 30s"
    except FileNotFoundError:
        return 127, "", "node executable not found"
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def main() -> int:
    if not os.path.exists(SRC):
        print("source not found: %s" % SRC)
        return 2
    with open(SRC, encoding="utf-8") as fh:
        text = fh.read()

    blocks = extract_blocks(text)
    js_blocks = [(i, b) for i, b in enumerate(blocks) if b["lang"] == "js"]
    failures = 0
    skipped = 0
    passed = 0

    print("Vol. 03 JavaScript - executing %d examples with Node\n" % len(js_blocks))

    outdir = os.path.join(HERE, "examples")
    os.makedirs(outdir, exist_ok=True)

    # Group consecutive MODULE EXAMPLE blocks: they form one multi-file example.
    module_groups: list[list[int]] = []
    current: list[int] = []
    for n, (idx, blk) in enumerate(js_blocks, 1):
        if "MODULE EXAMPLE" in blk["code"]:
            current.append(n)
        elif current:
            module_groups.append(current)
            current = []
    if current:
        module_groups.append(current)
    in_group = {n: g for g in module_groups for n in g}

    for n, (idx, blk) in enumerate(js_blocks, 1):
        code = blk["code"]
        label = code.strip().splitlines()[0][:56] if code.strip() else "(empty)"
        expected = blk["expected"]

        # DOM examples need a browser.
        if "DOM EXAMPLE" in code:
            skipped += 1
            print("skip %3d (src line %4d) browser only: %s" % (n, blk["line"], label))
            continue

        # Multi-file module examples run together, below.
        if n in in_group:
            group = in_group[n]
            if group[0] != n:
                continue                      # handled by the first block of the group
            code_by_name = {}
            for member in group:
                member_blk = js_blocks[member - 1][1]
                name = module_file_name(member_blk["code"])
                if name:
                    code_by_name[name] = member_blk["code"]
            main_name = module_file_name(code) or "main.mjs"
            rc, detail = run_module_group(list(code_by_name), code_by_name,
                                           main_name, expected)
            if rc == 0:
                passed += 1
                print("ok   %3d (src line %4d) module %s runs, output matches"
                      % (n, blk["line"], main_name))
            else:
                failures += 1
                print("FAIL %3d (src line %4d) module %s: %s"
                      % (n, blk["line"], main_name,
                         detail.strip().splitlines()[0] if detail else "?"))
                for line in detail.strip().splitlines()[1:5]:
                    print("       | %s" % line)
            continue

        # syntax check first, for every block
        rc, _out, err = run_node(code, ".mjs", check_only=True)
        if rc != 0:
            failures += 1
            print("FAIL %3d (src line %4d) syntax: %s" % (n, blk["line"], label))
            for line in err.strip().splitlines()[:4]:
                print("       | %s" % line)
            continue

        rc, out, err = run_node(code, ".mjs", check_only=False)
        if rc != 0:
            failures += 1
            print("FAIL %3d (src line %4d) runtime error: %s"
                  % (n, blk["line"], label))
            for line in err.strip().splitlines()[:4]:
                print("       | %s" % line)
            continue

        actual = normalise(out)
        if expected is None:
            passed += 1
            print("ok   %3d (src line %4d) runs, no expected output: %s"
                  % (n, blk["line"], label))
        else:
            want = normalise(expected)
            if actual == want:
                passed += 1
                print("ok   %3d (src line %4d) output matches: %s"
                      % (n, blk["line"], label))
            else:
                failures += 1
                print("FAIL %3d (src line %4d) output differs: %s"
                      % (n, blk["line"], label))
                for a, b in zip(actual + ["<none>"] * len(want),
                                want + ["<none>"] * len(actual)):
                    if a != b:
                        print("        expected: %r" % b)
                        print("        actual  : %r" % a)
                        break

        # save the example
        with open(os.path.join(outdir, "%03d.mjs" % n), "w", encoding="utf-8") as fh:
            fh.write("// src/03-javascript.md line %d\n" % blk["line"])
            fh.write(code.rstrip() + "\n")

    # save the module examples as real files
    for group in module_groups:
        for member in group:
            member_blk = js_blocks[member - 1][1]
            name = module_file_name(member_blk["code"]) or ("mod-%03d.mjs" % member)
            with open(os.path.join(outdir, name), "w", encoding="utf-8") as fh:
                fh.write("// src/03-javascript.md line %d\n" % member_blk["line"])
                fh.write(member_blk["code"].rstrip() + "\n")

    print("\nsaved %d examples to %s" % (len(js_blocks), os.path.relpath(outdir, HERE)))
    print("RESULT: %d ok, %d skipped (browser or multi-file), %d FAILED"
          % (passed, skipped, failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
