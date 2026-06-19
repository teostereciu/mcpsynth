from typing import Any, Dict, Optional

from ._client import get_client


def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products.json

    Doc: docs/api_product.md
    Body wrapper: {"product": {...}}
    """
    client = get_client()
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
) -> Dict[str, Any]:
    """GET /products.json

    Doc: docs/api_product.md
    """
    client = get_client()
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
        "collection_id": collection_id,
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


def get_product(product_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}.json

    Doc: docs/api_product.md
    """
    client = get_client()
    params = {"fields": fields} if fields else None
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
) -> Dict[str, Any]:
    """GET /products/count.json

    Doc: docs/api_product.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {
        "vendor": vendor,
        "product_type": product_type,
        "collection_id": collection_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "published_at_min": published_at_min,
        "published_at_max": published_at_max,
        "status": status,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products/count.json", params=params)


def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}.json

    Doc: docs/api_product.md
    Body wrapper: {"product": {..., "id": product_id}}
    """
    client = get_client()
    body = dict(product)
    body.setdefault("id", product_id)
    return client.request("PUT", f"/products/{product_id}.json", json={"product": body})


def delete_product(product_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}.json

    Doc: docs/api_product.md
    """
    client = get_client()
    return client.request("DELETE", f"/products/{product_id}.json")
