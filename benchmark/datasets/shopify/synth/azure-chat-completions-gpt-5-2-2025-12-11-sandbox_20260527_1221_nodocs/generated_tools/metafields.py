from typing import Any, Dict, Optional

from .client import request_json


# Metafields (generic + product/order/customer convenience)

def list_metafields(*, limit: int = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", "/metafields.json", params=params)


def get_metafield(metafield_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/metafields/{metafield_id}.json")


def create_metafield(metafield: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/metafields.json", json_body={"metafield": metafield})


def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    body = {"metafield": {**metafield, "id": metafield_id}}
    return request_json("PUT", f"/metafields/{metafield_id}.json", json_body=body)


def delete_metafield(metafield_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/metafields/{metafield_id}.json")


def list_product_metafields(product_id: int, *, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/products/{product_id}/metafields.json", params={"limit": limit})


def list_order_metafields(order_id: int, *, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}/metafields.json", params={"limit": limit})


def list_customer_metafields(customer_id: int, *, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", f"/customers/{customer_id}/metafields.json", params={"limit": limit})
