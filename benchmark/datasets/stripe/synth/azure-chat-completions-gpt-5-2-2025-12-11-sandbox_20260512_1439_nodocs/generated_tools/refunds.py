from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def refunds_create(**kwargs) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/refunds", kwargs)


def refunds_retrieve(refund_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund_id}", kwargs or None)


def refunds_update(refund_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/refunds/{refund_id}", kwargs)


def refunds_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/refunds", params)


def refunds_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/refunds", kwargs, limit=limit)
