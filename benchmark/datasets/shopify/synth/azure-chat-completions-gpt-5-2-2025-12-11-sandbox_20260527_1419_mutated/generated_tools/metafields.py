from typing import Any, Dict, Optional

from .client import ShopifyClient


def _resource_metafields_base(resource: str, resource_id: int) -> str:
    # resource examples: products, orders, customers, collections, blogs, pages, locations, variants, images
    return f"/{resource}/{resource_id}/metafields"


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /{resource}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    return client.request("POST", _resource_metafields_base(resource, resource_id) + ".json", json={"metafield": metafield})


def list_metafields(resource: str, resource_id: int, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, since_id: Optional[int] = None, namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "namespace": namespace, "key": key}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", _resource_metafields_base(resource, resource_id) + ".json", params=params or None)


def get_metafield(resource: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", _resource_metafields_base(resource, resource_id) + f"/{metafield_id}.json")


def count_metafields(resource: str, resource_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", _resource_metafields_base(resource, resource_id) + "/count.json")


def update_metafield(resource: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request("PUT", _resource_metafields_base(resource, resource_id) + f"/{metafield_id}.json", json=body)


def delete_metafield(resource: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", _resource_metafields_base(resource, resource_id) + f"/{metafield_id}.json")
