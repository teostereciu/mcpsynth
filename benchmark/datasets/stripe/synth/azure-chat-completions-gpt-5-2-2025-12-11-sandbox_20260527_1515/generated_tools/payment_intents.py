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
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
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
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
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
        "metadata": metadata,
        "shipping": shipping,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )


def confirm_payment_intent(
    payment_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[bool | str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "payment_method": payment_method,
        "return_url": return_url,
        "off_session": off_session,
        "receipt_email": receipt_email,
        "setup_future_usage": setup_future_usage,
        "metadata": metadata,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def capture_payment_intent(
    payment_intent_id: str,
    *,
    amount_to_capture: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount_to_capture": amount_to_capture, "metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_payment_intent(
    payment_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
