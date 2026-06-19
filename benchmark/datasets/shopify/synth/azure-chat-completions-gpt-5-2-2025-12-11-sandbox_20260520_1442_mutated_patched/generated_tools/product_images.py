from typing import Any, Dict, Optional

from .http_client import request_json


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json

    Doc: docs/api_product-image.md
    Body wrapper: {"image": {...}}
    """
    return request_json("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def list_product_images(product_id: int, *, since_id: Optional[int] = None, limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json

    Doc: docs/api_product-image.md
    """
    params: Dict[str, Any] = {}
    if since_id is not None:
        params["since_id"] = since_id
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}/images.json", params=params)


def get_product_image(product_id: int, image_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/images/{image_id}.json

    Doc: docs/api_product-image.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/products/{product_id}/images/{image_id}.json", params=params)


def count_product_images(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/images/count.json

    Doc: docs/api_product-image.md
    """
    return request_json("GET", f"/products/{product_id}/images/count.json")


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}/images/{image_id}.json

    Doc: docs/api_product-image.md
    Body wrapper: {"image": {...}}
    """
    return request_json("PUT", f"/products/{product_id}/images/{image_id}.json", json_body={"image": image})


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/images/{image_id}.json

    Doc: docs/api_product-image.md
    """
    return request_json("DELETE", f"/products/{product_id}/images/{image_id}.json")
