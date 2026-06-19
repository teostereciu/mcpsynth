from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def customers_create(**kwargs) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/customers", kwargs)


def customers_retrieve(customer_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/customers/{customer_id}", kwargs or None)


def customers_update(customer_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/customers/{customer_id}", kwargs)


def customers_delete(customer_id: str) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}")


def customers_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/customers", params)


def customers_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/customers", kwargs, limit=limit)


def customers_search(query: str, limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"query": query, "limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/customers/search", params)
