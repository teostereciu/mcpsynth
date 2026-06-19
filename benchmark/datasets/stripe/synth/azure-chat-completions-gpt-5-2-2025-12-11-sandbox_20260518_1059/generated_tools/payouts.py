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
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
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
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/payouts",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        {"metadata": metadata},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/payouts/{payout_id}",
        None,
        stripe_account=stripe_account,
    )
