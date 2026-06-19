"""Seller/authorization domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .client import TikTokShopClient


def get_authorized_shops(*, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /authorization/202309/shops

    Retrieves shops authorized to the app.

    Args:
        shop_cipher: Not required for this endpoint; accepted for convenience.
    """

    client = TikTokShopClient.from_env()
    return client.request("GET", "/authorization/202309/shops", params={"shop_cipher": shop_cipher}, use_shop_cipher=False)
