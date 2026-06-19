from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def payouts_create(
    *,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    payout_method: Optional[str] = None,
    source_type: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if destination is not None:
        data["destination"] = destination
    if method is not None:
        data["method"] = method
    if payout_method is not None:
        data["payout_method"] = payout_method
    if source_type is not None:
        data["source_type"] = source_type
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/payouts",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payouts_retrieve(*, payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)


def payouts_update(
    *,
    payout_id: str,
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
        f"/v1/payouts/{payout_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payouts_cancel(
    *,
    payout_id: str,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        data=extra or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payouts_reverse(
    *,
    payout_id: str,
    amount: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount is not None:
        data["amount"] = amount
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payouts_list(
    *,
    limit: Optional[int] = 10,
    status: Optional[str] = None,
    arrival_date: Optional[Dict[str, Any]] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if status is not None:
        query["status"] = status
    if arrival_date is not None:
        query["arrival_date"] = arrival_date
    if created is not None:
        query["created"] = created
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/payouts", params=query, stripe_account=stripe_account)
