from typing import Any, Dict, Optional

from .http_client import get_client


def order_create(order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders.json

    Args:
        order: Order payload (wrapped under {"order": ...} by this tool).
    """
    return get_client().request("POST", "/orders.json", json_body={"order": order})


def orders_list(
    *,
    status: Optional[str] = None,
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
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {
        "status": status,
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
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", "/orders.json", params=params or None)


def order_get(order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}.json"""
    params = {"fields": fields} if fields else None
    return get_client().request("GET", f"/orders/{order_id}.json", params=params)


def orders_count(*, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/count.json"""
    params = {"status": status} if status else None
    return get_client().request("GET", "/orders/count.json", params=params)


def order_update(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /orders/{order_id}.json"""
    body = {"order": {**order, "id": order_id}}
    return get_client().request("PUT", f"/orders/{order_id}.json", json_body=body)


def order_delete(order_id: int) -> Dict[str, Any]:
    """DELETE /orders/{order_id}.json"""
    return get_client().request("DELETE", f"/orders/{order_id}.json")


def order_cancel(order_id: int, *, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/cancel.json"""
    body: Dict[str, Any] = {}
    for k, v in {"reason": reason, "email": email, "restock": restock}.items():
        if v is not None:
            body[k] = v
    return get_client().request("POST", f"/orders/{order_id}/cancel.json", json_body=body or None)


def order_close(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/close.json"""
    return get_client().request("POST", f"/orders/{order_id}/close.json")


def order_open(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/open.json"""
    return get_client().request("POST", f"/orders/{order_id}/open.json")
