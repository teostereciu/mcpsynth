from typing import Any, Dict, Optional

from .client import EbayClient


def get_merchandised_products(
    client: EbayClient,
    *,
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/marketing/v1_beta/merchandised_product"""
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    params: Dict[str, Any] = {"category_id": category_id, "metric_name": metric_name}
    if limit is not None:
        params["limit"] = limit
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter

    return client.request("GET", "/buy/marketing/v1_beta/merchandised_product", params=params, headers=headers)
