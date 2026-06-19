from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_setup_intent(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "usage": usage,
        "description": description,
        "metadata": metadata,
        "confirm": confirm,
        "return_url": return_url,
        "automatic_payment_methods": automatic_payment_methods,
        "payment_method_types": payment_method_types,
    }
    _, data = stripe_request(
        "POST",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret} if client_secret else None
    _, data = stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "description": description,
        "metadata": metadata,
    }
    _, data = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "payment_method": payment_method,
        "return_url": return_url,
        "use_stripe_sdk": use_stripe_sdk,
    }
    _, data = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def cancel_setup_intent(
    setup_intent_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        stripe_account=stripe_account,
    )
    return data


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    _, data = stripe_request(
        "GET",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
    )
    return data
