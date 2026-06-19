"""
eBay Commerce Catalog API tools.
Base URL: https://api.sandbox.ebay.com/commerce/catalog/v1_beta
Auth: App token (client_credentials)
"""

import requests
from .auth import app_headers, _base_url


def _catalog_url(path: str) -> str:
    return f"{_base_url()}/commerce/catalog/v1_beta{path}"


def get_product(epid: str, marketplace_id: str | None = None) -> dict:
    """
    Retrieve full details of a catalog product by its eBay product identifier (ePID).
    Returns title, description, aspects, images, category IDs, and recognized identifiers.
    """
    try:
        resp = requests.get(
            _catalog_url(f"/product/{epid}"),
            headers=app_headers(marketplace_id),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def search_products(
    query: str | None = None,
    gtin: str | None = None,
    mpn: str | None = None,
    category_id: str | None = None,
    aspects: str | None = None,
    field_groups: str | None = None,
    page_size: int | None = None,
    offset: int | None = None,
    marketplace_id: str | None = None,
) -> dict:
    """
    Search for product summaries in the eBay catalog.
    At least one of: query, gtin, mpn, or category_id must be provided.
    field_groups: MATCHING_PRODUCTS | ASPECT_REFINEMENTS | FULL
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
            params["fieldGroups"] = field_groups
        if page_size is not None:
            params["page_size"] = page_size
        if offset is not None:
            params["offset"] = offset

        resp = requests.get(
            _catalog_url("/product_summary/search"),
            headers=app_headers(marketplace_id),
            params=params,
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
