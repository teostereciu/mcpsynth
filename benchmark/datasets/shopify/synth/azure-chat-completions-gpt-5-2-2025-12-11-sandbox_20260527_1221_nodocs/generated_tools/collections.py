from typing import Any, Dict, Optional

from .client import request_json


# Custom collections

def list_custom_collections(*, limit: int = 50, since_id: Optional[int] = None, title: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if title is not None:
        params["title"] = title
    return request_json("GET", "/custom_collections.json", params=params)


def get_custom_collection(collection_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/custom_collections/{collection_id}.json")


def create_custom_collection(custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/custom_collections.json", json_body={"custom_collection": custom_collection})


def update_custom_collection(collection_id: int, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    body = {"custom_collection": {**custom_collection, "id": collection_id}}
    return request_json("PUT", f"/custom_collections/{collection_id}.json", json_body=body)


def delete_custom_collection(collection_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/custom_collections/{collection_id}.json")


# Smart collections

def list_smart_collections(*, limit: int = 50, since_id: Optional[int] = None, title: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if title is not None:
        params["title"] = title
    return request_json("GET", "/smart_collections.json", params=params)


def get_smart_collection(collection_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/smart_collections/{collection_id}.json")


def create_smart_collection(smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/smart_collections.json", json_body={"smart_collection": smart_collection})


def update_smart_collection(collection_id: int, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    body = {"smart_collection": {**smart_collection, "id": collection_id}}
    return request_json("PUT", f"/smart_collections/{collection_id}.json", json_body=body)


def delete_smart_collection(collection_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/smart_collections/{collection_id}.json")


# Collects (product <-> collection)

def list_collects(*, limit: int = 50, since_id: Optional[int] = None, product_id: Optional[int] = None, collection_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if product_id is not None:
        params["product_id"] = product_id
    if collection_id is not None:
        params["collection_id"] = collection_id
    return request_json("GET", "/collects.json", params=params)


def create_collect(collect: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/collects.json", json_body={"collect": collect})


def delete_collect(collect_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/collects/{collect_id}.json")
