from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_payout(
    amount: int,
    currency: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts"""
    body: Dict[str, Any] = {"amount": amount, "currency": currency}
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/payouts",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payouts/{id}"""
    return stripe_request("GET", f"/v1/payouts/{payout_id}", None, stripe_account=stripe_account)


def update_payout(
    payout_id: str,
    *,
    metadata: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{id}"""
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        {"metadata": metadata},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{id}/cancel"""
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payouts(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payouts"""
    return stripe_request("GET", "/v1/payouts", params, stripe_account=stripe_account)
