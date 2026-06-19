from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_customers(
    *,
    limit: Optional[int] = 50,
    page_info: Optional[str] = None,
    since_id: Optional[int] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    query: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /customers.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if email is not None:
        params["email"] = email
    if phone is not None:
        params["phone"] = phone
    if query is not None:
        params["query"] = query
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", "/customers.json", params=params)


def search_customers(*, query: str, limit: Optional[int] = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/search.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", "/customers/search.json", params=params)


def get_customer(*, customer_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /customers/{customer_id}.json"""
    c = ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return c.request("GET", f"/customers/{customer_id}.json", params=params)


def create_customer(*, customer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /customers.json"""
    c = ShopifyClient()
    return c.request("POST", "/customers.json", json={"customer": customer})


def update_customer(*, customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /customers/{customer_id}.json"""
    c = ShopifyClient()
    body = {"customer": {**customer, "id": customer_id}}
    return c.request("PUT", f"/customers/{customer_id}.json", json=body)


def delete_customer(*, customer_id: int) -> Dict[str, Any]:
    """DELETE /customers/{customer_id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/customers/{customer_id}.json")
