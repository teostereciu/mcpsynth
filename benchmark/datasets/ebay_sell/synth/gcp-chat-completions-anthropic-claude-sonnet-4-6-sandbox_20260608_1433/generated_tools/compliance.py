"""eBay Sell Compliance API tools."""
from typing import Optional
from .client import get_client


def get_listing_violations(compliance_type: str, marketplace_id: str = "EBAY_US",
                            offset: Optional[str] = None, limit: Optional[str] = None,
                            filter: Optional[str] = None) -> dict:
    """Return specific listing violations for a supported compliance type."""
    client = get_client()
    params = {"compliance_type": compliance_type}
    if offset:
        params["offset"] = offset
    if limit:
        params["limit"] = limit
    if filter:
        params["filter"] = filter
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/compliance/v1/listing_violation", params=params, headers=headers)


def get_listing_violations_summary(compliance_type: Optional[str] = None,
                                    marketplace_id: str = "EBAY_US") -> dict:
    """Return listing violation counts for a seller."""
    client = get_client()
    params = {}
    if compliance_type:
        params["compliance_type"] = compliance_type
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/compliance/v1/listing_violation_summary", params=params, headers=headers)
