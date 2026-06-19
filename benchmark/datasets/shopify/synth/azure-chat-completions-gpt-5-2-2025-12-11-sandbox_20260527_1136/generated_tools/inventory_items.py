from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def list_inventory_items(ids: str, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_items.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/inventory_items.json", params=build_params(ids=ids, limit=limit))


def get_inventory_item(inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(
    inventory_item_id: int,
    inventory_item: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return client.request("PUT", f"/inventory_items/{inventory_item_id}.json", json_body=body)
