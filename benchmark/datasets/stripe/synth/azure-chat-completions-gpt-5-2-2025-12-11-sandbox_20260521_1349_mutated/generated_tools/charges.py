from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_charge(
    amount: int,
    currency: str,
    source: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges (Deprecated in Stripe docs, but still useful for legacy flows)"""
    body: Dict[str, Any] = {"amount": amount, "currency": currency, "source": source}
    if params:
        body.update(params)
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
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges/{charge}"""
    return stripe_request("GET", f"/v1/charges/{charge_id}", params, stripe_account=stripe_account)


def update_charge(
    charge_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges/{charge}"""
    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_charges(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/charges"""
    return stripe_request("GET", "/v1/charges", params, stripe_account=stripe_account)


def capture_charge(
    charge_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/charges/{charge}/capture"""
    return stripe_request(
        "POST",
        f"/v1/charges/{charge_id}/capture",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
