from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


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
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """List orders (GET /orders.json)."""
    client = ShopifyClient()
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
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max

    data = client.request("GET", "/orders.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def get_order(order_id: Union[int, str], fields: Optional[str] = None) -> Dict[str, Any]:
    """Get a specific order (GET /orders/{order_id}.json)."""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    data = client.request("GET", f"/orders/{order_id}.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def cancel_order(
    order_id: Union[int, str],
    reason: Optional[str] = None,
    email: Optional[bool] = None,
    restock: Optional[bool] = None,
    refund: Optional[bool] = None,
) -> Dict[str, Any]:
    """Cancel an order (POST /orders/{order_id}/cancel.json)."""
    client = ShopifyClient()
    body: Dict[str, Any] = {}
    if reason:
        body["reason"] = reason
    if email is not None:
        body["email"] = email
    if restock is not None:
        body["restock"] = restock
    if refund is not None:
        body["refund"] = refund

    data = client.request("POST", f"/orders/{order_id}/cancel.json", body=body or None)
    return unwrap_envelope(data)


@mcp.tool()
def close_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Close an order (POST /orders/{order_id}/close.json)."""
    client = ShopifyClient()
    data = client.request("POST", f"/orders/{order_id}/close.json")
    return unwrap_envelope(data)


@mcp.tool()
def open_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Re-open a closed order (POST /orders/{order_id}/open.json)."""
    client = ShopifyClient()
    data = client.request("POST", f"/orders/{order_id}/open.json")
    return unwrap_envelope(data)


@mcp.tool()
def update_order(order_id: Union[int, str], order: Dict[str, Any]) -> Dict[str, Any]:
    """Update an order (PUT /orders/{order_id}.json)."""
    client = ShopifyClient()
    payload = dict(order)
    payload["id"] = int(order_id) if str(order_id).isdigit() else order_id
    data = client.request("PUT", f"/orders/{order_id}.json", body={"order": payload})
    return unwrap_envelope(data)


@mcp.tool()
def delete_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Delete an order (DELETE /orders/{order_id}.json)."""
    client = ShopifyClient()
    return client.request("DELETE", f"/orders/{order_id}.json")


@mcp.tool()
def calculate_refund(order_id: Union[int, str], refund: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate a refund (POST /orders/{order_id}/refunds/calculate.json)."""
    client = ShopifyClient()
    data = client.request(
        "POST",
        f"/orders/{order_id}/refunds/calculate.json",
        body={"refund": refund},
    )
    return unwrap_envelope(data)


@mcp.tool()
def create_refund(order_id: Union[int, str], refund: Dict[str, Any]) -> Dict[str, Any]:
    """Create a refund (POST /orders/{order_id}/refunds.json)."""
    client = ShopifyClient()
    data = client.request("POST", f"/orders/{order_id}/refunds.json", body={"refund": refund})
    return unwrap_envelope(data)


@mcp.tool()
def list_refunds(order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """List refunds for an order (GET /orders/{order_id}/refunds.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/orders/{order_id}/refunds.json")
    return unwrap_envelope(data)


@mcp.tool()
def get_refund(order_id: Union[int, str], refund_id: Union[int, str]) -> Dict[str, Any]:
    """Get a specific refund (GET /orders/{order_id}/refunds/{refund_id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")
    return unwrap_envelope(data)
