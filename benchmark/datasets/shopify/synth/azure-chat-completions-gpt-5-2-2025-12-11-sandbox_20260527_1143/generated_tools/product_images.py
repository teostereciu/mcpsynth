from typing import Any, Dict, Optional

from .http import request_json


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json"""
    return request_json("POST", f"/products/{product_id}/images.json", json_body={"image": image})


def list_product_images(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/products/{product_id}/images.json", params=params)


def get_product_image(product_id: int, image_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/images/{image_id}.json"""
    params = {"fields": fields} if fields else None
    return request_json("GET", f"/products/{product_id}/images/{image_id}.json", params=params)


def count_product_images(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/images/count.json"""
    return request_json("GET", f"/products/{product_id}/images/count.json")


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}/images/{image_id}.json"""
    return request_json(
        "PUT",
        f"/products/{product_id}/images/{image_id}.json",
        json_body={"image": image},
    )


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/images/{image_id}.json"""
    return request_json("DELETE", f"/products/{product_id}/images/{image_id}.json")
