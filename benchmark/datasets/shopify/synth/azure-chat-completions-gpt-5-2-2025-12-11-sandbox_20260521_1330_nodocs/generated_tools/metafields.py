from typing import Any, Dict, Optional

from .client import request_json


def list_metafields(resource: str, resource_id: int, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/{resource}/{resource_id}/metafields.json", params={"limit": limit})


def get_metafield(metafield_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/metafields/{metafield_id}.json")


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/{resource}/{resource_id}/metafields.json", json={"metafield": metafield})


def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/metafields/{metafield_id}.json", json={"metafield": metafield})


def delete_metafield(metafield_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/metafields/{metafield_id}.json")


def list_metafield_definitions(limit: int = 50, owner_resource: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if owner_resource:
        params["owner_resource"] = owner_resource
    return request_json("GET", "/metafield_definitions.json", params=params)
