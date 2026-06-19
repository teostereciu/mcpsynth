from typing import Any, Dict, Optional

from .client import request_json


def create_metafield(resource_path: str, metafield: Dict[str, Any]) -> Any:
    """POST {resource_path}/metafields.json (resource_path like /products/{id} or /orders/{id})"""
    return request_json("POST", f"{resource_path}/metafields.json", json_body={"metafield": metafield})


def list_metafields(resource_path: str, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET {resource_path}/metafields.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"{resource_path}/metafields.json", params=params)


def get_metafield(resource_path: str, metafield_id: int) -> Any:
    """GET {resource_path}/metafields/{metafield_id}.json"""
    return request_json("GET", f"{resource_path}/metafields/{metafield_id}.json")


def count_metafields(resource_path: str) -> Any:
    """GET {resource_path}/metafields/count.json"""
    return request_json("GET", f"{resource_path}/metafields/count.json")


def update_metafield(resource_path: str, metafield_id: int, metafield: Dict[str, Any]) -> Any:
    """PUT {resource_path}/metafields/{metafield_id}.json"""
    return request_json("PUT", f"{resource_path}/metafields/{metafield_id}.json", json_body={"metafield": metafield})


def delete_metafield(resource_path: str, metafield_id: int) -> Any:
    """DELETE {resource_path}/metafields/{metafield_id}.json"""
    return request_json("DELETE", f"{resource_path}/metafields/{metafield_id}.json")
