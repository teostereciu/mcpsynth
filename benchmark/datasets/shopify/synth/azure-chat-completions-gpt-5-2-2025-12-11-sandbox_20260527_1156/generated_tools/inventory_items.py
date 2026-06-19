from typing import Any, Dict, Optional

from ._client import get_client


def list_inventory_items(ids: str, *, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_items.json?ids=...

    Doc: docs/api_inventoryitem.md
    """
    client = get_client()
    params: Dict[str, Any] = {"ids": ids}
    if limit is not None:
        params["limit"] = limit
    return client.request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    """GET /inventory_items/{inventory_item_id}.json

    Doc: docs/api_inventoryitem.md
    """
    client = get_client()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /inventory_items/{inventory_item_id}.json

    Doc: docs/api_inventoryitem.md
    Body wrapper: {"inventory_item": {..., "id": inventory_item_id}}
    """
    client = get_client()
    body = dict(inventory_item)
    body.setdefault("id", inventory_item_id)
    return client.request(
        "PUT", f"/inventory_items/{inventory_item_id}.json", json={"inventory_item": body}
    )
