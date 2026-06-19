from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_products(
    limit: int = 50,
    page_info: Optional[str] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products.json"""
    client = ShopifyClient()
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
    return client.request("GET", "/products.json", params=params)


def get_product(product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}.json"""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/products/{product_id}.json", params=params)


def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products.json"""
    client = ShopifyClient()
    return client.request("POST", "/products.json", json_body={"product": product})


def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}.json"""
    client = ShopifyClient()
    body = {"product": {**product, "id": product_id}}
    return client.request("PUT", f"/products/{product_id}.json", json_body=body)


def delete_product(product_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}.json")


def list_product_variants(product_id: int, limit: int = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return client.request("GET", f"/products/{product_id}/variants.json", params=params)


def get_variant(variant_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json"""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/variants/{variant_id}.json", params=params)


def create_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/variants.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/products/{product_id}/variants.json",
        json_body={"variant": variant},
    )


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json"""
    client = ShopifyClient()
    body = {"variant": {**variant, "id": variant_id}}
    return client.request("PUT", f"/variants/{variant_id}.json", json_body=body)


def delete_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/variants/{variant_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


def list_product_images(product_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json"""
    client = ShopifyClient()
    return client.request("GET", f"/products/{product_id}/images.json", params={"limit": limit})


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json"""
    client = ShopifyClient()
    return client.request("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/images/{image_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}/images/{image_id}.json")
