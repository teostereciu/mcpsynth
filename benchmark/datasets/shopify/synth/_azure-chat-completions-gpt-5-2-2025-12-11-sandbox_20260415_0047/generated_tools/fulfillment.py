from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


# Fulfillment orders

@mcp.tool()
def list_fulfillment_orders(order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """List fulfillment orders for an order (GET /orders/{order_id}/fulfillment_orders.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/orders/{order_id}/fulfillment_orders.json")
    return unwrap_envelope(data)


@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Dict[str, Any]:
    """Get a fulfillment order (GET /fulfillment_orders/{id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")
    return unwrap_envelope(data)


@mcp.tool()
def open_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Dict[str, Any]:
    """Mark fulfillment order as open (POST /fulfillment_orders/{id}/open.json)."""
    client = ShopifyClient()
    data = client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")
    return unwrap_envelope(data)


@mcp.tool()
def close_fulfillment_order(fulfillment_order_id: Union[int, str], message: Optional[str] = None) -> Dict[str, Any]:
    """Close fulfillment order (POST /fulfillment_orders/{id}/close.json)."""
    client = ShopifyClient()
    body = {"message": message} if message else None
    data = client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", body=body)
    return unwrap_envelope(data)


@mcp.tool()
def cancel_fulfillment_order(fulfillment_order_id: Union[int, str], message: Optional[str] = None) -> Dict[str, Any]:
    """Cancel fulfillment order (POST /fulfillment_orders/{id}/cancel.json)."""
    client = ShopifyClient()
    body = {"message": message} if message else None
    data = client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", body=body)
    return unwrap_envelope(data)


# Fulfillments

@mcp.tool()
def create_fulfillment(
    line_items_by_fulfillment_order: List[Dict[str, Any]],
    notify_customer: Optional[bool] = None,
    tracking_info: Optional[Dict[str, Any]] = None,
    message: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a fulfillment (POST /fulfillments.json).

    Args:
        line_items_by_fulfillment_order: List entries like {"fulfillment_order_id": ..., "fulfillment_order_line_items": [{"id": ..., "quantity": ...}, ...]}
        notify_customer: Whether to notify customer.
        tracking_info: Optional tracking info dict.
        message: Optional message.
    """
    client = ShopifyClient()
    fulfillment: Dict[str, Any] = {"line_items_by_fulfillment_order": line_items_by_fulfillment_order}
    if notify_customer is not None:
        fulfillment["notify_customer"] = notify_customer
    if tracking_info is not None:
        fulfillment["tracking_info"] = tracking_info
    if message is not None:
        fulfillment["message"] = message

    data = client.request("POST", "/fulfillments.json", body={"fulfillment": fulfillment})
    return unwrap_envelope(data)


@mcp.tool()
def list_order_fulfillments(order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """List fulfillments for an order (GET /orders/{order_id}/fulfillments.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/orders/{order_id}/fulfillments.json")
    return unwrap_envelope(data)


@mcp.tool()
def get_order_fulfillment(order_id: Union[int, str], fulfillment_id: Union[int, str]) -> Dict[str, Any]:
    """Get a fulfillment for an order (GET /orders/{order_id}/fulfillments/{fulfillment_id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")
    return unwrap_envelope(data)


@mcp.tool()
def list_fulfillment_order_fulfillments(fulfillment_order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """List fulfillments for a fulfillment order (GET /fulfillment_orders/{id}/fulfillments.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")
    return unwrap_envelope(data)


@mcp.tool()
def cancel_fulfillment(fulfillment_id: Union[int, str]) -> Dict[str, Any]:
    """Cancel a fulfillment (POST /fulfillments/{id}/cancel.json)."""
    client = ShopifyClient()
    data = client.request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")
    return unwrap_envelope(data)


@mcp.tool()
def update_fulfillment_tracking(
    fulfillment_id: Union[int, str],
    tracking_info: Dict[str, Any],
    notify_customer: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update tracking info (POST /fulfillments/{id}/update_tracking.json)."""
    client = ShopifyClient()
    body: Dict[str, Any] = {"tracking_info": tracking_info}
    if notify_customer is not None:
        body["notify_customer"] = notify_customer
    data = client.request("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", body=body)
    return unwrap_envelope(data)
