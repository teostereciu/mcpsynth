from typing import Any, Dict, Optional

from .http_client import EbayClient


client = EbayClient()


def marketing_get_merchandised_products(
    *,
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: Optional[int] = 8,
    aspect_filter: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "category_id": category_id,
        "metric_name": metric_name,
    }
    if limit is not None:
        params["limit"] = int(limit)
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter

    return client.request("GET", "/buy/marketing/v1_beta/merchandised_product", params=params)
