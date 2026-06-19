from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


def create_customer(customer: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", "/customers.json", json_body={"customer": customer})


def list_customers(
    *,
    api_version: str = "2026-01",
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers.json"""
    client = ShopifyAdminClient(api_version=api_version)
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


def get_customer(customer_id: int, *, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/customers/{customer_id}.json", params=params)


def count_customers(*, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", "/customers/count.json")


def search_customers(query: str, *, api_version: str = "2026-01", limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/search.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return client.request("GET", "/customers/search.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"customer": {**customer, "id": customer_id}}
    return client.request("PUT", f"/customers/{customer_id}.json", json_body=body)


def create_customer_account_activation_url(customer_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/account_activation_url.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/customers/{customer_id}/account_activation_url.json", json_body={})


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/send_invite.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/customers/{customer_id}/send_invite.json", json_body=invite or {})


def list_customer_orders(customer_id: int, *, api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/orders.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/customers/{customer_id}/orders.json", params=params or None)
