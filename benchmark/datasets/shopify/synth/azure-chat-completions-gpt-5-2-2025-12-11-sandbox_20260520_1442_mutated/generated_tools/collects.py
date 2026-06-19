from typing import Any, Dict, Optional

from .http_client import request_json


def create_collect(collect: Dict[str, Any]) -> Dict[str, Any]:
    """POST /collects.json

    Doc: docs/api_collect.md
    Body wrapper: {"collect": {...}}
    """
    return request_json("POST", "/collects.json", json_body={"collect": collect})


def list_collects(*, collection_id: Optional[int] = None, product_id: Optional[int] = None, fields: Optional[str] = None, count: Optional[int] = None, after_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /collects.json

    Doc: docs/api_collect.md
    """
    params: Dict[str, Any] = {}
    if collection_id is not None:
        params["collection_id"] = collection_id
    if product_id is not None:
        params["product_id"] = product_id
    if fields is not None:
        params["fields"] = fields
    if count is not None:
        params["count"] = count
    if after_id is not None:
        params["after_id"] = after_id
    return request_json("GET", "/collects.json", params=params)


def get_collect(collect_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /collects/{collect_id}.json

    Doc: docs/api_collect.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/collects/{collect_id}.json", params=params)


def count_collects(*, collection_id: Optional[int] = None, product_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /collects/count.json

    Doc: docs/api_collect.md
    """
    params: Dict[str, Any] = {}
    if collection_id is not None:
        params["collection_id"] = collection_id
    if product_id is not None:
        params["product_id"] = product_id
    return request_json("GET", "/collects/count.json", params=params)


def delete_collect(collect_id: int) -> Dict[str, Any]:
    """DELETE /collects/{collect_id}.json

    Doc: docs/api_collect.md
    """
    return request_json("DELETE", f"/collects/{collect_id}.json")
