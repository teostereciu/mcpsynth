from typing import Any, Dict, Optional

from shopify_api import shopify_request


def create_order(order: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/orders.json", json_body={"order": order})


def list_orders(status: str = "any", limit: Optional[int] = None, financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None, created_at_min: Optional[str] = None, updated_at_min: Optional[str] = None) -> Any:
    params = {
        "status": status,
        "limit": limit,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "created_at_min": created_at_min,
        "updated_at_min": updated_at_min,
    }
    return shopify_request("GET", "/orders.json", params=params)


def get_order(order_id: int, fields: Optional[str] = None) -> Any:
    return shopify_request("GET", f"/orders/{order_id}.json", params={"fields": fields})


def count_orders(status: str = "any") -> Any:
    return shopify_request("GET", "/orders/count.json", params={"status": status})


def update_order(order_id: int, order: Dict[str, Any]) -> Any:
    payload = dict(order)
    payload["id"] = order_id
    return shopify_request("PUT", f"/orders/{order_id}.json", json_body={"order": payload})


def delete_order(order_id: int) -> Any:
    return shopify_request("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, refund: Optional[bool] = None, restock: Optional[bool] = None, reason: Optional[str] = None, email: Optional[bool] = None, amount: Optional[str] = None) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/cancel.json", json_body={"refund": refund, "restock": restock, "reason": reason, "email": email, "amount": amount})


def close_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/open.json")
