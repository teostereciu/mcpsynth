from typing import Any, Dict, Optional

from .http import request_json


def create_metafield(resource_path: str, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST {resource_path}/metafields.json

    resource_path examples:
      /products/{product_id}
      /orders/{order_id}
      /customers/{customer_id}
      /blogs/{blog_id}

    This doc is generic; Shopify supports metafields on many resources.
    """
    if not resource_path.startswith("/"):
        resource_path = "/" + resource_path
    return request_json("POST", f"{resource_path}/metafields.json", json_body={"metafield": metafield})


def list_metafields(resource_path: str, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET {resource_path}/metafields.json"""
    if not resource_path.startswith("/"):
        resource_path = "/" + resource_path
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"{resource_path}/metafields.json", params=params)


def get_metafield(resource_path: str, metafield_id: int) -> Dict[str, Any]:
    """GET {resource_path}/metafields/{metafield_id}.json"""
    if not resource_path.startswith("/"):
        resource_path = "/" + resource_path
    return request_json("GET", f"{resource_path}/metafields/{metafield_id}.json")


def count_metafields(resource_path: str) -> Dict[str, Any]:
    """GET {resource_path}/metafields/count.json"""
    if not resource_path.startswith("/"):
        resource_path = "/" + resource_path
    return request_json("GET", f"{resource_path}/metafields/count.json")


def update_metafield(resource_path: str, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT {resource_path}/metafields/{metafield_id}.json"""
    if not resource_path.startswith("/"):
        resource_path = "/" + resource_path
    return request_json(
        "PUT",
        f"{resource_path}/metafields/{metafield_id}.json",
        json_body={"metafield": metafield},
    )


def delete_metafield(resource_path: str, metafield_id: int) -> Dict[str, Any]:
    """DELETE {resource_path}/metafields/{metafield_id}.json"""
    if not resource_path.startswith("/"):
        resource_path = "/" + resource_path
    return request_json("DELETE", f"{resource_path}/metafields/{metafield_id}.json")
