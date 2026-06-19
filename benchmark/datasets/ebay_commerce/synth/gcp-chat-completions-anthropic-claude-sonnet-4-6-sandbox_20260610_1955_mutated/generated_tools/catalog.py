"""
eBay Commerce Catalog API tools.
Uses app token (client_credentials).
Base: /commerce/catalog/v1_beta
"""
from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

CATALOG_BASE = f"{BASE_URL}/commerce/catalog/v1_beta"


def get_product(epid: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve full details of a catalog product by its eBay Product ID (ePID).
    Returns title, description, aspects, images, category IDs, GTINs, etc.

    Args:
        epid: The eBay product identifier (ePID).
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    try:
        resp = requests.get(
            f"{CATALOG_BASE}/product/{epid}",
            headers=app_headers(marketplace_id),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def search_products(
    query: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_id: Optional[str] = None,
    aspects: Optional[str] = None,
    field_groups: Optional[str] = None,
    page_size: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for products in the eBay catalog by keyword, GTIN, MPN, or category.
    Returns product summaries and optional aspect refinements.

    Args:
        query: Keyword search string (cannot be combined with gtin or mpn).
        gtin: Comma-separated GTINs (EAN, ISBN, UPC).
        mpn: Comma-separated Manufacturer Part Numbers.
        category_id: Category ID to narrow results.
        aspects: Aspect filter string e.g. 'categoryId:9355,Color:{Black|White}'.
        field_groups: ASPECT_REFINEMENTS, MATCHING_PRODUCTS, or FULL.
        page_size: Number of results per page (max 200, default 20).
        offset: Pagination offset.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    try:
        params: dict = {}
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
            params["field_groups"] = field_groups
        params["page_size"] = page_size
        params["offset"] = offset

        resp = requests.get(
            f"{CATALOG_BASE}/product_summary/search",
            headers=app_headers(marketplace_id),
            params=params,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
