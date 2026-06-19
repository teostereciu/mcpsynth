from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def list_inventory_levels(
    *,
    client: Optional[ShopifyClient] = None,
    location_ids: Optional[str] = None,
    inventory_item_ids: Optional[str] = None,
    limit: Optional[int] = None,
    updated_at_min: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /inventory_levels.json"""
    client = client or ShopifyClient()
    params = build_params(
        location_ids=location_ids,
        inventory_item_ids=inventory_item_ids,
        limit=limit,
        updated_at_min=updated_at_min,
    )
    return client.request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available_adjustment: int,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/adjust.json"""
    client = client or ShopifyClient()
    body = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available_adjustment": available_adjustment,
    }
    return client.request("POST", "/inventory_levels/adjust.json", json_body=body)


def connect_inventory_level(
    location_id: int,
    inventory_item_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    relocate_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/connect.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id}
    if relocate_if_necessary is not None:
        body["relocate_if_necessary"] = relocate_if_necessary
    return client.request("POST", "/inventory_levels/connect.json", json_body=body)


def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    *,
    client: Optional[ShopifyClient] = None,
    disconnect_if_necessary: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /inventory_levels/set.json"""
    client = client or ShopifyClient()
    body: Dict[str, Any] = {"location_id": location_id, "inventory_item_id": inventory_item_id, "available": available}
    if disconnect_if_necessary is not None:
        body["disconnect_if_necessary"] = disconnect_if_necessary
    return client.request("POST", "/inventory_levels/set.json", json_body=body)


def delete_inventory_level(
    inventory_item_id: int,
    location_id: int,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """DELETE /inventory_levels.json"""
    client = client or ShopifyClient()
    return client.request(
        "DELETE",
        "/inventory_levels.json",
        params={"inventory_item_id": inventory_item_id, "location_id": location_id},
    )
