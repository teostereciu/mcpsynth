from typing import Any, Dict, Optional

from .http_client import stripe_request, stripe_list_all


def payment_intents_create(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    params = {"amount": amount, "currency": currency}
    params.update(kwargs)
    return stripe_request("POST", "/v1/payment_intents", params)


def payment_intents_retrieve(payment_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", kwargs or None)


def payment_intents_update(payment_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", kwargs)


def payment_intents_confirm(payment_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", kwargs)


def payment_intents_capture(payment_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/capture", kwargs)


def payment_intents_cancel(payment_intent_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", kwargs)


def payment_intents_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/payment_intents", params)


def payment_intents_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/payment_intents", kwargs, limit=limit)
