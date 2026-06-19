from typing import Any, Dict, Optional

from .client import request_json


def customer_create(customer: Dict[str, Any]) -> Any:
    """POST /customers.json"""
    return request_json("POST", "/customers.json", json_body={"customer": customer})


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
) -> Any:
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


def customers_count(*, created_at_min: Optional[str] = None, created_at_max: Optional[str] = None, updated_at_min: Optional[str] = None, updated_at_max: Optional[str] = None) -> Any:
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


def customers_search(query: str, *, limit: Optional[int] = None, fields: Optional[str] = None) -> Any:
    """GET /customers/search.json"""
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/customers/search.json", params=params)


def customer_update(customer_id: int, customer: Dict[str, Any]) -> Any:
    """PUT /customers/{customer_id}.json"""
    body = {"customer": {**customer, "id": customer_id}}
    return request_json("PUT", f"/customers/{customer_id}.json", json_body=body)


def customer_orders_list(customer_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, status: Optional[str] = None, fields: Optional[str] = None) -> Any:
    """GET /customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "status": status, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/customers/{customer_id}/orders.json", params=params)


def customer_account_activation_url(customer_id: int) -> Any:
    """POST /customers/{customer_id}/account_activation_url.json"""
    return request_json("POST", f"/customers/{customer_id}/account_activation_url.json")


def customer_send_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Any:
    """POST /customers/{customer_id}/send_invite.json"""
    body = {"customer_invite": invite} if invite is not None else None
    return request_json("POST", f"/customers/{customer_id}/send_invite.json", json_body=body)
