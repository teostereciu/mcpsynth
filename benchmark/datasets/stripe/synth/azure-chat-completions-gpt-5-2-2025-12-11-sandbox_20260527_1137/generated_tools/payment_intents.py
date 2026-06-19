from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents"""
    body = {"amount": amount, "currency": currency}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/payment_intents",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payment_intent(
    payment_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}"""
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_intent(
    payment_intent_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_intents/{intent}"""
    return stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def list_payment_intents(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_intents"""
    return stripe_request("GET", "/v1/payment_intents", params or {}, stripe_account=stripe_account)


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
        params or {},
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
        params or {},
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
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
