from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def refunds_create(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    instructions_email: Optional[str] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
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
    if instructions_email is not None:
        data["instructions_email"] = instructions_email
    if refund_application_fee is not None:
        data["refund_application_fee"] = refund_application_fee
    if reverse_transfer is not None:
        data["reverse_transfer"] = reverse_transfer
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/refunds",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def refunds_retrieve(*, refund_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)


def refunds_update(
    *,
    refund_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def refunds_list(
    *,
    limit: Optional[int] = 10,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if charge is not None:
        query["charge"] = charge
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    if created is not None:
        query["created"] = created
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/refunds", params=query, stripe_account=stripe_account)
