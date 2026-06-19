from typing import Any, Dict, Optional

from .http_client import get_client


def product_create(product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products.json

    Args:
        product: Product payload (wrapped under {"product": ...} by this tool).
    """
    return get_client().request("POST", "/products.json", json_body={"product": product})


def products_list(
    *,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    handle: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products.json"""
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
    return get_client().request("GET", "/products.json", params=params)


def product_get(product_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}.json"""
    params = {"fields": fields} if fields else None
    return get_client().request("GET", f"/products/{product_id}.json", params=params)


def products_count(*, status: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"status": status, "vendor": vendor, "product_type": product_type}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", "/products/count.json", params=params or None)


def product_update(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}.json"""
    body = {"product": {**product, "id": product_id}}
    return get_client().request("PUT", f"/products/{product_id}.json", json_body=body)


def product_delete(product_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}.json"""
    return get_client().request("DELETE", f"/products/{product_id}.json")


# Variants

def product_variant_create(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json"""
    return get_client().request(
        "POST",
        f"/products/{product_id}/variants.json",
        json_body={"variant": variant},
    )


def product_variants_list(product_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", f"/products/{product_id}/variants.json", params=params or None)


def product_variants_count(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/variants/count.json"""
    return get_client().request("GET", f"/products/{product_id}/variants/count.json")


def product_variant_get(variant_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json"""
    params = {"fields": fields} if fields else None
    return get_client().request("GET", f"/variants/{variant_id}.json", params=params)


def product_variant_update(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json"""
    body = {"variant": {**variant, "id": variant_id}}
    return get_client().request("PUT", f"/variants/{variant_id}.json", json_body=body)


def product_variant_delete(product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json"""
    return get_client().request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


# Images

def product_image_create(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json"""
    return get_client().request(
        "POST",
        f"/products/{product_id}/images.json",
        json_body={"image": image},
    )


def product_images_list(product_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", f"/products/{product_id}/images.json", params=params or None)


def product_images_count(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/images/count.json"""
    return get_client().request("GET", f"/products/{product_id}/images/count.json")


def product_image_get(product_id: int, image_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/images/{image_id}.json"""
    return get_client().request("GET", f"/products/{product_id}/images/{image_id}.json")


def product_image_update(product_id: int, image_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}/images/{image_id}.json"""
    body = {"image": {**image, "id": image_id}}
    return get_client().request("PUT", f"/products/{product_id}/images/{image_id}.json", json_body=body)


def product_image_delete(product_id: int, image_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/images/{image_id}.json"""
    return get_client().request("DELETE", f"/products/{product_id}/images/{image_id}.json")
