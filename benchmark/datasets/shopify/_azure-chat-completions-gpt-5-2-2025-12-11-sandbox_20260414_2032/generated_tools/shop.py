from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def get_shop_info(fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve the shop's configuration.

    Args:
        fields: Optional comma-separated list of fields.

    Returns:
        Shop object dict or {"error": ...}.
    """

    params = {"fields": fields} if fields else None
    data = shopify_request("GET", "/shop.json", params=params)
    if "error" in data:
        return data
    shop = unwrap_envelope(data)
    return shop
