from typing import Any, Dict, Optional

from .client import EbayApiClient


def get_merchandised_products(
    marketplace_id: str,
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/marketing/v1_beta/merchandised_product"""
    client = EbayApiClient()
    params: Dict[str, Any] = {"category_id": category_id, "metric_name": metric_name}
    if limit is not None:
        params["limit"] = limit
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/buy/marketing/v1_beta/merchandised_product", params=params, headers=headers)
