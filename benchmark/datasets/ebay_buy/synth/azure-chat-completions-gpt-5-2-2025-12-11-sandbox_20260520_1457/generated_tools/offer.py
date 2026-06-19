from typing import Any, Dict, Optional

from .client import EbayClient


def offer_get_bidding(
    client: EbayClient,
    item_id: str,
    *,
    marketplace_id: str,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", f"/buy/offer/v1_beta/bidding/{item_id}", headers=headers)


def offer_place_proxy_bid(
    client: EbayClient,
    item_id: str,
    *,
    marketplace_id: str,
    max_amount_currency: str,
    max_amount_value: str,
    adult_only_item_consent: Optional[bool] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    payload: Dict[str, Any] = {
        "maxAmount": {"currency": max_amount_currency, "value": max_amount_value}
    }
    if adult_only_item_consent is not None:
        payload["userConsent"] = {"adultOnlyItem": bool(adult_only_item_consent)}

    return client.request(
        "POST",
        f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid",
        json=payload,
        headers=headers,
    )
