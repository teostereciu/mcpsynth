"""Tools for eBay Buy Marketing API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayApiError, make_buy_api_request, tool_error


def marketing_get_merchandised_products(
    metric_name: str,
    category_id: str,
    *,
    limit: int = 8,
    aspect_filter: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    allow_sandbox_mock_category: bool = True,
) -> Dict[str, Any]:
    """Get merchandised products for a category and metric.

    Maps to GET /buy/marketing/v1_beta/merchandised_product

    Note: In Sandbox, eBay requires category_id=9355 and returns mock data.
    """

    # Sandbox note: eBay requires category_id=9355 and returns mock data.
    # To keep tools usable in tests that pass other category IDs, optionally
    # fall back to 9355 when running in SANDBOX.
    import os

    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    effective_category_id = category_id
    if allow_sandbox_mock_category and env == "SANDBOX":
        effective_category_id = "9355"

    params: Dict[str, Any] = {
        "metric_name": metric_name,
        "category_id": effective_category_id,
        "limit": limit,
    }
    if aspect_filter:
        params["aspect_filter"] = aspect_filter

    try:
        return make_buy_api_request(
            "GET",
            "/buy/marketing/v1_beta/merchandised_product",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))
