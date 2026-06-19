from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
    }
    _, data = stripe_request(
        "POST",
        "/v1/refunds",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_refund(
    refund_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/refunds/{refund_id}",
        stripe_account=stripe_account,
    )
    return data


def update_refund(
    refund_id: str,
    *,
    metadata: Dict[str, Any],
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"metadata": metadata}
    _, data = stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def list_refunds(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    _, data = stripe_request(
        "GET",
        "/v1/refunds",
        params=params,
        stripe_account=stripe_account,
    )
    return data
