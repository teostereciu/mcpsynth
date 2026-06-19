from typing import Any, Dict, Optional

from .http import shopify_request


def _resource_metafields_path(resource: str, resource_id: int) -> str:
    # resource examples: products, orders, customers, collections, blogs, pages, locations, variants, images
    return f"/{resource}/{resource_id}/metafields"


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /{resource}/{resource_id}/metafields.json"""
    return shopify_request("POST", _resource_metafields_path(resource, resource_id) + ".json", json={"metafield": metafield})


def list_metafields(resource: str, resource_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", _resource_metafields_path(resource, resource_id) + ".json", params=params or None)


def get_metafield(resource: str, resource_id: int, metafield_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    params = {"fields": fields} if fields else None
    return shopify_request("GET", _resource_metafields_path(resource, resource_id) + f"/{metafield_id}.json", params=params)


def count_metafields(resource: str, resource_id: int) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/count.json"""
    return shopify_request("GET", _resource_metafields_path(resource, resource_id) + "/count.json")


def update_metafield(resource: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    payload = dict(metafield)
    payload.setdefault("id", metafield_id)
    return shopify_request("PUT", _resource_metafields_path(resource, resource_id) + f"/{metafield_id}.json", json={"metafield": payload})


def delete_metafield(resource: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /{resource}/{resource_id}/metafields/{metafield_id}.json"""
    return shopify_request("DELETE", _resource_metafields_path(resource, resource_id) + f"/{metafield_id}.json")
