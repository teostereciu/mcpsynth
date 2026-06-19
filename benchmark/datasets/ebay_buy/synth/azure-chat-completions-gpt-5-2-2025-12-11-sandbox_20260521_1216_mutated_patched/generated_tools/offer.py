from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class OfferTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_bidding(self, listing_id: str, *, marketplace_id: str) -> Dict[str, Any]:
        headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
        return self.client.request(
            "GET",
            f"/buy/offer/v1/bidding/{listing_id}",
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.offer.auction",
        )

    def place_proxy_bid(
        self,
        listing_id: str,
        max_amount: Dict[str, str],
        *,
        marketplace_id: str,
        adult_only_item_consent: Optional[bool] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
        payload: Dict[str, Any] = {"maxAmount": max_amount}
        if adult_only_item_consent is not None:
            payload["userConsent"] = {"adultOnlyItem": bool(adult_only_item_consent)}
        return self.client.request(
            "POST",
            f"/buy/offer/v1/bidding/{listing_id}/place_proxy_bid",
            json=payload,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.offer.auction",
        )
