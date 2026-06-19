"""Orders domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import TikTokRequestOptions, tiktok_request


def get_order_list(
    *,
    order_status: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Search orders.

    API: POST /order/202309/orders/search
    """

    params: Dict[str, Any] = {
        "page_size": page_size,
        "sort_field": sort_field,
        "sort_order": sort_order,
    }
    if page_token is not None:
        params["page_token"] = page_token

    body: Dict[str, Any] = {}
    if order_status is not None:
        body["order_status"] = order_status

    return tiktok_request(
        "POST",
        "/order/202309/orders/search",
        params=params,
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def get_order_detail(
    *,
    order_id: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get order detail.

    API: GET /order/202309/orders/{order_id}

    Note: Some docs also mention newer versions; this uses 202309.
    """

    return tiktok_request(
        "GET",
        f"/order/202309/orders/{order_id}",
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
