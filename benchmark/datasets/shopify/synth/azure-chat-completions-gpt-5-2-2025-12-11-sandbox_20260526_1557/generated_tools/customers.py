from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_customers(
    *,
    ids: Optional[str] = None,
    limit: Optional[int] = 50,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
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
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", "/customers.json", params=params)


def search_customers(*, query: str, limit: Optional[int] = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/search.json"""
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", "/customers/search.json", params=params)


def get_customer(*, customer_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}.json"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/customers/{customer_id}.json", params=params)


def count_customers() -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/count.json"""
    return ShopifyClient().request("GET", "/customers/count.json")


def create_customer(*, customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers.json"""
    return ShopifyClient().request("POST", "/customers.json", json_body={"customer": customer})


def update_customer(*, customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}.json"""
    body = {"customer": {**customer, "id": customer_id}}
    return ShopifyClient().request("PUT", f"/customers/{customer_id}.json", json_body=body)


def get_customer_orders(*, customer_id: int, limit: Optional[int] = 50, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/orders.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if fields is not None:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_account_activation_url(*, customer_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/account_activation_url.json"""
    return ShopifyClient().request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(*, customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/send_invite.json"""
    body = {"customer_invite": invite} if invite is not None else None
    return ShopifyClient().request("POST", f"/customers/{customer_id}/send_invite.json", json_body=body)


# Customer addresses

def list_customer_addresses(*, customer_id: int, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/addresses.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return ShopifyClient().request("GET", f"/customers/{customer_id}/addresses.json", params=params or None)


def get_customer_address(*, customer_id: int, address_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}.json"""
    return ShopifyClient().request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


def create_customer_address(*, customer_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/addresses.json"""
    return ShopifyClient().request("POST", f"/customers/{customer_id}/addresses.json", json_body={"address": address})


def update_customer_address(*, customer_id: int, address_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}.json"""
    return ShopifyClient().request(
        "PUT",
        f"/customers/{customer_id}/addresses/{address_id}.json",
        json_body={"address": address},
    )


def set_default_customer_address(*, customer_id: int, address_id: int) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}/default.json"""
    return ShopifyClient().request("PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json")


def delete_customer_address(*, customer_id: int, address_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}.json"""
    return ShopifyClient().request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")


def bulk_customer_addresses(*, customer_id: int, address_ids: list[int], operation: str) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}/addresses/set.json"""
    params: Dict[str, Any] = {"operation": operation}
    # Shopify expects address_ids[] repeated
    for i, aid in enumerate(address_ids):
        params[f"address_ids[{i}]"] = aid
    return ShopifyClient().request("PUT", f"/customers/{customer_id}/addresses/set.json", params=params)
