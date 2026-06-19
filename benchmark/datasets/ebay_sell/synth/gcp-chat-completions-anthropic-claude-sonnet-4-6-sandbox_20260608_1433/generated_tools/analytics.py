"""eBay Sell Analytics API tools."""
from typing import Optional
from .client import get_client


def get_traffic_report(dimension: Optional[str] = None, filter: Optional[str] = None,
                       metric: Optional[str] = None, sort: Optional[str] = None) -> dict:
    """Return a report detailing user traffic received by a seller's listings."""
    client = get_client()
    params = {}
    if dimension:
        params["dimension"] = dimension
    if filter:
        params["filter"] = filter
    if metric:
        params["metric"] = metric
    if sort:
        params["sort"] = sort
    return client.request("GET", "/sell/analytics/v1/traffic_report", params=params)


def find_seller_standards_profiles() -> dict:
    """Retrieve all standards profiles for the associated seller."""
    client = get_client()
    return client.request("GET", "/sell/analytics/v1/seller_standards_profile")


def get_seller_standards_profile(program: str, cycle: str) -> dict:
    """Retrieve a single standards profile for a seller by program and cycle."""
    client = get_client()
    return client.request("GET", f"/sell/analytics/v1/seller_standards_profile/{program}/{cycle}")


def get_customer_service_metric(customer_service_metric_type: str, evaluation_type: str,
                                 evaluation_marketplace_id: str) -> dict:
    """Retrieve a seller's performance rating for the customer service metric."""
    client = get_client()
    params = {"evaluation_marketplace_id": evaluation_marketplace_id}
    return client.request("GET",
                          f"/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}",
                          params=params)
