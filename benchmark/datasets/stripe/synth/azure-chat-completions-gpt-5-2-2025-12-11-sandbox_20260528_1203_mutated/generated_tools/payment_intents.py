from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "confirm": confirm,
        "customer": customer,
        "payment_method": payment_method,
        "description": description,
        "receipt_email": receipt_email,
        "setup_future_usage": setup_future_usage,
        "automatic_payment_methods": automatic_payment_methods,
        "metadata": metadata,
        "shipping": shipping,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
    }
    return stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
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
        stripe_account=stripe_account,
    )


def update_payment_intent(
    payment_intent_id: str,
    *,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "payment_method": payment_method,
        "description": description,
        "receipt_email": receipt_email,
        "setup_future_usage": setup_future_usage,
        "automatic_payment_methods": automatic_payment_methods,
        "metadata": metadata,
        "shipping": shipping,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )
