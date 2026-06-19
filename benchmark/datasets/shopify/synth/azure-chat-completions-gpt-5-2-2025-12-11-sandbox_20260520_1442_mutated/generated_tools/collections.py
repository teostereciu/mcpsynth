from typing import Any, Dict, Optional

from .http_client import request_json


def get_collection(collection_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /collections/{collection_id}.json

    Doc: docs/api_collection.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/collections/{collection_id}.json", params=params)


def list_collection_products(collection_id: int, *, count: Optional[int] = None) -> Dict[str, Any]:
    """GET /collections/{collection_id}/products.json

    Doc: docs/api_collection.md
    """
    params: Dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    return request_json("GET", f"/collections/{collection_id}/products.json", params=params)
