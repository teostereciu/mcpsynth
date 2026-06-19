from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    instructions_email: Optional[str] = None,
    origin: Optional[str] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds"""
    params: Dict[str, Any] = {}
    if charge is not None:
        params["charge"] = charge
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if amount is not None:
        params["amount"] = amount
    if reason is not None:
        params["reason"] = reason
    if metadata is not None:
        params["metadata"] = metadata
    if instructions_email is not None:
        params["instructions_email"] = instructions_email
    if origin is not None:
        params["origin"] = origin
    if refund_application_fee is not None:
        params["refund_application_fee"] = refund_application_fee
    if reverse_transfer is not None:
        params["reverse_transfer"] = reverse_transfer

    if charge is None and payment_intent is None:
        return {"error": "invalid_request", "message": "Must provide either charge or payment_intent"}

    data, err = stripe_request(
        "POST",
        "/v1/refunds",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_refund(
    refund_id: str,
    *,
    metadata: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds/{refund}"""
    data, err = stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params={"metadata": metadata},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_refund(
    refund_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds/{refund}"""
    data, err = stripe_request(
        "GET",
        f"/v1/refunds/{refund_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
