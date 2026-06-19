from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_products(
    *,
    ids: Optional[str] = None,
    limit: int = 50,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products.json

    Common filters supported by Shopify include ids, limit, since_id, title, vendor,
    product_type, status, fields.
    """
    params: Dict[str, Any] = {"limit": limit}
    if ids:
        params["ids"] = ids
    if since_id is not None:
        params["since_id"] = since_id
    if title:
        params["title"] = title
    if vendor:
        params["vendor"] = vendor
    if product_type:
        params["product_type"] = product_type
    if status:
        params["status"] = status
    if fields:
        params["fields"] = fields
    return ShopifyClient().request("GET", "/products.json", params=params)


def get_product(*, product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}.json"""
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/products/{product_id}.json", params=params)


def count_products(*, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/count.json"""
    params: Dict[str, Any] = {}
    if status:
        params["status"] = status
    return ShopifyClient().request("GET", "/products/count.json", params=params)


def create_product(*, product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products.json"""
    return ShopifyClient().request("POST", "/products.json", json={"product": product})


def update_product(*, product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}.json"""
    body = {"product": {**product, "id": product_id}}
    return ShopifyClient().request("PUT", f"/products/{product_id}.json", json=body)


def delete_product(*, product_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}.json"""
    return ShopifyClient().request("DELETE", f"/products/{product_id}.json")
