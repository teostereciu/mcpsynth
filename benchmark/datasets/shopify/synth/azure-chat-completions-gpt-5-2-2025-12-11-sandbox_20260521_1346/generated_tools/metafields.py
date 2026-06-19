from typing import Any, Dict, Optional

from .client import ShopifyClient, clean_params


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /{resource}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/{resource}/{resource_id}/metafields.json", json={"metafield": metafield})


def list_metafields(
    resource: str,
    resource_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Any:
    """GET /{resource}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    params = clean_params({"limit": limit, "since_id": since_id, "namespace": namespace, "key": key})
    return client.request("GET", f"/{resource}/{resource_id}/metafields.json", params=params)


def get_metafield(resource: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/{resource}/{resource_id}/metafields/{metafield_id}.json")


def count_metafields(resource: str, resource_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /{resource}/{resource_id}/metafields/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/{resource}/{resource_id}/metafields/count.json")


def update_metafield(resource: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request("PUT", f"/{resource}/{resource_id}/metafields/{metafield_id}.json", json=body)


def delete_metafield(resource: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/{resource}/{resource_id}/metafields/{metafield_id}.json")
