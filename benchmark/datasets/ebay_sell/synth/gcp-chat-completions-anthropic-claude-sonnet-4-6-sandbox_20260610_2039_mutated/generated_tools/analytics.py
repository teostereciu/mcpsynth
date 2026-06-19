"""eBay Sell Analytics API tools."""
from typing import Any, Optional
from .client import get_client


def get_traffic_report(
    dimension: Optional[str] = None,
    filter: Optional[str] = None,
    metric: Optional[str] = None,
    sort_by: Optional[str] = None,
) -> dict:
    """Retrieve a traffic report detailing user traffic received by seller's listings."""
    client = get_client()
    params = {}
    if dimension is not None:
        params["dimension"] = dimension
    if filter is not None:
        params["filter"] = filter
    if metric is not None:
        params["metric"] = metric
    if sort_by is not None:
        params["sort_by"] = sort_by
    return client.request("GET", "/sell/analytics/v1/traffic_report", params=params)


def find_seller_standards_profiles() -> dict:
    """Retrieve all standards profiles for the associated seller."""
    client = get_client()
    return client.request("GET", "/sell/analytics/v1/seller_standards_profile")


def get_seller_standards_profile(program: str, cycle: str) -> dict:
    """Retrieve a single standards profile for the seller by program and cycle."""
    client = get_client()
    return client.request("GET", f"/sell/analytics/v1/seller_standards_profile/{program}/{cycle}")


def get_customer_service_metric(
    customer_service_metric_type: str,
    evaluation_type: str,
    evaluation_marketplace_id: str,
) -> dict:
    """Retrieve a seller's performance and rating for the customer service metric."""
    client = get_client()
    params = {"evaluation_marketplace_id": evaluation_marketplace_id}
    return client.request(
        "GET",
        f"/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}",
        params=params,
    )
