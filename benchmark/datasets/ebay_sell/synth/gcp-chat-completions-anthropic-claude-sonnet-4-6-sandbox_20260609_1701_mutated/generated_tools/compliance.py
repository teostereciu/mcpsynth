"""eBay Sell Compliance API tools."""
from typing import Optional
from .client import get_client


def get_listing_violations(violation_type: str, marketplace_id: str = "EBAY_US",
                            offset: Optional[str] = None, limit: Optional[str] = None,
                            filter: Optional[str] = None) -> dict:
    """Retrieve specific listing violations for a supported compliance type."""
    client = get_client()
    params = {"violation_type": violation_type}
    if offset:
        params["offset"] = offset
    if limit:
        params["limit"] = limit
    if filter:
        params["filter"] = filter
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/compliance/v1/listing_violation", params=params, extra_headers=headers)


def get_listing_violations_summary(violation_type: Optional[str] = None,
                                    marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve listing violation counts for a seller, optionally filtered by compliance type."""
    client = get_client()
    params = {}
    if violation_type:
        params["violation_type"] = violation_type
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/compliance/v1/listing_violation_summary", params=params, extra_headers=headers)
