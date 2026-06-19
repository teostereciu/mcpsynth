from typing import Any, Dict, Optional

from generated_tools.common import shopify_request


def create_product(product: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/products.json", json_body={"product": product})


def list_products(limit: Optional[int] = None, since_id: Optional[int] = None, collection_id: Optional[int] = None, fields: Optional[str] = None, ids: Optional[str] = None, presentment_currencies: Optional[str] = None) -> Any:
    params = {k: v for k, v in {
        "limit": limit,
        "since_id": since_id,
        "collection_id": collection_id,
        "fields": fields,
        "ids": ids,
        "presentment_currencies": presentment_currencies,
    }.items() if v is not None}
    return shopify_request("GET", "/products.json", params=params)


def get_product(product_id: int, fields: Optional[str] = None) -> Any:
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/products/{product_id}.json", params=params)


def count_products(collection_id: Optional[int] = None) -> Any:
    params = {"collection_id": collection_id} if collection_id is not None else None
    return shopify_request("GET", "/products/count.json", params=params)


def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    payload = dict(product)
    payload.setdefault("id", product_id)
    return shopify_request("PUT", f"/products/{product_id}.json", json_body={"product": payload})


def delete_product(product_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}.json")


def create_variant(product_id: int, variant: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def list_variants(product_id: int, limit: Optional[int] = None, since_id: Optional[int] = None, presentment_currencies: Optional[str] = None) -> Any:
    params = {k: v for k, v in {
        "limit": limit,
        "since_id": since_id,
        "presentment_currencies": presentment_currencies,
    }.items() if v is not None}
    return shopify_request("GET", f"/products/{product_id}/variants.json", params=params)


def count_variants(product_id: int) -> Any:
    return shopify_request("GET", f"/products/{product_id}/variants/count.json")


def get_variant(variant_id: int) -> Any:
    return shopify_request("GET", f"/variants/{variant_id}.json")


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Any:
    payload = dict(variant)
    payload.setdefault("id", variant_id)
    return shopify_request("PUT", f"/variants/{variant_id}.json", json_body={"variant": payload})


def delete_variant(product_id: int, variant_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


def create_product_image(product_id: int, image: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def list_product_images(product_id: int, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "since_id": since_id}.items() if v is not None}
    return shopify_request("GET", f"/products/{product_id}/images.json", params=params)


def get_product_image(product_id: int, image_id: int) -> Any:
    return shopify_request("GET", f"/products/{product_id}/images/{image_id}.json")


def count_product_images(product_id: int, since_id: Optional[int] = None) -> Any:
    params = {"since_id": since_id} if since_id is not None else None
    return shopify_request("GET", f"/products/{product_id}/images/count.json", params=params)


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Any:
    payload = dict(image)
    payload.setdefault("id", image_id)
    return shopify_request("PUT", f"/products/{product_id}/images/{image_id}.json", json_body={"image": payload})


def delete_product_image(product_id: int, image_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


def create_custom_collection(custom_collection: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/custom_collections.json", json_body={"custom_collection": custom_collection})


def list_custom_collections(limit: Optional[int] = None, since_id: Optional[int] = None, product_id: Optional[int] = None, handle: Optional[str] = None, title: Optional[str] = None, updated_at_min: Optional[str] = None) -> Any:
    params = {k: v for k, v in {
        "limit": limit,
        "since_id": since_id,
        "product_id": product_id,
        "handle": handle,
        "title": title,
        "updated_at_min": updated_at_min,
    }.items() if v is not None}
    return shopify_request("GET", "/custom_collections.json", params=params)


def get_custom_collection(custom_collection_id: int) -> Any:
    return shopify_request("GET", f"/custom_collections/{custom_collection_id}.json")


def count_custom_collections(product_id: Optional[int] = None) -> Any:
    params = {"product_id": product_id} if product_id is not None else None
    return shopify_request("GET", "/custom_collections/count.json", params=params)


def update_custom_collection(custom_collection_id: int, custom_collection: Dict[str, Any]) -> Any:
    payload = dict(custom_collection)
    payload.setdefault("id", custom_collection_id)
    return shopify_request("PUT", f"/custom_collections/{custom_collection_id}.json", json_body={"custom_collection": payload})


def delete_custom_collection(custom_collection_id: int) -> Any:
    return shopify_request("DELETE", f"/custom_collections/{custom_collection_id}.json")


def create_collect(collect: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/collects.json", json_body={"collect": collect})


def list_collects(limit: Optional[int] = None, since_id: Optional[int] = None, collection_id: Optional[int] = None, product_id: Optional[int] = None, fields: Optional[str] = None) -> Any:
    params = {k: v for k, v in {
        "limit": limit,
        "since_id": since_id,
        "collection_id": collection_id,
        "product_id": product_id,
        "fields": fields,
    }.items() if v is not None}
    return shopify_request("GET", "/collects.json", params=params)


def get_collect(collect_id: int, fields: Optional[str] = None) -> Any:
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/collects/{collect_id}.json", params=params)


def count_collects(collection_id: Optional[int] = None, product_id: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"collection_id": collection_id, "product_id": product_id}.items() if v is not None}
    return shopify_request("GET", "/collects/count.json", params=params)


def delete_collect(collect_id: int) -> Any:
    return shopify_request("DELETE", f"/collects/{collect_id}.json")


def create_smart_collection(smart_collection: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/smart_collections.json", json_body={"smart_collection": smart_collection})


def list_smart_collections(limit: Optional[int] = None, since_id: Optional[int] = None, product_id: Optional[int] = None, handle: Optional[str] = None, title: Optional[str] = None, updated_at_min: Optional[str] = None) -> Any:
    params = {k: v for k, v in {
        "limit": limit,
        "since_id": since_id,
        "product_id": product_id,
        "handle": handle,
        "title": title,
        "updated_at_min": updated_at_min,
    }.items() if v is not None}
    return shopify_request("GET", "/smart_collections.json", params=params)


def get_smart_collection(smart_collection_id: int) -> Any:
    return shopify_request("GET", f"/smart_collections/{smart_collection_id}.json")


def count_smart_collections(product_id: Optional[int] = None) -> Any:
    params = {"product_id": product_id} if product_id is not None else None
    return shopify_request("GET", "/smart_collections/count.json", params=params)


def update_smart_collection(smart_collection_id: int, smart_collection: Dict[str, Any]) -> Any:
    payload = dict(smart_collection)
    payload.setdefault("id", smart_collection_id)
    return shopify_request("PUT", f"/smart_collections/{smart_collection_id}.json", json_body={"smart_collection": payload})


def reorder_smart_collection_products(smart_collection_id: int, products: list[int]) -> Any:
    return shopify_request("PUT", f"/smart_collections/{smart_collection_id}/order.json", params={"products[]": products})


def delete_smart_collection(smart_collection_id: int) -> Any:
    return shopify_request("DELETE", f"/smart_collections/{smart_collection_id}.json")
