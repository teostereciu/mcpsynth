"""
eBay Buy Marketplace Insights API tools.
Covers: searchByImage (sold items), search (sold items analytics).
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post

mcp = FastMCP("ebay-marketplace-insights")

INSIGHTS_BASE = "/buy/marketplace_insights/v1_beta"


@mcp.tool()
def search_sold_items(
    q: str = "",
    category_ids: str = "",
    filter: str = "",
    sort: str = "",
    limit: int = 50,
    offset: int = 0,
    aspect_filter: str = "",
    fieldgroups: str = "",
) -> dict:
    """
    Search for recently sold eBay items to research market prices and demand.

    Args:
        q: Free-text keyword query (e.g. 'vintage rolex submariner').
        category_ids: Comma-separated category IDs to restrict results.
        filter: eBay filter string (e.g. 'conditionIds:{1000},buyingOptions:{FIXED_PRICE}').
        sort: Sort order (e.g. 'price', '-price', 'endingSoonest').
        limit: Number of results per page (1-200, default 50).
        offset: Pagination offset.
        aspect_filter: Aspect filter string.
        fieldgroups: Comma-separated field groups to include.
    Returns:
        dict with itemSales list and pagination metadata.
    """
    params: dict = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return api_get(f"{INSIGHTS_BASE}/item_sales/search", params=params)


@mcp.tool()
def search_sold_items_by_image(
    image_base64: str,
    category_ids: str = "",
    filter: str = "",
    sort: str = "",
    limit: int = 50,
    offset: int = 0,
    aspect_filter: str = "",
) -> dict:
    """
    Search for recently sold eBay items visually similar to a provided image.

    Args:
        image_base64: Base64-encoded image data (JPEG/PNG).
        category_ids: Comma-separated category IDs to restrict results.
        filter: eBay filter string.
        sort: Sort order.
        limit: Number of results per page (1-200, default 50).
        offset: Pagination offset.
        aspect_filter: Aspect filter string.
    Returns:
        dict with itemSales list and pagination metadata.
    """
    params: dict = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    body = {"image": image_base64}
    return api_post(
        f"{INSIGHTS_BASE}/item_sales/search_by_image", body=body, params=params
    )
