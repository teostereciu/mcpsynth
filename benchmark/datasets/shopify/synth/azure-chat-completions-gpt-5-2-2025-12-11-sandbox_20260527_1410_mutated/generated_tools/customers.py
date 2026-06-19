from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def customer_create(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers.json"""
    client = ShopifyClient()
    return client.request("POST", "/customers.json", json_body={"customer": customer})


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
    """GET /admin/api/2026-01/customers.json"""
    client = ShopifyClient()
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


def customers_count() -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/count.json"""
    client = ShopifyClient()
    return client.request("GET", "/customers/count.json")


def customers_search(query: str, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/search.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"query": query}
    if fields:
        params["fields"] = fields
    return client.request("GET", "/customers/search.json", params=params)


def customer_update(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}.json"""
    client = ShopifyClient()
    body = {"customer": {**customer, "id": customer_id}}
    return client.request("PUT", f"/customers/{customer_id}.json", json_body=body)


def customer_orders_list(customer_id: int, *, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/orders.json"""
    client = ShopifyClient()
    params = {"status": status} if status else None
    return client.request("GET", f"/customers/{customer_id}/orders.json", params=params)


def customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/account_activation_url.json"""
    client = ShopifyClient()
    return client.request(
        "POST", f"/customers/{customer_id}/account_activation_url.json"
    )


def customer_send_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/send_invite.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/customers/{customer_id}/send_invite.json",
        json_body={"customer_invite": invite} if invite else None,
    )
