from typing import Any, Dict, Optional

from .common import client


def get_bidding(listing_id: str, marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/offer/v1_beta/bidding/{listing_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def place_proxy_bid(
    listing_id: str,
    marketplace_id: str,
    currency: str,
    value: str,
    adult_only_item: Optional[bool] = None,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {"maxAmount": {"currency": currency, "value": value}}
    if adult_only_item is not None:
        body["userConsent"] = {"adultOnlyItem": adult_only_item}
    return client.request(
        "POST",
        f"/buy/offer/v1_beta/bidding/{listing_id}/place_proxy_bid",
        json_body=body,
        headers={
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        },
    )
