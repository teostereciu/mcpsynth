"""
eBay Sell Analytics API tools.
Covers: seller standards, traffic reports, listing quality, and performance metrics.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-analytics")

# ---------------------------------------------------------------------------
# Seller Standards
# ---------------------------------------------------------------------------

@mcp.tool()
def get_seller_standards_profiles() -> dict:
    """
    Retrieve all seller standards profiles (Top Rated, Above Standard, etc.)
    for the seller across all programs.
    """
    return ebay_request("GET", "/sell/analytics/v1/seller_standards_profile")


@mcp.tool()
def get_seller_standards_profile(program: str, cycle: str) -> dict:
    """
    Retrieve a specific seller standards profile.

    Args:
        program: The standards program, e.g. 'PROGRAM_US', 'PROGRAM_UK'.
        cycle: The evaluation cycle, e.g. 'CURRENT', 'PROJECTED'.
    """
    return ebay_request(
        "GET",
        f"/sell/analytics/v1/seller_standards_profile/{program}/{cycle}",
    )


# ---------------------------------------------------------------------------
# Traffic Reports
# ---------------------------------------------------------------------------

@mcp.tool()
def get_traffic_report(
    dimension: str,
    metric: str,
    filter: str | None = None,
    sort: str | None = None,
) -> dict:
    """
    Retrieve a traffic report for listings.

    Args:
        dimension: The dimension to group by, e.g. 'DAY', 'LISTING'.
        metric: Comma-separated metrics to include, e.g.
                'CLICK_THROUGH_RATE,LISTING_IMPRESSION_TOTAL,TRANSACTION'.
        filter: Filter string, e.g. 'date:[2024-01-01..2024-01-31],
                marketplace_ids:{EBAY_US}' (optional).
        sort: Sort field and direction, e.g. 'LISTING_IMPRESSION_TOTAL' (optional).
    """
    params: dict = {"dimension": dimension, "metric": metric}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return ebay_request("GET", "/sell/analytics/v1/traffic_report", params=params)


# ---------------------------------------------------------------------------
# Finding / Listing Quality
# ---------------------------------------------------------------------------

@mcp.tool()
def get_customer_service_metric(
    customer_service_metric_type: str,
    evaluation_marketplace_id: str,
    evaluation_type: str,
) -> dict:
    """
    Retrieve customer service metrics for the seller.

    Args:
        customer_service_metric_type: Metric type, e.g.
            'ITEM_NOT_AS_DESCRIBED', 'ITEM_NOT_RECEIVED'.
        evaluation_marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        evaluation_type: Evaluation period type, e.g. 'CURRENT', 'PROJECTED'.
    """
    return ebay_request(
        "GET",
        f"/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_marketplace_id}/{evaluation_type}",
    )
