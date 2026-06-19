from typing import Any, Dict, Optional

from ._client import get_client


def create_product_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json

    Doc: docs/api_product-variant.md
    Body wrapper: {"variant": {...}}
    """
    client = get_client()
    return client.request(
        "POST", f"/products/{product_id}/variants.json", json={"variant": variant}
    )


def list_product_variants(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json

    Doc: docs/api_product-variant.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/products/{product_id}/variants.json", params=params)


def count_product_variants(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/variants/count.json

    Doc: docs/api_product-variant.md
    """
    client = get_client()
    return client.request("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json

    Doc: docs/api_product-variant.md
    """
    client = get_client()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/variants/{variant_id}.json", params=params)


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json

    Doc: docs/api_product-variant.md
    Body wrapper: {"variant": {..., "id": variant_id}}
    """
    client = get_client()
    body = dict(variant)
    body.setdefault("id", variant_id)
    return client.request("PUT", f"/variants/{variant_id}.json", json={"variant": body})


def delete_product_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json

    Doc: docs/api_product-variant.md
    """
    client = get_client()
    return client.request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
