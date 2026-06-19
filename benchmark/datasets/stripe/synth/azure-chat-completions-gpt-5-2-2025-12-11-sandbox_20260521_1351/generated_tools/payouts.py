from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_payout(
    amount: int,
    currency: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    payout_method: Optional[str] = None,
    source_type: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "currency": currency}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if destination is not None:
        params["destination"] = destination
    if method is not None:
        params["method"] = method
    if payout_method is not None:
        params["payout_method"] = payout_method
    if source_type is not None:
        params["source_type"] = source_type

    return stripe_request("POST", "/v1/payouts", params=params, account=account, idempotency_key=idempotency_key)


def retrieve_payout(payout_id: str, *, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", params={}, account=account)


def update_payout(
    payout_id: str,
    *,
    metadata: Dict[str, str],
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params={"metadata": metadata},
        account=account,
        idempotency_key=idempotency_key,
    )


def cancel_payout(
    payout_id: str,
    *,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        params={},
        account=account,
        idempotency_key=idempotency_key,
    )


def reverse_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def list_payouts(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    arrival_date: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if destination is not None:
        params["destination"] = destination
    if created is not None:
        params["created"] = created
    if arrival_date is not None:
        params["arrival_date"] = arrival_date
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/payouts", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/payouts", params=params, account=account)
