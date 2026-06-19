from typing import Any, Dict, Optional

from .http_client import request_json


def create_product_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json

    Doc: docs/api_product-variant.md
    Body wrapper: {"variant": {...}}
    """
    return request_json("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def list_product_variants(product_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json

    Doc: docs/api_product-variant.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}/variants.json", params=params)


def count_product_variants(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/variants/count.json

    Doc: docs/api_product-variant.md
    """
    return request_json("GET", f"/products/{product_id}/variants/count.json")


def get_product_variant(variant_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json

    Doc: docs/api_product-variant.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/variants/{variant_id}.json", params=params)


def update_product_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json

    Doc: docs/api_product-variant.md
    Body wrapper: {"variant": {...}}
    """
    return request_json("PUT", f"/variants/{variant_id}.json", json_body={"variant": variant})


def delete_product_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json

    Doc: docs/api_product-variant.md
    """
    return request_json("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
