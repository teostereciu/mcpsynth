from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_setup_intent(
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
        "usage": usage,
        "confirm": confirm,
        "return_url": return_url,
        "automatic_payment_methods": automatic_payment_methods,
        "payment_method_types": payment_method_types,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/setup_intents",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret} if client_secret else None
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
    )
