from typing import Any, Dict, Optional

from shopify_api import shopify_request


def create_product(product: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/products.json", json_body={"product": product})


def list_products(limit: Optional[int] = None, since_id: Optional[int] = None, title: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None, status: Optional[str] = None, collection_id: Optional[int] = None) -> Any:
    params = {
        "limit": limit,
        "since_id": since_id,
        "title": title,
        "vendor": vendor,
        "product_type": product_type,
        "status": status,
        "collection_id": collection_id,
    }
    return shopify_request("GET", "/products.json", params=params)


def get_product(product_id: int, fields: Optional[str] = None) -> Any:
    return shopify_request("GET", f"/products/{product_id}.json", params={"fields": fields})


def count_products() -> Any:
    return shopify_request("GET", "/products/count.json")


def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    payload = dict(product)
    payload["id"] = product_id
    return shopify_request("PUT", f"/products/{product_id}.json", json_body={"product": payload})


def delete_product(product_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}.json")


def create_product_variant(product_id: int, variant: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def list_product_variants(product_id: int, limit: Optional[int] = None) -> Any:
    return shopify_request("GET", f"/products/{product_id}/variants.json", params={"limit": limit})


def count_product_variants(product_id: int) -> Any:
    return shopify_request("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int, fields: Optional[str] = None) -> Any:
    return shopify_request("GET", f"/variants/{variant_id}.json", params={"fields": fields})


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Any:
    payload = dict(variant)
    payload["id"] = variant_id
    return shopify_request("PUT", f"/variants/{variant_id}.json", json_body={"variant": payload})


def delete_product_variant(product_id: int, variant_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")
