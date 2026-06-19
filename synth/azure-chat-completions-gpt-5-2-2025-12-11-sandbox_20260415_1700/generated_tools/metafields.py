from typing import Any, Dict, Optional

from .client import request_json


# Metafields are accessed via the owning resource's endpoint.
# This module provides generic helpers for common owners.


def metafield_create(owner_path: str, owner_id: int, metafield: Dict[str, Any]) -> Any:
    """POST /{owner_path}/{owner_id}/metafields.json

    owner_path examples: 'products', 'orders', 'customers', 'blogs', 'pages', 'locations',
    'collections', 'smart_collections', 'draft_orders', 'articles', 'product_images', 'variants'
    (exact paths vary by resource).
    """
    return request_json("POST", f"/{owner_path}/{owner_id}/metafields.json", json_body={"metafield": metafield})


def metafields_list(owner_path: str, owner_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, namespace: Optional[str] = None, key: Optional[str] = None) -> Any:
    """GET /{owner_path}/{owner_id}/metafields.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "namespace": namespace, "key": key}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/{owner_path}/{owner_id}/metafields.json", params=params or None)


def metafield_get(owner_path: str, owner_id: int, metafield_id: int) -> Any:
    """GET /{owner_path}/{owner_id}/metafields/{metafield_id}.json"""
    return request_json("GET", f"/{owner_path}/{owner_id}/metafields/{metafield_id}.json")


def metafields_count(owner_path: str, owner_id: int) -> Any:
    """GET /{owner_path}/{owner_id}/metafields/count.json"""
    return request_json("GET", f"/{owner_path}/{owner_id}/metafields/count.json")


def metafield_update(owner_path: str, owner_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Any:
    """PUT /{owner_path}/{owner_id}/metafields/{metafield_id}.json"""
    body = {"metafield": {**metafield, "id": metafield_id}}
    return request_json("PUT", f"/{owner_path}/{owner_id}/metafields/{metafield_id}.json", json_body=body)


def metafield_delete(owner_path: str, owner_id: int, metafield_id: int) -> Any:
    """DELETE /{owner_path}/{owner_id}/metafields/{metafield_id}.json"""
    return request_json("DELETE", f"/{owner_path}/{owner_id}/metafields/{metafield_id}.json")
