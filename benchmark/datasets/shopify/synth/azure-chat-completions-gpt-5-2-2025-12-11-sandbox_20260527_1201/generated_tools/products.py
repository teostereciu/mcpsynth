from typing import Any, Dict, Optional

from .http_client import request_json


def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products.json"""
    return request_json("POST", "/products.json", json_body={"product": product})


def list_products(
    *,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    handle: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products.json"""
    params: Dict[str, Any] = {}
    if ids is not None:
        params["ids"] = ids
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if title is not None:
        params["title"] = title
    if vendor is not None:
        params["vendor"] = vendor
    if handle is not None:
        params["handle"] = handle
    if product_type is not None:
        params["product_type"] = product_type
    if status is not None:
        params["status"] = status
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}.json"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}.json", params=params)


def count_products(*, status: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/count.json"""
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if vendor is not None:
        params["vendor"] = vendor
    if product_type is not None:
        params["product_type"] = product_type
    return request_json("GET", "/products/count.json", params=params)


def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}.json"""
    return request_json("PUT", f"/products/{product_id}.json", json_body={"product": product})


def delete_product(product_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}.json"""
    return request_json("DELETE", f"/products/{product_id}.json")
