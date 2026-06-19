from typing import Any, Dict

from generated_tools.common import client


def get_bidding(item_id: str, marketplace_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/offer/v1_beta/bidding/{item_id}", headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id})


def place_proxy_bid(
    item_id: str,
    marketplace_id: str,
    currency: str,
    value: str,
    adult_only_item: bool = False,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Type": "application/json"},
        json_body={
            "maxAmount": {"currency": currency, "value": value},
            "userConsent": {"adultOnlyItem": adult_only_item},
        },
    )
