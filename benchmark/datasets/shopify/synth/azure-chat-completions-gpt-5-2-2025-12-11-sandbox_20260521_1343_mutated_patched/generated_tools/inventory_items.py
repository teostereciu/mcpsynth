from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def list_inventory_items(ids: str, *, limit: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_items.json?ids=..."""
    client = client or ShopifyClient()
    params = build_params(ids=ids, limit=limit)
    return client.request("GET", "/inventory_items.json", params=params)


def get_inventory_item(inventory_item_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/inventory_items/{inventory_item_id}.json")


def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/inventory_items/{inventory_item_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/inventory_items/{inventory_item_id}.json", json={"inventory_item": inventory_item})
