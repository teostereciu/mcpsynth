"""Seller/Authorization domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import TikTokRequestOptions, tiktok_request


def get_authorized_shops() -> Dict[str, Any]:
    """Get shops authorized to the app.

    API: GET /authorization/202309/shops
    """

    return tiktok_request("GET", "/authorization/202309/shops", options=TikTokRequestOptions(use_shop_cipher=False))


def get_active_shops() -> Dict[str, Any]:
    """Get active shops.

    API: GET /authorization/202309/shops/active

    Note: Some apps use this to filter currently active shops.
    """

    return tiktok_request("GET", "/authorization/202309/shops/active", options=TikTokRequestOptions(use_shop_cipher=False))


def get_seller_permissions(shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """Get seller permissions/scopes for the shop.

    API: GET /authorization/202309/permissions
    """

    return tiktok_request(
        "GET",
        "/authorization/202309/permissions",
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
