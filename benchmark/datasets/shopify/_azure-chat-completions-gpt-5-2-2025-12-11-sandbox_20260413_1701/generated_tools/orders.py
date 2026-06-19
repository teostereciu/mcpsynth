from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_orders(
    limit: int = 50,
    status: str = "any",
    fields: Optional[str] = None,
    ids: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[Union[int, str]] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    order: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Retrieve a list of orders."""
    params: Dict[str, Any] = {"limit": limit, "status": status}
    for k, v in {
        "fields": fields,
        "ids": ids,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "processed_at_min": processed_at_min,
        "processed_at_max": processed_at_max,
        "attribution_app_id": attribution_app_id,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "order": order,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/orders.json", params=params)


@mcp.tool()
def get_order(order_id: Union[int, str], fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a specific order."""
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


@mcp.tool()
def count_orders(status: str = "any") -> Dict[str, Any]:
    """Retrieve an order count."""
    return client.request("GET", "/orders/count.json", params={"status": status})


@mcp.tool()
def create_order(order: Dict[str, Any]) -> Dict[str, Any]:
    """Create an order."""
    return client.request("POST", "/orders.json", body={"order": order})


@mcp.tool()
def update_order(order_id: Union[int, str], order: Dict[str, Any]) -> Dict[str, Any]:
    """Update an order."""
    payload = dict(order)
    payload["id"] = int(order_id) if str(order_id).isdigit() else order_id
    return client.request("PUT", f"/orders/{order_id}.json", body={"order": payload})


@mcp.tool()
def delete_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Delete an order."""
    return client.request("DELETE", f"/orders/{order_id}.json", unwrap=False)


@mcp.tool()
def cancel_order(
    order_id: Union[int, str],
    reason: Optional[str] = None,
    email: Optional[bool] = None,
    restock: Optional[bool] = None,
    refund: Optional[bool] = None,
) -> Dict[str, Any]:
    """Cancel an order."""
    body: Dict[str, Any] = {}
    for k, v in {"reason": reason, "email": email, "restock": restock, "refund": refund}.items():
        if v is not None:
            body[k] = v
    return client.request("POST", f"/orders/{order_id}/cancel.json", body=body or None)


@mcp.tool()
def close_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Close an order."""
    return client.request("POST", f"/orders/{order_id}/close.json")


@mcp.tool()
def open_order(order_id: Union[int, str]) -> Dict[str, Any]:
    """Re-open a closed order."""
    return client.request("POST", f"/orders/{order_id}/open.json")


@mcp.tool()
def list_refunds(order_id: Union[int, str]) -> List[Dict[str, Any]]:
    """Retrieve a list of refunds for an order."""
    return client.request("GET", f"/orders/{order_id}/refunds.json")


@mcp.tool()
def get_refund(order_id: Union[int, str], refund_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a specific refund."""
    return client.request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")


@mcp.tool()
def calculate_refund(order_id: Union[int, str], refund: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate a refund (recommended before creating)."""
    return client.request(
        "POST",
        f"/orders/{order_id}/refunds/calculate.json",
        body={"refund": refund},
    )


@mcp.tool()
def create_refund(order_id: Union[int, str], refund: Dict[str, Any]) -> Dict[str, Any]:
    """Create a refund for an order."""
    return client.request("POST", f"/orders/{order_id}/refunds.json", body={"refund": refund})
