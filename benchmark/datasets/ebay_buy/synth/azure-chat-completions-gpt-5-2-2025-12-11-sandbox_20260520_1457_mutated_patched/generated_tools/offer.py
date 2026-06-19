from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


_AUCTION_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.offer.auction"


def get_bidding(
    client: EbayClient,
    *,
    listing_id: str,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Requires user access token in real eBay; this server uses app token and may fail."""

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request(
        "GET",
        f"/buy/offer/v1_beta/bidding/{listing_id}",
        headers=headers,
        scope=_AUCTION_SCOPE,
    )


def place_proxy_bid(
    client: EbayClient,
    *,
    listing_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    adult_only_item_consent: Optional[bool] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Requires user access token in real eBay; this server uses app token and may fail."""

    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    payload: Dict[str, Any] = {
        "maxAmount": {"value": max_amount_value, "currency": max_amount_currency}
    }
    if adult_only_item_consent is not None:
        payload["userConsent"] = {"adultOnlyItem": bool(adult_only_item_consent)}

    return client.request(
        "POST",
        f"/buy/offer/v1_beta/bidding/{listing_id}/place_proxy_bid",
        headers=headers,
        json=payload,
        scope=_AUCTION_SCOPE,
    )
