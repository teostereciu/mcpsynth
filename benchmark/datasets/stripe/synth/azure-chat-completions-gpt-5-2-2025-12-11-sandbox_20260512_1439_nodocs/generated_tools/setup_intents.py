from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def setup_intents_create(**kwargs) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/setup_intents", kwargs)


def setup_intents_retrieve(setup_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", kwargs or None)


def setup_intents_update(setup_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}", kwargs)


def setup_intents_confirm(setup_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", kwargs)


def setup_intents_cancel(setup_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", kwargs)


def setup_intents_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/setup_intents", params)


def setup_intents_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/setup_intents", kwargs, limit=limit)
