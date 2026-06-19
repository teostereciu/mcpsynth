"""eBay Commerce Catalog API tools — app-token authenticated."""
from __future__ import annotations
import os
from typing import Optional
import requests
from .auth import get_app_token

SANDBOX = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper() == "SANDBOX"
BASE = "https://api.sandbox.ebay.com" if SANDBOX else "https://api.ebay.com"


def _headers(marketplace_id: str = "EBAY_US") -> dict:
    token = get_app_token()
    return {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }


def get_product(epid: str, marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve full details of a catalog product by eBay Product ID (ePID).

    Args:
        epid: The eBay product identifier (ePID).
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    url = f"{BASE}/commerce/catalog/v1_beta/product/{epid}"
    try:
        resp = requests.get(url, headers=_headers(marketplace_id), timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def search_products(
    query: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_id: Optional[str] = None,
    aspects: Optional[str] = None,
    field_groups: Optional[str] = None,
    page_size: int = 50,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Search for product summaries in the eBay catalog.

    At least one of query, gtin, mpn, or category_id must be provided.

    Args:
        query: Keyword search string.
        gtin: Comma-separated GTINs (EAN/ISBN/UPC).
        mpn: Comma-separated Manufacturer Part Numbers.
        category_id: Category ID to narrow results.
        aspects: Aspect filter string e.g. 'categoryId:9355,Color:{Black|White}'.
        field_groups: ASPECT_REFINEMENTS, MATCHING_PRODUCTS, or FULL.
        page_size: Number of results (max 200, default 50).
        offset: Pagination offset.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    url = f"{BASE}/commerce/catalog/v1_beta/product_summary/search"
    params: dict = {"page_size": page_size, "offset": offset}
    if query:
        params["q"] = query
    if gtin:
        params["gtin"] = gtin
    if mpn:
        params["mpn"] = mpn
    if category_id:
        params["category_id"] = category_id
    if aspects:
        params["aspects"] = aspects
    if field_groups:
        params["fieldGroups"] = field_groups
    try:
        resp = requests.get(url, headers=_headers(marketplace_id), params=params, timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
