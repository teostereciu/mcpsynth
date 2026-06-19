from typing import Any, Dict, Optional

from .http_client import request_json


def list_inventory_items(ids: str, *, count: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_items.json?ids=...

    Doc: docs/api_inventoryitem.md
    """
    params: Dict[str, Any] = {"ids": ids}
    if count is not None:
        params["count"] = count
    return request_json("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    """GET /inventory_items/{inventory_item_id}.json

    Doc: docs/api_inventoryitem.md
    """
    return request_json("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /inventory_items/{inventory_item_id}.json

    Doc: docs/api_inventoryitem.md
    Body wrapper: {"inventory_item": {...}}
    """
    return request_json(
        "PUT",
        f"/inventory_items/{inventory_item_id}.json",
        json_body={"inventory_item": inventory_item},
    )
