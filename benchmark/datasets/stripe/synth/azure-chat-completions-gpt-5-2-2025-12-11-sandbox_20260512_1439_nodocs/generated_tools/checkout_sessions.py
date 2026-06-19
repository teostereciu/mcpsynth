from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def checkout_sessions_create(mode: str, success_url: str, cancel_url: str, **kwargs) -> Dict[str, Any]:
    params = {"mode": mode, "success_url": success_url, "cancel_url": cancel_url}
    params.update(kwargs)
    return stripe_request("POST", "/v1/checkout/sessions", params)


def checkout_sessions_retrieve(session_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}", kwargs or None)


def checkout_sessions_update(session_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/checkout/sessions/{session_id}", kwargs)


def checkout_sessions_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/checkout/sessions", params)


def checkout_sessions_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/checkout/sessions", kwargs, limit=limit)


def checkout_sessions_expire(session_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/checkout/sessions/{session_id}/expire", kwargs)
