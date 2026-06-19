from typing import Any, Dict, List, Optional

from .shopify_client import ShopifyClient, build_params


def create_customer_address(customer_id: int, address: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/addresses.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/addresses.json", json={"address": address})


def list_customer_addresses(
    customer_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/addresses.json"""
    client = client or ShopifyClient()
    params = build_params(limit=limit, since_id=since_id)
    return client.request("GET", f"/customers/{customer_id}/addresses.json", params=params)


def get_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


def update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", json={"address": address})


def set_default_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}/default.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json", json={})


def bulk_customer_addresses_set(
    customer_id: int,
    address_ids: List[int],
    operation: str,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/customers/{customer_id}/addresses/set.json"""
    client = client or ShopifyClient()
    params = {"operation": operation}
    for i, aid in enumerate(address_ids):
        params[f"address_ids[{i}]" if False else "address_ids[]"] = aid  # requests will encode repeated keys
    return client.request("PUT", f"/customers/{customer_id}/addresses/set.json", params=params, json={})


def delete_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
