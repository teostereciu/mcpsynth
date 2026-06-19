from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents"""
    body: Dict[str, Any] = {"amount": amount, "currency": currency}
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/payment_intents",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_intent(
    payment_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_intents/{intent}"""
    return stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        params,
        stripe_account=stripe_account,
    )


def update_payment_intent(
    payment_intent_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}"""
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def confirm_payment_intent(
    payment_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}/confirm"""
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def capture_payment_intent(
    payment_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}/capture"""
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_payment_intent(
    payment_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}/cancel"""
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_intents(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_intents"""
    return stripe_request(
        "GET",
        "/v1/payment_intents",
        params,
        stripe_account=stripe_account,
    )
