from typing import Any, Dict, Optional

from .http_client import request_json


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers.json"""
    return request_json("POST", "/customers.json", json_body={"customer": customer})


def list_customers(
    *,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers.json"""
    params: Dict[str, Any] = {}
    if ids is not None:
        params["ids"] = ids
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if created_at_min is not None:
        params["created_at_min"] = created_at_min
    if created_at_max is not None:
        params["created_at_max"] = created_at_max
    if updated_at_min is not None:
        params["updated_at_min"] = updated_at_min
    if updated_at_max is not None:
        params["updated_at_max"] = updated_at_max
    if email is not None:
        params["email"] = email
    if phone is not None:
        params["phone"] = phone
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/customers.json", params=params)


def search_customers(query: str, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/search.json"""
    params: Dict[str, Any] = {"query": query}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/customers/search.json", params=params)


def count_customers() -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/count.json"""
    return request_json("GET", "/customers/count.json")


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}.json"""
    return request_json("PUT", f"/customers/{customer_id}.json", json_body={"customer": customer})


def get_customer_orders(customer_id: int, *, status: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/account_activation_url.json"""
    return request_json("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/send_invite.json"""
    return request_json("POST", f"/customers/{customer_id}/send_invite.json", json_body={"customer_invite": invite} if invite is not None else None)
