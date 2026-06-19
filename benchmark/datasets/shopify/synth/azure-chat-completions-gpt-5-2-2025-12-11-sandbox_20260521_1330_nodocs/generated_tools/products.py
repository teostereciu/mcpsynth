from typing import Any, Dict, Optional

from .client import request_json


def list_products(limit: int = 50, page_info: Optional[str] = None, **filters: Any) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    params.update({k: v for k, v in filters.items() if v is not None})
    return request_json("GET", "/products.json", params=params)


def get_product(product_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/products/{product_id}.json")


def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/products.json", json={"product": product})


def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/products/{product_id}.json", json={"product": product})


def delete_product(product_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/products/{product_id}.json")


def list_product_variants(product_id: int, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


def get_variant(variant_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/variants/{variant_id}.json")


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/variants/{variant_id}.json", json={"variant": variant})


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/products/{product_id}/images.json", json={"image": image})


def list_product_images(product_id: int, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/products/{product_id}/images.json", params={"limit": limit})


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/products/{product_id}/images/{image_id}.json")
