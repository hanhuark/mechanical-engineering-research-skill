#!/usr/bin/env python3
"""Validate repository packaging, docs links, commands, and eval fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def require_file(path: str) -> Path:
    full = ROOT / path
    if not full.is_file():
        fail(f"missing required file: {path}")
    return full


def require_dir(path: str) -> Path:
    full = ROOT / path
    if not full.is_dir():
        fail(f"missing required directory: {path}")
    return full


def load_json(path: str):
    try:
        return json.loads(require_file(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def validate_manifests() -> None:
    codex = load_json(".codex-plugin/plugin.json")
    claude = load_json(".claude-plugin/plugin.json")

    for name, data in [("Codex", codex), ("Claude", claude)]:
        if data.get("name") != "thermal-fluid-research-workflow":
            fail(f"{name} manifest has unexpected plugin name")
        if data.get("version") != VERSION:
            fail(f"{name} manifest version must be {VERSION}")
        if not data.get("description"):
            fail(f"{name} manifest is missing description")

    if codex.get("skills") != "./skills/":
        fail("Codex manifest must point skills to ./skills/")

    for keyword in ["cfd", "heat-transfer", "fluid-dynamics", "mechanical-engineering"]:
        if keyword not in codex.get("keywords", []):
            fail(f"Codex manifest missing keyword: {keyword}")


def validate_commands() -> None:
    command_dir = require_dir("commands")
    commands = sorted(command_dir.glob("*.md"))
    if len(commands) < 13:
        fail("expected at least 13 command prompts")

    for command in commands:
        text = command.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"{command.relative_to(ROOT)} missing frontmatter")
        if "description:" not in text.split("---", 2)[1]:
            fail(f"{command.relative_to(ROOT)} missing description in frontmatter")
        if "Expected output:" not in text:
            fail(f"{command.relative_to(ROOT)} missing Expected output section")


def validate_eval_fixtures() -> None:
    data = load_json("tests/thermal-fluid-evals/prompt-fixtures.json")
    if not isinstance(data, list):
        fail("eval fixture file must contain a list")
    if len(data) != 10:
        fail("expected exactly 10 thermal-fluid eval fixtures")

    seen = set()
    for item in data:
        item_id = item.get("id")
        if not item_id or item_id in seen:
            fail("eval fixtures must have unique non-empty ids")
        seen.add(item_id)
        if not item.get("prompt"):
            fail(f"eval fixture {item_id} missing prompt")
        checks = item.get("expected_checks")
        if not isinstance(checks, list) or len(checks) < 3:
            fail(f"eval fixture {item_id} must include at least three expected checks")


def validate_markdown_links() -> None:
    markdown_files = [
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and path.name.upper() != "LICENSE"
    ]
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_link in link_pattern.findall(text):
            link = raw_link.strip()
            if not link or link.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = link.split("#", 1)[0]
            if not target:
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                fail(f"{path.relative_to(ROOT)} links outside repo: {raw_link}")
            if not target_path.exists():
                fail(f"{path.relative_to(ROOT)} has broken link: {raw_link}")


def validate_docs() -> None:
    for required in [
        "README.md",
        "README.zh-CN.md",
        "README.zh-TW.md",
        "QUICKSTART.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "assets/workflow.mmd",
        "examples/showcase/README.md",
        "docs/GITHUB_TOPICS.md",
    ]:
        require_file(required)

    workflow = require_file("assets/workflow.mmd").read_text(encoding="utf-8")
    if "flowchart TB" not in workflow or "Thermal-fluid rigor gate" not in workflow:
        fail("workflow.mmd does not contain expected workflow diagram")


def main() -> int:
    validate_docs()
    validate_manifests()
    validate_commands()
    validate_eval_fixtures()
    validate_markdown_links()
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
