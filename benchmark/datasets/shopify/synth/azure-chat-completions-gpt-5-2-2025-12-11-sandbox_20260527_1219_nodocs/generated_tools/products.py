from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_products(
    *,
    limit: Optional[int] = 50,
    page_info: Optional[str] = None,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
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
    return c.request("GET", "/products.json", params=params)


def get_product(*, product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", f"/products/{product_id}.json", params=params)


def create_product(*, product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products.json"""
    c = ShopifyClient()
    return c.request("POST", "/products.json", json={"product": product})


def update_product(*, product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}.json"""
    c = ShopifyClient()
    body = {"product": {**product, "id": product_id}}
    return c.request("PUT", f"/products/{product_id}.json", json=body)


def delete_product(*, product_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/products/{product_id}.json")


def list_product_variants(*, product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", f"/products/{product_id}/variants.json", params=params)


def get_variant(*, variant_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /variants/{variant_id}.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", f"/variants/{variant_id}.json", params=params)


def update_variant(*, variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{variant_id}.json"""
    c = ShopifyClient()
    body = {"variant": {**variant, "id": variant_id}}
    return c.request("PUT", f"/variants/{variant_id}.json", json=body)


def create_product_image(*, product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json"""
    c = ShopifyClient()
    return c.request("POST", f"/products/{product_id}/images.json", json={"image": image})


def list_product_images(*, product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", f"/products/{product_id}/images.json", params=params)
