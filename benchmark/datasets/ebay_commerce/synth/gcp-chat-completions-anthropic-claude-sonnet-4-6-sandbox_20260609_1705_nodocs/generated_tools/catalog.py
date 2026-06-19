"""
eBay Commerce Catalog API tools.
Uses app-token (client_credentials).
Base: /commerce/catalog/v1
"""

from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

_BASE = f"{BASE_URL}/commerce/catalog/v1"


# ── Product Search ────────────────────────────────────────────────────────────

def search_catalog_products(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    epid: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Search the eBay product catalog.

    Args:
        q: Free-text keyword query (e.g. 'iPhone 14').
        gtin: Global Trade Item Number (UPC, EAN, ISBN, etc.).
        epid: eBay Product ID.
        category_ids: Comma-separated list of category IDs to filter by.
        aspect_filter: Aspect filter string (e.g. 'categoryId:9355,Brand:Apple').
        limit: Number of results to return (1–200, default 10).
        offset: Pagination offset (default 0).
    """
    url = f"{_BASE}/product_summary/search"
    params: dict = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if gtin:
        params["gtin"] = gtin
    if epid:
        params["epid"] = epid
    if category_ids:
        params["category_ids"] = category_ids
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    resp = requests.get(url, headers=app_headers(), params=params, timeout=20)
    return safe_json(resp)


def get_catalog_product(epid: str) -> dict:
    """
    Retrieve a single eBay catalog product by its eBay Product ID (ePID).

    Args:
        epid: The eBay Product ID (e.g. 'EPD720125610').
    """
    url = f"{_BASE}/product/{epid}"
    resp = requests.get(url, headers=app_headers(), timeout=15)
    return safe_json(resp)
