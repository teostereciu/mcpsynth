"""
eBay Buy Marketing API tools.
Covers: merchandised products (best sellers, trending items).
"""
from typing import Optional
from . import _client as client


def get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    limit: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> dict:
    """Retrieve best-selling or trending products for a specific eBay category.

    Returns product details including eBay product ID (EPID), title, ratings,
    reviews, and market price details. The EPID can be used in Browse API search.

    Note: In Sandbox, use category_id='9355' for mock data.

    Args:
        category_id: eBay category ID to retrieve products for (required).
            Use Browse API search with fieldgroups=ASPECT_REFINEMENTS to find
            the dominantCategoryId for a keyword.
        metric_name: Metric to filter by. Currently only 'BEST_SELLING' is supported.
        limit: Maximum number of products to return (default 8, max 100).
        aspect_filter: Aspect name/value pairs to refine results
            (e.g. 'Brand:Canon'). Use Browse API search with
            fieldgroups=ASPECT_REFINEMENTS to find valid aspect values.
    """
    params = {
        "category_id": category_id,
        "metric_name": metric_name,
    }
    if limit is not None:
        params["limit"] = limit
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter

    return client.get(
        "/buy/marketing/v1_beta/merchandised_product",
        params=params,
    )
