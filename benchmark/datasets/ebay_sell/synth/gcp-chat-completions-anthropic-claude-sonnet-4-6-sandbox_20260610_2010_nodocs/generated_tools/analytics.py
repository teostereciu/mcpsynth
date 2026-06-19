"""
eBay Sell Analytics API tools.
Covers: seller standards, traffic reports, listing quality, customer service metrics.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get

mcp = FastMCP("ebay-analytics")


# ── Seller Standards ─────────────────────────────────────────────────────────

@mcp.tool()
def get_seller_standards_profiles() -> dict:
    """
    Retrieve all seller standards profiles (Top Rated, Above Standard, etc.)
    for the authenticated seller.
    """
    return api_get("/sell/analytics/v1/seller_standards_profile")


@mcp.tool()
def get_seller_standards_profile(program: str, cycle: str) -> dict:
    """
    Retrieve a specific seller standards profile.

    Args:
        program: Program type (e.g. PROGRAM_DE, PROGRAM_GLOBAL, PROGRAM_US, PROGRAM_UK).
        cycle: Cycle type (e.g. CURRENT, PROJECTED).
    """
    return api_get(f"/sell/analytics/v1/seller_standards_profile/{program}/{cycle}")


# ── Traffic Reports ──────────────────────────────────────────────────────────

@mcp.tool()
def get_traffic_report(dimension: str,
                        metric: str,
                        filter: str | None = None,
                        sort: str | None = None) -> dict:
    """
    Retrieve a traffic report for listings.

    Args:
        dimension: Dimension to group by (e.g. DAY, LISTING).
        metric: Metric to report (e.g. CLICK_THROUGH_RATE, LISTING_IMPRESSION_TOTAL).
        filter: Filter string (e.g. 'marketplace_ids:{EBAY_US},date_range:[2024-01-01..]').
        sort: Sort field.
    """
    params: dict = {"dimension": dimension, "metric": metric}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/analytics/v1/traffic_report", params=params)


# ── Customer Service Metrics ─────────────────────────────────────────────────

@mcp.tool()
def get_customer_service_metric(customer_service_metric_type: str,
                                 evaluation_marketplace_id: str,
                                 evaluation_type: str) -> dict:
    """
    Retrieve customer service metrics for the seller.

    Args:
        customer_service_metric_type: Metric type (e.g. ITEM_NOT_AS_DESCRIBED, ITEM_NOT_RECEIVED).
        evaluation_marketplace_id: Marketplace ID for evaluation.
        evaluation_type: Evaluation period (e.g. CURRENT, PROJECTED).
    """
    return api_get(f"/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_marketplace_id}/{evaluation_type}")


# ── Listing Quality ──────────────────────────────────────────────────────────

@mcp.tool()
def find_listing_violations(compliance_type: str | None = None,
                             marketplace_id: str | None = None,
                             limit: int = 100,
                             offset: int = 0) -> dict:
    """
    Find listing policy compliance violations.

    Args:
        compliance_type: Type of compliance check (e.g. PRODUCT_ADOPTION, OUTSIDE_EBAY_BUYING_AND_SELLING).
        marketplace_id: eBay marketplace ID.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if compliance_type:
        params["compliance_type"] = compliance_type
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return api_get("/sell/compliance/v1/listing_violation", params=params)


@mcp.tool()
def get_listing_violation_summary(marketplace_id: str | None = None,
                                   compliance_type: str | None = None) -> dict:
    """
    Retrieve a summary count of listing violations.

    Args:
        marketplace_id: eBay marketplace ID.
        compliance_type: Compliance type to filter.
    """
    params: dict = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    if compliance_type:
        params["compliance_type"] = compliance_type
    return api_get("/sell/compliance/v1/listing_violation_summary", params=params or None)


@mcp.tool()
def suppress_listing_violation(listing_id: str, compliance_type: str) -> dict:
    """
    Suppress a listing violation to remove it from the violations list.

    Args:
        listing_id: The listing ID with the violation.
        compliance_type: The compliance type of the violation.
    """
    from .auth import api_post
    return api_post("/sell/compliance/v1/suppress_listing_violation",
                    body={"listingId": listing_id, "complianceType": compliance_type})
