from typing import Any, Dict, Optional

from .http import stripe_request


def payment_intents_create(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    capture_method: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "payment_method": payment_method,
        "confirm": confirm,
        "capture_method": capture_method,
        "setup_future_usage": setup_future_usage,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
        "transfer_data": transfer_data,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        "/v1/payment_intents",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_intents_retrieve(*, payment_intent_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def payment_intents_update(
    *,
    payment_intent_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "customer": customer,
        "payment_method": payment_method,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_intents_confirm(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"payment_method": payment_method, "return_url": return_url}
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_intents_capture(
    *,
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount_to_capture": amount_to_capture}
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_intents_cancel(
    *,
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    result, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_intents_list(
    *,
    customer: Optional[str] = None,
    limit: int = 10,
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
    result, err = stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
