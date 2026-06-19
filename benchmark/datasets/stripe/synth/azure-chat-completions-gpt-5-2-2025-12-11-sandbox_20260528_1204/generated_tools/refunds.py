from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/refunds
# GET /v1/refunds/{refund}
# POST /v1/refunds/{refund}
# GET /v1/refunds


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/refunds",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_refund(refund_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)


def update_refund(
    refund_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params={"metadata": metadata} if metadata is not None else {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


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
    return stripe_request("GET", "/v1/refunds", params=params, stripe_account=stripe_account)
