#!/usr/bin/env python3
"""
Clockify API Documentation Scraper

The Clockify docs (docs.clockify.me) are a Redoc SPA — requires Playwright
to render. Falls back to fetching the raw OpenAPI spec from the public endpoint
and converting each tag group to markdown (same approach as Forgejo).

Usage:
    # First try: Playwright (if installed)
    python3 benchmark/scripts/scrape_clockify.py

    # The script auto-falls back to spec-based scraping if Playwright unavailable
"""

import json
import re
from datetime import datetime
from pathlib import Path

import requests

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "clockify" / "docs"

# Clockify publishes their OpenAPI spec here
SPEC_URL = "https://docs.clockify.me/api-reference"
OPENAPI_URL = "https://docs.clockify.me/openapi.yaml"

HEADERS = {"User-Agent": "Mozilla/5.0", "Accept": "application/json, text/plain"}

INCLUDE_TAGS = [
    "User", "Workspace", "Client", "Project", "Task", "Tag",
    "Time entry", "Approval", "Expense", "Invoice", "Group",
    "Time Off", "Balance", "Policy", "Scheduling", "Webhooks",
]


def param_doc(param: dict) -> str:
    location = param.get("in", "?")
    name = param.get("name", "?")
    required = " (required)" if param.get("required") else ""
    schema = param.get("schema", {})
    ptype = schema.get("type", param.get("type", "any"))
    desc = param.get("description", "").strip().replace("\n", " ")
    return f"  - `{name}` [{location}]{required} *{ptype}*: {desc}"


def response_doc(responses: dict) -> str:
    lines = []
    for code, resp in sorted(responses.items()):
        desc = resp.get("description", "").strip()
        lines.append(f"  - `{code}`: {desc}")
    return "\n".join(lines)


def endpoint_to_md(method: str, path: str, op: dict) -> str:
    lines = []
    summary = op.get("summary", "").strip()
    desc = op.get("description", "").strip()

    lines.append(f"### {method.upper()} `{path}`")
    if summary:
        lines.append(f"\n**{summary}**")
    if desc and desc != summary:
        lines.append(f"\n{re.sub(r'<[^>]+>', '', desc)}")

    params = [p for p in op.get("parameters", []) if p.get("in") != "body"]
    if params:
        lines.append("\n**Parameters:**")
        for p in params:
            lines.append(param_doc(p))

    req_body = op.get("requestBody", {})
    if req_body:
        desc_rb = req_body.get("description", "").strip()
        lines.append(f"\n**Request body**: {desc_rb}")

    responses = op.get("responses", {})
    if responses:
        lines.append("\n**Responses:**")
        lines.append(response_doc(responses))

    return "\n".join(lines)


def scrape_from_spec(spec: dict) -> None:
    paths = spec.get("paths", {})
    version = spec.get("info", {}).get("version", "unknown")
    print(f"Clockify API version: {version}")

    by_tag: dict[str, list] = {t: [] for t in INCLUDE_TAGS}

    for path, path_item in paths.items():
        for method, op in path_item.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue
            tags = op.get("tags", [])
            for tag in tags:
                if tag in by_tag:
                    by_tag[tag].append((method, path, op))

    scraped_files = []

    for tag in INCLUDE_TAGS:
        endpoints = by_tag.get(tag, [])
        if not endpoints:
            continue
        filename = f"api_{tag.lower().replace(' ', '_')}.md"
        print(f"  {tag:<25} {len(endpoints)} endpoints")

        lines = [f"# {tag}", f"\n*Source: {SPEC_URL}*", "\n---\n"]
        for method, path, op in sorted(endpoints, key=lambda x: (x[1], x[0])):
            lines.append(endpoint_to_md(method, path, op))
            lines.append("")

        content = "\n".join(lines)
        (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")
        scraped_files.append({
            "filename": filename,
            "title": tag,
            "url": SPEC_URL,
            "endpoint_count": len(endpoints),
        })

    manifest = {
        "source": f"Clockify API v{version} (OpenAPI spec)",
        "scraped_from": OPENAPI_URL,
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nScraped: {len(scraped_files)} tag groups")
    print(f"Output:  {OUTPUT_DIR}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Clockify API Documentation Scraper")
    print("=" * 60)

    session = requests.Session()
    session.headers.update(HEADERS)

    # Try to fetch the OpenAPI spec directly
    for spec_url in [OPENAPI_URL, "https://docs.clockify.me/openapi.json"]:
        print(f"Trying spec at {spec_url}...", flush=True)
        try:
            resp = session.get(spec_url, timeout=(10, 30))
            if resp.ok:
                try:
                    import yaml
                    spec = yaml.safe_load(resp.text)
                except ImportError:
                    spec = json.loads(resp.text)
                print("Got spec.")
                scrape_from_spec(spec)
                return
        except Exception as e:
            print(f"  failed: {e}")

    print("\nCould not fetch OpenAPI spec. Try installing playwright:")
    print("  uv pip install playwright && playwright install chromium")
    print("Then re-run this script.")


if __name__ == "__main__":
    main()
