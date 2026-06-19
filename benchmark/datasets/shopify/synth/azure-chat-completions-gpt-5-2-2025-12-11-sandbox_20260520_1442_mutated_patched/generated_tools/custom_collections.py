from typing import Any, Dict, Optional

from .http_client import request_json


def create_custom_collection(custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    """POST /custom_collections.json

    Doc: docs/api_customcollection.md
    Body wrapper: {"custom_collection": {...}}
    """
    return request_json("POST", "/custom_collections.json", json_body={"custom_collection": custom_collection})


def list_custom_collections(*, ids: Optional[str] = None, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /custom_collections.json

    Doc: docs/api_customcollection.md
    """
    params: Dict[str, Any] = {}
    if ids is not None:
        params["ids"] = ids
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/custom_collections.json", params=params)


def get_custom_collection(custom_collection_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /custom_collections/{custom_collection_id}.json

    Doc: docs/api_customcollection.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/custom_collections/{custom_collection_id}.json", params=params)


def count_custom_collections() -> Dict[str, Any]:
    """GET /custom_collections/count.json

    Doc: docs/api_customcollection.md
    """
    return request_json("GET", "/custom_collections/count.json")


def update_custom_collection(custom_collection_id: int, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /custom_collections/{custom_collection_id}.json

    Doc: docs/api_customcollection.md
    Body wrapper: {"custom_collection": {...}}
    """
    return request_json(
        "PUT",
        f"/custom_collections/{custom_collection_id}.json",
        json_body={"custom_collection": custom_collection},
    )


def delete_custom_collection(custom_collection_id: int) -> Dict[str, Any]:
    """DELETE /custom_collections/{custom_collection_id}.json

    Doc: docs/api_customcollection.md
    """
    return request_json("DELETE", f"/custom_collections/{custom_collection_id}.json")
