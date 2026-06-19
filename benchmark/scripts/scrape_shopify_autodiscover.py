#!/usr/bin/env python3
"""
Shopify Admin REST API Documentation Scraper

Strategy:
  Uses a hardcoded list of resource URLs from the Shopify Admin REST API
  sitemap (version 2026-01). Pages are server-rendered (~1.1MB each) so
  plain requests fetches work — no JS rendering needed.

Content extraction:
  After removing <script>, <style>, <noscript> tags, the main content lives
  in a div whose class contains "ResourcePage". Falls back to locating <h1>
  and walking 5 parent levels up if that selector is not found.

Usage:
    uv run python benchmark/scripts/scrape_shopify_autodiscover.py
    # or
    python benchmark/scripts/scrape_shopify_autodiscover.py

Output:
    benchmark/datasets/shopify/docs/
        _manifest.json
        api_order.md
        api_product.md
        ...
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

BASE_URL   = "https://shopify.dev"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "shopify" / "docs"

DELAY = 1.0            # seconds between requests — pages are large, be polite
MIN_CONTENT_LEN = 500  # minimum characters to keep a page

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

# Hardcoded list of resource URLs (version 2026-01, from sitemap)
RESOURCE_URLS = [
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/abandoned-checkouts",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/accessscope",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/applicationcharge",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/applicationcredit",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/article",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/asset",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/blog",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/cancellationrequest",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/carrierservice",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/checkout",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/collect",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/collection",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/comment",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/country",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/currency",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/customcollection",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/customer",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/customer-address",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/discountcode",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/dispute",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/draftorder",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/event",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillment",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentevent",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentorder",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentrequest",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentservice",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/gift-card",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/inventoryitem",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/inventorylevel",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/location",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/marketingevent",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/metafield",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/order",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/order-risk",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/page",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/payment",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/payouts",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/policy",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/pricerule",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/product",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/product-image",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/product-variant",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/productlisting",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/province",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/recurringapplicationcharge",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/redirect",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/refund",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/resourcefeedback",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/shippingzone",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/shop",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/smartcollection",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/theme",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/transaction",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/usagecharge",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/user",
    "https://shopify.dev/docs/api/admin-rest/2026-01/resources/webhook",
]


# ---------------------------------------------------------------------------
# HTML -> Markdown conversion
# ---------------------------------------------------------------------------

def _build_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0           # don't wrap lines
    h.protect_links = False
    h.unicode_snob = True
    h.skip_internal_links = True
    h.single_line_break = False
    return h


_CONVERTER = _build_converter()


def _extract_main_content(html: str) -> str:
    """
    Extract the main article content from a Shopify Admin REST docs page.

    Primary strategy: find a div whose class contains "ResourcePage" — this
    is the content wrapper used by shopify.dev for resource reference pages.

    Fallback: locate <h1> and walk 5 parent levels up to reach the content
    container div.

    In both cases, <script>, <style>, and <noscript> tags are removed first.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove noisy/invisible elements
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    # Primary: div with class containing "ResourcePage"
    resource_page = soup.select_one('[class*="ResourcePage"]')
    if resource_page:
        return str(resource_page)

    # Fallback: find h1 and walk 5 parent levels up
    h1 = soup.find("h1")
    if h1:
        content_el = h1
        for _ in range(5):
            if content_el.parent:
                content_el = content_el.parent
        return str(content_el)

    # Last resort: full body
    body = soup.find("body")
    return str(body) if body else html


def html_to_markdown(html: str) -> str:
    """Convert a Shopify docs page HTML to clean markdown."""
    main_html = _extract_main_content(html)
    md = _CONVERTER.handle(main_html)

    # Clean up common conversion artefacts
    md = re.sub(r"\n{4,}", "\n\n\n", md)       # collapse excessive blank lines
    md = re.sub(r"[ \t]+\n", "\n", md)          # trailing whitespace
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)      # remove ¶ anchor links
    md = re.sub(r"\[#\]\([^)]*\)", "", md)      # remove # anchor links
    md = md.strip()

    return md


# ---------------------------------------------------------------------------
# Title extraction
# ---------------------------------------------------------------------------

def extract_title(html: str, url: str) -> str:
    """Extract page title from HTML <title> tag, split on '|', take left part."""
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Shopify titles are like "Order | Shopify API Reference" — take the left part
        title = title.split("|")[0].strip()
        if title:
            return title

    # Fall back to h1 text
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)

    # Derive from URL last path segment
    return url.rstrip("/").split("/")[-1]


# ---------------------------------------------------------------------------
# URL -> filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str) -> str:
    """
    Convert a Shopify resource URL to a local markdown filename.

    Takes the last path segment (the resource name) and prefixes with "api_".

    Examples:
      .../resources/order          ->  api_order.md
      .../resources/product-image  ->  api_product-image.md
      .../resources/customer       ->  api_customer.md
    """
    resource_name = url.rstrip("/").split("/")[-1]
    # Sanitize any unexpected characters (hyphens are fine for readability)
    resource_name = re.sub(r"[^\w\-]", "_", resource_name).strip("_")
    return f"api_{resource_name}.md"


# ---------------------------------------------------------------------------
# Main scrape loop
# ---------------------------------------------------------------------------

def scrape_page(session: requests.Session, url: str) -> tuple[str, str] | None:
    """
    Fetch a single Shopify resource page and return (title, markdown_content).
    Returns None on failure or if content is too short.
    """
    try:
        resp = session.get(url, timeout=(10, 60))
        if resp.status_code == 404:
            return None
        resp.raise_for_status()

        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return None

        title = extract_title(resp.text, url)
        md    = html_to_markdown(resp.text)

        if len(md) < MIN_CONTENT_LEN:
            return None

        return title, md

    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def main():
    # --- Backup existing output dir if it has content ---
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.iterdir()):
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs -> {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Shopify Admin REST API Documentation Scraper")
    print(f"Source: {BASE_URL}/docs/api/admin-rest/2026-01/resources")
    print(f"Pages:  {len(RESOURCE_URLS)}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    scraped_files = []
    skipped = []

    for i, url in enumerate(RESOURCE_URLS, 1):
        filename = url_to_filename(url)
        label    = url.replace(BASE_URL, "")
        print(f"[{i:2d}/{len(RESOURCE_URLS)}] {label[:65]:<65}", end=" ", flush=True)

        result = scrape_page(session, url)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            skipped.append(url)
            continue

        title, content = result

        filepath = OUTPUT_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"*Source: {url}*\n\n")
            f.write("---\n\n")
            f.write(content)

        lines = content.count("\n")
        print(f"({lines} lines)")

        scraped_files.append({
            "filename": filename,
            "title":    title,
            "url":      url,
        })

    print()
    print("=" * 70)
    print(f"Scraped: {len(scraped_files)}")
    print(f"Skipped: {len(skipped)}")
    if skipped:
        print("Skipped URLs:")
        for u in skipped:
            print(f"  {u}")

    manifest = {
        "source":       "Shopify Admin REST API Documentation (shopify.dev)",
        "scraped_from": f"{BASE_URL}/docs/api/admin-rest/2026-01/resources",
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
