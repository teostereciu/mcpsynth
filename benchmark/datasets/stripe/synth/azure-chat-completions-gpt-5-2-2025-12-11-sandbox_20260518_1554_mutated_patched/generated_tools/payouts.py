from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payout(
    amount: int,
    currency: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    source_type: Optional[str] = None,
    payout_method: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
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
    return stripe_request(
        "POST",
        "/v1/payouts",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_payout(
    payout_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/payouts/{payout_id}",
        params=params or None,
        stripe_account=stripe_account,
    )


def update_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params=params,
        stripe_account=stripe_account,
    )


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        params=None,
        stripe_account=stripe_account,
    )


def reverse_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params=params,
        stripe_account=stripe_account,
    )


def list_payouts(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "status": status,
        "destination": destination,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    return stripe_request(
        "GET",
        "/v1/payouts",
        params=params,
        stripe_account=stripe_account,
    )
