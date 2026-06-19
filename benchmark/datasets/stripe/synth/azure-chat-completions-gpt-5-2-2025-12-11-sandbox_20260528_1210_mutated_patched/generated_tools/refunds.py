from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
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

    return stripe_request_with_retries(
        "POST",
        "/v1/refunds",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_refund(refund_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/refunds/{refund_id}",
        stripe_account=stripe_account,
    )


def update_refund(
    refund_id: str,
    *,
    metadata: Dict[str, Any],
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "POST",
        f"/v1/refunds/{refund_id}",
        params={"metadata": metadata},
        stripe_account=stripe_account,
    )


def list_refunds(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if charge is not None:
        params["charge"] = charge
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/refunds",
        params=params,
        stripe_account=stripe_account,
    )
