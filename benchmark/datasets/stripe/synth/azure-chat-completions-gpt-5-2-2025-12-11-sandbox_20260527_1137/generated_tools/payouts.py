from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_payout(
    amount: int,
    currency: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts"""
    body = {"amount": amount, "currency": currency}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/payouts",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{payout}"""
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        {"metadata": metadata or {}},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payout(
    payout_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payouts/{payout}"""
    return stripe_request(
        "GET",
        f"/v1/payouts/{payout_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{payout}/cancel"""
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def reverse_payout(
    payout_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{payout}/reverse"""
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payouts(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payouts"""
    return stripe_request("GET", "/v1/payouts", params or {}, stripe_account=stripe_account)
