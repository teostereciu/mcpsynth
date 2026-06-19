"""Finance domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .client import TikTokShopClient


def get_payments(
    *,
    sort_field: str = "create_time",
    sort_order: Optional[str] = None,
    create_time_ge: Optional[int] = None,
    create_time_lt: Optional[int] = None,
    page_size: Optional[int] = None,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /finance/202309/payments"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "sort_field": sort_field,
        "sort_order": sort_order,
        "create_time_ge": create_time_ge,
        "create_time_lt": create_time_lt,
        "page_size": page_size,
        "page_token": page_token,
        "shop_cipher": shop_cipher,
    }
    return client.request(
        "GET",
        "/finance/202309/payments",
        params=params,
        use_shop_cipher=True,
    )
