from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def _metafields_base_path(owner_resource: str, owner_id: int) -> str:
    # owner_resource examples: products, orders, customers, draft_orders, locations, blogs, pages, etc.
    return f"/{owner_resource}/{owner_id}/metafields"


def metafield_create(owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        _metafields_base_path(owner_resource, owner_id) + ".json",
        json_body={"metafield": metafield},
    )


def metafields_list(owner_resource: str, owner_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request(
        "GET",
        _metafields_base_path(owner_resource, owner_id) + ".json",
        params=params if params else None,
    )


def metafield_get(owner_resource: str, owner_id: int, metafield_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = ShopifyClient()
    return client.request(
        "GET",
        _metafields_base_path(owner_resource, owner_id) + f"/{metafield_id}.json",
    )


def metafields_count(owner_resource: str, owner_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/count.json"""
    client = ShopifyClient()
    return client.request(
        "GET", _metafields_base_path(owner_resource, owner_id) + "/count.json"
    )


def metafield_update(owner_resource: str, owner_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request(
        "PUT",
        _metafields_base_path(owner_resource, owner_id) + f"/{metafield_id}.json",
        json_body=body,
    )


def metafield_delete(owner_resource: str, owner_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = ShopifyClient()
    return client.request(
        "DELETE",
        _metafields_base_path(owner_resource, owner_id) + f"/{metafield_id}.json",
    )
