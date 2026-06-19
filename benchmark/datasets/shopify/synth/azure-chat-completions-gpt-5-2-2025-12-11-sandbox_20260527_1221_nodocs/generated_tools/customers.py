from typing import Any, Dict, Optional

from .client import request_json


def list_customers(*, limit: int = 50, since_id: Optional[int] = None, email: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if email is not None:
        params["email"] = email
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/customers.json", params=params)


def search_customers(*, query: str, limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", "/customers/search.json", params={"query": query, "limit": limit})


def get_customer(customer_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/customers/{customer_id}.json", params=params or None)


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/customers.json", json_body={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    body = {"customer": {**customer, "id": customer_id}}
    return request_json("PUT", f"/customers/{customer_id}.json", json_body=body)


def delete_customer(customer_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/customers/{customer_id}.json")
