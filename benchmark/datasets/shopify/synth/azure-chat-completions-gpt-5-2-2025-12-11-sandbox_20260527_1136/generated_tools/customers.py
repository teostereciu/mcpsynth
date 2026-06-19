from typing import Any, Dict, List, Optional

from .http_client import ShopifyClient


def create_customer(customer: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /customers.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/customers.json", json_body={"customer": customer})


def list_customers(
    *,
    client: Optional[ShopifyClient] = None,
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
    client = client or ShopifyClient()
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


def search_customers(query: str, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/search.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return client.request("GET", "/customers/search.json", params=params)


def count_customers(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /customers/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/customers/count.json")


def update_customer(customer_id: int, customer: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json"""
    client = client or ShopifyClient()
    body = {"customer": {**customer, "id": customer_id}}
    return client.request("PUT", f"/customers/{customer_id}.json", json_body=body)


def get_customer_orders(customer_id: int, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/orders.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/customers/{customer_id}/orders.json", params=params or None)


def create_customer_account_activation_url(customer_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/account_activation_url.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/send_invite.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/send_invite.json", json_body=invite)


# Customer addresses

def create_customer_address(customer_id: int, address: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/addresses.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/addresses.json", json_body={"address": address})


def list_customer_addresses(customer_id: int, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/addresses.json"""
    client = client or ShopifyClient()
    params = {"limit": limit} if limit is not None else None
    return client.request("GET", f"/customers/{customer_id}/addresses.json", params=params)


def get_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


def update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request(
        "PUT",
        f"/customers/{customer_id}/addresses/{address_id}.json",
        json_body={"address": address},
    )


def set_default_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/{address_id}/default.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json")


def bulk_customer_addresses_set(
    customer_id: int,
    address_ids: List[int],
    operation: str,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/set.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"operation": operation}
    # Shopify expects address_ids[] repeated
    for i, aid in enumerate(address_ids):
        params[f"address_ids[{i}]" if False else "address_ids[]"] = aid  # requests will handle list poorly; we pass repeated keys via list below
    # Better: pass list for address_ids[]
    params = {"operation": operation, "address_ids[]": address_ids}
    return client.request("PUT", f"/customers/{customer_id}/addresses/set.json", params=params)


def delete_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
