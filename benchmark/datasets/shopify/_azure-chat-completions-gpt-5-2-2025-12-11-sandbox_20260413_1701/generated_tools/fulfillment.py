from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


# ---- Fulfillment Orders ----

@mcp.tool()
def list_fulfillment_orders_for_order(order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """Retrieve fulfillment orders for a specific order."""
    return client.request("GET", f"/orders/{order_id}/fulfillment_orders.json")


@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a specific fulfillment order."""
    return client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


@mcp.tool()
def cancel_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Dict[str, Any]:
    """Cancel a fulfillment order."""
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")


@mcp.tool()
def close_fulfillment_order(fulfillment_order_id: Union[int, str], message: Optional[str] = None) -> Dict[str, Any]:
    """Mark a fulfillment order as incomplete (close)."""
    body = {"message": message} if message else None
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/close.json", body=body)


@mcp.tool()
def open_fulfillment_order(fulfillment_order_id: Union[int, str]) -> Dict[str, Any]:
    """Mark a fulfillment order as open."""
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/open.json")


@mcp.tool()
def hold_fulfillment_order(fulfillment_order_id: Union[int, str], hold: Dict[str, Any]) -> Dict[str, Any]:
    """Hold fulfillment of a fulfillment order."""
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", body={"fulfillment_hold": hold})


@mcp.tool()
def release_fulfillment_order_hold(fulfillment_order_id: Union[int, str]) -> Dict[str, Any]:
    """Release all holds on a fulfillment order."""
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json")


@mcp.tool()
def move_fulfillment_order(fulfillment_order_id: Union[int, str], new_location_id: Union[int, str]) -> Dict[str, Any]:
    """Move a fulfillment order to a new location."""
    return client.request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/move.json",
        body={"fulfillment_order": {"new_location_id": int(new_location_id)}},
    )


@mcp.tool()
def reschedule_fulfillment_order(fulfillment_order_id: Union[int, str], fulfill_at: str) -> Dict[str, Any]:
    """Reschedule the fulfill_at time of a scheduled fulfillment order."""
    return client.request(
        "POST",
        f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
        body={"fulfillment_order": {"fulfill_at": fulfill_at}},
    )


# ---- Fulfillments ----

@mcp.tool()
def list_fulfillments_for_order(order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """Retrieve fulfillments associated with an order."""
    return client.request("GET", f"/orders/{order_id}/fulfillments.json")


@mcp.tool()
def get_fulfillment(order_id: Union[int, str], fulfillment_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a single fulfillment for an order."""
    return client.request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")


@mcp.tool()
def count_fulfillments_for_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a count of fulfillments associated with an order."""
    return client.request("GET", f"/orders/{order_id}/fulfillments/count.json")


@mcp.tool()
def list_fulfillments_for_fulfillment_order(fulfillment_order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """Retrieve fulfillments associated with a fulfillment order."""
    return client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")


@mcp.tool()
def create_fulfillment(fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """Create a fulfillment for one or many fulfillment orders.

    The payload should match Shopify's Fulfillment create endpoint.
    Common fields include:
      - line_items_by_fulfillment_order: [{fulfillment_order_id, fulfillment_order_line_items:[{id, quantity}]}]
      - notify_customer: bool
      - tracking_info: {number, company, url}
    """
    return client.request("POST", "/fulfillments.json", body={"fulfillment": fulfillment})


@mcp.tool()
def cancel_fulfillment(fulfillment_id: Union[int, str]) -> Dict[str, Any]:
    """Cancel a fulfillment."""
    return client.request("POST", f"/fulfillments/{fulfillment_id}/cancel.json")


@mcp.tool()
def update_fulfillment_tracking(fulfillment_id: Union[int, str], tracking_info: Dict[str, Any], notify_customer: Optional[bool] = None) -> Dict[str, Any]:
    """Update tracking information for a fulfillment."""
    body: Dict[str, Any] = {"tracking_info": tracking_info}
    if notify_customer is not None:
        body["notify_customer"] = notify_customer
    return client.request("POST", f"/fulfillments/{fulfillment_id}/update_tracking.json", body=body)
