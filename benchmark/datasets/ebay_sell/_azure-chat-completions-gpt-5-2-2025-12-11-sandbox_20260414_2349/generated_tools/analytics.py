from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_ANALYTICS
from . import mcp

API = "/sell/analytics/v1"


@mcp.tool()
def analytics_get_traffic_report(
    *,
    metric: str,
    filter: str,
    dimension: Optional[str] = None,
    sort: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /traffic_report"""
    params: Dict[str, Any] = {"metric": metric, "filter": filter}
    if dimension is not None:
        params["dimension"] = dimension
    if sort is not None:
        params["sort"] = sort
    return _shared.client.request(
        "GET",
        API,
        "/traffic_report",
        scope=SCOPE_ANALYTICS,
        marketplace_id=marketplace_id,
        params=params,
    )


@mcp.tool()
def analytics_get_customer_service_metric(
    *,
    filter: str,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /customer_service_metric"""
    return _shared.client.request(
        "GET",
        API,
        "/customer_service_metric",
        scope=SCOPE_ANALYTICS,
        marketplace_id=marketplace_id,
        params={"filter": filter},
    )


@mcp.tool()
def analytics_find_seller_standards_profiles(
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /seller_standards_profile"""
    return _shared.client.request(
        "GET",
        API,
        "/seller_standards_profile",
        scope=SCOPE_ANALYTICS,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def analytics_get_seller_standards_profile(
    program: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /seller_standards_profile/{program}"""
    return _shared.client.request(
        "GET",
        API,
        f"/seller_standards_profile/{program}",
        scope=SCOPE_ANALYTICS,
        marketplace_id=marketplace_id,
    )
