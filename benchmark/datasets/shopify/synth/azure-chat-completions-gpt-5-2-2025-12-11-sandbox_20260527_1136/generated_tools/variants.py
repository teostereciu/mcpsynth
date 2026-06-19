from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def create_variant(product_id: int, variant: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def list_variants(
    product_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    client = client or ShopifyClient()
    return client.request(
        "GET",
        f"/products/{product_id}/variants.json",
        params=build_params(limit=limit, since_id=since_id, fields=fields),
    )


def count_variants(product_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/variants/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int, *, client: Optional[ShopifyClient] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/variants/{variant_id}.json", params=build_params(fields=fields))


def update_variant(variant_id: int, variant: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json"""
    client = client or ShopifyClient()
    body = {"variant": {**variant, "id": variant_id}}
    return client.request("PUT", f"/variants/{variant_id}.json", json_body=body)


def delete_variant(product_id: int, variant_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
