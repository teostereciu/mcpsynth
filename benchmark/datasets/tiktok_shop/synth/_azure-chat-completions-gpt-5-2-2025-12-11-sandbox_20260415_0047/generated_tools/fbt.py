from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def fbt_get_warehouse_list(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get FBT warehouse list.

    API: GET /fbt/202408/warehouses
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/fbt/202408/warehouses", params=params)


@mcp.tool()
def fbt_search_inventory(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Search FBT inventory.

    API: POST /fbt/202408/inventory/search
    """

    body: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        body["page_token"] = page_token
    return tiktok_request("POST", "/fbt/202408/inventory/search", body=body)
