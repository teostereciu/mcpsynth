from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def create_draft_order(draft_order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def list_draft_orders(
    *,
    client: Optional[ShopifyClient] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    status: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /draft_orders.json"""
    client = client or ShopifyClient()
    params = build_params(
        limit=limit,
        since_id=since_id,
        status=status,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        fields=fields,
    )
    return client.request("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/draft_orders/{draft_order_id}.json", params=build_params(fields=fields))


def count_draft_orders(*, client: Optional[ShopifyClient] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/draft_orders/count.json", params=build_params(status=status))


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return client.request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def delete_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/draft_orders/{draft_order_id}.json")


def send_draft_order_invoice(
    draft_order_id: int,
    invoice: Optional[Dict[str, Any]] = None,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json"""
    client = client or ShopifyClient()
    return client.request(
        "POST",
        f"/draft_orders/{draft_order_id}/send_invoice.json",
        json_body={"draft_order_invoice": invoice} if invoice is not None else {},
    )


def complete_draft_order(
    draft_order_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    payment_pending: Optional[bool] = None,
) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json"""
    client = client or ShopifyClient()
    return client.request(
        "PUT",
        f"/draft_orders/{draft_order_id}/complete.json",
        params=build_params(payment_pending=payment_pending),
    )
