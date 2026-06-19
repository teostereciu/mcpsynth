from typing import Any, Dict, Optional

from .client import request_json


# Custom collections

def list_custom_collections(*, limit: int = 50, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return request_json("GET", "/custom_collections.json", params=params)


def get_custom_collection(collection_id: int) -> Any:
    return request_json("GET", f"/custom_collections/{collection_id}.json")


def create_custom_collection(custom_collection: Dict[str, Any]) -> Any:
    return request_json("POST", "/custom_collections.json", json={"custom_collection": custom_collection})


def update_custom_collection(collection_id: int, custom_collection: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/custom_collections/{collection_id}.json", json={"custom_collection": custom_collection})


def delete_custom_collection(collection_id: int) -> Any:
    return request_json("DELETE", f"/custom_collections/{collection_id}.json")


# Smart collections

def list_smart_collections(*, limit: int = 50, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return request_json("GET", "/smart_collections.json", params=params)


def get_smart_collection(collection_id: int) -> Any:
    return request_json("GET", f"/smart_collections/{collection_id}.json")


def create_smart_collection(smart_collection: Dict[str, Any]) -> Any:
    return request_json("POST", "/smart_collections.json", json={"smart_collection": smart_collection})


def update_smart_collection(collection_id: int, smart_collection: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/smart_collections/{collection_id}.json", json={"smart_collection": smart_collection})


def delete_smart_collection(collection_id: int) -> Any:
    return request_json("DELETE", f"/smart_collections/{collection_id}.json")


# Collects (product <-> collection)

def list_collects(*, limit: int = 50, product_id: Optional[int] = None, collection_id: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if product_id is not None:
        params["product_id"] = product_id
    if collection_id is not None:
        params["collection_id"] = collection_id
    return request_json("GET", "/collects.json", params=params)


def create_collect(collect: Dict[str, Any]) -> Any:
    return request_json("POST", "/collects.json", json={"collect": collect})


def delete_collect(collect_id: int) -> Any:
    return request_json("DELETE", f"/collects/{collect_id}.json")
