from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_product_variant(product_id: int, variant: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/variants.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/products/{product_id}/variants.json", json={"variant": variant})


def list_product_variants(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/variants.json"""
    client = client or ShopifyClient()
    params = build_params(limit=limit, since_id=since_id, fields=fields)
    return client.request("GET", f"/products/{product_id}/variants.json", params=params)


def count_product_variants(product_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/variants/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/variants/{variant_id}.json"""
    client = client or ShopifyClient()
    params = build_params(fields=fields)
    return client.request("GET", f"/variants/{variant_id}.json", params=params)


def update_variant(variant_id: int, variant: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/variants/{variant_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/variants/{variant_id}.json", json={"variant": variant})


def delete_product_variant(product_id: int, variant_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}/variants/{variant_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
