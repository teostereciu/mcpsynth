from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/setup_intents.md

def create_setup_intent(
    *,
    payment_method_types: Optional[list[str]] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "payment_method_types": payment_method_types,
        "customer": customer,
        "payment_method": payment_method,
        "usage": usage,
        "description": description,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
        "confirm": confirm,
        "return_url": return_url,
        "payment_method_options": payment_method_options,
        "payment_method_data": payment_method_data,
    }
    return stripe_request(
        "POST",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret, "expand": expand}
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "customer": customer,
        "payment_method": payment_method,
        "description": description,
        "metadata": metadata,
        "payment_method_types": payment_method_types,
        "payment_method_options": payment_method_options,
    }
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"payment_method": payment_method, "return_url": return_url, "use_stripe_sdk": use_stripe_sdk}
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_setup_intent(
    setup_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params={"cancellation_reason": cancellation_reason},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "customer": customer,
        "payment_method": payment_method,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
    )
