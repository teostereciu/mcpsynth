from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def prices_create(currency: str, **kwargs) -> Dict[str, Any]:
    params = {"currency": currency}
    params.update(kwargs)
    return stripe_request("POST", "/v1/prices", params)


def prices_retrieve(price_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/prices/{price_id}", kwargs or None)


def prices_update(price_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/prices/{price_id}", kwargs)


def prices_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/prices", params)


def prices_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/prices", kwargs, limit=limit)


def prices_search(query: str, limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"query": query, "limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/prices/search", params)
