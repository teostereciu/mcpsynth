"""eBay Sell Recommendation API tools."""
from typing import Any, Optional
from .client import get_client


def find_listing_recommendations(
    body: Optional[dict] = None,
    marketplace_id: str = "EBAY_US",
    filter: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Find listing recommendations for Promoted Listings ad campaigns."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/recommendation/v1/find", json=body or {}, params=params, headers=headers)
