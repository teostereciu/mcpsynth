from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def calculate_refund(order_id: Union[int, str], refund: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Calculate a refund for an order.

    Args:
        order_id: Order ID.
        refund: Refund calculation payload (Refund resource input).

    Returns:
        Calculated refund object (envelope unwrapped) or error dict.
    """

    data = shopify_request(
        "POST",
        f"/orders/{order_id}/refunds/calculate.json",
        body={"refund": refund},
    )
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def create_refund(order_id: Union[int, str], refund: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a refund for an order.

    Args:
        order_id: Order ID.
        refund: Refund payload.

    Returns:
        Refund object or error dict.
    """

    data = shopify_request("POST", f"/orders/{order_id}/refunds.json", body={"refund": refund})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def list_refunds(order_id: Union[int, str]) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List refunds for an order."""

    data = shopify_request("GET", f"/orders/{order_id}/refunds.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_refund(order_id: Union[int, str], refund_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a specific refund."""

    data = shopify_request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)
