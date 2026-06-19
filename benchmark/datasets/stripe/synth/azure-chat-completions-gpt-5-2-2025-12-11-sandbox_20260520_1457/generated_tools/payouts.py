from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


def create_payout(
    *,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    payout_method: Optional[str] = None,
    source_type: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "description": description,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
        "destination": destination,
        "method": method,
        "payout_method": payout_method,
        "source_type": source_type,
    }
    status, payload = stripe_request(
        "POST", "/v1/payouts", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_payout(
    *,
    payout_id: str,
    metadata: Dict[str, str],
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    status, payload = stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params={"metadata": metadata},
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def retrieve_payout(*, payout_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_payouts(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "status": status,
        "destination": destination,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    status_code, payload = stripe_request("GET", "/v1/payouts", params=params, stripe_account=stripe_account)
    return ok_or_error(status_code, payload)
