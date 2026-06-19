from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_product_image(product_id: int, image: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/images.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/products/{product_id}/images.json", json={"image": image})


def list_product_images(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/images.json"""
    client = client or ShopifyClient()
    params = build_params(limit=limit, since_id=since_id, fields=fields)
    return client.request("GET", f"/products/{product_id}/images.json", params=params)


def get_product_image(
    product_id: int,
    image_id: int,
    *,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/images/{image_id}.json"""
    client = client or ShopifyClient()
    params = build_params(fields=fields)
    return client.request("GET", f"/products/{product_id}/images/{image_id}.json", params=params)


def count_product_images(product_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/images/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/products/{product_id}/images/count.json")


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}/images/{image_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/products/{product_id}/images/{image_id}.json", json={"image": image})


def delete_product_image(product_id: int, image_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}/images/{image_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}/images/{image_id}.json")
