from typing import Any, Dict, List, Optional

from generated_tools.common import clean_params, shopify_request


def list_products(limit: Optional[int] = None, page_info: Optional[str] = None, title: Optional[str] = None, vendor: Optional[str] = None, product_type: Optional[str] = None, collection_id: Optional[int] = None, status: Optional[str] = None, published_status: Optional[str] = None, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(
        limit=limit,
        page_info=page_info,
        title=title,
        vendor=vendor,
        product_type=product_type,
        collection_id=collection_id,
        status=status,
        published_status=published_status,
        fields=",".join(fields) if fields else None,
    )
    return shopify_request("GET", "/products.json", params=params)


def get_product(product_id: int, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(fields=",".join(fields) if fields else None)
    return shopify_request("GET", f"/products/{product_id}.json", params=params)


def create_product(product: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/products.json", json_body={"product": product})


def update_product(product_id: int, product: Dict[str, Any]) -> Any:
    body = {"product": {"id": product_id, **product}}
    return shopify_request("PUT", f"/products/{product_id}.json", json_body=body)


def delete_product(product_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}.json")


def list_product_variants(product_id: int, limit: Optional[int] = None, page_info: Optional[str] = None, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(limit=limit, page_info=page_info, fields=",".join(fields) if fields else None)
    return shopify_request("GET", f"/products/{product_id}/variants.json", params=params)


def get_variant(variant_id: int, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(fields=",".join(fields) if fields else None)
    return shopify_request("GET", f"/variants/{variant_id}.json", params=params)


def create_variant(product_id: int, variant: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/products/{product_id}/variants.json", json_body={"variant": variant})


def update_variant(variant_id: int, variant: Dict[str, Any]) -> Any:
    body = {"variant": {"id": variant_id, **variant}}
    return shopify_request("PUT", f"/variants/{variant_id}.json", json_body=body)


def delete_variant(product_id: int, variant_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")


def list_product_images(product_id: int, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(fields=",".join(fields) if fields else None)
    return shopify_request("GET", f"/products/{product_id}/images.json", params=params)


def create_product_image(product_id: int, image: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def delete_product_image(product_id: int, image_id: int) -> Any:
    return shopify_request("DELETE", f"/products/{product_id}/images/{image_id}.json")


def list_custom_collections(limit: Optional[int] = None, page_info: Optional[str] = None, title: Optional[str] = None) -> Any:
    params = clean_params(limit=limit, page_info=page_info, title=title)
    return shopify_request("GET", "/custom_collections.json", params=params)


def create_custom_collection(collection: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/custom_collections.json", json_body={"custom_collection": collection})


def list_smart_collections(limit: Optional[int] = None, page_info: Optional[str] = None, title: Optional[str] = None) -> Any:
    params = clean_params(limit=limit, page_info=page_info, title=title)
    return shopify_request("GET", "/smart_collections.json", params=params)


def create_smart_collection(collection: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/smart_collections.json", json_body={"smart_collection": collection})


def collect_product_into_collection(product_id: int, collection_id: int) -> Any:
    return shopify_request("POST", "/collects.json", json_body={"collect": {"product_id": product_id, "collection_id": collection_id}})
