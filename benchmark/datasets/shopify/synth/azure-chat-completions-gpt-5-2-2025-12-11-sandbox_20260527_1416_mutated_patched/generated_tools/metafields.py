from typing import Any, Dict, Optional

from .client import shopify_request


def create_metafield(resource_path: str, resource_id: int, metafield: Dict[str, Any]) -> Any:
    """POST /{resource_path}/{resource_id}/metafields.json"""
    return shopify_request("POST", f"/{resource_path}/{resource_id}/metafields.json", json={"metafield": metafield})


def list_metafields(resource_path: str, resource_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET /{resource_path}/{resource_id}/metafields.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", f"/{resource_path}/{resource_id}/metafields.json", params=params or None)


def get_metafield(resource_path: str, resource_id: int, metafield_id: int) -> Any:
    """GET /{resource_path}/{resource_id}/metafields/{metafield_id}.json"""
    return shopify_request("GET", f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json")


def count_metafields(resource_path: str, resource_id: int) -> Any:
    """GET /{resource_path}/{resource_id}/metafields/count.json"""
    return shopify_request("GET", f"/{resource_path}/{resource_id}/metafields/count.json")


def update_metafield(resource_path: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Any:
    """PUT /{resource_path}/{resource_id}/metafields/{metafield_id}.json"""
    body = {"metafield": {**metafield, "id": metafield_id}}
    return shopify_request("PUT", f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json", json=body)


def delete_metafield(resource_path: str, resource_id: int, metafield_id: int) -> Any:
    """DELETE /{resource_path}/{resource_id}/metafields/{metafield_id}.json"""
    return shopify_request("DELETE", f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json")
