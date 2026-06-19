from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    off_session: Optional[Any] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "automatic_payment_methods": automatic_payment_methods,
        "confirm": confirm,
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
        "receipt_email": receipt_email,
        "setup_future_usage": setup_future_usage,
        "shipping": shipping,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "off_session": off_session,
    }
    return stripe_request(
        "POST",
        "/v1/payment_intents",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payment_intent(
    payment_intent_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "metadata": metadata,
        "description": description,
        "receipt_email": receipt_email,
        "shipping": shipping,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_intent(
    payment_intent_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        None,
        stripe_account=stripe_account,
    )
