from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_customer(customer: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /customers.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/customers.json", json={"customer": customer})


def list_customers(
    *,
    client: Optional[ShopifyClient] = None,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Any:
    """GET /customers.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "ids": ids,
        "limit": limit,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/customers.json", params=params or None)


def get_customer_orders(customer_id: int, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Any:
    """GET /customers/{customer_id}/orders.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/customers/{customer_id}/orders.json", params=params or None)


def count_customers(*, client: Optional[ShopifyClient] = None) -> Any:
    """GET /customers/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/customers/count.json")


def search_customers(query: str, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, fields: Optional[str] = None) -> Any:
    """GET /customers/search.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return client.request("GET", "/customers/search.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /customers/{customer_id}.json"""
    client = client or ShopifyClient()
    body = {"customer": {**customer, "id": customer_id}}
    return client.request("PUT", f"/customers/{customer_id}.json", json=body)


def create_customer_account_activation_url(customer_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /customers/{customer_id}/account_activation_url.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None, *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /customers/{customer_id}/send_invite.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/send_invite.json", json=invite or {})
