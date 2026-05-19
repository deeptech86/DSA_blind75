"""
clear_solutions.py
Resets all solution function bodies to `pass`, preserving:
  - Module-level problem docstrings
  - Function signatures
  - Function docstrings (Time/Space complexity + TODO hint)
  - Helper classes and functions
  - Test cases

Run this any time you want to clear your practice solutions and start fresh.
"""

import ast
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def clear_file(filepath):
    with open(filepath, "r") as f:
        source = f.read()

    lines = source.splitlines(keepends=True)

    try:
        tree = ast.parse(source)
    except SyntaxError:
        print(f"  Skipping (syntax error): {os.path.basename(filepath)}")
        return False

    # Collect solution functions: those whose first body statement is a
    # docstring containing "TODO". Store (doc_end_lineno, def_col, body_col).
    targets = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.body:
            continue
        first = node.body[0]
        if not (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
            and "TODO" in first.value.value
        ):
            continue
        targets.append((first.end_lineno, node.col_offset, first.col_offset))

    if not targets:
        return False

    # Process bottom-up so earlier line numbers stay valid after edits.
    targets.sort(reverse=True)

    changed = False
    for doc_end, def_col, body_col in targets:
        # Find the last line that still belongs to this function body.
        # A line belongs to the body when its indentation is deeper than
        # the `def` keyword; blank lines are skipped in this check.
        body_end = doc_end  # 1-indexed, inclusive; starts just at docstring end

        for i in range(doc_end, len(lines)):
            line = lines[i]
            if not line.strip():
                continue  # blank lines don't determine the boundary
            col = len(line) - len(line.lstrip())
            if col > def_col:
                body_end = i + 1  # extend to this line (1-indexed inclusive)
            else:
                break

        if body_end <= doc_end:
            continue  # nothing after the docstring

        # Skip if the body is already just `pass` (and nothing else).
        body_text = "".join(lines[doc_end:body_end]).strip()
        if body_text == "pass":
            continue

        # Replace everything after the docstring with a single `pass`.
        lines[doc_end:body_end] = [" " * body_col + "pass\n"]
        changed = True

    if changed:
        with open(filepath, "w") as f:
            f.write("".join(lines))
        return True
    return False


def main():
    cleared = 0
    total = 0
    script_name = os.path.basename(__file__)

    for dirpath, dirnames, filenames in os.walk(BASE_DIR):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]

        for filename in sorted(filenames):
            if not filename.endswith(".py") or filename == script_name:
                continue
            total += 1
            filepath = os.path.join(dirpath, filename)
            rel = os.path.relpath(filepath, BASE_DIR)

            if clear_file(filepath):
                print(f"  Cleared: {rel}")
                cleared += 1

    already_clean = total - cleared
    print(f"\nDone — {cleared} file(s) cleared, {already_clean} already clean.")


if __name__ == "__main__":
    main()
