from typing import Any, Dict, List, Optional

from ._client import get_client


def create_customer_address(customer_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers/{customer_id}/addresses.json

    Doc: docs/api_customer-address.md
    Body wrapper: {"address": {...}}
    """
    client = get_client()
    return client.request(
        "POST", f"/customers/{customer_id}/addresses.json", json={"address": address}
    )


def list_customer_addresses(
    customer_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /customers/{customer_id}/addresses.json

    Doc: docs/api_customer-address.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/customers/{customer_id}/addresses.json", params=params or None)


def get_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    """GET /customers/{customer_id}/addresses/{address_id}.json

    Doc: docs/api_customer-address.md
    """
    client = get_client()
    return client.request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


def update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/{address_id}.json

    Doc: docs/api_customer-address.md
    Body wrapper: {"address": {...}}
    """
    client = get_client()
    return client.request(
        "PUT",
        f"/customers/{customer_id}/addresses/{address_id}.json",
        json={"address": address},
    )


def set_default_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/{address_id}/default.json

    Doc: docs/api_customer-address.md
    """
    client = get_client()
    return client.request(
        "PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json"
    )


def bulk_customer_addresses_set(
    customer_id: int,
    address_ids: List[int],
    operation: str,
) -> Dict[str, Any]:
    """PUT /customers/{customer_id}/addresses/set.json

    Doc: docs/api_customer-address.md
    Query params: address_ids[]=...&operation=destroy
    """
    client = get_client()
    params: Dict[str, Any] = {"operation": operation}
    # requests encodes list values as repeated params when value is list
    params["address_ids[]"] = address_ids
    return client.request("PUT", f"/customers/{customer_id}/addresses/set.json", params=params)


def delete_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    """DELETE /customers/{customer_id}/addresses/{address_id}.json

    Doc: docs/api_customer-address.md
    """
    client = get_client()
    return client.request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
