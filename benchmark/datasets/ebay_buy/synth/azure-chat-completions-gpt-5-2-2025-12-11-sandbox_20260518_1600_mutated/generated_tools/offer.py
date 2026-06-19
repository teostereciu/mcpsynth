from typing import Any, Dict

from .client import EbayClient


# NOTE: Offer API bidding endpoints require a *user access token* (authorization code grant)
# with buy.offer.auction scope. This server uses application tokens, so these calls will
# typically fail unless you adapt authentication.


def get_bidding(
    client: EbayClient,
    *,
    item_id: str,
    marketplace_id: str,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", f"/buy/offer/v1_beta/bidding/{item_id}", headers=headers)


def place_proxy_bid(
    client: EbayClient,
    *,
    item_id: str,
    marketplace_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: bool = False,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"}
    payload: Dict[str, Any] = {
        "maxAmount": {"value": max_amount_value, "currency": max_amount_currency},
    }
    if adult_only_item_consent:
        payload["userConsent"] = {"adultOnlyItem": True}

    return client.request(
        "POST",
        f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid",
        json=payload,
        headers=headers,
    )
