#!/usr/bin/env python3
"""
Jira Cloud REST API v3 Documentation Scraper

Fetches and converts the actual human-written HTML documentation pages
from developer.atlassian.com/cloud/jira/platform/rest/v3/ — no OpenAPI spec.

Discovery strategy:
  - 97 known API group slugs are scraped; the URL pattern is:
      https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-{slug}/

Content strategy:
  - The pages are server-rendered: all 3.9MB of HTML contains the full API
    documentation rendered into <div class="resource-section"> elements.
  - We fetch with requests, strip scripts/styles, find all resource-section
    divs, and convert to markdown with html2text.

Usage:
    python3 benchmark/scripts/scrape_jira_autodiscover.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL   = "https://developer.atlassian.com"
DOCS_BASE  = "https://developer.atlassian.com/cloud/jira/platform/rest/v3"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "jira" / "docs"

DELAY = 0.5  # seconds between requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

MIN_CONTENT_LEN = 200  # minimum characters to keep a page

# All 97 API group slugs from the Jira Cloud REST v3 docs
SLUGS = [
    "announcement-banner",
    "app-data-policies",
    "app-migration",
    "app-properties",
    "application-roles",
    "audit-records",
    "avatars",
    "classification-levels",
    "dashboards",
    "dynamic-modules",
    "field-schemes",
    "filter-sharing",
    "filters",
    "group-and-user-picker",
    "groups",
    "issue-attachments",
    "issue-bulk-operations",
    "issue-comment-properties",
    "issue-comments",
    "issue-custom-field-associations",
    "issue-custom-field-configuration-(apps)",
    "issue-custom-field-contexts",
    "issue-custom-field-options",
    "issue-custom-field-options-(apps)",
    "issue-custom-field-values-(apps)",
    "issue-field-configurations",
    "issue-fields",
    "issue-link-types",
    "issue-links",
    "issue-navigator-settings",
    "issue-notification-schemes",
    "issue-panels",
    "issue-priorities",
    "issue-properties",
    "issue-redaction",
    "issue-remote-links",
    "issue-resolutions",
    "issue-search",
    "issue-security-level",
    "issue-security-schemes",
    "issue-type-properties",
    "issue-type-schemes",
    "issue-type-screen-schemes",
    "issue-types",
    "issue-votes",
    "issue-watchers",
    "issue-worklog-properties",
    "issue-worklogs",
    "issues",
    "jql",
    "jql-functions-(apps)",
    "jira-expressions",
    "jira-settings",
    "labels",
    "license-metrics",
    "migration-of-connect-modules-to-forge",
    "myself",
    "permission-schemes",
    "permissions",
    "plans",
    "priority-schemes",
    "project-avatars",
    "project-categories",
    "project-classification-levels",
    "project-components",
    "project-email",
    "project-features",
    "project-key-and-name-validation",
    "project-permission-schemes",
    "project-properties",
    "project-role-actors",
    "project-roles",
    "project-templates",
    "project-types",
    "project-versions",
    "projects",
    "screen-schemes",
    "screen-tab-fields",
    "screen-tabs",
    "screens",
    "server-info",
    "service-registry",
    "status",
    "tasks",
    "teams-in-plan",
    "time-tracking",
    "ui-modifications-(apps)",
    "user-properties",
    "user-search",
    "users",
    "webhooks",
    "workflow-scheme-drafts",
    "workflow-scheme-project-associations",
    "workflow-schemes",
    "workflow-status-categories",
    "workflow-statuses",
    "workflow-transition-properties",
    "workflow-transition-rules",
    "workflows",
    "other-operations",
]


# ---------------------------------------------------------------------------
# HTML -> Markdown
# ---------------------------------------------------------------------------

def _build_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = True
    h.single_line_break = False
    return h


_CONVERTER = _build_converter()


def extract_content(html: str) -> tuple[str, str]:
    """
    Extract (title, markdown) from a Jira REST API group page.

    The pages are server-rendered with all content in
    <div class="resource-section"> elements. We strip noise, collect
    all resource-section divs, and convert with html2text.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Strip scripts, styles, noscript — they bloat the page but have no content
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    # Extract title
    title = "Jira API"
    title_tag = soup.find("title")
    if title_tag:
        t = title_tag.get_text(strip=True).split("|")[0].strip()
        if t:
            title = t
    # Prefer h1 if present
    h1 = soup.find("h1")
    if h1:
        t = h1.get_text(" ", strip=True)
        if t:
            title = t

    # Collect all resource-section divs (one per API endpoint group)
    resource_sections = soup.find_all("div", class_="resource-section")

    if not resource_sections:
        # Fallback: try body text
        body = soup.find("body")
        if body:
            md = _CONVERTER.handle(str(body))
            return title, _clean(md)
        return title, ""

    # Convert each section and join
    parts = []
    for sec in resource_sections:
        md = _CONVERTER.handle(str(sec))
        md = _clean(md)
        if md:
            parts.append(md)

    return title, "\n\n---\n\n".join(parts)


def _clean(md: str) -> str:
    md = re.sub(r"[ \t]+\n", "\n", md)       # trailing spaces
    md = re.sub(r"\n{4,}", "\n\n\n", md)      # collapse excessive blank lines
    md = re.sub(r"\[#\]\([^)]*\)", "", md)    # remove # anchor links
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)    # remove ¶ anchor links
    return md.strip()


# ---------------------------------------------------------------------------
# Scrape a single slug
# ---------------------------------------------------------------------------

def scrape_slug(session: requests.Session, slug: str) -> tuple[str, str] | None:
    """
    Fetch the Jira API group page for the given slug.
    Returns (title, markdown_content) or None on failure.
    """
    url = f"{DOCS_BASE}/api-group-{slug}/"

    try:
        resp = session.get(url, timeout=(10, 60))
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

    title, content = extract_content(resp.text)

    if len(content) < MIN_CONTENT_LEN:
        return None

    return title, content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # --- Backup existing output dir ---
    if OUTPUT_DIR.exists():
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs -> {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Jira Cloud REST API v3 Documentation Scraper")
    print(f"Source: {DOCS_BASE}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    print(f"\nScraping {len(SLUGS)} API group pages...")
    print("=" * 70)

    scraped_files = []
    skipped = []

    for i, slug in enumerate(SLUGS, 1):
        filename = f"api_{slug}.md"
        print(f"[{i}/{len(SLUGS)}] {slug:<55}", end=" ", flush=True)

        result = scrape_slug(session, slug)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            skipped.append(slug)
            continue

        title, content = result
        source_url = f"{DOCS_BASE}/api-group-{slug}/"

        filepath = OUTPUT_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"*Source: {source_url}*\n\n")
            f.write("---\n\n")
            f.write(content)

        lines = content.count("\n")
        print(f"({lines} lines)")

        scraped_files.append({
            "filename": filename,
            "title":    title,
            "url":      source_url,
        })

    print()
    print("=" * 70)
    print(f"Scraped: {len(scraped_files)}")
    print(f"Skipped: {len(skipped)}")

    if skipped:
        print(f"  Skipped slugs: {', '.join(skipped)}")

    manifest = {
        "source":       "Jira Cloud REST API v3 (developer.atlassian.com)",
        "scraped_from": DOCS_BASE,
        "scrape_date":  datetime.now().isoformat(),
        "total_pages":  len(scraped_files),
        "files":        scraped_files,
    }
    manifest_path = OUTPUT_DIR / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nOutput:   {OUTPUT_DIR}")
    print(f"Manifest: {manifest_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
