"""
eBay Sell Recommendation API tools.
Covers: listing recommendations for improving quality and visibility.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-recommendation")

# ---------------------------------------------------------------------------
# Listing Recommendations
# ---------------------------------------------------------------------------

@mcp.tool()
def find_listing_recommendations(
    listing_ids: list | None = None,
    filter: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> dict:
    """
    Retrieve listing quality recommendations for one or more listings.

    Args:
        listing_ids: List of listing IDs to get recommendations for (optional;
                     if omitted, returns recommendations for all listings).
        filter: Filter string, e.g. 'recommendationTypes:{AD}' (optional).
        limit: Number of recommendations to return (default 100, max 500).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter

    body: dict = {}
    if listing_ids:
        body["listingIds"] = listing_ids

    if body:
        return ebay_request(
            "POST",
            "/sell/recommendation/v1/find",
            json=body,
            extra_headers={"X-EBAY-C-MARKETPLACE-ID": "EBAY_US"},
        )
    return ebay_request(
        "GET",
        "/sell/recommendation/v1/find",
        params=params,
    )
