from typing import Any, Dict, Optional

from ._client import stripe_request


def payment_intents_create(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirmation_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    capture_method: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "payment_method": payment_method,
        "confirmation_method": confirmation_method,
        "confirm": confirm,
        "capture_method": capture_method,
        "setup_future_usage": setup_future_usage,
        "description": description,
        "receipt_email": receipt_email,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
        "payment_method_types": payment_method_types,
        "transfer_data": transfer_data,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "shipping": shipping,
    }
    data, err = stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def payment_intents_retrieve(*, payment_intent_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def payment_intents_update(
    *,
    payment_intent_id: str,
    amount: Optional[int] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    setup_future_usage: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "shipping": shipping,
        "payment_method": payment_method,
        "payment_method_types": payment_method_types,
        "setup_future_usage": setup_future_usage,
        "transfer_data": transfer_data,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def payment_intents_confirm(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    receipt_email: Optional[str] = None,
    mandate: Optional[str] = None,
    off_session: Optional[bool] = None,
    setup_future_usage: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "payment_method": payment_method,
        "return_url": return_url,
        "receipt_email": receipt_email,
        "mandate": mandate,
        "off_session": off_session,
        "setup_future_usage": setup_future_usage,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def payment_intents_capture(
    *,
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    application_fee_amount: Optional[int] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount_to_capture": amount_to_capture,
        "application_fee_amount": application_fee_amount,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "transfer_data": transfer_data,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def payment_intents_cancel(
    *,
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"cancellation_reason": cancellation_reason}
    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


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
    data, err = stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]
