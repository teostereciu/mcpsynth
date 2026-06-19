from typing import Any, Dict, Optional

from .client import request_json


def list_customers(limit: int = 50, **filters: Any) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    params.update({k: v for k, v in filters.items() if v is not None})
    return request_json("GET", "/customers.json", params=params)


def search_customers(query: str, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", "/customers/search.json", params={"query": query, "limit": limit})


def get_customer(customer_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/customers/{customer_id}.json")


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/customers.json", json={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/customers/{customer_id}.json", json={"customer": customer})


def delete_customer(customer_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/customers/{customer_id}.json")


def list_customer_orders(customer_id: int, limit: int = 50, status: str = "any") -> Dict[str, Any]:
    return request_json("GET", f"/customers/{customer_id}/orders.json", params={"limit": limit, "status": status})


def create_customer_address(customer_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/customers/{customer_id}/addresses.json", json={"address": address})


def update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", json={"address": address})


def delete_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")
