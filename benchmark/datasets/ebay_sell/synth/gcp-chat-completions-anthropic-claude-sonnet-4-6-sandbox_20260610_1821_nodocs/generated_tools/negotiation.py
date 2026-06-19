"""
eBay Sell Negotiation API tools.
Covers: sending offers to buyers (Best Offer / Buyer Offer management).
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-negotiation")

# ---------------------------------------------------------------------------
# Offers to Buyers
# ---------------------------------------------------------------------------

@mcp.tool()
def find_eligible_items(
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Find listings that are eligible for sending offers to buyers.

    Args:
        limit: Number of eligible items to return (default 10, max 200).
        offset: Pagination offset (default 0).
    """
    return ebay_request(
        "GET",
        "/sell/negotiation/v1/find_eligible_items",
        params={"limit": limit, "offset": offset},
    )


@mcp.tool()
def send_offers_to_interested_buyers(offers: list) -> dict:
    """
    Send discount offers to buyers who have shown interest in your listings
    (watched, added to cart, or made a Best Offer).

    Args:
        offers: List of offer objects, each containing:
                - listingId: The listing to send the offer for.
                - offeredItems: List of items with price and quantity.
                - message: Optional message to the buyer.
                - expirationDate: Offer expiration date in ISO 8601 format.
                Example: [{
                  "listingId": "123456789",
                  "offeredItems": [{
                    "offeredPrice": {"value": "19.99", "currency": "USD"},
                    "quantity": 1
                  }],
                  "message": "Special offer just for you!",
                  "expirationDate": "2024-06-30T23:59:59Z"
                }]
    """
    return ebay_request(
        "POST",
        "/sell/negotiation/v1/send_offers_to_interested_buyers",
        json={"counteroffer": offers},
    )


@mcp.tool()
def get_offers_to_interested_buyers(
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Retrieve offers that have been sent to interested buyers.

    Args:
        limit: Number of offers to return (default 10).
        offset: Pagination offset (default 0).
    """
    return ebay_request(
        "GET",
        "/sell/negotiation/v1/get_offers_to_interested_buyers",
        params={"limit": limit, "offset": offset},
    )
