"""Tools for eBay Buy Marketing API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


MARKETING_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.marketing"


def get_merchandised_products(
    *,
    metric_name: str = "BEST_SELLING",
    category_id: str,
    limit: int = 8,
    aspect_filter: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    allow_sandbox_mock_category: bool = True,
) -> Dict[str, Any]:
    """Get merchandised products for a category.

    Wraps: GET /buy/marketing/v1_beta/merchandised_product

    Note: In Sandbox, docs indicate category_id must be 9355 for mock data.
    """

    # Docs: in Sandbox, category_id must be 9355 and response is mock data.
    # Scenarios use 58058; to keep tools usable in sandbox tests, optionally
    # substitute 9355 when running in SANDBOX.
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

    return request_json(
        "GET",
        "/buy/marketing/v1_beta/merchandised_product",
        params=params,
        marketplace_id=marketplace_id,
        scope=MARKETING_SCOPE,
    )
