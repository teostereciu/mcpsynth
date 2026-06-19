from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def products_create(name: str, **kwargs) -> Dict[str, Any]:
    params = {"name": name}
    params.update(kwargs)
    return stripe_request("POST", "/v1/products", params)


def products_retrieve(product_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/products/{product_id}", kwargs or None)


def products_update(product_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/products/{product_id}", kwargs)


def products_delete(product_id: str) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/products/{product_id}")


def products_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/products", params)


def products_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/products", kwargs, limit=limit)


def products_search(query: str, limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"query": query, "limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/products/search", params)
