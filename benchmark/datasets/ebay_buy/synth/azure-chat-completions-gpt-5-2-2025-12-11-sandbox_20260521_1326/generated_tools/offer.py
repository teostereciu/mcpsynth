from typing import Any, Dict, Optional

from .client import EbayApiClient


def get_bidding(item_id: str, marketplace_id: str) -> Dict[str, Any]:
    """GET /buy/offer/v1_beta/bidding/{item_id}

    Note: eBay docs require a *user* access token (authorization code grant). This server
    uses application tokens; calls may fail with 403.
    """
    client = EbayApiClient()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", f"/buy/offer/v1_beta/bidding/{item_id}", headers=headers)


def place_proxy_bid(
    item_id: str,
    marketplace_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid

    Note: eBay docs require a *user* access token (authorization code grant). This server
    uses application tokens; calls may fail with 403.
    """
    client = EbayApiClient()
    headers = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    body: Dict[str, Any] = {
        "maxAmount": {"value": max_amount_value, "currency": max_amount_currency},
    }
    if adult_only_item_consent is not None:
        body["userConsent"] = {"adultOnlyItem": bool(adult_only_item_consent)}

    return client.request(
        "POST",
        f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid",
        json=body,
        headers=headers,
    )
