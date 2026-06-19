from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_custom_collections(limit: int = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /custom_collections.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return client.request("GET", "/custom_collections.json", params=params)


def get_custom_collection(collection_id: int) -> Dict[str, Any]:
    """GET /custom_collections/{collection_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/custom_collections/{collection_id}.json")


def create_custom_collection(custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    """POST /custom_collections.json"""
    client = ShopifyClient()
    return client.request("POST", "/custom_collections.json", json_body={"custom_collection": custom_collection})


def update_custom_collection(collection_id: int, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /custom_collections/{collection_id}.json"""
    client = ShopifyClient()
    body = {"custom_collection": {**custom_collection, "id": collection_id}}
    return client.request("PUT", f"/custom_collections/{collection_id}.json", json_body=body)


def delete_custom_collection(collection_id: int) -> Dict[str, Any]:
    """DELETE /custom_collections/{collection_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/custom_collections/{collection_id}.json")


def list_smart_collections(limit: int = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /smart_collections.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return client.request("GET", "/smart_collections.json", params=params)


def get_smart_collection(collection_id: int) -> Dict[str, Any]:
    """GET /smart_collections/{collection_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/smart_collections/{collection_id}.json")


def create_smart_collection(smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    """POST /smart_collections.json"""
    client = ShopifyClient()
    return client.request("POST", "/smart_collections.json", json_body={"smart_collection": smart_collection})


def update_smart_collection(collection_id: int, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /smart_collections/{collection_id}.json"""
    client = ShopifyClient()
    body = {"smart_collection": {**smart_collection, "id": collection_id}}
    return client.request("PUT", f"/smart_collections/{collection_id}.json", json_body=body)


def delete_smart_collection(collection_id: int) -> Dict[str, Any]:
    """DELETE /smart_collections/{collection_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/smart_collections/{collection_id}.json")


def list_collects(limit: int = 50, product_id: Optional[int] = None, collection_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /collects.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if product_id:
        params["product_id"] = product_id
    if collection_id:
        params["collection_id"] = collection_id
    return client.request("GET", "/collects.json", params=params)


def create_collect(collect: Dict[str, Any]) -> Dict[str, Any]:
    """POST /collects.json"""
    client = ShopifyClient()
    return client.request("POST", "/collects.json", json_body={"collect": collect})


def delete_collect(collect_id: int) -> Dict[str, Any]:
    """DELETE /collects/{collect_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/collects/{collect_id}.json")
