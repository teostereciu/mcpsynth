"""
eBay Sell Negotiation API tools.
Covers: sending offers to buyers (Best Offer / Buyer Offer workflows).
"""

from typing import Optional
from auth import api_get, api_post


def find_eligible_items_for_offer(
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Find listings that are eligible to receive a seller-initiated offer."""
    return api_get("/sell/negotiation/v1/find_eligible_items",
                   params={"limit": limit, "offset": offset})


def send_offer_to_buyers(body: dict) -> dict:
    """
    Send a price offer to interested buyers for a listing.

    body fields:
      allowCounterOffer: bool
      message: str
      offeredItems: list of dicts with listingId, offeredPrice (value, currency),
                    quantity
      offerDuration: dict with unit and value (e.g. unit="DAY", value=3)
    """
    return api_post("/sell/negotiation/v1/send_offer_to_buyers", body=body)


def get_offers_sent_to_buyers(
    limit: int = 10,
    offset: int = 0,
    listing_id: Optional[str] = None,
) -> dict:
    """Get a list of offers sent to buyers."""
    params: dict = {"limit": limit, "offset": offset}
    if listing_id:
        params["listing_id"] = listing_id
    return api_get("/sell/negotiation/v1/get_offers_sent_to_buyers", params=params)
