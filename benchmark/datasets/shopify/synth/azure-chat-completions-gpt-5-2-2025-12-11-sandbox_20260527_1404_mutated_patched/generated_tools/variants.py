from typing import Any, Dict, Optional

from .http import shopify_request


def create_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json"""
    return shopify_request("POST", f"/products/{product_id}/variants.json", json={"variant": variant})


def list_variants(product_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", f"/products/{product_id}/variants.json", params=params or None)


def count_variants(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/variants/count.json"""
    return shopify_request("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json"""
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/variants/{variant_id}.json", params=params)


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json"""
    payload = dict(variant)
    payload.setdefault("id", variant_id)
    return shopify_request("PUT", f"/variants/{variant_id}.json", json={"variant": payload})


def delete_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json"""
    return shopify_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
