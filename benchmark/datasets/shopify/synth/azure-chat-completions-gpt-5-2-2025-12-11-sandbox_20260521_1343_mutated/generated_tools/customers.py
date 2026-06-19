from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_customer(customer: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/customers.json", json={"customer": customer})


def list_customers(
    *,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers.json"""
    client = client or ShopifyClient()
    params = build_params(
        ids=ids,
        limit=limit,
        since_id=since_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        fields=fields,
    )
    return client.request("GET", "/customers.json", params=params)


def search_customers(query: str, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/search.json?query=..."""
    client = client or ShopifyClient()
    params = build_params(query=query, fields=fields)
    return client.request("GET", "/customers/search.json", params=params)


def get_customer(customer_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}.json"""
    client = client or ShopifyClient()
    params = build_params(fields=fields)
    return client.request("GET", f"/customers/{customer_id}.json", params=params)


def count_customers(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/customers/count.json")


def update_customer(customer_id: int, customer: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/customers/{customer_id}.json", json={"customer": customer})


def list_customer_orders(
    customer_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/orders.json"""
    client = client or ShopifyClient()
    params = build_params(limit=limit, since_id=since_id, status=status, fields=fields)
    return client.request("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_customer_account_activation_url(customer_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/account_activation_url.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/account_activation_url.json", json={})


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/send_invite.json"""
    client = client or ShopifyClient()
    payload = {"customer_invite": invite} if invite is not None else {}
    return client.request("POST", f"/customers/{customer_id}/send_invite.json", json=payload)
