"""
eBay Commerce Catalog API tools.
Base: /commerce/catalog/v1
Auth: app token (client_credentials)
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
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Search the eBay product catalog.

    Args:
        q: Free-text keyword query.
        gtin: Global Trade Item Number (UPC, EAN, ISBN).
        epid: eBay Product ID to look up a specific product.
        category_ids: Comma-separated category IDs to restrict search.
        aspect_filter: Aspect filter string, e.g. 'categoryId:9355,Brand:Apple'.
        limit: Number of results per page (max 200, default 20).
        offset: Pagination offset.
    """
    try:
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

        resp = requests.get(
            f"{_BASE}/product_summary/search",
            headers=app_headers(),
            params=params,
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_catalog_product(epid: str) -> dict:
    """
    Retrieve full details for a specific eBay catalog product by ePID.

    Args:
        epid: The eBay Product ID (ePID).
    """
    try:
        resp = requests.get(
            f"{_BASE}/product/{epid}",
            headers=app_headers(),
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
