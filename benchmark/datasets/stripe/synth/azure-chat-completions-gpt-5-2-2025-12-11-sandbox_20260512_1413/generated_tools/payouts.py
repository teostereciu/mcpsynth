from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def payouts_create(
    amount: int,
    currency: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    source_type: Optional[str] = None,
    payout_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "description": description,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
        "destination": destination,
        "method": method,
        "source_type": source_type,
        "payout_method": payout_method,
    }
    return stripe_request("POST", "/v1/payouts", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def payouts_retrieve(payout_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", None, stripe_account=stripe_account)


def payouts_update(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request("POST", f"/v1/payouts/{payout_id}", params, stripe_account=stripe_account)


def payouts_cancel(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payouts_reverse(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payouts_list(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    arrival_date: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "status": status,
        "destination": destination,
        "created": created,
        "arrival_date": arrival_date,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/payouts", params, stripe_account=stripe_account)


def payouts_list_all(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    arrival_date: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"status": status, "destination": destination, "created": created, "arrival_date": arrival_date}
    return stripe_list_all("/v1/payouts", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
