from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def refunds_create(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    instructions_email: Optional[str] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
        "instructions_email": instructions_email,
        "refund_application_fee": refund_application_fee,
        "reverse_transfer": reverse_transfer,
    }
    return stripe_request("POST", "/v1/refunds", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def refunds_retrieve(refund_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund_id}", None, stripe_account=stripe_account)


def refunds_update(
    refund_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request("POST", f"/v1/refunds/{refund_id}", params, stripe_account=stripe_account)


def refunds_list(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/refunds", params, stripe_account=stripe_account)


def refunds_list_all(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"charge": charge, "payment_intent": payment_intent, "created": created}
    return stripe_list_all("/v1/refunds", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
