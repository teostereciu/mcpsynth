#!/usr/bin/env python3
"""
TikTok Shop Partner API Documentation Scraper

Uses the TikTok Shop partner docs JSON API directly — no browser required.

Discovery strategy:
  - /api/v1/document/detail returns `prev_document_id` and `next_document_id`,
    so we walk the entire doc tree as a doubly-linked list starting from a
    known seed slug.
  - We also seed from the JS bundle slugs found during initial debug to catch
    any disconnected sections.

Content strategy:
  - The `content` field in /api/v1/document/detail is already clean markdown.
  - We write it directly, no HTML parsing needed.

Usage:
    python3 benchmark/scripts/scrape_tiktok_shop_autodiscover.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import requests


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL   = "https://partner.tiktokshop.com"
API_BASE   = f"{BASE_URL}/api/v1/document/detail"
PARAMS_BASE = {"workspace_id": "3", "aid": "359713", "locale": "en-US"}

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "tiktok_shop" / "docs"

DELAY = 0.4   # seconds between requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Referer": BASE_URL,
}

# Seed slugs — one per disconnected section to ensure full coverage.
# The linked-list walk will discover everything reachable from each seed.
SEEDS = [
    "get-authorized-category-assets-202405",  # Authorization / Category
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_doc(session: requests.Session, doc_id: str) -> dict | None:
    """Fetch a single document from the detail API. Returns parsed data or None."""
    print(f"    GET {doc_id[:60]}...", end=" ", flush=True)
    try:
        resp = session.get(
            API_BASE,
            params={**PARAMS_BASE, "document_id": doc_id},
            timeout=(5, 15),  # (connect, read)
        )
        resp.raise_for_status()
        body = resp.json()
        print(f"HTTP {resp.status_code} code={body.get('code')}")
        if body.get("code") == 0 and body.get("data"):
            return body["data"]
    except Exception as e:
        print(f"ERROR: {e}")
    return None


def slug_to_filename(slug: str) -> str:
    safe = re.sub(r"[^\w\-]", "_", slug)
    return f"api_{safe}.md"


def content_to_markdown(data: dict) -> str:
    """
    The API returns content as markdown already.
    We clean up stray HTML-style table width annotations and normalise spacing.
    """
    content = data.get("content", "")
    # Remove <!-- width:Npx --> annotations from table headers
    content = re.sub(r"\s*<!--[^>]*-->", "", content)
    # Normalise excessive blank lines
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    return content.strip()


# ---------------------------------------------------------------------------
# Discovery: walk prev/next linked list from each seed
# ---------------------------------------------------------------------------

def discover_all_slugs(session: requests.Session) -> list[str]:
    """
    Walk the prev_document_path / next_document_path linked list bidirectionally
    from each seed slug. Returns deduplicated ordered list of slugs.
    """
    visited: set[str] = set()
    ordered: list[str] = []

    def walk(start_slug: str):
        # Walk forward (next) and backward (prev) from start
        for direction in ("next", "prev"):
            current = start_slug
            while current and current not in visited:
                visited.add(current)
                ordered.append(current)

                data = fetch_doc(session, current)
                time.sleep(DELAY)

                if not data:
                    break

                if direction == "next":
                    current = data.get("next_document_path") or None
                else:
                    current = data.get("prev_document_path") or None

    for seed in SEEDS:
        if seed not in visited:
            print(f"  Seeding from: {seed}")
            walk(seed)
            print(f"  Discovered so far: {len(visited)} docs")

    return ordered


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if OUTPUT_DIR.exists():
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs → {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("TikTok Shop Partner API Documentation Scraper")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    # --- Discovery ---
    print("\nDiscovering all doc slugs via prev/next linked list...")
    slugs = discover_all_slugs(session)
    print(f"\nTotal discovered: {len(slugs)} documents")
    print("=" * 70)

    # --- Scrape ---
    scraped_files = []
    skipped = []

    for i, slug in enumerate(slugs, 1):
        filename = slug_to_filename(slug)
        print(f"[{i}/{len(slugs)}] {slug}... ", end="", flush=True)

        data = fetch_doc(session, slug)
        time.sleep(DELAY)

        if not data:
            print("✗ no data")
            skipped.append(slug)
            continue

        title   = data.get("title", slug)
        content = content_to_markdown(data)

        if len(content) < 50:
            print("✗ too short")
            skipped.append(slug)
            continue

        source_url = f"{BASE_URL}/docv2/page/{slug}"
        filepath = OUTPUT_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"*Source: {source_url}*\n\n")
            f.write("---\n\n")
            f.write(content)

        lines = len(content.split("\n"))
        print(f"✓ ({lines} lines)")

        scraped_files.append({
            "filename": filename,
            "title": title,
            "url": source_url,
        })

    print("\n" + "=" * 70)
    print(f"✓ Scraped: {len(scraped_files)}/{len(slugs)}")
    print(f"✗ Skipped: {len(skipped)}")

    manifest = {
        "source": "TikTok Shop Partner API Documentation (Scraped)",
        "scraped_from": f"{BASE_URL}/docv2/page/get-authorized-category-assets-202405",
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    manifest_path = OUTPUT_DIR / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nOutput:   {OUTPUT_DIR}")
    print(f"Manifest: {manifest_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
