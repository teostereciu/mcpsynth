from typing import Any, Dict, Optional

from .http_client import stripe_request


# Endpoints (Stripe API v1)
# POST /v1/payment_intents
# GET /v1/payment_intents/{intent}
# POST /v1/payment_intents/{intent}
# POST /v1/payment_intents/{intent}/confirm
# POST /v1/payment_intents/{intent}/capture
# POST /v1/payment_intents/{intent}/cancel
# GET /v1/payment_intents


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    description: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    off_session: Optional[Any] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "confirm": confirm,
        "customer": customer,
        "payment_method": payment_method,
        "receipt_email": receipt_email,
        "description": description,
        "setup_future_usage": setup_future_usage,
        "automatic_payment_methods": automatic_payment_methods,
        "metadata": metadata,
        "shipping": shipping,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "off_session": off_session,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_intent(
    intent_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_intents/{intent_id}", params=None, stripe_account=stripe_account)


def update_payment_intent(
    intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{intent_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def confirm_payment_intent(
    intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{intent_id}/confirm",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def capture_payment_intent(
    intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{intent_id}/capture",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_payment_intent(
    intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{intent_id}/cancel",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    return stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
