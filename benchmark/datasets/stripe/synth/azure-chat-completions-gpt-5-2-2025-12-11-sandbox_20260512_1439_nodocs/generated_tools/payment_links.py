from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def payment_links_create(line_items: list, **kwargs) -> Dict[str, Any]:
    params = {"line_items": line_items}
    params.update(kwargs)
    return stripe_request("POST", "/v1/payment_links", params)


def payment_links_retrieve(payment_link_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}", kwargs or None)


def payment_links_update(payment_link_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_links/{payment_link_id}", kwargs)


def payment_links_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/payment_links", params)


def payment_links_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/payment_links", kwargs, limit=limit)
