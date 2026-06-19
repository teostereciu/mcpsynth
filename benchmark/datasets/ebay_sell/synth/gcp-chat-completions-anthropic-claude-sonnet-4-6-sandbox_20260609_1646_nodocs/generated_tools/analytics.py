"""
eBay Sell Analytics API tools.
Covers: seller standards profiles, traffic reports, customer service metrics.
"""

from typing import Optional
from auth import api_get


# ---------------------------------------------------------------------------
# Seller Standards Profiles
# ---------------------------------------------------------------------------

def get_seller_standards_profiles() -> dict:
    """Get all seller standards profiles (Top Rated, Above Standard, etc.)."""
    return api_get("/sell/analytics/v1/seller_standards_profile")


def get_seller_standards_profile(program: str, cycle: str) -> dict:
    """
    Get a specific seller standards profile.

    program: "PROGRAM_DA" (eBay Defect Rate) or "PROGRAM_CSP" (Customer Service)
    cycle: "CURRENT" or "PROJECTED"
    """
    return api_get(f"/sell/analytics/v1/seller_standards_profile/{program}/{cycle}")


# ---------------------------------------------------------------------------
# Traffic Reports
# ---------------------------------------------------------------------------

def get_traffic_report(
    dimension: str,
    metric: str,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
) -> dict:
    """
    Get a traffic report for listings.

    dimension: e.g. "DAY", "LISTING"
    metric: e.g. "CLICK_THROUGH_RATE,IMPRESSION_COUNT,LISTING_IMPRESSION_STORE,
                   LISTING_IMPRESSION_TOTAL,LISTING_VIEWS_SOURCE_DIRECT,
                   LISTING_VIEWS_SOURCE_OFF_EBAY,LISTING_VIEWS_SOURCE_OTHER_EBAY,
                   LISTING_VIEWS_SOURCE_SEARCH_RESULTS_PAGE,LISTING_VIEWS_TOTAL,
                   SALES_CONVERSION_RATE,TRANSACTION"
    filter: e.g. "date:[20240101..20240131],listingIds:{123456789}"
    sort: e.g. "CLICK_THROUGH_RATE"
    """
    params: dict = {"dimension": dimension, "metric": metric}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/analytics/v1/traffic_report", params=params)


# ---------------------------------------------------------------------------
# Customer Service Metric
# ---------------------------------------------------------------------------

def get_customer_service_metric(
    customer_service_metric_type: str,
    evaluation_marketplace_id: str,
    evaluation_type: str,
) -> dict:
    """
    Get customer service metric data.

    customer_service_metric_type: e.g. "ITEM_NOT_AS_DESCRIBED", "ITEM_NOT_RECEIVED"
    evaluation_marketplace_id: e.g. "EBAY_US"
    evaluation_type: "CURRENT" or "PROJECTED"
    """
    return api_get(
        "/sell/analytics/v1/customer_service_metric",
        params={
            "customer_service_metric_type": customer_service_metric_type,
            "evaluation_marketplace_id": evaluation_marketplace_id,
            "evaluation_type": evaluation_type,
        },
    )


# ---------------------------------------------------------------------------
# Finding Items (Listing Performance)
# ---------------------------------------------------------------------------

def get_listing_performance_report(
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get listing performance data.

    filter: e.g. "listingIds:{123456789|987654321}"
    sort: e.g. "TRANSACTION"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/analytics/v1/listing_performance_report", params=params)
