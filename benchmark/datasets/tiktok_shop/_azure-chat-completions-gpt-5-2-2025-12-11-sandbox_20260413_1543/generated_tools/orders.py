"""Orders domain tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .client import TikTokShopClient


def get_order_detail(*, order_id: str, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /order/202507/orders

    Wrapper for single order id.
    """

    client = TikTokShopClient.from_env()
    return client.request(
        "GET",
        "/order/202507/orders",
        params={"ids": order_id, "shop_cipher": shop_cipher},
        use_shop_cipher=True,
    )


def get_order_list(
    *,
    page_size: int = 20,
    page_token: Optional[str] = None,
    sort_field: Optional[str] = None,
    sort_order: Optional[str] = None,
    order_status: Optional[str] = None,
    create_time_ge: Optional[int] = None,
    create_time_lt: Optional[int] = None,
    update_time_ge: Optional[int] = None,
    update_time_lt: Optional[int] = None,
    shipping_type: Optional[str] = None,
    buyer_user_id: Optional[str] = None,
    is_buyer_request_cancel: Optional[bool] = None,
    warehouse_ids: Optional[List[str]] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /order/202309/orders/search"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "page_size": page_size,
        "page_token": page_token,
        "sort_field": sort_field,
        "sort_order": sort_order,
        "shop_cipher": shop_cipher,
    }
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
    body = {k: v for k, v in body.items() if v is not None}

    return client.request(
        "POST",
        "/order/202309/orders/search",
        params=params,
        body=body,
        use_shop_cipher=True,
    )
