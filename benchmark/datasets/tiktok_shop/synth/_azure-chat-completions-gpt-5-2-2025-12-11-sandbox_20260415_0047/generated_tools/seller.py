from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def seller_get_authorized_shops() -> Dict[str, Any]:
    """Get shops authorized to the app.

    API: GET /authorization/202309/shops
    """

    return tiktok_request("GET", "/authorization/202309/shops", use_shop_cipher=False)


@mcp.tool()
def seller_get_active_shops(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get active shops.

    API: GET /seller/202309/shops (see docs api_get-active-shops-202309)
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/seller/202309/shops", params=params)


@mcp.tool()
def seller_get_permissions() -> Dict[str, Any]:
    """Get seller permissions for the app.

    API: GET /seller/202309/permissions
    """

    return tiktok_request("GET", "/seller/202309/permissions")
