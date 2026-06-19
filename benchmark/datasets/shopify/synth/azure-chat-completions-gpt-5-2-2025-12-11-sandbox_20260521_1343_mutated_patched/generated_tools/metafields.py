from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def _metafields_base_path(owner_resource: str, owner_id: int) -> str:
    # owner_resource examples: products, orders, customers, draft_orders, locations, pages, blogs, articles, collections, smart_collections
    return f"/{owner_resource}/{owner_id}/metafields"


def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    client = client or ShopifyClient()
    return client.request("POST", _metafields_base_path(owner_resource, owner_id) + ".json", json={"metafield": metafield})


def list_metafields(
    owner_resource: str,
    owner_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    client = client or ShopifyClient()
    params = build_params(limit=limit, since_id=since_id, namespace=namespace, key=key)
    return client.request("GET", _metafields_base_path(owner_resource, owner_id) + ".json", params=params)


def get_metafield(owner_resource: str, owner_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", _metafields_base_path(owner_resource, owner_id) + f"/{metafield_id}.json")


def count_metafields(owner_resource: str, owner_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", _metafields_base_path(owner_resource, owner_id) + "/count.json")


def update_metafield(
    owner_resource: str,
    owner_id: int,
    metafield_id: int,
    metafield: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", _metafields_base_path(owner_resource, owner_id) + f"/{metafield_id}.json", json={"metafield": metafield})


def delete_metafield(owner_resource: str, owner_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", _metafields_base_path(owner_resource, owner_id) + f"/{metafield_id}.json")
