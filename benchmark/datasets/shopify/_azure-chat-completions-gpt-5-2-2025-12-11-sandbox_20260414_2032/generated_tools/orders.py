from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def list_orders(
    status: str = "any",
    limit: int = 50,
    fields: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List orders.

    Args:
        status: open|closed|cancelled|any.
        limit: Max number of orders.
        fields: Comma-separated fields.
        since_id: Return orders after this ID.
        financial_status: Filter by financial status.
        fulfillment_status: Filter by fulfillment status.
        created_at_min/max: ISO8601 timestamps.
    """

    params: Dict[str, Any] = {"status": status, "limit": limit}
    if fields:
        params["fields"] = fields
    if since_id is not None:
        params["since_id"] = since_id
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max

    data = shopify_request("GET", "/orders.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_order(order_id: Union[int, str], fields: Optional[str] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a single order."""

    params = {"fields": fields} if fields else None
    data = shopify_request("GET", f"/orders/{order_id}.json", params=params)
    if "error" in data:
        return {"error": f"Order {order_id} not found or could not be retrieved", **data}
    return unwrap_envelope(data)


@mcp.tool()
def cancel_order(
    order_id: Union[int, str],
    reason: Optional[str] = None,
    email: Optional[bool] = None,
    restock: Optional[bool] = None,
    refund: Optional[bool] = None,
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Cancel an order.

    Args:
        reason: customer|inventory|fraud|declined|other.
        email: Send cancellation email.
        restock: Restock items.
        refund: Refund payment.
    """

    body: Dict[str, Any] = {}
    if reason:
        body["reason"] = reason
    if email is not None:
        body["email"] = bool(email)
    if restock is not None:
        body["restock"] = bool(restock)
    if refund is not None:
        body["refund"] = bool(refund)

    data = shopify_request("POST", f"/orders/{order_id}/cancel.json", body=body or None)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def close_order(order_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Close an order."""

    data = shopify_request("POST", f"/orders/{order_id}/close.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def open_order(order_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Re-open a closed order."""

    data = shopify_request("POST", f"/orders/{order_id}/open.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_order(order_id: Union[int, str], order: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update an order (limited fields)."""

    payload = dict(order)
    payload["id"] = int(order_id) if str(order_id).isdigit() else order_id
    data = shopify_request("PUT", f"/orders/{order_id}.json", body={"order": payload})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def delete_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Delete an order."""

    data = shopify_request("DELETE", f"/orders/{order_id}.json")
    if "error" in data:
        return data
    return {"ok": True}


@mcp.tool()
def count_orders(status: str = "any") -> Union[int, Dict[str, Any]]:
    """Count orders."""

    data = shopify_request("GET", "/orders/count.json", params={"status": status})
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped
