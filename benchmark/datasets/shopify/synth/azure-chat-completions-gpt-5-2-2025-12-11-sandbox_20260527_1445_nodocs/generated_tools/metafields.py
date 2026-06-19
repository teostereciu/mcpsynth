from typing import Any, Dict, Optional

from .client import request_json


# Metafields (generic)

def list_metafields(*, owner_resource: Optional[str] = None, owner_id: Optional[int] = None, limit: int = 50) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if owner_resource:
        params["metafield[owner_resource]"] = owner_resource
    if owner_id is not None:
        params["metafield[owner_id]"] = owner_id
    return request_json("GET", "/metafields.json", params=params)


def get_metafield(metafield_id: int) -> Any:
    return request_json("GET", f"/metafields/{metafield_id}.json")


def create_metafield(metafield: Dict[str, Any]) -> Any:
    return request_json("POST", "/metafields.json", json={"metafield": metafield})


def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/metafields/{metafield_id}.json", json={"metafield": metafield})


def delete_metafield(metafield_id: int) -> Any:
    return request_json("DELETE", f"/metafields/{metafield_id}.json")
