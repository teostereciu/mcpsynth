"""
eBay Sell Compliance API tools.
Covers: listing violations, product compliance, seller compliance summary.
"""

from typing import Optional
from auth import api_get, api_post


# ---------------------------------------------------------------------------
# Listing Violations
# ---------------------------------------------------------------------------

def get_listing_violations(
    compliance_type: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    offset: int = 0,
    limit: int = 100,
) -> dict:
    """
    Get listing violations for the seller.

    compliance_type: e.g. "PRODUCT_ADOPTION", "OUTSIDE_EBAY_BUYING_AND_SELLING",
                     "KEYWORD_SPAMMING", "HTTPS", "RETURN_POLICY", "ITEM_SPECIFICS",
                     "LISTING_STRUCTURE_POLICY", "REGULATED_SUBSTANCE",
                     "PRODUCT_SAFETY", "AUTHENTICITY_VERIFICATION"
    marketplace_id: e.g. "EBAY_US"
    """
    params: dict = {"offset": offset, "limit": limit}
    if compliance_type:
        params["compliance_type"] = compliance_type
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return api_get("/sell/compliance/v1/listing_violation", params=params)


def get_listing_violation_summary(
    marketplace_id: Optional[str] = None,
    compliance_type: Optional[str] = None,
) -> dict:
    """Get a summary count of listing violations by compliance type."""
    params: dict = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    if compliance_type:
        params["compliance_type"] = compliance_type
    return api_get("/sell/compliance/v1/listing_violation_summary", params=params or None)


def suppress_listing_violation(body: dict) -> dict:
    """
    Suppress a listing violation (mark as acknowledged).

    body fields:
      listingId: str
      complianceType: str
    """
    return api_post("/sell/compliance/v1/suppress_listing_violation", body=body)
