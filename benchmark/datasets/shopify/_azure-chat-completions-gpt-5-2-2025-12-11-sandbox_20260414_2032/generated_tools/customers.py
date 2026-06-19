from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def list_customers(limit: int = 50, fields: Optional[str] = None, since_id: Optional[Union[int, str]] = None) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List customers."""

    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    if since_id is not None:
        params["since_id"] = since_id

    data = shopify_request("GET", "/customers.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def search_customers(query: str, limit: int = 50, fields: Optional[str] = None) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """Search customers using Shopify query syntax.

    Example query: "email:bob.norman@mail.example.com"
    """

    params: Dict[str, Any] = {"query": query, "limit": limit}
    if fields:
        params["fields"] = fields

    data = shopify_request("GET", "/customers/search.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_customer(customer_id: Union[int, str], fields: Optional[str] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a customer by ID."""

    params = {"fields": fields} if fields else None
    data = shopify_request("GET", f"/customers/{customer_id}.json", params=params)
    if "error" in data:
        return {"error": f"Customer {customer_id} not found or could not be retrieved", **data}
    return unwrap_envelope(data)


@mcp.tool()
def create_customer(customer: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a customer."""

    data = shopify_request("POST", "/customers.json", body={"customer": customer})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_customer(customer_id: Union[int, str], customer: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update a customer."""

    payload = dict(customer)
    payload["id"] = int(customer_id) if str(customer_id).isdigit() else customer_id
    data = shopify_request("PUT", f"/customers/{customer_id}.json", body={"customer": payload})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_customer_orders(customer_id: Union[int, str], limit: int = 50, status: str = "any") -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List orders for a customer."""

    data = shopify_request(
        "GET",
        f"/customers/{customer_id}/orders.json",
        params={"limit": limit, "status": status},
    )
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def count_customers() -> Union[int, Dict[str, Any]]:
    """Count customers."""

    data = shopify_request("GET", "/customers/count.json")
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped


@mcp.tool()
def create_customer_account_activation_url(customer_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create an account activation URL for a customer."""

    data = shopify_request("POST", f"/customers/{customer_id}/account_activation_url.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def send_customer_invite(customer_id: Union[int, str], invite: Optional[Dict[str, Any]] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Send an account invite to a customer."""

    body = {"customer_invite": invite} if invite else None
    data = shopify_request("POST", f"/customers/{customer_id}/send_invite.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)
