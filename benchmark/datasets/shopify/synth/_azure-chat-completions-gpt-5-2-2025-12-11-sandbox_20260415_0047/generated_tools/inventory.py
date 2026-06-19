from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


# Locations

@mcp.tool()
def list_locations(limit: int = 50) -> List[Dict[str, Any]]:
    """List locations (GET /locations.json)."""
    client = ShopifyClient()
    data = client.request("GET", "/locations.json", params={"limit": limit})
    return unwrap_envelope(data)


@mcp.tool()
def get_location(location_id: Union[int, str]) -> Dict[str, Any]:
    """Get a location (GET /locations/{location_id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/locations/{location_id}.json")
    return unwrap_envelope(data)


@mcp.tool()
def list_location_inventory_levels(location_id: Union[int, str]) -> List[Dict[str, Any]]:
    """List inventory levels for a location (GET /locations/{location_id}/inventory_levels.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/locations/{location_id}/inventory_levels.json")
    return unwrap_envelope(data)


# Inventory levels

@mcp.tool()
def list_inventory_levels(
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: int = 50,
) -> List[Dict[str, Any]]:
    """List inventory levels (GET /inventory_levels.json)."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if location_ids:
        params["location_ids"] = location_ids
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    data = client.request("GET", "/inventory_levels.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def adjust_inventory_level(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    available_adjustment: int,
) -> Dict[str, Any]:
    """Adjust inventory level (POST /inventory_levels/adjust.json)."""
    client = ShopifyClient()
    body = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
        "available_adjustment": int(available_adjustment),
    }
    data = client.request("POST", "/inventory_levels/adjust.json", body=body)
    return unwrap_envelope(data)


@mcp.tool()
def set_inventory_level(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    available: int,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """Set inventory level (POST /inventory_levels/set.json)."""
    client = ShopifyClient()
    body: Dict[str, Any] = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
        "available": int(available),
    }
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    data = client.request("POST", "/inventory_levels/set.json", body=body)
    return unwrap_envelope(data)


@mcp.tool()
def connect_inventory_item(
    inventory_item_id: Union[int, str],
    location_id: Union[int, str],
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """Connect inventory item to location (POST /inventory_levels/connect.json)."""
    client = ShopifyClient()
    body: Dict[str, Any] = {
        "inventory_item_id": int(inventory_item_id),
        "location_id": int(location_id),
    }
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    data = client.request("POST", "/inventory_levels/connect.json", body=body)
    return unwrap_envelope(data)


@mcp.tool()
def delete_inventory_level(inventory_item_id: Union[int, str], location_id: Union[int, str]) -> Dict[str, Any]:
    """Delete inventory level (DELETE /inventory_levels.json?inventory_item_id=...&location_id=...)."""
    client = ShopifyClient()
    params = {"inventory_item_id": int(inventory_item_id), "location_id": int(location_id)}
    return client.request("DELETE", "/inventory_levels.json", params=params)
