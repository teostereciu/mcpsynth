from typing import Any, Dict, Optional

from .client import shopify_request


def list_custom_collections(*, limit: int = 50, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if fields is not None:
        params["fields"] = fields
    return shopify_request("GET", "/custom_collections.json", params=params)


def get_custom_collection(*, collection_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/custom_collections/{collection_id}.json")


def create_custom_collection(*, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", "/custom_collections.json", json_body={"custom_collection": custom_collection})


def update_custom_collection(*, collection_id: int, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    body = {"custom_collection": {**custom_collection, "id": collection_id}}
    return shopify_request("PUT", f"/custom_collections/{collection_id}.json", json_body=body)


def delete_custom_collection(*, collection_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/custom_collections/{collection_id}.json")


def list_smart_collections(*, limit: int = 50, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if fields is not None:
        params["fields"] = fields
    return shopify_request("GET", "/smart_collections.json", params=params)


def get_smart_collection(*, collection_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/smart_collections/{collection_id}.json")


def create_smart_collection(*, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", "/smart_collections.json", json_body={"smart_collection": smart_collection})


def update_smart_collection(*, collection_id: int, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    body = {"smart_collection": {**smart_collection, "id": collection_id}}
    return shopify_request("PUT", f"/smart_collections/{collection_id}.json", json_body=body)


def delete_smart_collection(*, collection_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/smart_collections/{collection_id}.json")


def list_collects(*, limit: int = 50, product_id: Optional[int] = None, collection_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if product_id is not None:
        params["product_id"] = product_id
    if collection_id is not None:
        params["collection_id"] = collection_id
    return shopify_request("GET", "/collects.json", params=params)


def create_collect(*, product_id: int, collection_id: int, position: Optional[int] = None) -> Dict[str, Any]:
    collect: Dict[str, Any] = {"product_id": product_id, "collection_id": collection_id}
    if position is not None:
        collect["position"] = position
    return shopify_request("POST", "/collects.json", json_body={"collect": collect})


def delete_collect(*, collect_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/collects/{collect_id}.json")
