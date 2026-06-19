"""
eBay Sell Compliance API tools.
Covers: listing violations, seller compliance summaries.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-compliance")

# ---------------------------------------------------------------------------
# Listing Violations
# ---------------------------------------------------------------------------

@mcp.tool()
def get_listing_violations(
    compliance_type: str | None = None,
    marketplace_id: str | None = None,
    listing_ids: str | None = None,
    offset: int = 0,
    limit: int = 100,
) -> dict:
    """
    Retrieve listing violations for the seller.

    Args:
        compliance_type: Filter by compliance type, e.g.
            'PRODUCT_ADOPTION', 'OUTSIDE_EBAY_BUYING_AND_SELLING',
            'KEYWORD_SPAMMING', 'ITEM_SPECIFICS_ADOPTION' (optional).
        marketplace_id: Filter by marketplace ID, e.g. 'EBAY_US' (optional).
        listing_ids: Comma-separated listing IDs to check (optional).
        offset: Pagination offset (default 0).
        limit: Number of violations to return (default 100, max 200).
    """
    params: dict = {"offset": offset, "limit": limit}
    if compliance_type:
        params["compliance_type"] = compliance_type
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    if listing_ids:
        params["listing_ids"] = listing_ids
    return ebay_request(
        "GET",
        "/sell/compliance/v1/listing_violation",
        params=params,
    )


@mcp.tool()
def get_listing_violations_summary(
    marketplace_id: str | None = None,
    compliance_type: str | None = None,
) -> dict:
    """
    Retrieve a summary count of listing violations by compliance type.

    Args:
        marketplace_id: Filter by marketplace ID, e.g. 'EBAY_US' (optional).
        compliance_type: Filter by compliance type (optional).
    """
    params: dict = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    if compliance_type:
        params["compliance_type"] = compliance_type
    return ebay_request(
        "GET",
        "/sell/compliance/v1/listing_violation_summary",
        params=params or None,
    )


@mcp.tool()
def suppress_listing_violation(
    compliance_type: str,
    listing_id: str,
    reason_code: str | None = None,
) -> dict:
    """
    Suppress a listing violation to remove it from the violations list.

    Args:
        compliance_type: The compliance type of the violation to suppress.
        listing_id: The listing ID with the violation.
        reason_code: Optional reason code for suppression.
    """
    body: dict = {
        "complianceType": compliance_type,
        "listingId": listing_id,
    }
    if reason_code:
        body["reasonCode"] = reason_code
    return ebay_request(
        "POST",
        "/sell/compliance/v1/suppress_listing_violation",
        json=body,
    )
