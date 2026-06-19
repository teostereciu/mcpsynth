from typing import Any, Dict, Optional

from .client import shopify_request


def list_orders(
    *,
    limit: int = 50,
    status: str = "any",
    since_id: Optional[int] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "status": status}
    if since_id is not None:
        params["since_id"] = since_id
    if financial_status is not None:
        params["financial_status"] = financial_status
    if fulfillment_status is not None:
        params["fulfillment_status"] = fulfillment_status
    if created_at_min is not None:
        params["created_at_min"] = created_at_min
    if created_at_max is not None:
        params["created_at_max"] = created_at_max
    if fields is not None:
        params["fields"] = fields
    return shopify_request("GET", "/orders.json", params=params)


def get_order(*, order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return shopify_request("GET", f"/orders/{order_id}.json", params=params)


def update_order(*, order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    body = {"order": {**order, "id": order_id}}
    return shopify_request("PUT", f"/orders/{order_id}.json", json_body=body)


def close_order(*, order_id: int) -> Dict[str, Any]:
    return shopify_request("POST", f"/orders/{order_id}/close.json")


def open_order(*, order_id: int) -> Dict[str, Any]:
    return shopify_request("POST", f"/orders/{order_id}/open.json")


def cancel_order(*, order_id: int, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {}
    if reason is not None:
        body["reason"] = reason
    if email is not None:
        body["email"] = email
    if restock is not None:
        body["restock"] = restock
    return shopify_request("POST", f"/orders/{order_id}/cancel.json", json_body=body if body else None)


def list_order_transactions(*, order_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/orders/{order_id}/transactions.json")


def create_order_transaction(*, order_id: int, transaction: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", f"/orders/{order_id}/transactions.json", json_body={"transaction": transaction})


def create_refund(*, order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})
