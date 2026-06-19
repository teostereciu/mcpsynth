from __future__ import annotations

from typing import Any, Dict, Optional

from .http import safe_call


def get_authorized_shops() -> Dict[str, Any]:
    """GET /authorization/202309/shops

    Retrieves shops authorized to the app. Does not require shop_cipher.
    """
    return safe_call("GET", "/authorization/202309/shops", use_shop_cipher=False)


def get_active_shops() -> Dict[str, Any]:
    """GET /authorization/202309/shops/active

    Some integrations use this to list active shops; if unsupported, API returns error.
    """
    return safe_call("GET", "/authorization/202309/shops/active", use_shop_cipher=False)


def get_seller_permissions(shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /seller/202309/permissions

    Returns seller permissions/features for the shop.
    """
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("GET", "/seller/202309/permissions", params=params)
