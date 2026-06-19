"""
eBay Commerce Catalog API tools.
Base path: /commerce/catalog/v1
Auth: app token (client_credentials)
"""

from .auth import app_get, app_post

_BASE = "/commerce/catalog/v1"


# ---------------------------------------------------------------------------
# Product search
# ---------------------------------------------------------------------------

def search_catalog_products(
    q: str | None = None,
    gtin: str | None = None,
    epid: str | None = None,
    category_ids: str | None = None,
    aspect_filter: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Search the eBay product catalog.

    Args:
        q: Free-text search query (keywords).
        gtin: Global Trade Item Number (UPC, EAN, ISBN, etc.).
        epid: eBay Product ID to look up directly.
        category_ids: Comma-separated list of category IDs to restrict results.
        aspect_filter: Aspect name/value filter string, e.g. "Brand:Apple".
        limit: Number of results to return (max 200).
        offset: Pagination offset.

    Returns:
        Dict with productSummaries list and pagination info.
    """
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
    return app_get(f"{_BASE}/product_summary/search", params=params)


# ---------------------------------------------------------------------------
# Product detail
# ---------------------------------------------------------------------------

def get_catalog_product(epid: str) -> dict:
    """
    Retrieve full details for a single eBay catalog product by its eBay Product ID (ePID).

    Args:
        epid: The eBay Product ID (e.g. "15032").

    Returns:
        Dict with product title, description, aspects, images, GTINs, etc.
    """
    return app_get(f"{_BASE}/product/{epid}")
