"""Validate catalog metadata, README freshness, and local links without networking."""

from __future__ import annotations

from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from build_readme import render

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(([^\s)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
STATUSES = {"conference", "journal", "preprint", "technical-report"}


def slug(heading: str) -> str:
    heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def anchors(text: str) -> set[str]:
    result: set[str] = set()
    seen: Counter[str] = Counter()
    for heading in HEADING.findall(text):
        base = slug(heading)
        suffix = "" if not seen[base] else f"-{seen[base]}"
        result.add(base + suffix)
        seen[base] += 1
    return result


def canonical_url(url: str) -> str:
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/")
    if parsed.netloc == "arxiv.org":
        path = path.replace("/pdf/", "/abs/")
        path = re.sub(r"(v\d+)?(\.pdf)?$", "", path)
    return parsed.netloc.lower() + path


def main() -> int:
    errors: list[str] = []
    try:
        catalog = json.loads((ROOT / "resources/papers.json").read_text(encoding="utf-8"))
        checked_on = date.fromisoformat(catalog["checked_on"])
        sections = catalog["sections"]
        if not isinstance(sections, list) or not sections:
            raise ValueError("Expected a nonempty sections array")
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"Invalid catalog: {exc}", file=sys.stderr)
        return 1

    papers: list[dict] = []
    ids: list[str] = []
    for section in sections:
        if section.get("id") != slug(section.get("title", "")):
            errors.append(f"Section ID does not match heading: {section.get('id')}")
        ids.append(section.get("id", ""))
        if not section.get("description") or not section.get("papers"):
            errors.append(f"Empty section: {section.get('id')}")
        for paper in section.get("papers", []):
            label = paper.get("id", "<missing ID>")
            for field in ("id", "title", "url", "venue", "status", "summary"):
                if not isinstance(paper.get(field), str) or not paper[field].strip():
                    errors.append(f"{label}: missing or invalid {field}")
            year = paper.get("year")
            if not isinstance(year, int) or not 1900 <= year <= checked_on.year:
                errors.append(f"{label}: invalid publication year")
            if paper.get("status") not in STATUSES:
                errors.append(f"{label}: invalid publication status")
            if paper.get("status") in {"preprint", "technical-report"} and paper.get("venue") != "arXiv":
                errors.append(f"{label}: update rendering for a non-arXiv report")
            source = urlsplit(paper.get("url", ""))
            if source.scheme != "https" or not source.netloc or source.fragment:
                errors.append(f"{label}: expected a direct HTTPS primary source")
            if not paper.get("summary", "").endswith("."):
                errors.append(f"{label}: summary must end with a period")
            first = paper.get("first_preprint")
            if first is not None and (not isinstance(first, int) or not isinstance(year, int) or first > year):
                errors.append(f"{label}: invalid first preprint year")
            papers.append(paper)

    for kind, values in (
        ("section ID", ids),
        ("paper ID", [p.get("id", "") for p in papers]),
        ("paper title", [p.get("title", "").casefold() for p in papers]),
        ("primary URL", [canonical_url(p.get("url", "")) for p in papers]),
    ):
        for value, count in Counter(values).items():
            if count > 1:
                errors.append(f"Duplicate {kind}: {value}")

    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not text.endswith("\n"):
            errors.append(f"{relative}: missing final newline")
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{relative}:{number}: trailing whitespace")
            if re.search(r"[\u4e00-\u9fff]", line):
                errors.append(f"{relative}:{number}: expected English-only content")
        for target in LINK.findall(text):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if destination != ROOT and ROOT not in destination.parents:
                errors.append(f"{relative}: link escapes repository: {target}")
                continue
            if not destination.is_file():
                errors.append(f"{relative}: missing local target: {target}")
                continue
            if parsed.fragment and destination.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"{relative}: missing anchor: {target}")

    if not errors:
        expected = render(catalog)
        readme = ROOT / "README.md"
        if not readme.is_file() or readme.read_text(encoding="utf-8") != expected:
            errors.append("README.md is stale. Run python scripts/build_readme.py.")
    if re.search(r"[\u4e00-\u9fff]", json.dumps(catalog, ensure_ascii=False)):
        errors.append("Catalog must be in English")

    for required in (
        "LICENSE", "CONTRIBUTING.md", "docs/taxonomy.md", "docs/reading-guide.md",
        "docs/model-guide.md", "docs/evaluation.md", "docs/version-notes.md",
        "docs/repository-setup.md", ".github/ISSUE_TEMPLATE/add-resource.yml",
        ".github/ISSUE_TEMPLATE/correction.yml", ".github/pull_request_template.md",
        ".github/workflows/quality.yml",
    ):
        if not (ROOT / required).is_file():
            errors.append(f"Missing required file: {required}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(papers)} unique papers in {len(sections)} categories and {len(files)} Markdown files.")
    print("Catalog metadata, README freshness, local links, anchors, and English content passed.")
    print("Remote availability and scientific results were not tested by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
