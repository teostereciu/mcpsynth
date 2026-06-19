from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_checkout_session(
    mode: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions"""
    body = {"mode": mode}
    body.update(params or {})
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
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions/{session}"""
    return stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def list_checkout_sessions(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions"""
    return stripe_request("GET", "/v1/checkout/sessions", params or {}, stripe_account=stripe_account)


def expire_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions/{session}/expire"""
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
