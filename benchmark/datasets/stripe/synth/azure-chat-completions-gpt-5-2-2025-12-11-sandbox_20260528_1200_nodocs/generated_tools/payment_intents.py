from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def payment_intents_create(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    capture_method: Optional[str] = None,
    confirmation_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "payment_method": payment_method,
        "confirm": confirm,
        "capture_method": capture_method,
        "confirmation_method": confirmation_method,
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "setup_future_usage": setup_future_usage,
        "statement_descriptor": statement_descriptor,
        "statement_descriptor_suffix": statement_descriptor_suffix,
        "shipping": shipping,
        "automatic_payment_methods": automatic_payment_methods,
        "transfer_data": transfer_data,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
    }
    res, err = stripe_post(
        "/v1/payment_intents",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def payment_intents_retrieve(*, payment_intent_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/payment_intents/{payment_intent_id}", stripe_account=stripe_account)
    return err or res


def payment_intents_update(
    *,
    payment_intent_id: str,
    amount: Optional[int] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    payment_method: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "amount": amount,
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "payment_method": payment_method,
        "shipping": shipping,
    }
    res, err = stripe_post(f"/v1/payment_intents/{payment_intent_id}", data=data, stripe_account=stripe_account)
    return err or res


def payment_intents_confirm(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    mandate: Optional[str] = None,
    off_session: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "payment_method": payment_method,
        "return_url": return_url,
        "mandate": mandate,
        "off_session": off_session,
    }
    res, err = stripe_post(
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def payment_intents_capture(
    *,
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {"amount_to_capture": amount_to_capture, "metadata": metadata}
    res, err = stripe_post(
        f"/v1/payment_intents/{payment_intent_id}/capture",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def payment_intents_cancel(
    *,
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    res, err = stripe_post(
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def payment_intents_list(
    *,
    customer: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    res, err = stripe_get("/v1/payment_intents", params=params, stripe_account=stripe_account)
    return err or res
