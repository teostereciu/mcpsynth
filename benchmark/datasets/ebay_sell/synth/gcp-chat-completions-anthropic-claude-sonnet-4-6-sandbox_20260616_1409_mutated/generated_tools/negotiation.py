"""eBay Sell Negotiation API tools."""
from typing import Optional
from .client import get_client


def find_eligible_items(marketplace_id: str = "EBAY_US", limit: Optional[str] = None,
                         offset: Optional[str] = None) -> dict:
    """Evaluate seller's listings and return IDs eligible for seller-initiated discount offers."""
    client = get_client()
    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/negotiation/v1/find_eligible_items", params=params, extra_headers=headers)


def send_offer_to_interested_buyers(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Send eligible buyers offers to purchase items in a listing at a discount."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/negotiation/v1/send_offer_to_interested_buyers", json=body, extra_headers=headers)
