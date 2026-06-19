from typing import Any, Dict, Optional

from .client import shopify_request


def create_product(product: Dict[str, Any]) -> Any:
    """POST /products.json"""
    return shopify_request("POST", "/products.json", json={"product": product})


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
    collection_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Any:
    """GET /products.json"""
    params: Dict[str, Any] = {}
    for k, v in {
        "ids": ids,
        "limit": limit,
        "since_id": since_id,
        "title": title,
        "vendor": vendor,
        "handle": handle,
        "product_type": product_type,
        "status": status,
        "collection_id": collection_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "published_at_min": published_at_min,
        "published_at_max": published_at_max,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None) -> Any:
    """GET /products/{product_id}.json"""
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/products/{product_id}.json", params=params)


def count_products(*, status: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None) -> Any:
    """GET /products/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"status": status, "vendor": vendor, "product_type": product_type}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/products/count.json", params=params or None)


def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    """PUT /products/{product_id}.json"""
    body = {"product": {**product, "id": product_id}}
    return shopify_request("PUT", f"/products/{product_id}.json", json=body)


def delete_product(product_id: int) -> Any:
    """DELETE /products/{product_id}.json"""
    return shopify_request("DELETE", f"/products/{product_id}.json")
