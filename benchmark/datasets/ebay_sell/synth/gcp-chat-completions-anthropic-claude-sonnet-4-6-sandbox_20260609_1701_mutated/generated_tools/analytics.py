"""eBay Sell Analytics API tools."""
from typing import Optional
from .client import get_client


def get_traffic_report(filter: str, dimension: Optional[str] = None,
                       metric: Optional[str] = None, sort_by: Optional[str] = None) -> dict:
    """Retrieve a traffic report detailing user traffic received by seller's listings."""
    client = get_client()
    params = {"filter": filter}
    if dimension:
        params["dimension"] = dimension
    if metric:
        params["metric"] = metric
    if sort_by:
        params["sort_by"] = sort_by
    return client.request("GET", "/sell/analytics/v1/traffic_report", params=params)


def find_seller_standards_profiles() -> dict:
    """Retrieve all standards profiles for the associated seller."""
    client = get_client()
    return client.request("GET", "/sell/analytics/v1/seller_standards_profile")


def get_seller_standards_profile(program: str, cycle: str) -> dict:
    """Retrieve a specific seller standards profile by program and cycle."""
    client = get_client()
    return client.request("GET", f"/sell/analytics/v1/seller_standards_profile/{program}/{cycle}")


def get_customer_service_metric(customer_service_metric_type: str, evaluation_type: str) -> dict:
    """Retrieve customer service metric data for a seller."""
    client = get_client()
    return client.request("GET", f"/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}")
