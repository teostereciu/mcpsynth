from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def _resource_metafields_path(resource: str, resource_id: int) -> str:
    # resource should be plural endpoint base, e.g. "products", "orders", "customers", "blogs", "articles", "pages", "draft_orders", "locations", "smart_collections", "custom_collections", "product_images", "variants"
    return f"/{resource}/{resource_id}/metafields.json"


def _resource_metafield_path(resource: str, resource_id: int, metafield_id: int) -> str:
    return f"/{resource}/{resource_id}/metafields/{metafield_id}.json"


def _resource_metafields_count_path(resource: str, resource_id: int) -> str:
    return f"/{resource}/{resource_id}/metafields/count.json"


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /{resource}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    return client.request("POST", _resource_metafields_path(resource, resource_id), json_body={"metafield": metafield})


def list_metafields(
    resource: str,
    resource_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    return client.request(
        "GET",
        _resource_metafields_path(resource, resource_id),
        params=build_params(limit=limit, since_id=since_id, namespace=namespace, key=key),
    )


def get_metafield(resource: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", _resource_metafield_path(resource, resource_id, metafield_id))


def count_metafields(resource: str, resource_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", _resource_metafields_count_path(resource, resource_id))


def update_metafield(
    resource: str,
    resource_id: int,
    metafield_id: int,
    metafield: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request("PUT", _resource_metafield_path(resource, resource_id, metafield_id), json_body=body)


def delete_metafield(resource: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", _resource_metafield_path(resource, resource_id, metafield_id))
