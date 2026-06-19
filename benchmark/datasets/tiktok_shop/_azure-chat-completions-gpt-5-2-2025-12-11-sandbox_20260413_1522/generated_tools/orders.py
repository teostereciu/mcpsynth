from __future__ import annotations

from typing import Any, Dict, Optional

from .http import safe_call


def search_orders(
    order_status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    create_time_ge: Optional[int] = None,
    create_time_lt: Optional[int] = None,
    update_time_ge: Optional[int] = None,
    update_time_lt: Optional[int] = None,
    shipping_type: Optional[str] = None,
    buyer_user_id: Optional[str] = None,
    is_buyer_request_cancel: Optional[bool] = None,
    warehouse_ids: Optional[list[str]] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /order/202309/orders/search"""
    params: Dict[str, Any] = {
        "page_size": page_size,
        "page_token": page_token,
        "sort_field": sort_field,
        "sort_order": sort_order,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher

    body: Dict[str, Any] = {
        "order_status": order_status,
        "create_time_ge": create_time_ge,
        "create_time_lt": create_time_lt,
        "update_time_ge": update_time_ge,
        "update_time_lt": update_time_lt,
        "shipping_type": shipping_type,
        "buyer_user_id": buyer_user_id,
        "is_buyer_request_cancel": is_buyer_request_cancel,
        "warehouse_ids": warehouse_ids,
    }
    return safe_call("POST", "/order/202309/orders/search", params=params, body=body)


def get_order_detail(order_id: str, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /order/202309/orders/{order_id}"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("GET", f"/order/202309/orders/{order_id}", params=params)
