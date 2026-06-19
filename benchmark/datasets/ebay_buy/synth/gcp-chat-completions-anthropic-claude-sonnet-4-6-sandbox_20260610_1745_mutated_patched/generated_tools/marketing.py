"""
eBay Buy Marketing API tools.
Covers: merchandised products (best sellers, trending items).
"""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .auth import get_auth_headers, get_base_url


def register_marketing_tools(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_merchandised_products(
        category_id: str,
        metric_name: str = "BEST_SELLING",
        max_results: Optional[int] = None,
        aspect_filter: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve best-selling or trending products for a category.
        Returns product details including eBay product ID (EPID), title,
        ratings, reviews, and market price details.

        Args:
            category_id: eBay category ID to retrieve products for
                         (e.g. '31388' for Cameras, '9355' for Sandbox testing).
            metric_name: Metric to filter by. Currently only 'BEST_SELLING' is supported.
            max_results: Max products to return (default 8, max 100).
            aspect_filter: Aspect name/value pair to refine results
                           (e.g. 'Brand:Canon').
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {
            "category_id": category_id,
            "metric_name": metric_name,
        }
        if max_results is not None:
            params["limit"] = max_results
        if aspect_filter:
            params["aspect_filter"] = aspect_filter

        url = f"{get_base_url()}/buy/marketing/v1_beta/merchandised_product"
        try:
            resp = requests.get(
                url,
                params=params,
                headers={**get_auth_headers(), "X-EBAY-C-MARKETPLACE-ID": marketplace_id},
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
