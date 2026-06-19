from typing import Any, Dict, Optional

from .http import request_json


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json"""
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
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /customers.json"""
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
    return request_json("GET", "/customers.json", params=params)


def count_customers(
    *,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /customers/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/customers/count.json", params=params)


def search_customers(query: str, *, limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/search.json?query=..."""
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/customers/search.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json"""
    return request_json("PUT", f"/customers/{customer_id}.json", json_body={"customer": customer})


def get_customer_orders(customer_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, status: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "status": status, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    """POST /customers/{customer_id}/account_activation_url.json"""
    return request_json("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/send_invite.json"""
    body = {"customer_invite": invite} if invite is not None else None
    return request_json("POST", f"/customers/{customer_id}/send_invite.json", json_body=body)
