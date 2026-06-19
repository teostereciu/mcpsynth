from typing import Any, Dict, Optional

from generated_tools.common import shopify_request


def create_order(order: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/orders.json", json_body={"order": order})


def list_orders(status: Optional[str] = None, financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None, limit: Optional[int] = None, since_id: Optional[int] = None, created_at_min: Optional[str] = None, created_at_max: Optional[str] = None, updated_at_min: Optional[str] = None, updated_at_max: Optional[str] = None, processed_at_min: Optional[str] = None, processed_at_max: Optional[str] = None, fields: Optional[str] = None) -> Any:
    params = {k: v for k, v in {
        "status": status,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "limit": limit,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "processed_at_min": processed_at_min,
        "processed_at_max": processed_at_max,
        "fields": fields,
    }.items() if v is not None}
    return shopify_request("GET", "/orders.json", params=params)


def get_order(order_id: int, fields: Optional[str] = None, status: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"fields": fields, "status": status}.items() if v is not None}
    return shopify_request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(status: Optional[str] = None, financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"status": status, "financial_status": financial_status, "fulfillment_status": fulfillment_status}.items() if v is not None}
    return shopify_request("GET", "/orders/count.json", params=params)


def update_order(order_id: int, order: Dict[str, Any]) -> Any:
    payload = dict(order)
    payload.setdefault("id", order_id)
    return shopify_request("PUT", f"/orders/{order_id}.json", json_body={"order": payload})


def delete_order(order_id: int) -> Any:
    return shopify_request("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, amount: Optional[str] = None, currency: Optional[str] = None, email: Optional[bool] = None, reason: Optional[str] = None, refund: Optional[bool] = None, restock: Optional[bool] = None) -> Any:
    payload = {k: v for k, v in {
        "amount": amount,
        "currency": currency,
        "email": email,
        "reason": reason,
        "refund": refund,
        "restock": restock,
    }.items() if v is not None}
    return shopify_request("POST", f"/orders/{order_id}/cancel.json", json_body=payload or None)


def close_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/open.json")


def calculate_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/refunds/calculate.json", json_body={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


def list_refunds(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/refunds.json")


def get_refund(order_id: int, refund_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")
