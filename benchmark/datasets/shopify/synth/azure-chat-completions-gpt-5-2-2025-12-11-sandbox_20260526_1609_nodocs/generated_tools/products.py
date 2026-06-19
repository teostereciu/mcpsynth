from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_products(limit: int = 50, page_info: Optional[str] = None, **filters: Any) -> Dict[str, Any]:
    """GET /products.json"""
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    params.update({k: v for k, v in filters.items() if v is not None})
    return ShopifyClient().request("GET", "/products.json", params=params)


def get_product(product_id: int) -> Dict[str, Any]:
    """GET /products/{id}.json"""
    return ShopifyClient().request("GET", f"/products/{product_id}.json")


def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products.json"""
    return ShopifyClient().request("POST", "/products.json", json={"product": product})


def update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{id}.json"""
    return ShopifyClient().request("PUT", f"/products/{product_id}.json", json={"product": product})


def delete_product(product_id: int) -> Dict[str, Any]:
    """DELETE /products/{id}.json"""
    return ShopifyClient().request("DELETE", f"/products/{product_id}.json")


def list_product_variants(product_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /products/{product_id}/variants.json"""
    return ShopifyClient().request("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


def get_variant(variant_id: int) -> Dict[str, Any]:
    """GET /variants/{id}.json"""
    return ShopifyClient().request("GET", f"/variants/{variant_id}.json")


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /variants/{id}.json"""
    return ShopifyClient().request("PUT", f"/variants/{variant_id}.json", json={"variant": variant})


def list_product_images(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json"""
    return ShopifyClient().request("GET", f"/products/{product_id}/images.json")


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json"""
    return ShopifyClient().request("POST", f"/products/{product_id}/images.json", json={"image": image})


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/images/{id}.json"""
    return ShopifyClient().request("DELETE", f"/products/{product_id}/images/{image_id}.json")


def list_collections(limit: int = 50, collection_type: str = "custom") -> Dict[str, Any]:
    """GET /custom_collections.json or /smart_collections.json"""
    path = "/custom_collections.json" if collection_type == "custom" else "/smart_collections.json"
    return ShopifyClient().request("GET", path, params={"limit": limit})


def get_collection(collection_id: int, collection_type: str = "custom") -> Dict[str, Any]:
    """GET /custom_collections/{id}.json or /smart_collections/{id}.json"""
    path = f"/custom_collections/{collection_id}.json" if collection_type == "custom" else f"/smart_collections/{collection_id}.json"
    return ShopifyClient().request("GET", path)


def create_collection(collection: Dict[str, Any], collection_type: str = "custom") -> Dict[str, Any]:
    """POST /custom_collections.json or /smart_collections.json"""
    path = "/custom_collections.json" if collection_type == "custom" else "/smart_collections.json"
    key = "custom_collection" if collection_type == "custom" else "smart_collection"
    return ShopifyClient().request("POST", path, json={key: collection})


def update_collection(collection_id: int, collection: Dict[str, Any], collection_type: str = "custom") -> Dict[str, Any]:
    """PUT /custom_collections/{id}.json or /smart_collections/{id}.json"""
    path = f"/custom_collections/{collection_id}.json" if collection_type == "custom" else f"/smart_collections/{collection_id}.json"
    key = "custom_collection" if collection_type == "custom" else "smart_collection"
    return ShopifyClient().request("PUT", path, json={key: collection})


def delete_collection(collection_id: int, collection_type: str = "custom") -> Dict[str, Any]:
    """DELETE /custom_collections/{id}.json or /smart_collections/{id}.json"""
    path = f"/custom_collections/{collection_id}.json" if collection_type == "custom" else f"/smart_collections/{collection_id}.json"
    return ShopifyClient().request("DELETE", path)
