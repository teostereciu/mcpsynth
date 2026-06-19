from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/payouts
# GET /v1/payouts/{payout}
# POST /v1/payouts/{payout}
# GET /v1/payouts
# POST /v1/payouts/{payout}/cancel
# POST /v1/payouts/{payout}/reverse


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
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
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
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/payouts",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payout(payout_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)


def update_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"metadata": metadata} if metadata is not None else {}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


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
    return stripe_request("GET", "/v1/payouts", params=params, stripe_account=stripe_account)


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        params={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def reverse_payout(
    payout_id: str,
    *,
    amount: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
