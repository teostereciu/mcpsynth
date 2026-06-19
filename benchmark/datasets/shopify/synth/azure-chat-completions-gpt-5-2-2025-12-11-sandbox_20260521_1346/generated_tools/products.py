from typing import Any, Dict, Optional

from .client import ShopifyClient, clean_params


def create_product(product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /products.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/products.json", json={"product": product})


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
) -> Any:
    """GET /products.json"""
    client = client or ShopifyClient()
    params = clean_params(
        {
            "ids": ids,
            "limit": limit,
            "since_id": since_id,
            "title": title,
            "vendor": vendor,
            "handle": handle,
            "product_type": product_type,
            "status": status,
            "fields": fields,
        }
    )
    return client.request("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /products/{product_id}.json"""
    client = client or ShopifyClient()
    params = clean_params({"fields": fields})
    return client.request("GET", f"/products/{product_id}.json", params=params)


def count_products(*, status: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /products/count.json"""
    client = client or ShopifyClient()
    params = clean_params({"status": status})
    return client.request("GET", "/products/count.json", params=params)


def update_product(product_id: int, product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /products/{product_id}.json"""
    client = client or ShopifyClient()
    body = {"product": {**product, "id": product_id}}
    return client.request("PUT", f"/products/{product_id}.json", json=body)


def delete_product(product_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /products/{product_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}.json")
