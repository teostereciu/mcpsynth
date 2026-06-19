"""
eBay Buy Marketing API tools.
Covers: merchandised products (best sellers).
"""

from __future__ import annotations
from typing import Optional
from .auth import get_auth_header, get_base_url


def get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    max_results: Optional[int] = None,
    aspect_filter: Optional[str] = None,
) -> dict:
    """
    Retrieve best-selling or top-rated products for a specific eBay category.
    Returns product details including ePID, title, ratings, and market prices.
    The returned ePID can be used with the Browse API search to find listings.

    Args:
        category_id: The eBay category ID to retrieve products for (required).
            Use category ID 9355 in Sandbox for mock data.
        metric_name: The metric to sort by. Currently only 'BEST_SELLING' is
            supported (default: 'BEST_SELLING').
        max_results: Maximum number of products to return (1-100, default 8).
        aspect_filter: Aspect name/value pairs to refine results.
            Format: 'AspectName:Value' (e.g. 'Brand:Canon').
    """
    import requests
    params = {
        "category_id": category_id,
        "metric_name": metric_name,
    }
    if max_results is not None:
        params["max_results"] = max_results
    if aspect_filter:
        params["aspect_filter"] = aspect_filter

    url = f"{get_base_url()}/buy/marketing/v1_beta/merchandised_product"
    headers = get_auth_header()
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
