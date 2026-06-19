from typing import Any, Dict, Optional

from .client import request_json


# Products

def list_products(
    *,
    limit: int = 50,
    page_info: Optional[str] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    if title:
        params["title"] = title
    if vendor:
        params["vendor"] = vendor
    if product_type:
        params["product_type"] = product_type
    if status:
        params["status"] = status
    if fields:
        params["fields"] = fields
    return request_json("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}.json", params=params)


def create_product(product: Dict[str, Any]) -> Any:
    return request_json("POST", "/products.json", json={"product": product})


def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/products/{product_id}.json", json={"product": product})


def delete_product(product_id: int) -> Any:
    return request_json("DELETE", f"/products/{product_id}.json")


# Variants

def list_product_variants(product_id: int, *, limit: int = 50, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}/variants.json", params=params)


def get_variant(variant_id: int, *, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"/variants/{variant_id}.json", params=params)


def create_variant(product_id: int, variant: Dict[str, Any]) -> Any:
    return request_json("POST", f"/products/{product_id}/variants.json", json={"variant": variant})


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/variants/{variant_id}.json", json={"variant": variant})


def delete_variant(product_id: int, variant_id: int) -> Any:
    return request_json("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


# Images

def list_product_images(product_id: int, *, limit: int = 50) -> Any:
    return request_json("GET", f"/products/{product_id}/images.json", params={"limit": limit})


def get_product_image(product_id: int, image_id: int) -> Any:
    return request_json("GET", f"/products/{product_id}/images/{image_id}.json")


def create_product_image(product_id: int, image: Dict[str, Any]) -> Any:
    return request_json("POST", f"/products/{product_id}/images.json", json={"image": image})


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/products/{product_id}/images/{image_id}.json", json={"image": image})


def delete_product_image(product_id: int, image_id: int) -> Any:
    return request_json("DELETE", f"/products/{product_id}/images/{image_id}.json")
