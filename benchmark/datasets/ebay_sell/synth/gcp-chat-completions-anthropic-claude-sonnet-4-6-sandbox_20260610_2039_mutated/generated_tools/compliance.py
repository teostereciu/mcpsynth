"""eBay Sell Compliance API tools."""
from typing import Any, Optional
from .client import get_client


def get_listing_violations(
    violation_type: str,
    marketplace_id: str = "EBAY_US",
    filter: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve specific listing violations for a supported compliance type."""
    client = get_client()
    params = {"violation_type": violation_type}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/compliance/v1/listing_violation", params=params, headers=headers)


def get_listing_violations_summary(
    marketplace_id: str = "EBAY_US",
    violation_type: Optional[str] = None,
) -> dict:
    """Retrieve listing violation counts for a seller across compliance types."""
    client = get_client()
    params = {}
    if violation_type is not None:
        params["violation_type"] = violation_type
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/compliance/v1/listing_violation_summary", params=params, headers=headers)
