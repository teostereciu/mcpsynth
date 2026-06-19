from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


def create_payment_intent(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    confirm: Optional[bool] = None,
    off_session: Optional[Any] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "description": description,
        "payment_method": payment_method,
        "receipt_email": receipt_email,
        "confirm": confirm,
        "off_session": off_session,
        "setup_future_usage": setup_future_usage,
        "automatic_payment_methods": automatic_payment_methods,
        "shipping": shipping,
        "metadata": metadata,
    }
    status, payload = stripe_request(
        "POST", "/v1/payment_intents", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_payment_intent(*, payment_intent_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_payment_intent(
    *,
    payment_intent_id: str,
    amount: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "amount": amount,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
        "receipt_email": receipt_email,
        "shipping": shipping,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def confirm_payment_intent(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    error_on_requires_action: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "payment_method": payment_method,
        "return_url": return_url,
        "off_session": off_session,
        "receipt_email": receipt_email,
        "setup_future_usage": setup_future_usage,
        "error_on_requires_action": error_on_requires_action,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def capture_payment_intent(
    *,
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"amount_to_capture": amount_to_capture, "metadata": metadata}
    status, payload = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def cancel_payment_intent(
    *,
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    status, payload = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    status, payload = stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
