"""Tools for eBay Buy Marketing API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json, tool_safe_call


_MARKETING_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.marketing"


def marketing_get_merchandised_products(
    *,
    metric_name: str,
    category_id: str,
    limit: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get merchandised products (e.g., BEST_SELLING).

    Wraps: GET /buy/marketing/v1_beta/merchandised_product

    Note: Sandbox requires category_id=9355 for mock data per docs.

    Note: Scenario tests request metric_name="TRENDING"; the docs mention BEST_SELLING.
    This tool passes through whatever metric_name you provide.
    """

    params: Dict[str, Any] = {"metric_name": metric_name, "category_id": category_id}
    if limit is not None:
        params["limit"] = int(limit)
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter

    return tool_safe_call(
        request_json,
        "GET",
        "/buy/marketing/v1_beta/merchandised_product",
        params=params,
        marketplace_id=marketplace_id,
        scope=_MARKETING_SCOPE,
    )
