from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def payment_intents_create(
    amount: int,
    currency: str,
    *,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
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
        "metadata": metadata,
        "shipping": shipping,
        "automatic_payment_methods": automatic_payment_methods,
    }
    return stripe_request("POST", "/v1/payment_intents", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def payment_intents_retrieve(payment_intent_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", None, stripe_account=stripe_account)


def payment_intents_update(
    payment_intent_id: str,
    *,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
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
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", params, stripe_account=stripe_account)


def payment_intents_confirm(
    payment_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
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
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_capture(
    payment_intent_id: str,
    *,
    amount_to_capture: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount_to_capture": amount_to_capture, "metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_cancel(
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
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_list(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/payment_intents", params, stripe_account=stripe_account)


def payment_intents_list_all(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "created": created}
    return stripe_list_all("/v1/payment_intents", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
