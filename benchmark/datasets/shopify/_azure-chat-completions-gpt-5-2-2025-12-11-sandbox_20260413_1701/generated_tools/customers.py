from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_customers(
    limit: int = 50,
    fields: Optional[str] = None,
    ids: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Retrieve a list of customers."""
    params: Dict[str, Any] = {"limit": limit}
    for k, v in {
        "fields": fields,
        "ids": ids,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/customers.json", params=params)


@mcp.tool()
def get_customer(customer_id: Union[int, str], fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a single customer."""
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/customers/{customer_id}.json", params=params)


@mcp.tool()
def count_customers() -> Dict[str, Any]:
    """Retrieve a count of customers."""
    return client.request("GET", "/customers/count.json")


@mcp.tool()
def search_customers(query: str, limit: int = 50, fields: Optional[str] = None) -> List[Dict[str, Any]]:
    """Search customers by query string (e.g. 'email:foo@bar.com')."""
    params: Dict[str, Any] = {"query": query, "limit": limit}
    if fields:
        params["fields"] = fields
    return client.request("GET", "/customers/search.json", params=params)


@mcp.tool()
def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """Create a customer."""
    return client.request("POST", "/customers.json", body={"customer": customer})


@mcp.tool()
def update_customer(customer_id: Union[int, str], customer: Dict[str, Any]) -> Dict[str, Any]:
    """Update a customer."""
    payload = dict(customer)
    payload["id"] = int(customer_id) if str(customer_id).isdigit() else customer_id
    return client.request("PUT", f"/customers/{customer_id}.json", body={"customer": payload})


@mcp.tool()
def customer_orders(customer_id: Union[int, str], limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieve all orders that belong to a customer."""
    return client.request("GET", f"/customers/{customer_id}/orders.json", params={"limit": limit})


@mcp.tool()
def create_customer_account_activation_url(customer_id: Union[int, str]) -> Dict[str, Any]:
    """Create an account activation URL for a customer."""
    return client.request("POST", f"/customers/{customer_id}/account_activation_url.json")


@mcp.tool()
def send_customer_invite(customer_id: Union[int, str], invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Send an account invite to a customer."""
    body = {"customer_invite": invite} if invite else None
    return client.request("POST", f"/customers/{customer_id}/send_invite.json", body=body)
