"""
eBay Buy Offer API tools.
Covers: auction bidding (get bidding info, place proxy bid).
Note: getBidding and placeProxyBid require a user access token (authorization code grant),
not just client credentials. The token must be passed explicitly by the caller.
"""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .auth import get_auth_headers, get_base_url


def register_offer_tools(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_bidding(
        listing_id: str,
        user_access_token: str,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve the buyer's bidding details for a specific auction item.
        Returns current price, bid count, proxy bid, high bidder status,
        reserve price met status, and suggested bid amounts.

        Note: Requires a USER access token (authorization code grant), not
        the application token. The buyer must have already placed at least one bid.

        Args:
            listing_id: RESTful item ID of the auction (e.g. 'v1|123456789|0').
            user_access_token: OAuth user access token with buy.offer.auction scope.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        url = f"{get_base_url()}/buy/offer/v1_beta/bidding/{listing_id}"
        headers = {
            "Authorization": f"Bearer {user_access_token}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def place_proxy_bid(
        listing_id: str,
        max_amount_value: str,
        max_amount_currency: str,
        user_access_token: str,
        adult_only_item_consent: bool = False,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Place a proxy bid on an eBay auction item on behalf of a buyer.
        eBay will automatically bid up to the max amount if outbid.
        Returns the proxyBidId confirming the bid was placed.

        Note: Requires a USER access token (authorization code grant), not
        the application token. By placing a bid, the buyer agrees to purchase
        the item if they win.

        Args:
            listing_id: RESTful item ID of the auction (e.g. 'v1|123456789|0').
            max_amount_value: Maximum bid amount as a string (e.g. '150.00').
            max_amount_currency: ISO 4217 currency code (e.g. 'USD', 'GBP').
            user_access_token: OAuth user access token with buy.offer.auction scope.
            adult_only_item_consent: Set True if bidding on adult-only items
                                     and buyer has consented.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        url = f"{get_base_url()}/buy/offer/v1_beta/bidding/{listing_id}/place_proxy_bid"
        payload = {
            "maxAmount": {
                "value": max_amount_value,
                "currency": max_amount_currency,
            }
        }
        if adult_only_item_consent:
            payload["userConsent"] = {"adultOnlyItem": True}

        headers = {
            "Authorization": f"Bearer {user_access_token}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
            "Content-Type": "application/json",
        }
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
