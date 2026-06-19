from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def subscriptions_create(customer: str, items: list, **kwargs) -> Dict[str, Any]:
    params = {"customer": customer, "items": items}
    params.update(kwargs)
    return stripe_request("POST", "/v1/subscriptions", params)


def subscriptions_retrieve(subscription_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", kwargs or None)


def subscriptions_update(subscription_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}", kwargs)


def subscriptions_cancel(subscription_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", kwargs)


def subscriptions_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/subscriptions", params)


def subscriptions_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/subscriptions", kwargs, limit=limit)


def subscriptions_search(query: str, limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"query": query, "limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/subscriptions/search", params)
