"""eBay Sell Recommendation API tools."""
from typing import Optional
from .client import get_client


def find_listing_recommendations(body: Optional[dict] = None, marketplace_id: str = "EBAY_US",
                                   filter: Optional[str] = None, limit: Optional[str] = None,
                                   offset: Optional[str] = None) -> dict:
    """Return listing recommendations (e.g., AD type) to help configure Promoted Listings campaigns."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/recommendation/v1/find", json=body or {}, params=params, extra_headers=headers)
