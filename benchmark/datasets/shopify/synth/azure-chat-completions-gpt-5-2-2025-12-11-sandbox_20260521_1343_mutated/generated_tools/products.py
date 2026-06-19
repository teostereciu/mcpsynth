from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_product(product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products.json"""
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
    collection_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products.json"""
    client = client or ShopifyClient()
    params = build_params(
        ids=ids,
        limit=limit,
        since_id=since_id,
        title=title,
        vendor=vendor,
        handle=handle,
        product_type=product_type,
        status=status,
        collection_id=collection_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        published_at_min=published_at_min,
        published_at_max=published_at_max,
        fields=fields,
    )
    return client.request("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}.json"""
    client = client or ShopifyClient()
    params = build_params(fields=fields)
    return client.request("GET", f"/products/{product_id}.json", params=params)


def count_products(
    *,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    collection_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    status: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/count.json"""
    client = client or ShopifyClient()
    params = build_params(
        vendor=vendor,
        product_type=product_type,
        collection_id=collection_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        published_at_min=published_at_min,
        published_at_max=published_at_max,
        status=status,
    )
    return client.request("GET", "/products/count.json", params=params)


def update_product(product_id: int, product: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/products/{product_id}.json", json={"product": product})


def delete_product(product_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}.json")
