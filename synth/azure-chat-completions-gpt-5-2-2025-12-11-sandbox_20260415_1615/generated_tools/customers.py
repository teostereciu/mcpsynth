from typing import Any, Dict, Optional

from .http_client import get_client


def customer_create(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json"""
    return get_client().request("POST", "/customers.json", json_body={"customer": customer})


def customers_list(
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
    return get_client().request("GET", "/customers.json", params=params or None)


def customers_count() -> Dict[str, Any]:
    """GET /customers/count.json"""
    return get_client().request("GET", "/customers/count.json")


def customers_search(query: str, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/search.json?query=..."""
    params: Dict[str, Any] = {"query": query}
    if fields:
        params["fields"] = fields
    return get_client().request("GET", "/customers/search.json", params=params)


def customer_update(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json"""
    body = {"customer": {**customer, "id": customer_id}}
    return get_client().request("PUT", f"/customers/{customer_id}.json", json_body=body)


def customer_orders_list(customer_id: int, *, limit: Optional[int] = None, status: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "status": status, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", f"/customers/{customer_id}/orders.json", params=params or None)


def customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    """POST /customers/{customer_id}/account_activation_url.json"""
    return get_client().request("POST", f"/customers/{customer_id}/account_activation_url.json")


def customer_send_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/send_invite.json"""
    body = {"customer_invite": invite} if invite else None
    return get_client().request("POST", f"/customers/{customer_id}/send_invite.json", json_body=body)
