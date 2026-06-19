from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def charges_retrieve(charge_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/charges/{charge_id}", kwargs or None)


def charges_update(charge_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/charges/{charge_id}", kwargs)


def charges_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/charges", params)


def charges_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/charges", kwargs, limit=limit)


def charges_capture(charge_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/charges/{charge_id}/capture", kwargs)
