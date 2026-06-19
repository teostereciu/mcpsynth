from typing import Any, Dict, Optional

from ._client import get_client


def create_order(order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders.json

    Doc: docs/api_order.md
    Body wrapper: {"order": {...}}
    """
    client = get_client()
    return client.request("POST", "/orders.json", json={"order": order})


def list_orders(
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
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /orders.json

    Doc: docs/api_order.md
    """
    client = get_client()
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
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}.json

    Doc: docs/api_order.md
    """
    client = get_client()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(
    *,
    status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /orders/count.json

    Doc: docs/api_order.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {
        "status": status,
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
    return client.request("GET", "/orders/count.json", params=params)


def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /orders/{order_id}.json

    Doc: docs/api_order.md
    Body wrapper: {"order": {..., "id": order_id}}
    """
    client = get_client()
    body = dict(order)
    body.setdefault("id", order_id)
    return client.request("PUT", f"/orders/{order_id}.json", json={"order": body})


def delete_order(order_id: int) -> Dict[str, Any]:
    """DELETE /orders/{order_id}.json

    Doc: docs/api_order.md
    """
    client = get_client()
    return client.request("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/cancel.json

    Doc: docs/api_order.md
    Body wrapper: {"order": {...}} (Shopify uses order wrapper for cancel options)
    """
    client = get_client()
    payload = {"order": cancel} if cancel is not None else None
    return client.request("POST", f"/orders/{order_id}/cancel.json", json=payload)


def close_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/close.json

    Doc: docs/api_order.md
    """
    client = get_client()
    return client.request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/open.json

    Doc: docs/api_order.md
    """
    client = get_client()
    return client.request("POST", f"/orders/{order_id}/open.json")
