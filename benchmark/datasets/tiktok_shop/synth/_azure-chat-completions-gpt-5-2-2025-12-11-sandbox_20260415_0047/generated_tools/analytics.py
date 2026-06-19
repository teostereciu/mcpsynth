from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import tiktok_request


@mcp.tool()
def analytics_get_shop_performance(start_time: int, end_time: int, granularity: str = "DAY") -> Dict[str, Any]:
    """Get shop performance.

    API: GET /analytics/202509/shop/performance
    """

    params = {"start_time": start_time, "end_time": end_time, "granularity": granularity}
    return tiktok_request("GET", "/analytics/202509/shop/performance", params=params)


@mcp.tool()
def analytics_get_product_performance_list(start_time: int, end_time: int, page_size: int = 20) -> Dict[str, Any]:
    """Get shop product performance list.

    API: GET /analytics/202509/shop/products/performance
    """

    params = {"start_time": start_time, "end_time": end_time, "page_size": page_size}
    return tiktok_request("GET", "/analytics/202509/shop/products/performance", params=params)
