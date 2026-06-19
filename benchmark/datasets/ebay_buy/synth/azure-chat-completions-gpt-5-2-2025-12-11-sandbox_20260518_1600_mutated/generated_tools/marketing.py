from typing import Any, Dict, Optional

from .client import EbayClient


def get_merchandised_products(
    client: EbayClient,
    *,
    metric_name: str,
    category_id: str,
    limit: Optional[int] = None,
    facet_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metric_name": metric_name, "category_id": category_id}
    if limit is not None:
        params["limit"] = limit
    if facet_filter is not None:
        params["facet_filter"] = facet_filter

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.request("GET", "/buy/marketing/v1_beta/merchandised_product", params=params, headers=headers)
