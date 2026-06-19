from typing import Any, Dict, Optional

from .client import request_json


def create_order(order: Dict[str, Any]) -> Any:
    """POST /orders.json"""
    return request_json("POST", "/orders.json", json_body={"order": order})


def list_orders(
    *,
    status: str = "any",
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[int] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Any:
    """GET /orders.json"""
    params: Dict[str, Any] = {"status": status}
    for k, v in {
        "ids": ids,
        "limit": limit,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "processed_at_min": processed_at_min,
        "processed_at_max": processed_at_max,
        "attribution_app_id": attribution_app_id,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None) -> Any:
    """GET /orders/{order_id}.json"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/orders/{order_id}.json", params=params)


def count_orders(
    *,
    status: str = "any",
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
) -> Any:
    """GET /orders/count.json"""
    params: Dict[str, Any] = {"status": status}
    for k, v in {
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "processed_at_min": processed_at_min,
        "processed_at_max": processed_at_max,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/orders/count.json", params=params)


def update_order(order_id: int, order: Dict[str, Any]) -> Any:
    """PUT /orders/{order_id}.json"""
    return request_json("PUT", f"/orders/{order_id}.json", json_body={"order": order})


def delete_order(order_id: int) -> Any:
    """DELETE /orders/{order_id}.json"""
    return request_json("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, *, payload: Optional[Dict[str, Any]] = None) -> Any:
    """POST /orders/{order_id}/cancel.json"""
    return request_json("POST", f"/orders/{order_id}/cancel.json", json_body=(payload or {}))


def close_order(order_id: int) -> Any:
    """POST /orders/{order_id}/close.json"""
    return request_json("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Any:
    """POST /orders/{order_id}/open.json"""
    return request_json("POST", f"/orders/{order_id}/open.json")
