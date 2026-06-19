from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def orders_get_order_list(status: Optional[str] = None, page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get order list.

    API: GET /order/202309/orders
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if status:
        params["order_status"] = status
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/order/202309/orders", params=params)


@mcp.tool()
def orders_get_order_detail(order_id: str) -> Dict[str, Any]:
    """Get order detail.

    API: GET /order/202309/orders/{order_id}
    """

    return tiktok_request("GET", f"/order/202309/orders/{order_id}")


@mcp.tool()
def orders_split_order(order_id: str) -> Dict[str, Any]:
    """Split an order (if eligible).

    API: POST /order/202309/orders/split
    """

    body = {"order_id": order_id}
    return tiktok_request("POST", "/order/202309/orders/split", body=body)
