#!/usr/bin/env python3
"""
Forgejo API Documentation Scraper

Fetches the OpenAPI/Swagger spec from a Forgejo instance and converts
each tag group into a separate markdown file documenting the endpoints.

Usage:
    python3 benchmark/scripts/scrape_forgejo.py
"""

import json
import re
from datetime import datetime
from pathlib import Path

import requests

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "forgejo" / "docs"
SPEC_URL = "https://codeberg.org/swagger.v1.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

# Tag groups to include (skip admin)
INCLUDE_TAGS = {
    "issue", "miscellaneous", "notification", "organization",
    "package", "repository", "user",
}


def param_doc(param: dict) -> str:
    location = param.get("in", "?")
    name = param.get("name", "?")
    required = " (required)" if param.get("required") else ""
    ptype = param.get("type", param.get("schema", {}).get("type", "any"))
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
    summary = op.get("summary", op.get("operationId", "")).strip()
    desc = op.get("description", "").strip()

    lines.append(f"### {method.upper()} `{path}`")
    if summary:
        lines.append(f"\n**{summary}**")
    if desc and desc != summary:
        lines.append(f"\n{desc}")

    params = op.get("parameters", [])
    if params:
        lines.append("\n**Parameters:**")
        for p in params:
            lines.append(param_doc(p))

    body = op.get("body") or next(
        (p for p in params if p.get("in") == "body"), None
    )
    if body:
        schema = body.get("schema", {})
        lines.append(f"\n**Request body** (`{body.get('name', 'body')}`): {body.get('description', '').strip()}")

    responses = op.get("responses", {})
    if responses:
        lines.append("\n**Responses:**")
        lines.append(response_doc(responses))

    return "\n".join(lines)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Forgejo API Documentation Scraper")
    print(f"Spec: {SPEC_URL}")
    print("=" * 60)

    session = requests.Session()
    session.headers.update(HEADERS)
    session.verify = "/etc/ssl/cert.pem"

    print("Fetching OpenAPI spec...", flush=True)
    resp = session.get(SPEC_URL, timeout=(10, 60))
    resp.raise_for_status()
    spec = resp.json()

    info = spec.get("info", {})
    version = info.get("version", "unknown")
    print(f"Forgejo API version: {version}")

    paths = spec.get("paths", {})

    # Group endpoints by tag
    by_tag: dict[str, list[tuple]] = {t: [] for t in INCLUDE_TAGS}

    for path, path_item in paths.items():
        for method, op in path_item.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue
            tags = op.get("tags", ["miscellaneous"])
            for tag in tags:
                tag_lower = tag.lower()
                if tag_lower in INCLUDE_TAGS:
                    by_tag[tag_lower].append((method, path, op))

    scraped_files = []

    for tag, endpoints in by_tag.items():
        if not endpoints:
            continue
        filename = f"api_{tag}.md"
        title = tag.replace("_", " ").title()
        print(f"  {title:<25} {len(endpoints)} endpoints")

        lines = [f"# {title}", f"\n*Source: {SPEC_URL}*", "\n---\n"]
        for method, path, op in sorted(endpoints, key=lambda x: (x[1], x[0])):
            lines.append(endpoint_to_md(method, path, op))
            lines.append("")

        content = "\n".join(lines)
        (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")
        scraped_files.append({
            "filename": filename,
            "title": title,
            "url": SPEC_URL,
            "endpoint_count": len(endpoints),
        })

    manifest = {
        "source": f"Forgejo API v{version} (OpenAPI spec)",
        "scraped_from": SPEC_URL,
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nScraped: {len(scraped_files)} tag groups")
    print(f"Output:  {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
