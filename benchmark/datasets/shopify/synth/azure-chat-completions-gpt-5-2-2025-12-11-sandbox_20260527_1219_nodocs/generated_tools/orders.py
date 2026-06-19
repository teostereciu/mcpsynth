from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_orders(
    *,
    limit: Optional[int] = 50,
    page_info: Optional[str] = None,
    since_id: Optional[int] = None,
    status: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /orders.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if status is not None:
        params["status"] = status
    if financial_status is not None:
        params["financial_status"] = financial_status
    if fulfillment_status is not None:
        params["fulfillment_status"] = fulfillment_status
    if created_at_min is not None:
        params["created_at_min"] = created_at_min
    if created_at_max is not None:
        params["created_at_max"] = created_at_max
    if updated_at_min is not None:
        params["updated_at_min"] = updated_at_min
    if updated_at_max is not None:
        params["updated_at_max"] = updated_at_max
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", "/orders.json", params=params)


def get_order(*, order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", f"/orders/{order_id}.json", params=params)


def update_order(*, order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /orders/{order_id}.json"""
    c = ShopifyClient()
    body = {"order": {**order, "id": order_id}}
    return c.request("PUT", f"/orders/{order_id}.json", json=body)


def close_order(*, order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/close.json"""
    c = ShopifyClient()
    return c.request("POST", f"/orders/{order_id}/close.json")


def open_order(*, order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/open.json"""
    c = ShopifyClient()
    return c.request("POST", f"/orders/{order_id}/open.json")


def cancel_order(*, order_id: int, amount: Optional[str] = None, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/cancel.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if reason is not None:
        params["reason"] = reason
    if email is not None:
        params["email"] = email
    if restock is not None:
        params["restock"] = restock
    return c.request("POST", f"/orders/{order_id}/cancel.json", params=params)


def list_order_transactions(*, order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions.json"""
    c = ShopifyClient()
    return c.request("GET", f"/orders/{order_id}/transactions.json")


def create_order_refund(*, order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds.json"""
    c = ShopifyClient()
    return c.request("POST", f"/orders/{order_id}/refunds.json", json={"refund": refund})


def list_draft_orders(*, limit: Optional[int] = 50, page_info: Optional[str] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", "/draft_orders.json", params=params)


def get_draft_order(*, draft_order_id: int) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/draft_orders/{draft_order_id}.json")


def create_draft_order(*, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    c = ShopifyClient()
    return c.request("POST", "/draft_orders.json", json={"draft_order": draft_order})


def update_draft_order(*, draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json"""
    c = ShopifyClient()
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return c.request("PUT", f"/draft_orders/{draft_order_id}.json", json=body)


def complete_draft_order(*, draft_order_id: int, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = payment_pending
    return c.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)
