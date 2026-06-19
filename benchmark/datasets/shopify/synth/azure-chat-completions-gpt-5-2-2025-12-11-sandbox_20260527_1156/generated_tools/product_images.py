from typing import Any, Dict, Optional

from ._client import get_client


def create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/images.json

    Doc: docs/api_product-image.md
    Body wrapper: {"image": {...}}
    """
    client = get_client()
    return client.request("POST", f"/products/{product_id}/images.json", json={"image": image})


def list_product_images(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /products/{product_id}/images.json

    Doc: docs/api_product-image.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/products/{product_id}/images.json", params=params)


def get_product_image(product_id: int, image_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /products/{product_id}/images/{image_id}.json

    Doc: docs/api_product-image.md
    """
    client = get_client()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/products/{product_id}/images/{image_id}.json", params=params)


def count_product_images(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/images/count.json

    Doc: docs/api_product-image.md
    """
    client = get_client()
    return client.request("GET", f"/products/{product_id}/images/count.json")


def update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}/images/{image_id}.json

    Doc: docs/api_product-image.md
    Body wrapper: {"image": {..., "id": image_id}}
    """
    client = get_client()
    body = dict(image)
    body.setdefault("id", image_id)
    return client.request(
        "PUT",
        f"/products/{product_id}/images/{image_id}.json",
        json={"image": body},
    )


def delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/images/{image_id}.json

    Doc: docs/api_product-image.md
    """
    client = get_client()
    return client.request("DELETE", f"/products/{product_id}/images/{image_id}.json")
