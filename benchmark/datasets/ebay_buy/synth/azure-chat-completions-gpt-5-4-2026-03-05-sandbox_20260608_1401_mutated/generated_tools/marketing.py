from typing import Any, Dict, Optional

from .common import client


def get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    max_results: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/buy/marketing/v1_beta/merchandised_product",
        params={
            "category_id": category_id,
            "metric_name": metric_name,
            "max_results": max_results,
            "aspect_filter": aspect_filter,
        },
    )
