from typing import Any, Dict, Optional

from ._client import get_client


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json

    Doc: docs/api_customer.md
    Body wrapper: {"customer": {...}}
    """
    client = get_client()
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
) -> Dict[str, Any]:
    """GET /customers.json

    Doc: docs/api_customer.md
    """
    client = get_client()
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
    return client.request("GET", "/customers.json", params=params)


def get_customer(customer_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}.json

    Doc: docs/api_customer.md
    """
    client = get_client()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/customers/{customer_id}.json", params=params)


def count_customers(*, created_at_min: Optional[str] = None, created_at_max: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/count.json

    Doc: docs/api_customer.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if created_at_min is not None:
        params["created_at_min"] = created_at_min
    if created_at_max is not None:
        params["created_at_max"] = created_at_max
    return client.request("GET", "/customers/count.json", params=params or None)


def search_customers(query: str, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/search.json

    Doc: docs/api_customer.md
    """
    client = get_client()
    params: Dict[str, Any] = {"query": query}
    if fields:
        params["fields"] = fields
    return client.request("GET", "/customers/search.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json

    Doc: docs/api_customer.md
    Body wrapper: {"customer": {..., "id": customer_id}}
    """
    client = get_client()
    body = dict(customer)
    body.setdefault("id", customer_id)
    return client.request("PUT", f"/customers/{customer_id}.json", json={"customer": body})


def get_customer_orders(
    customer_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /customers/{customer_id}/orders.json

    Doc: docs/api_customer.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "status": status, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    """POST /customers/{customer_id}/account_activation_url.json

    Doc: docs/api_customer.md
    """
    client = get_client()
    return client.request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/send_invite.json

    Doc: docs/api_customer.md
    Body wrapper: {"customer_invite": {...}}
    """
    client = get_client()
    payload = {"customer_invite": invite} if invite is not None else None
    return client.request("POST", f"/customers/{customer_id}/send_invite.json", json=payload)
