from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_products(
    *,
    ids: Optional[str] = None,
    limit: Optional[int] = 50,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
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
    if product_type is not None:
        params["product_type"] = product_type
    if status is not None:
        params["status"] = status
    if fields is not None:
        params["fields"] = fields

    return ShopifyClient().request("GET", "/products.json", params=params)


def get_product(*, product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}.json"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/products/{product_id}.json", params=params)


def count_products(*, status: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/count.json"""
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if vendor is not None:
        params["vendor"] = vendor
    if product_type is not None:
        params["product_type"] = product_type
    return ShopifyClient().request("GET", "/products/count.json", params=params)


def create_product(*, product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products.json"""
    return ShopifyClient().request("POST", "/products.json", json_body={"product": product})


def update_product(*, product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}.json"""
    body = {"product": {**product, "id": product_id}}
    return ShopifyClient().request("PUT", f"/products/{product_id}.json", json_body=body)


def delete_product(*, product_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}.json"""
    return ShopifyClient().request("DELETE", f"/products/{product_id}.json")


def list_product_variants(*, product_id: int, limit: Optional[int] = 50, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/variants.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/products/{product_id}/variants.json", params=params)


def get_variant(*, variant_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/variants/{variant_id}.json"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/variants/{variant_id}.json", params=params)


def create_variant(*, product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/variants.json"""
    return ShopifyClient().request("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def update_variant(*, variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/variants/{variant_id}.json"""
    body = {"variant": {**variant, "id": variant_id}}
    return ShopifyClient().request("PUT", f"/variants/{variant_id}.json", json_body=body)


def delete_variant(*, product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}/variants/{variant_id}.json"""
    return ShopifyClient().request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
