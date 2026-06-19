from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_inventory_levels(
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: int = 250,
    updated_at_min: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Retrieve a list of inventory levels."""
    params: Dict[str, Any] = {"limit": limit}
    for k, v in {
        "location_ids": location_ids,
        "inventory_item_ids": inventory_item_ids,
        "updated_at_min": updated_at_min,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/inventory_levels.json", params=params)


@mcp.tool()
def set_inventory_level(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    available: int,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """Set the inventory level for an inventory item at a location."""
    body: Dict[str, Any] = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
        "available": int(available),
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", body=body)


@mcp.tool()
def adjust_inventory_level(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    available_adjustment: int,
) -> Dict[str, Any]:
    """Adjust the inventory level for an inventory item at a location."""
    body = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
        "available_adjustment": int(available_adjustment),
    }
    return client.request("POST", "/inventory_levels/adjust.json", body=body)


@mcp.tool()
def connect_inventory_item(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """Connect an inventory item to a location."""
    body: Dict[str, Any] = {"inventory_item_id": int(inventory_item_id), "location_id": int(location_id)}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return client.request("POST", "/inventory_levels/connect.json", body=body)


@mcp.tool()
def delete_inventory_level(inventory_item_id: Union[int, str], location_id: Union[int, str]) -> Dict[str, Any]:
    """Delete an inventory level from a location."""
    return client.request(
        "DELETE",
        "/inventory_levels.json",
        params={"inventory_item_id": int(inventory_item_id), "location_id": int(location_id)},
        unwrap=False,
    )
