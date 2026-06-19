from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/transfers"""
    body = {"amount": amount, "currency": currency, "destination": destination}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/transfers",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_transfer(
    transfer_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/transfers/{transfer}"""
    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_transfer(
    transfer_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/transfers/{transfer}"""
    return stripe_request(
        "GET",
        f"/v1/transfers/{transfer_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def list_transfers(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/transfers"""
    return stripe_request("GET", "/v1/transfers", params or {}, stripe_account=stripe_account)
