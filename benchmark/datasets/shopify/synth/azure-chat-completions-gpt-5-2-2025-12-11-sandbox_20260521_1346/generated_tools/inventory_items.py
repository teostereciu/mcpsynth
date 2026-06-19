from typing import Any, Dict, Optional

from .client import ShopifyClient, clean_params


def list_inventory_items(ids: str, *, limit: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /inventory_items.json"""
    client = client or ShopifyClient()
    params = clean_params({"ids": ids, "limit": limit})
    return client.request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    body = {"inventory_item": {**inventory_item, "id": inventory_item_id}}
    return client.request("PUT", f"/inventory_items/{inventory_item_id}.json", json=body)
