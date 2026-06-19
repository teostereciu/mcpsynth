from typing import Any, Dict, Optional

from .client import request_json


def list_customers(*, limit: int = 50, page_info: Optional[str] = None, query: Optional[str] = None, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    if query:
        params["query"] = query
    if fields:
        params["fields"] = fields
    return request_json("GET", "/customers.json", params=params)


def search_customers(*, query: str, limit: int = 50) -> Any:
    return request_json("GET", "/customers/search.json", params={"query": query, "limit": limit})


def get_customer(customer_id: int, *, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"/customers/{customer_id}.json", params=params)


def create_customer(customer: Dict[str, Any]) -> Any:
    return request_json("POST", "/customers.json", json={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/customers/{customer_id}.json", json={"customer": customer})


def delete_customer(customer_id: int) -> Any:
    return request_json("DELETE", f"/customers/{customer_id}.json")
