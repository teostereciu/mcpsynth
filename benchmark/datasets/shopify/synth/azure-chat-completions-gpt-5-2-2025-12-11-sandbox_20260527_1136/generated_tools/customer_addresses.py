from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def create_customer_address(customer_id: int, address: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /customers/{customer_id}/addresses.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/customers/{customer_id}/addresses.json", json_body={"address": address})


def list_customer_addresses(
    customer_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /customers/{customer_id}/addresses.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/customers/{customer_id}/addresses.json", params=build_params(limit=limit))


def get_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


def update_customer_address(
    customer_id: int,
    address_id: int,
    address: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
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
    address_ids: list[int],
    operation: str,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/set.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"operation": operation, "address_ids[]": address_ids}
    return client.request("PUT", f"/customers/{customer_id}/addresses/set.json", params=params)


def delete_customer_address(customer_id: int, address_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /customers/{customer_id}/addresses/{address_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
