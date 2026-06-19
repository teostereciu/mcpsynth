from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_orders(
    *,
    status: str = "any",
    limit: Optional[int] = 50,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders.json"""
    params: Dict[str, Any] = {"status": status}
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
    if financial_status is not None:
        params["financial_status"] = financial_status
    if fulfillment_status is not None:
        params["fulfillment_status"] = fulfillment_status
    if fields is not None:
        params["fields"] = fields

    return ShopifyClient().request("GET", "/orders.json", params=params)


def get_order(*, order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}.json"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(*, status: str = "any", financial_status: Optional[str] = None, fulfillment_status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/count.json"""
    params: Dict[str, Any] = {"status": status}
    if financial_status is not None:
        params["financial_status"] = financial_status
    if fulfillment_status is not None:
        params["fulfillment_status"] = fulfillment_status
    return ShopifyClient().request("GET", "/orders/count.json", params=params)


def create_order(*, order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders.json"""
    return ShopifyClient().request("POST", "/orders.json", json_body={"order": order})


def update_order(*, order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/orders/{order_id}.json"""
    body = {"order": {**order, "id": order_id}}
    return ShopifyClient().request("PUT", f"/orders/{order_id}.json", json_body=body)


def delete_order(*, order_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/orders/{order_id}.json"""
    return ShopifyClient().request("DELETE", f"/orders/{order_id}.json")


def cancel_order(*, order_id: int, amount: Optional[str] = None, email: Optional[bool] = None, reason: Optional[str] = None, restock: Optional[bool] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/cancel.json"""
    body: Dict[str, Any] = {}
    if amount is not None:
        body["amount"] = amount
    if email is not None:
        body["email"] = email
    if reason is not None:
        body["reason"] = reason
    if restock is not None:
        body["restock"] = restock
    return ShopifyClient().request("POST", f"/orders/{order_id}/cancel.json", json_body=body or None)


def close_order(*, order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/close.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/close.json")


def open_order(*, order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/open.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/open.json")


# Draft orders

def list_draft_orders(*, limit: Optional[int] = 50, since_id: Optional[int] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if status is not None:
        params["status"] = status
    return ShopifyClient().request("GET", "/draft_orders.json", params=params)


def get_draft_order(*, draft_order_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    return ShopifyClient().request("GET", f"/draft_orders/{draft_order_id}.json")


def count_draft_orders() -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders/count.json"""
    return ShopifyClient().request("GET", "/draft_orders/count.json")


def create_draft_order(*, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders.json"""
    return ShopifyClient().request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def update_draft_order(*, draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return ShopifyClient().request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def delete_draft_order(*, draft_order_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    return ShopifyClient().request("DELETE", f"/draft_orders/{draft_order_id}.json")


def send_draft_order_invoice(*, draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders/{draft_order_id}/send_invoice.json"""
    body = {"draft_order_invoice": invoice} if invoice is not None else None
    return ShopifyClient().request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)


def complete_draft_order(*, draft_order_id: int, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}/complete.json"""
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = payment_pending
    return ShopifyClient().request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params or None)
