from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


@mcp.tool()
def list_customers(
    limit: int = 50,
    fields: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
    ids: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """List customers (GET /customers.json)."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    if since_id is not None:
        params["since_id"] = since_id
    if ids:
        params["ids"] = ids
    data = client.request("GET", "/customers.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def search_customers(query: str, limit: int = 50, fields: Optional[str] = None) -> List[Dict[str, Any]]:
    """Search customers (GET /customers/search.json?query=...)."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"query": query, "limit": limit}
    if fields:
        params["fields"] = fields
    data = client.request("GET", "/customers/search.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def get_customer(customer_id: Union[int, str], fields: Optional[str] = None) -> Dict[str, Any]:
    """Get a customer (GET /customers/{customer_id}.json)."""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    data = client.request("GET", f"/customers/{customer_id}.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """Create a customer (POST /customers.json)."""
    client = ShopifyClient()
    data = client.request("POST", "/customers.json", body={"customer": customer})
    return unwrap_envelope(data)


@mcp.tool()
def update_customer(customer_id: Union[int, str], customer: Dict[str, Any]) -> Dict[str, Any]:
    """Update a customer (PUT /customers/{customer_id}.json)."""
    client = ShopifyClient()
    payload = dict(customer)
    payload["id"] = int(customer_id) if str(customer_id).isdigit() else customer_id
    data = client.request("PUT", f"/customers/{customer_id}.json", body={"customer": payload})
    return unwrap_envelope(data)


@mcp.tool()
def list_customer_orders(customer_id: Union[int, str], limit: int = 50, fields: Optional[str] = None) -> List[Dict[str, Any]]:
    """List orders for a customer (GET /customers/{customer_id}/orders.json)."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    data = client.request("GET", f"/customers/{customer_id}/orders.json", params=params)
    return unwrap_envelope(data)


# Customer addresses

@mcp.tool()
def list_customer_addresses(customer_id: Union[int, str], limit: Optional[int] = None) -> List[Dict[str, Any]]:
    """List customer addresses (GET /customers/{customer_id}/addresses.json)."""
    client = ShopifyClient()
    params = {"limit": limit} if limit is not None else None
    data = client.request("GET", f"/customers/{customer_id}/addresses.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def get_customer_address(customer_id: Union[int, str], address_id: Union[int, str]) -> Dict[str, Any]:
    """Get a customer address (GET /customers/{customer_id}/addresses/{address_id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")
    return unwrap_envelope(data)


@mcp.tool()
def create_customer_address(customer_id: Union[int, str], address: Dict[str, Any]) -> Dict[str, Any]:
    """Create a customer address (POST /customers/{customer_id}/addresses.json)."""
    client = ShopifyClient()
    data = client.request(
        "POST",
        f"/customers/{customer_id}/addresses.json",
        body={"address": address},
    )
    return unwrap_envelope(data)


@mcp.tool()
def update_customer_address(customer_id: Union[int, str], address_id: Union[int, str], address: Dict[str, Any]) -> Dict[str, Any]:
    """Update a customer address (PUT /customers/{customer_id}/addresses/{address_id}.json)."""
    client = ShopifyClient()
    data = client.request(
        "PUT",
        f"/customers/{customer_id}/addresses/{address_id}.json",
        body={"address": address},
    )
    return unwrap_envelope(data)


@mcp.tool()
def set_default_customer_address(customer_id: Union[int, str], address_id: Union[int, str]) -> Dict[str, Any]:
    """Set default customer address (PUT /customers/{customer_id}/addresses/{address_id}/default.json)."""
    client = ShopifyClient()
    data = client.request("PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json")
    return unwrap_envelope(data)


@mcp.tool()
def delete_customer_address(customer_id: Union[int, str], address_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a customer address (DELETE /customers/{customer_id}/addresses/{address_id}.json)."""
    client = ShopifyClient()
    return client.request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
