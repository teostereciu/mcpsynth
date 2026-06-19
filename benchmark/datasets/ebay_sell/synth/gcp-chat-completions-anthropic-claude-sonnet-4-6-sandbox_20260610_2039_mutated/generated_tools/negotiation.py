"""eBay Sell Negotiation API tools."""
from typing import Any, Optional
from .client import get_client


def find_eligible_items(
    marketplace_id: str = "EBAY_US",
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Find listings eligible for a seller-initiated discount offer to buyers."""
    client = get_client()
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/negotiation/v1/find_eligible_items", params=params, headers=headers)


def send_offer_to_interested_buyers(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Send eligible buyers offers to purchase items in a listing at a discount."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/negotiation/v1/send_offer_to_interested_buyers", json=body, headers=headers)
