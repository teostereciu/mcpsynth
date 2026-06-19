from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_product(product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /products.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/products.json", json={"product": product})


def list_products(
    *,
    client: Optional[ShopifyClient] = None,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    handle: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products.json"""
    client = client or ShopifyClient()
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
    return client.request("GET", "/products.json", params=params)


def get_product(product_id: int, *, client: Optional[ShopifyClient] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}.json"""
    client = client or ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/products/{product_id}.json", params=params)


def count_products(*, client: Optional[ShopifyClient] = None, status: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/count.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"status": status, "vendor": vendor, "product_type": product_type}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products/count.json", params=params or None)


def update_product(product_id: int, product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /products/{product_id}.json"""
    client = client or ShopifyClient()
    body = {"product": {**product, "id": product_id}}
    return client.request("PUT", f"/products/{product_id}.json", json=body)


def delete_product(product_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /products/{product_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}.json")
