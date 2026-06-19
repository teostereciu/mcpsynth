"""
eBay Buy Offer API tools.
Covers: auction bidding (get bidding info, place proxy bid).

Note: These methods require a USER access token (authorization code grant),
not the application token used by other Buy API methods.
"""
from typing import Optional
from . import _client as client


def get_bidding(
    item_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Retrieve buyer-specific bidding details for an auction item.

    Returns current bid status, proxy bid amount, whether the buyer is the
    highest bidder, suggested bid amounts, and auction status.

    Note: Requires a USER access token. The buyer must have already placed
    at least one bid on the item.

    Args:
        item_id: RESTful item ID of the auction (e.g. 'v1|123456789|0').
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.get(
        f"/buy/offer/v1_beta/bidding/{item_id}",
        extra_headers=headers,
    )


def place_proxy_bid(
    item_id: str,
    max_amount_value: str,
    max_amount_currency: str,
    marketplace_id: str = "EBAY_US",
    adult_only_consent: Optional[bool] = None,
) -> dict:
    """Place a proxy bid on an auction item on behalf of the buyer.

    eBay will automatically bid up to the max amount if outbid. The buyer
    agrees to purchase the item if they win the auction.

    Note: Requires a USER access token (authorization code grant).
    Use Browse API search with filter=buyingOptions:{AUCTION} to find auctions.

    Args:
        item_id: RESTful item ID of the auction (e.g. 'v1|123456789|0').
        max_amount_value: Maximum bid amount as a string (e.g. '150.00').
            Currency must match the seller's listing currency.
        max_amount_currency: ISO 4217 currency code (e.g. 'USD', 'GBP').
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
        adult_only_consent: Set to True if bidding on an adult-only item
            and the buyer has consented to the Terms of Use.
    """
    headers = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }

    body = {
        "maxAmount": {
            "value": max_amount_value,
            "currency": max_amount_currency,
        }
    }
    if adult_only_consent is not None:
        body["userConsent"] = {"adultOnlyItem": adult_only_consent}

    return client.post(
        f"/buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid",
        json=body,
        extra_headers=headers,
    )
