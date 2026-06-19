from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/analytics/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.analytics"


def register(mcp):
    @mcp.tool()
    def analytics_get_traffic_report(
        *,
        dimension: Optional[str] = None,
        metric: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GET /traffic_report - Get traffic report."""
        params: Dict[str, Any] = {}
        if dimension is not None:
            params["dimension"] = dimension
        if metric is not None:
            params["metric"] = metric
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        return request_json("GET", API_ROOT, "/traffic_report", scope=SCOPE, params=params or None)

    @mcp.tool()
    def analytics_find_seller_standards_profiles(*, program: Optional[str] = None) -> Dict[str, Any]:
        """GET /seller_standards_profile - Find seller standards profiles."""
        params = {"program": program} if program else None
        return request_json("GET", API_ROOT, "/seller_standards_profile", scope=SCOPE, params=params)

    @mcp.tool()
    def analytics_get_seller_standards_profile(program: str, cycle: str) -> Dict[str, Any]:
        """GET /seller_standards_profile/{program}/{cycle} - Get seller standards profile."""
        return request_json("GET", API_ROOT, f"/seller_standards_profile/{program}/{cycle}", scope=SCOPE)

    @mcp.tool()
    def analytics_get_customer_service_metric(customer_service_metric_type: str, evaluation_type: str) -> Dict[str, Any]:
        """GET /customer_service_metric/{type}/{evaluation_type} - Get customer service metric."""
        return request_json(
            "GET",
            API_ROOT,
            f"/customer_service_metric/{customer_service_metric_type}/{evaluation_type}",
            scope=SCOPE,
        )
