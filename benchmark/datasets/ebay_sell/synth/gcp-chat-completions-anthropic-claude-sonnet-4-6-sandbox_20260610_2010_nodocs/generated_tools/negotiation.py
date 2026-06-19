"""
eBay Sell Negotiation API tools.
Covers: sending offers to buyers (Best Offer / Offers to Buyers).
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post

mcp = FastMCP("ebay-negotiation")


@mcp.tool()
def find_eligible_items(limit: int = 10, offset: int = 0) -> dict:
    """
    Find listings eligible for sending offers to buyers.

    Args:
        limit: Results per page.
        offset: Pagination offset.
    """
    return api_get("/sell/negotiation/v1/find_eligible_items",
                   params={"limit": limit, "offset": offset})


@mcp.tool()
def send_offers_to_interested_buyers(offers: list[dict]) -> dict:
    """
    Send price offers to buyers who have shown interest in your listings.

    Args:
        offers: List of offer objects, each containing:
                - listingId: The listing ID.
                - price: Dict with value and currency.
                - message: Optional message to the buyer.
                - allowCounterOffer: Whether to allow counter-offers.
                - buyerUsernames: List of buyer usernames to send to.
    """
    return api_post("/sell/negotiation/v1/send_offers_to_interested_buyers",
                    body={"offers": offers})


@mcp.tool()
def get_offers_to_buyers(limit: int = 10, offset: int = 0,
                          listing_id: str | None = None) -> dict:
    """
    Retrieve offers previously sent to buyers.

    Args:
        limit: Results per page.
        offset: Pagination offset.
        listing_id: Filter by listing ID.
    """
    params: dict = {"limit": limit, "offset": offset}
    if listing_id:
        params["listing_id"] = listing_id
    return api_get("/sell/negotiation/v1/get_offers_to_buyers", params=params)
