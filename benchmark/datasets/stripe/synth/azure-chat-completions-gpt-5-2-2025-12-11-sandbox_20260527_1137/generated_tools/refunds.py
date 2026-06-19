from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds"""
    body: Dict[str, Any] = {}
    if charge:
        body["charge"] = charge
    if payment_intent:
        body["payment_intent"] = payment_intent
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/refunds",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_refund(
    refund_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds/{refund}"""
    return stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        {"metadata": metadata or {}},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_refund(
    refund_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds/{refund}"""
    return stripe_request(
        "GET",
        f"/v1/refunds/{refund_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def list_refunds(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds"""
    return stripe_request("GET", "/v1/refunds", params or {}, stripe_account=stripe_account)
