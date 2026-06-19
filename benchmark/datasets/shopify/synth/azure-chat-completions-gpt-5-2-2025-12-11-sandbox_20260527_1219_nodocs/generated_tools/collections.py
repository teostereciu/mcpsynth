from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_custom_collections(*, limit: Optional[int] = 50, page_info: Optional[str] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /custom_collections.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", "/custom_collections.json", params=params)


def get_custom_collection(*, custom_collection_id: int) -> Dict[str, Any]:
    """GET /custom_collections/{id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/custom_collections/{custom_collection_id}.json")


def create_custom_collection(*, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    """POST /custom_collections.json"""
    c = ShopifyClient()
    return c.request("POST", "/custom_collections.json", json={"custom_collection": custom_collection})


def update_custom_collection(*, custom_collection_id: int, custom_collection: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /custom_collections/{id}.json"""
    c = ShopifyClient()
    body = {"custom_collection": {**custom_collection, "id": custom_collection_id}}
    return c.request("PUT", f"/custom_collections/{custom_collection_id}.json", json=body)


def delete_custom_collection(*, custom_collection_id: int) -> Dict[str, Any]:
    """DELETE /custom_collections/{id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/custom_collections/{custom_collection_id}.json")


def list_smart_collections(*, limit: Optional[int] = 50, page_info: Optional[str] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /smart_collections.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", "/smart_collections.json", params=params)


def get_smart_collection(*, smart_collection_id: int) -> Dict[str, Any]:
    """GET /smart_collections/{id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/smart_collections/{smart_collection_id}.json")


def create_smart_collection(*, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    """POST /smart_collections.json"""
    c = ShopifyClient()
    return c.request("POST", "/smart_collections.json", json={"smart_collection": smart_collection})


def update_smart_collection(*, smart_collection_id: int, smart_collection: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /smart_collections/{id}.json"""
    c = ShopifyClient()
    body = {"smart_collection": {**smart_collection, "id": smart_collection_id}}
    return c.request("PUT", f"/smart_collections/{smart_collection_id}.json", json=body)


def delete_smart_collection(*, smart_collection_id: int) -> Dict[str, Any]:
    """DELETE /smart_collections/{id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/smart_collections/{smart_collection_id}.json")
