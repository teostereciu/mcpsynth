from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_charge(
    amount: int,
    currency: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges (Deprecated by Stripe, but still useful for legacy flows)"""
    body = {"amount": amount, "currency": currency}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/charges",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_charge(
    charge_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges/{charge}"""
    return stripe_request(
        "GET",
        f"/v1/charges/{charge_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def update_charge(
    charge_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges/{charge}"""
    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_charges(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges"""
    return stripe_request("GET", "/v1/charges", params or {}, stripe_account=stripe_account)
