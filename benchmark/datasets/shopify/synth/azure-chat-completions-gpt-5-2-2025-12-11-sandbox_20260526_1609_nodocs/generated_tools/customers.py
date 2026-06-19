from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_customers(limit: int = 50, page_info: Optional[str] = None, **filters: Any) -> Dict[str, Any]:
    """GET /customers.json"""
    params: Dict[str, Any] = {"limit": limit}
    if page_info:
        params["page_info"] = page_info
    params.update({k: v for k, v in filters.items() if v is not None})
    return ShopifyClient().request("GET", "/customers.json", params=params)


def search_customers(query: str, limit: int = 50) -> Dict[str, Any]:
    """GET /customers/search.json"""
    return ShopifyClient().request("GET", "/customers/search.json", params={"query": query, "limit": limit})


def get_customer(customer_id: int) -> Dict[str, Any]:
    """GET /customers/{id}.json"""
    return ShopifyClient().request("GET", f"/customers/{customer_id}.json")


def create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json"""
    return ShopifyClient().request("POST", "/customers.json", json={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{id}.json"""
    return ShopifyClient().request("PUT", f"/customers/{customer_id}.json", json={"customer": customer})


def delete_customer(customer_id: int) -> Dict[str, Any]:
    """DELETE /customers/{id}.json"""
    return ShopifyClient().request("DELETE", f"/customers/{customer_id}.json")
