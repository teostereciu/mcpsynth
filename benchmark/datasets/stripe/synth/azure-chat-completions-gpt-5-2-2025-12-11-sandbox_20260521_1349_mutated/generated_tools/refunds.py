from typing import Any, Dict, Optional

from .stripe_client import stripe_request


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
    if params:
        body.update(params)
    if not body.get("charge") and not body.get("payment_intent"):
        return {"error": "Either 'charge' or 'payment_intent' is required"}
    return stripe_request(
        "POST",
        "/v1/refunds",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_refund(
    refund_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds/{refund}"""
    return stripe_request("GET", f"/v1/refunds/{refund_id}", None, stripe_account=stripe_account)


def update_refund(
    refund_id: str,
    *,
    metadata: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds/{refund}"""
    return stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        {"metadata": metadata},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_refunds(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds"""
    return stripe_request("GET", "/v1/refunds", params, stripe_account=stripe_account)
