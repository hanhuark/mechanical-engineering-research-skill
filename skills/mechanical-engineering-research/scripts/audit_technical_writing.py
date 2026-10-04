#!/usr/bin/env python3
"""Screen plain-text technical drafts for editorial review candidates.

The output is an inventory, not an authorship detector or a grammar verdict.
Review every result in context and follow the target journal's style guide.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


DEFAULT_LAZY_TERM_PATTERNS = {
    "enable": r"\benabl(?:e|es|ed|ing)\b",
    "establish": r"\bestablish(?:es|ed|ing)?\b",
    "unusually": r"\bunusually\b",
    "together": r"\btogether\b",
}
EN_DASH = "\u2013"
EM_DASH = "\u2014"


def count_matches(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def count_spaced_characters(text: str, character: str) -> int:
    return len(re.findall(rf"\s{re.escape(character)}\s", text))


def count_unspaced_characters(text: str, character: str) -> int:
    total = text.count(character)
    return total - count_spaced_characters(text, character)


def collect_hyphenated_compounds(text: str) -> dict[str, int]:
    compounds = re.findall(r"\b[A-Za-z]+(?:-[A-Za-z]+)+\b", text)
    return dict(sorted(Counter(item.lower() for item in compounds).items()))


def term_patterns(extra_terms: Iterable[str]) -> dict[str, str]:
    patterns = dict(DEFAULT_LAZY_TERM_PATTERNS)
    for term in extra_terms:
        normalized = term.strip()
        if normalized:
            patterns[normalized] = rf"\b{re.escape(normalized)}\b"
    return patterns


def build_report(text: str, source: Path, extra_terms: Iterable[str]) -> dict[str, object]:
    patterns = term_patterns(extra_terms)
    return {
        "source": str(source),
        "lazy_term_counts": {
            term: count_matches(text, pattern) for term, pattern in patterns.items()
        },
        "dash_forms": {
            "hyphen_minus": text.count("-"),
            "spaced_hyphen_minus": count_spaced_characters(text, "-"),
            "en_dash": text.count(EN_DASH),
            "spaced_en_dash": count_spaced_characters(text, EN_DASH),
            "unspaced_en_dash": count_unspaced_characters(text, EN_DASH),
            "em_dash": text.count(EM_DASH),
            "spaced_em_dash": count_spaced_characters(text, EM_DASH),
            "unspaced_em_dash": count_unspaced_characters(text, EM_DASH),
        },
        "hyphenated_compounds": collect_hyphenated_compounds(text),
        "editorial_note": (
            "Counts and compound inventories are review candidates, not errors or evidence of AI authorship. "
            "Check whether a term states a specific mechanism or result, whether a compound is standard or defined, "
            "and whether dash spacing follows the target style."
        ),
    }


def format_report(report: dict[str, object]) -> str:
    lazy_terms = report["lazy_term_counts"]
    dashes = report["dash_forms"]
    compounds = report["hyphenated_compounds"]
    lines = ["Technical-writing editorial screen", f"Source: {report['source']}", "", "Lazy-term counts:"]
    lines.extend(f"- {term}: {count}" for term, count in lazy_terms.items())
    lines.extend(["", "Dash forms:"])
    lines.extend(f"- {name}: {count}" for name, count in dashes.items())
    lines.extend(["", "Hyphenated-compound inventory:"])
    if compounds:
        lines.extend(f"- {term}: {count}" for term, count in compounds.items())
    else:
        lines.append("- none detected")
    lines.extend(["", f"Editorial note: {report['editorial_note']}"])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Screen a UTF-8 plain-text, Markdown, or LaTeX draft for editorial review candidates."
    )
    parser.add_argument("source", type=Path, help="UTF-8 text, Markdown, or LaTeX draft to inspect")
    parser.add_argument(
        "--term",
        action="append",
        default=[],
        help="Additional exact word or phrase to count; repeat as needed",
    )
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable report")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.source.is_file():
        raise SystemExit(f"ERROR: source file not found: {args.source}")
    text = args.source.read_text(encoding="utf-8")
    report = build_report(text, args.source, args.term)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
