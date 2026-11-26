#!/usr/bin/env python3
"""Keep sub-skill reference copies identical to the coordinator's references.

The coordinator skill's `skills/mechanical-engineering-research/references/` is the source.
A focused sub-skill may carry a copy of a reference so that it works when installed on its
own. Each copy must equal the source, except that relative links to files the sub-skill
does not carry are rewritten to point at the coordinator's file.

    python scripts/sync_reference_copies.py          # rewrite stale copies
    python scripts/sync_reference_copies.py --check  # report stale copies, exit 1 if any
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "skills" / "mechanical-engineering-research" / "references"
LINK_PATTERN = re.compile(r"(?<!!)(\[[^\]]+\]\()([^)\s]+)(\))")


def copy_pairs() -> list[tuple[Path, Path]]:
    """Return (source, copy) pairs for every sub-skill reference named like a source reference."""
    pairs = []
    for copy in sorted((ROOT / "skills").glob("*/references/*.md")):
        if copy.parent == SOURCE_DIR:
            continue
        source = SOURCE_DIR / copy.name
        if source.is_file():
            pairs.append((source, copy))
    return pairs


def expected_copy_text(source: Path, copy: Path) -> str:
    """Source text with relative links re-pointed so that they resolve from the copy's folder."""
    text = source.read_text(encoding="utf-8")

    def relink(match: re.Match[str]) -> str:
        target = match.group(2)
        if target.startswith(("#", "http://", "https://", "mailto:")):
            return match.group(0)
        path_part, _, anchor = target.partition("#")
        resolved = (source.parent / path_part).resolve()
        local = copy.parent / resolved.name
        if resolved.parent == SOURCE_DIR.resolve() and local.is_file():
            new_target = resolved.name
        else:
            new_target = Path(os.path.relpath(resolved, copy.parent)).as_posix()
        if anchor:
            new_target += "#" + anchor
        return match.group(1) + new_target + match.group(3)

    return LINK_PATTERN.sub(relink, text)


def stale_copies() -> list[Path]:
    return [copy for source, copy in copy_pairs()
            if copy.read_text(encoding="utf-8") != expected_copy_text(source, copy)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report stale copies without writing")
    args = parser.parse_args()
    stale = stale_copies()
    for copy in stale:
        print(f"{'stale' if args.check else 'synced'}: {copy.relative_to(ROOT).as_posix()}")
        if not args.check:
            source = SOURCE_DIR / copy.name
            copy.write_text(expected_copy_text(source, copy), encoding="utf-8", newline="\n")
    if args.check and stale:
        return 1
    print(f"{len(copy_pairs())} reference copies checked; {len(stale)} {'stale' if args.check else 'synced'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
