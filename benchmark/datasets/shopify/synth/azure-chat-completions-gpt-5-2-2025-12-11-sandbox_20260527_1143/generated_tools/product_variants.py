from typing import Any, Dict, Optional

from .http import request_json


def create_product_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json"""
    return request_json(
        "POST",
        f"/products/{product_id}/variants.json",
        json_body={"variant": variant},
    )


def list_product_variants(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/products/{product_id}/variants.json", params=params)


def count_product_variants(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/variants/count.json"""
    return request_json("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json"""
    params = {"fields": fields} if fields else None
    return request_json("GET", f"/variants/{variant_id}.json", params=params)


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json"""
    return request_json("PUT", f"/variants/{variant_id}.json", json_body={"variant": variant})


def delete_product_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json"""
    return request_json("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
