from typing import Any, Dict, Optional

from .client import shopify_request


def create_customer(customer: Dict[str, Any]) -> Any:
    """POST /customers.json"""
    return shopify_request("POST", "/customers.json", json={"customer": customer})


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
    return shopify_request("GET", "/customers.json", params=params or None)


def get_customer(customer_id: int, *, fields: Optional[str] = None) -> Any:
    """GET /customers/{customer_id}.json"""
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/customers/{customer_id}.json", params=params)


def count_customers() -> Any:
    """GET /customers/count.json"""
    return shopify_request("GET", "/customers/count.json")


def search_customers(query: str, *, fields: Optional[str] = None) -> Any:
    """GET /customers/search.json"""
    params: Dict[str, Any] = {"query": query}
    if fields:
        params["fields"] = fields
    return shopify_request("GET", "/customers/search.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Any:
    """PUT /customers/{customer_id}.json"""
    body = {"customer": {**customer, "id": customer_id}}
    return shopify_request("PUT", f"/customers/{customer_id}.json", json=body)


def get_customer_orders(customer_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Any:
    """GET /customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", f"/customers/{customer_id}/orders.json", params=params or None)


def create_customer_account_activation_url(customer_id: int) -> Any:
    """POST /customers/{customer_id}/account_activation_url.json"""
    return shopify_request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Any:
    """POST /customers/{customer_id}/send_invite.json"""
    return shopify_request("POST", f"/customers/{customer_id}/send_invite.json", json={"customer_invite": invite or {}})
