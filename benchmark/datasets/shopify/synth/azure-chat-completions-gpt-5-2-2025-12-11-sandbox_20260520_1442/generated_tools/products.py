from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_product(product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/products.json", json_body={"product": product})


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
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products.json"""
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
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return client.request("GET", f"/products/{product_id}.json", params=params)


def count_products(
    *,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/count.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"vendor": vendor, "product_type": product_type, "status": status}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products/count.json", params=params)


def update_product(product_id: int, product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/products/{product_id}.json", json_body={"product": product})


def delete_product(product_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}.json")
