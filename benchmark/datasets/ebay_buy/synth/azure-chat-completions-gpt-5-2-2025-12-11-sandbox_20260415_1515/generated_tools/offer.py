from typing import Any, Dict, Optional

from .http_client import EbayClient


client = EbayClient()


def offer_get_bidding(
    item_id: str,
    *,
    marketplace_id: str,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", f"/buy/offer/v1_beta/bidding/{item_id}", headers=headers)


def offer_place_proxy_bid(
    item_id: str,
    *,
    marketplace_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    user_consent_adult_only_item: Optional[bool] = None,
) -> Dict[str, Any]:
    """Place a proxy bid.

    Note: eBay requires a USER access token for this endpoint (auth code grant).
    This server uses application tokens (client credentials), so this will likely fail unless eBay allows it.
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    payload: Dict[str, Any] = {
        "maxAmount": {"value": str(max_amount_value), "currency": str(max_amount_currency)},
    }
    if user_consent_adult_only_item is not None:
        payload["userConsent"] = {"adultOnlyItem": bool(user_consent_adult_only_item)}

    return client.request("POST", f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid", json=payload, headers=headers)
