from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


# Fulfillment Orders
@mcp.tool()
def list_fulfillment_orders(order_id: Union[int, str]) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List fulfillment orders for an order."""

    data = shopify_request("GET", f"/orders/{order_id}/fulfillment_orders.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a fulfillment order by ID."""

    data = shopify_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def open_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Mark a fulfillment order as open."""

    data = shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def close_fulfillment_order(fulfillment_order_id: Union[int, str], message: Optional[str] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Mark a fulfillment order as incomplete (close)."""

    body = {"message": message} if message else None
    data = shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def cancel_fulfillment_order(fulfillment_order_id: Union[int, str], message: Optional[str] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Cancel a fulfillment order."""

    body = {"message": message} if message else None
    data = shopify_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)


# Fulfillments
@mcp.tool()
def create_fulfillment(
    line_items_by_fulfillment_order: List[Dict[str, Any]],
    notify_customer: bool = False,
    tracking_info: Optional[Dict[str, Any]] = None,
    message: Optional[str] = None,
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a fulfillment for one or many fulfillment orders.

    Args:
        line_items_by_fulfillment_order: List of objects like:
            {"fulfillment_order_id": 123, "fulfillment_order_line_items": [{"id": 456, "quantity": 1}]}
            If you omit fulfillment_order_line_items, Shopify may fulfill all fulfillable items.
        notify_customer: Whether to notify customer.
        tracking_info: Optional tracking info dict.
        message: Optional message.
    """

    fulfillment: Dict[str, Any] = {
        "line_items_by_fulfillment_order": line_items_by_fulfillment_order,
        "notify_customer": bool(notify_customer),
    }
    if tracking_info:
        fulfillment["tracking_info"] = tracking_info
    if message:
        fulfillment["message"] = message

    data = shopify_request("POST", "/fulfillments.json", body={"fulfillment": fulfillment})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def list_order_fulfillments(order_id: Union[int, str]) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List fulfillments for an order."""

    data = shopify_request("GET", f"/orders/{order_id}/fulfillments.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_order_fulfillment(order_id: Union[int, str], fulfillment_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a fulfillment for an order."""

    data = shopify_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def list_fulfillment_order_fulfillments(fulfillment_order_id: Union[int, str]) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List fulfillments for a fulfillment order."""

    data = shopify_request("GET", f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def count_order_fulfillments(order_id: Union[int, str]) -> Union[int, Dict[str, Any]]:
    """Count fulfillments for an order."""

    data = shopify_request("GET", f"/orders/{order_id}/fulfillments/count.json")
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped


@mcp.tool()
def cancel_fulfillment(fulfillment_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Cancel a fulfillment."""

    data = shopify_request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_fulfillment_tracking(
    fulfillment_id: Union[int, str],
    tracking_info: Dict[str, Any],
    notify_customer: Optional[bool] = None,
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update tracking information for a fulfillment."""

    body: Dict[str, Any] = {"tracking_info": tracking_info}
    if notify_customer is not None:
        body["notify_customer"] = bool(notify_customer)

    data = shopify_request("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)
