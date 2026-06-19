from typing import Any, Dict, List, Optional

from generated_tools.common import clean_params, shopify_request


def list_orders(limit: Optional[int] = None, page_info: Optional[str] = None, status: Optional[str] = None, financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None, created_at_min: Optional[str] = None, created_at_max: Optional[str] = None, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(
        limit=limit,
        page_info=page_info,
        status=status,
        financial_status=financial_status,
        fulfillment_status=fulfillment_status,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        fields=",".join(fields) if fields else None,
    )
    return shopify_request("GET", "/orders.json", params=params)


def get_order(order_id: int, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(fields=",".join(fields) if fields else None)
    return shopify_request("GET", f"/orders/{order_id}.json", params=params)


def create_order(order: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/orders.json", json_body={"order": order})


def update_order(order_id: int, order: Dict[str, Any]) -> Any:
    body = {"order": {"id": order_id, **order}}
    return shopify_request("PUT", f"/orders/{order_id}.json", json_body=body)


def close_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/open.json")


def cancel_order(order_id: int, amount: Optional[str] = None, currency: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None, reason: Optional[str] = None) -> Any:
    body = clean_params(amount=amount, currency=currency, email=email, restock=restock, reason=reason)
    return shopify_request("POST", f"/orders/{order_id}/cancel.json", json_body=body or None)


def list_transactions(order_id: int) -> Any:
    return shopify_request("GET", f"/orders/{order_id}/transactions.json")


def create_transaction(order_id: int, transaction: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/transactions.json", json_body={"transaction": transaction})


def calculate_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/refunds/calculate.json", json_body={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


def list_draft_orders(limit: Optional[int] = None, page_info: Optional[str] = None, status: Optional[str] = None) -> Any:
    params = clean_params(limit=limit, page_info=page_info, status=status)
    return shopify_request("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int) -> Any:
    return shopify_request("GET", f"/draft_orders/{draft_order_id}.json")


def create_draft_order(draft_order: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Any:
    body = {"draft_order": {"id": draft_order_id, **draft_order}}
    return shopify_request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def complete_draft_order(draft_order_id: int, payment_pending: Optional[bool] = None) -> Any:
    params = clean_params(payment_pending=payment_pending)
    return shopify_request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def delete_draft_order(draft_order_id: int) -> Any:
    return shopify_request("DELETE", f"/draft_orders/{draft_order_id}.json")
