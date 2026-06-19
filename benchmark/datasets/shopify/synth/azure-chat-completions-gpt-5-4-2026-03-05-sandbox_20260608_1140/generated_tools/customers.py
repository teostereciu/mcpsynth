from typing import Any, Dict, Optional

from generated_tools.common import shopify_request


def create_customer(customer: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/customers.json", json_body={"customer": customer})


def list_customers(limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None, ids: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "since_id": since_id, "fields": fields, "ids": ids}.items() if v is not None}
    return shopify_request("GET", "/customers.json", params=params)


def count_customers() -> Any:
    return shopify_request("GET", "/customers/count.json")


def search_customers(query: str, limit: Optional[int] = None, fields: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"query": query, "limit": limit, "fields": fields}.items() if v is not None}
    return shopify_request("GET", "/customers/search.json", params=params)


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Any:
    payload = dict(customer)
    payload.setdefault("id", customer_id)
    return shopify_request("PUT", f"/customers/{customer_id}.json", json_body={"customer": payload})


def get_customer_orders(customer_id: int, status: Optional[str] = None, fields: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"status": status, "fields": fields}.items() if v is not None}
    return shopify_request("GET", f"/customers/{customer_id}/orders.json", params=params)


def create_account_activation_url(customer_id: int) -> Any:
    return shopify_request("POST", f"/customers/{customer_id}/account_activation_url.json")


def send_customer_invite(customer_id: int, customer_invite: Optional[Dict[str, Any]] = None) -> Any:
    body = {"customer_invite": customer_invite} if customer_invite is not None else None
    return shopify_request("POST", f"/customers/{customer_id}/send_invite.json", json_body=body)


def create_customer_address(customer_id: int, address: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/customers/{customer_id}/addresses.json", json_body={"address": address})


def list_customer_addresses(customer_id: int, limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return shopify_request("GET", f"/customers/{customer_id}/addresses.json", params=params)


def get_customer_address(customer_id: int, address_id: int) -> Any:
    return shopify_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")


def update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any]) -> Any:
    payload = dict(address)
    payload.setdefault("id", address_id)
    return shopify_request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", json_body={"address": payload})


def set_default_customer_address(customer_id: int, address_id: int) -> Any:
    return shopify_request("PUT", f"/customers/{customer_id}/addresses/{address_id}/default.json")


def bulk_customer_address_operation(customer_id: int, address_ids: str, operation: str) -> Any:
    return shopify_request("PUT", f"/customers/{customer_id}/addresses/set.json", params={"address_ids[]": address_ids, "operation": operation})


def delete_customer_address(customer_id: int, address_id: int) -> Any:
    return shopify_request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
