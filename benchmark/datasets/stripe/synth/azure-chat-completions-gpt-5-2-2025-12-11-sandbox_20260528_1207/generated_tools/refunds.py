from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    instructions_email: Optional[str] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
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
    if instructions_email is not None:
        params["instructions_email"] = instructions_email
    if refund_application_fee is not None:
        params["refund_application_fee"] = refund_application_fee
    if reverse_transfer is not None:
        params["reverse_transfer"] = reverse_transfer
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/refunds",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_refund(
    refund_id: str,
    *,
    metadata: Dict[str, str],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params={"metadata": metadata},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_refund(refund_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)


def list_refunds(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if charge is not None:
        params["charge"] = charge
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/refunds", params=params, stripe_account=stripe_account)
