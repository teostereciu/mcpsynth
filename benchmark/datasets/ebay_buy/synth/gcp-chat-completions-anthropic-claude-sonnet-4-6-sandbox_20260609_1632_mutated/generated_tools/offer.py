"""
eBay Buy Offer API tools.
Covers: auction bidding (get bidding info, place proxy bid).
Note: These methods require a user access token (authorization code grant),
not just a client credentials token.
"""

from __future__ import annotations
from typing import Optional
from .auth import get_auth_header, get_base_url


def get_bidding(
    listing_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve bidding details for a specific auction item for the authenticated buyer.
    The buyer must have already placed at least one bid on the item.
    Requires a user access token with buy.offer.auction scope.

    Args:
        listing_id: The RESTful item ID of the auction (e.g. 'v1|123456789|0').
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with auction status, current price, proxy bid, high bidder status,
        reserve price met, and suggested bid amounts.
    """
    import requests
    url = f"{get_base_url()}/buy/offer/v1_beta/bidding/{listing_id}"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def place_proxy_bid(
    listing_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: bool = False,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Place a proxy bid on an eBay auction item on behalf of the buyer.
    eBay will automatically bid up to the max amount if outbid.
    Requires a user access token with buy.offer.auction scope.

    Args:
        listing_id: The RESTful item ID of the auction (e.g. 'v1|123456789|0').
        max_amount_value: The maximum bid amount as a string (e.g. '25.00').
        max_amount_currency: The 3-letter ISO 4217 currency code (e.g. 'USD').
        adult_only_item_consent: Set to True if bidding on an adult-only item
            and the buyer consents to the Terms of Use (default False).
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with 'proxyBidId' if successful.
    """
    import requests
    url = f"{get_base_url()}/buy/offer/v1_beta/bidding/{listing_id}/place_proxy_bid"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Content-Type"] = "application/json"
    body = {
        "maxAmount": {
            "value": max_amount_value,
            "currency": max_amount_currency,
        },
        "userConsent": {
            "adultOnlyItem": adult_only_item_consent,
        },
    }
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
