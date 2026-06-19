from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def list_inventory_levels(
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: int = 50,
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List inventory levels.

    Args:
        location_ids: Comma-separated location IDs.
        inventory_item_ids: Comma-separated inventory item IDs.
        limit: Max results.
    """

    params: Dict[str, Any] = {"limit": limit}
    if location_ids:
        params["location_ids"] = location_ids
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids

    data = shopify_request("GET", "/inventory_levels.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def set_inventory_level(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    available: int,
    disconnect_if_necessary: Optional[bool] = None,
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Set inventory level for an item at a location."""

    body: Dict[str, Any] = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
        "available": int(available),
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = bool(disconnect_if_necessary)

    data = shopify_request("POST", "/inventory_levels/set.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def adjust_inventory_level(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    available_adjustment: int,
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Adjust inventory level for an item at a location."""

    body = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
        "available_adjustment": int(available_adjustment),
    }
    data = shopify_request("POST", "/inventory_levels/adjust.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def connect_inventory_item(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    relocate_if_necessary: Optional[bool] = None,
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Connect an inventory item to a location."""

    body: Dict[str, Any] = {"inventory_item_id": int(inventory_item_id), "location_id": int(location_id)}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = bool(relocate_if_necessary)

    data = shopify_request("POST", "/inventory_levels/connect.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def delete_inventory_level(inventory_item_id: Union[int, str], location_id: Union[int, str]) -> Dict[str, Any]:
    """Delete an inventory level from a location."""

    params = {"inventory_item_id": int(inventory_item_id), "location_id": int(location_id)}
    data = shopify_request("DELETE", "/inventory_levels.json", params=params)
    if "error" in data:
        return data
    return {"ok": True}
