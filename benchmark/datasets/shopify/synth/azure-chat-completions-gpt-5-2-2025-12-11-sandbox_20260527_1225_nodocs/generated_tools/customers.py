from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_customers(limit: int = 50, fields: Optional[str] = None, query: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    if query:
        params["query"] = query
    return client.request("GET", "/customers.json", params=params)


def search_customers(query: str, limit: int = 50) -> Dict[str, Any]:
    """GET /customers/search.json"""
    client = ShopifyClient()
    return client.request("GET", "/customers/search.json", params={"query": query, "limit": limit})


def get_customer(customer_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}.json"""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/customers/{customer_id}.json", params=params)


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json"""
    client = ShopifyClient()
    return client.request("POST", "/customers.json", json_body={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json"""
    client = ShopifyClient()
    body = {"customer": {**customer, "id": customer_id}}
    return client.request("PUT", f"/customers/{customer_id}.json", json_body=body)


def delete_customer(customer_id: int) -> Dict[str, Any]:
    """DELETE /customers/{customer_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/customers/{customer_id}.json")
