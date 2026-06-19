from typing import Any, Dict, Optional

from .http_client import request_json


def create_order(order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders.json

    Doc: docs/api_order.md
    Body wrapper: {"order": {...}}
    """
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
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /orders.json

    Doc: docs/api_order.md
    """
    params: Dict[str, Any] = {"status": status}
    if ids is not None:
        params["ids"] = ids
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if created_at_min is not None:
        params["created_at_min"] = created_at_min
    if created_at_max is not None:
        params["created_at_max"] = created_at_max
    if updated_at_min is not None:
        params["updated_at_min"] = updated_at_min
    if updated_at_max is not None:
        params["updated_at_max"] = updated_at_max
    if processed_at_min is not None:
        params["processed_at_min"] = processed_at_min
    if processed_at_max is not None:
        params["processed_at_max"] = processed_at_max
    if attribution_app_id is not None:
        params["attribution_app_id"] = attribution_app_id
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}.json

    Doc: docs/api_order.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/orders/{order_id}.json", params=params)


def count_orders(*, status: str = "any") -> Dict[str, Any]:
    """GET /orders/count.json

    Doc: docs/api_order.md
    """
    return request_json("GET", "/orders/count.json", params={"status": status})


def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /orders/{order_id}.json

    Doc: docs/api_order.md
    Body wrapper: {"order": {...}}
    """
    return request_json("PUT", f"/orders/{order_id}.json", json_body={"order": order})


def delete_order(order_id: int) -> Dict[str, Any]:
    """DELETE /orders/{order_id}.json

    Doc: docs/api_order.md
    """
    return request_json("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/cancel.json

    Doc: docs/api_order.md
    Body wrapper: {"cancel": {...}} (optional)
    """
    body = {"cancel": cancel} if cancel is not None else None
    return request_json("POST", f"/orders/{order_id}/cancel.json", json_body=body)


def close_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/close.json

    Doc: docs/api_order.md
    """
    return request_json("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/open.json

    Doc: docs/api_order.md
    """
    return request_json("POST", f"/orders/{order_id}/open.json")
