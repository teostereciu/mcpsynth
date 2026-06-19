from typing import Any, Dict, Optional, List

from .http_client import request_json


def create_smart_collection(smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    """POST /smart_collections.json

    Doc: docs/api_smartcollection.md
    Body wrapper: {"smart_collection": {...}}
    """
    return request_json("POST", "/smart_collections.json", json_body={"smart_collection": smart_collection})


def list_smart_collections(*, since_id: Optional[int] = None, limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /smart_collections.json

    Doc: docs/api_smartcollection.md
    """
    params: Dict[str, Any] = {}
    if since_id is not None:
        params["since_id"] = since_id
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/smart_collections.json", params=params)


def get_smart_collection(smart_collection_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /smart_collections/{smart_collection_id}.json

    Doc: docs/api_smartcollection.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/smart_collections/{smart_collection_id}.json", params=params)


def count_smart_collections() -> Dict[str, Any]:
    """GET /smart_collections/count.json

    Doc: docs/api_smartcollection.md
    """
    return request_json("GET", "/smart_collections/count.json")


def update_smart_collection(smart_collection_id: int, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /smart_collections/{smart_collection_id}.json

    Doc: docs/api_smartcollection.md
    Body wrapper: {"smart_collection": {...}}
    """
    return request_json(
        "PUT",
        f"/smart_collections/{smart_collection_id}.json",
        json_body={"smart_collection": smart_collection},
    )


def delete_smart_collection(smart_collection_id: int) -> Dict[str, Any]:
    """DELETE /smart_collections/{smart_collection_id}.json

    Doc: docs/api_smartcollection.md
    """
    return request_json("DELETE", f"/smart_collections/{smart_collection_id}.json")


def reorder_smart_collection_products(smart_collection_id: int, products: List[int]) -> Dict[str, Any]:
    """PUT /smart_collections/{smart_collection_id}/order.json?products[]=...

    Doc: docs/api_smartcollection.md
    """
    params: Dict[str, Any] = {}
    # requests will encode list as repeated params if value is list
    params["products[]"] = products
    return request_json("PUT", f"/smart_collections/{smart_collection_id}/order.json", params=params)
