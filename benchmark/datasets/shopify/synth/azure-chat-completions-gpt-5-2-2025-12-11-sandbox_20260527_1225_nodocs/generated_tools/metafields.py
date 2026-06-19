from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_metafields(
    owner_resource: str,
    owner_id: int,
    limit: int = 50,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /{owner_resource}/{owner_id}/metafields.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if namespace:
        params["namespace"] = namespace
    if key:
        params["key"] = key
    return client.request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params=params)


def get_metafield(metafield_id: int) -> Dict[str, Any]:
    """GET /metafields/{metafield_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/metafields/{metafield_id}.json")


def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /{owner_resource}/{owner_id}/metafields.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/{owner_resource}/{owner_id}/metafields.json",
        json_body={"metafield": metafield},
    )


def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /metafields/{metafield_id}.json"""
    client = ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request("PUT", f"/metafields/{metafield_id}.json", json_body=body)


def delete_metafield(metafield_id: int) -> Dict[str, Any]:
    """DELETE /metafields/{metafield_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/metafields/{metafield_id}.json")
