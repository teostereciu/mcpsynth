from typing import Any, Dict, Optional

from .client import request_json


def list_inventory_items(ids: str, *, limit: Optional[int] = None) -> Any:
    """GET /inventory_items.json"""
    params: Dict[str, Any] = {"ids": ids}
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Any:
    """GET /inventory_items/{inventory_item_id}.json"""
    return request_json("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Any:
    """PUT /inventory_items/{inventory_item_id}.json"""
    return request_json(
        "PUT",
        f"/inventory_items/{inventory_item_id}.json",
        json_body={"inventory_item": inventory_item},
    )
