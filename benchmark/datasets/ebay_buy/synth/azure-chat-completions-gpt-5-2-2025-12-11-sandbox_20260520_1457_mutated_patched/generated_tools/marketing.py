from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


_MARKETING_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.marketing"


def get_merchandised_products(
    client: EbayClient,
    *,
    metric_name: str,
    category_id: str,
    max_results: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metric_name": metric_name, "category_id": category_id}
    if max_results is not None:
        params["limit"] = max_results
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter

    return client.request(
        "GET",
        "/buy/marketing/v1_beta/merchandised_product",
        params=params,
        scope=_MARKETING_SCOPE,
    )
