"""
eBay Sell Recommendation API tools.
Covers: listing recommendations for improving quality and visibility.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post

mcp = FastMCP("ebay-recommendation")


@mcp.tool()
def find_listing_recommendations(listing_ids: list[str] | None = None,
                                   filter: str | None = None,
                                   limit: int = 100,
                                   offset: int = 0) -> dict:
    """
    Retrieve listing quality recommendations for one or more listings.

    Args:
        listing_ids: Optional list of listing IDs to get recommendations for.
        filter: Filter string (e.g. 'recommendationTypes:{AD}').
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    body: dict = {}
    if listing_ids:
        body["listingIds"] = listing_ids
    if body:
        return api_post("/sell/recommendation/v1/find_listing_recommendations",
                        body=body, params=params)
    return api_get("/sell/recommendation/v1/find_listing_recommendations", params=params)
