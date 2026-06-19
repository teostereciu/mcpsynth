from typing import Any, Dict, Optional

from ._client import get_client


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json

    Doc: docs/api_customer.md
    """
    return get_client().request("POST", "/customers.json", json_body={"customer": customer})


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
    if fields is not None:
        params["fields"] = fields
    return get_client().request("GET", "/customers.json", params=params)


def get_customer(customer_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}.json

    Doc: docs/api_customer.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return get_client().request("GET", f"/customers/{customer_id}.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json

    Doc: docs/api_customer.md
    """
    return get_client().request("PUT", f"/customers/{customer_id}.json", json_body={"customer": customer})


def count_customers() -> Dict[str, Any]:
    """GET /customers/count.json

    Doc: docs/api_customer.md
    """
    return get_client().request("GET", "/customers/count.json")


def search_customers(query: str, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/search.json?query=...

    Doc: docs/api_customer.md
    """
    params: Dict[str, Any] = {"query": query}
    if fields is not None:
        params["fields"] = fields
    return get_client().request("GET", "/customers/search.json", params=params)


def get_customer_orders(customer_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/orders.json

    Doc: docs/api_customer.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return get_client().request("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    """POST /customers/{customer_id}/account_activation_url.json

    Doc: docs/api_customer.md
    """
    return get_client().request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/send_invite.json

    Doc: docs/api_customer.md
    """
    body = {"customer_invite": invite} if invite is not None else None
    return get_client().request("POST", f"/customers/{customer_id}/send_invite.json", json_body=body)
