from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


def create_product(product: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/products.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", "/products.json", json_body={"product": product})


def list_products(
    *,
    api_version: str = "2026-01",
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
    """GET /admin/api/2026-01/products.json"""
    client = ShopifyAdminClient(api_version=api_version)
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


def get_product(product_id: int, *, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/products/{product_id}.json", params=params)


def count_products(*, api_version: str = "2026-01", vendor: Optional[str] = None, product_type: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"vendor": vendor, "product_type": product_type, "status": status}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products/count.json", params=params or None)


def update_product(product_id: int, product: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"product": {**product, "id": product_id}}
    return client.request("PUT", f"/products/{product_id}.json", json_body=body)


def delete_product(product_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/products/{product_id}.json")


def create_product_variant(product_id: int, variant: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/variants.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def list_product_variants(
    product_id: int,
    *,
    api_version: str = "2026-01",
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/variants.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/products/{product_id}/variants.json", params=params or None)


def get_variant(variant_id: int, *, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/variants/{variant_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/variants/{variant_id}.json", params=params)


def update_variant(variant_id: int, variant: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/variants/{variant_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"variant": {**variant, "id": variant_id}}
    return client.request("PUT", f"/variants/{variant_id}.json", json_body=body)


def delete_variant(product_id: int, variant_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}/variants/{variant_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


def create_product_image(product_id: int, image: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/images.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def list_product_images(
    product_id: int,
    *,
    api_version: str = "2026-01",
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/images.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/products/{product_id}/images.json", params=params or None)


def get_product_image(
    product_id: int,
    image_id: int,
    *,
    api_version: str = "2026-01",
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/images/{image_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/products/{product_id}/images/{image_id}.json", params=params)


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}/images/{image_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"image": {**image, "id": image_id}}
    return client.request("PUT", f"/products/{product_id}/images/{image_id}.json", json_body=body)


def delete_product_image(product_id: int, image_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}/images/{image_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/products/{product_id}/images/{image_id}.json")
