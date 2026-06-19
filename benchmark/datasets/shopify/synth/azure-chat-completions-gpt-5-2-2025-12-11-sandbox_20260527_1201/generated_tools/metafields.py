from typing import Any, Dict, Optional

from .http_client import request_json


def list_metafields(owner_resource: str, owner_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"/{owner_resource}/{owner_id}/metafields.json", params=params)


def get_metafield(owner_resource: str, owner_id: int, metafield_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    return request_json("GET", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json")


def count_metafields(owner_resource: str, owner_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/count.json"""
    return request_json("GET", f"/{owner_resource}/{owner_id}/metafields/count.json")


def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    return request_json("POST", f"/{owner_resource}/{owner_id}/metafields.json", json_body={"metafield": metafield})


def update_metafield(owner_resource: str, owner_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    return request_json(
        "PUT",
        f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json",
        json_body={"metafield": metafield},
    )


def delete_metafield(owner_resource: str, owner_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    return request_json("DELETE", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json")
