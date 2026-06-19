from typing import Any, Dict, Optional

from .http import stripe_request


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if charge is not None:
        data["charge"] = charge
    if payment_intent is not None:
        data["payment_intent"] = payment_intent
    if amount is not None:
        data["amount"] = amount
    if reason is not None:
        data["reason"] = reason
    if metadata is not None:
        data["metadata"] = metadata
    if refund_application_fee is not None:
        data["refund_application_fee"] = refund_application_fee
    if reverse_transfer is not None:
        data["reverse_transfer"] = reverse_transfer

    res, err = stripe_request(
        "POST",
        "/v1/refunds",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_refund(refund_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_refund(
    refund_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/refunds/{refund_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def list_refunds(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if charge is not None:
        query["charge"] = charge
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/refunds", query=query, stripe_account=stripe_account)
    return res if err is None else err


def cancel_refund(refund_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/refunds/{refund_id}/cancel", data={}, stripe_account=stripe_account)
    return res if err is None else err
