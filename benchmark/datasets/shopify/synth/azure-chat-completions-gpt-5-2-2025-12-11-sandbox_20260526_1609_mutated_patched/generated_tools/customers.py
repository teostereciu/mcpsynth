from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_customers(
    *,
    ids: Optional[str] = None,
    limit: int = 50,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers.json"""
    params: Dict[str, Any] = {"limit": limit}
    if ids:
        params["ids"] = ids
    if since_id is not None:
        params["since_id"] = since_id
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    if fields:
        params["fields"] = fields
    return ShopifyClient().request("GET", "/customers.json", params=params)


def search_customers(*, query: str, limit: int = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/search.json?query=..."""
    params: Dict[str, Any] = {"query": query, "limit": limit}
    if fields:
        params["fields"] = fields
    return ShopifyClient().request("GET", "/customers/search.json", params=params)


def count_customers() -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/count.json"""
    return ShopifyClient().request("GET", "/customers/count.json")


def create_customer(*, customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers.json"""
    return ShopifyClient().request("POST", "/customers.json", json={"customer": customer})


def update_customer(*, customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}.json"""
    body = {"customer": {**customer, "id": customer_id}}
    return ShopifyClient().request("PUT", f"/customers/{customer_id}.json", json=body)


def get_customer_orders(*, customer_id: int, limit: int = 50, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {"limit": limit}
    if status:
        params["status"] = status
    return ShopifyClient().request("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_customer_account_activation_url(*, customer_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/account_activation_url.json"""
    return ShopifyClient().request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(*, customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/send_invite.json"""
    payload = {"customer_invite": invite} if invite else None
    return ShopifyClient().request("POST", f"/customers/{customer_id}/send_invite.json", json=payload)
