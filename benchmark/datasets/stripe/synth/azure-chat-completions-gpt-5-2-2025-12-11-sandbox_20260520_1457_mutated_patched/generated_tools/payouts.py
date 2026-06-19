from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payout(
    amount: int,
    currency: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    source_type: Optional[str] = None,
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
    }
    _, data = stripe_request(
        "POST",
        "/v1/payouts",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/payouts/{payout_id}",
        stripe_account=stripe_account,
    )
    return data


def update_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"metadata": metadata}
    _, data = stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def reverse_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def list_payouts(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    limit: Optional[int] = None,
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
    _, data = stripe_request(
        "GET",
        "/v1/payouts",
        params=params,
        stripe_account=stripe_account,
    )
    return data
