#!/usr/bin/env python3
"""Add idempotent read-through navigation footers to Tiny Door option files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPTIONS_DIR = ROOT / "Options"
INDEX_PATH = OPTIONS_DIR / "INDEX.md"
START = "<!-- TINYDOOR_NAV_START -->"
END = "<!-- TINYDOOR_NAV_END -->"
NAV_RE = re.compile(r"\n?---\n\n<!-- TINYDOOR_NAV_START -->.*?<!-- TINYDOOR_NAV_END -->\s*\Z", re.S)
INDEX_RE = re.compile(r"^(\d{3})\. \[(.+?)\]\((.+?\.md)\)\s*$")


def read_index() -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    for line in INDEX_PATH.read_text(encoding="utf-8").splitlines():
        match = INDEX_RE.match(line)
        if match:
            number, title, filename = match.groups()
            entries.append((number, title, filename))
    return entries


def build_footer(entries: list[tuple[str, str, str]], index: int) -> str:
    lines = [
        "---",
        "",
        START,
        "## Continue reading",
        "",
        "[Options Index](INDEX.md)",
    ]

    if index + 1 < len(entries):
        next_number, next_title, next_filename = entries[index + 1]
        lines.extend([
            "",
            f"[Next: {next_number} — {next_title} →]({next_filename})",
        ])

    lines.extend([END, ""])
    return "\n".join(lines)


def main() -> None:
    entries = read_index()
    if not entries:
        raise SystemExit("No option entries found in Options/INDEX.md")

    for index, (_number, _title, filename) in enumerate(entries):
        path = OPTIONS_DIR / filename
        if not path.exists():
            raise FileNotFoundError(path)

        original = path.read_text(encoding="utf-8")
        body = NAV_RE.sub("", original).rstrip()
        updated = f"{body}\n\n{build_footer(entries, index)}"
        if updated != original:
            path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
