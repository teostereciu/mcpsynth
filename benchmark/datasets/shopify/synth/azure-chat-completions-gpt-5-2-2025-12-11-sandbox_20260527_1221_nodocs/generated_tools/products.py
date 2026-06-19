from typing import Any, Dict, Optional

from .client import request_json


# Products

def list_products(
    *,
    limit: int = 50,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if title is not None:
        params["title"] = title
    if vendor is not None:
        params["vendor"] = vendor
    if product_type is not None:
        params["product_type"] = product_type
    if status is not None:
        params["status"] = status
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/products.json", params=params)


def get_product(product_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}.json", params=params or None)


def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/products.json", json_body={"product": product})


def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    body = {"product": {**product, "id": product_id}}
    return request_json("PUT", f"/products/{product_id}.json", json_body=body)


def delete_product(product_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/products/{product_id}.json")


# Variants

def list_product_variants(product_id: int, *, limit: int = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}/variants.json", params=params)


def get_variant(variant_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/variants/{variant_id}.json", params=params or None)


def create_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    body = {"variant": {**variant, "id": variant_id}}
    return request_json("PUT", f"/variants/{variant_id}.json", json_body=body)


def delete_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


# Images

def list_product_images(product_id: int, *, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/products/{product_id}/images.json", params={"limit": limit})


def get_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/products/{product_id}/images/{image_id}.json")


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    body = {"image": {**image, "id": image_id}}
    return request_json("PUT", f"/products/{product_id}/images/{image_id}.json", json_body=body)


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/products/{product_id}/images/{image_id}.json")
