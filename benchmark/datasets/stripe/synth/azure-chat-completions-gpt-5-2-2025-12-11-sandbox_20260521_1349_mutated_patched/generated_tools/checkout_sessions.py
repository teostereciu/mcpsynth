from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_checkout_session(
    mode: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions"""
    body = {"mode": mode}
    body.update(params)
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(
    session_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions/{id}"""
    return stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        params,
        stripe_account=stripe_account,
    )


def expire_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions/{id}/expire"""
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_checkout_sessions(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions"""
    return stripe_request(
        "GET",
        "/v1/checkout/sessions",
        params,
        stripe_account=stripe_account,
    )
