from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def fulfillment_get_warehouse_list(page_size: int = 50, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get warehouse list.

    API: GET /logistics/202309/warehouses
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/logistics/202309/warehouses", params=params)


@mcp.tool()
def fulfillment_search_packages(status: Optional[str] = None, page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Search packages.

    API: GET /fulfillment/202309/packages
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if status:
        params["package_status"] = status
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/fulfillment/202309/packages", params=params)


@mcp.tool()
def fulfillment_ship_package(package_id: str, handover_method: str = "DROP_OFF") -> Dict[str, Any]:
    """Ship a package using TikTok logistics.

    API: POST /fulfillment/202309/packages/ship
    """

    body = {"package_id": package_id, "handover_method": handover_method}
    return tiktok_request("POST", "/fulfillment/202309/packages/ship", body=body)


@mcp.tool()
def fulfillment_get_package_shipping_document(package_id: str, document_type: str = "SHIPPING_LABEL") -> Dict[str, Any]:
    """Get package shipping document.

    API: GET /fulfillment/202309/packages/shipping_document
    """

    params = {"package_id": package_id, "document_type": document_type}
    return tiktok_request("GET", "/fulfillment/202309/packages/shipping_document", params=params)
