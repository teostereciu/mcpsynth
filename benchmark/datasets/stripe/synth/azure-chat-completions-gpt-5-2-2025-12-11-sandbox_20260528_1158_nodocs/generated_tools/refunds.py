from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def refunds_create(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/refunds", params=params, stripe_account=stripe_account)


def refunds_retrieve(*, refund_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)


def refunds_update(
    *,
    refund_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request("POST", f"/v1/refunds/{refund_id}", params=params, stripe_account=stripe_account)


def refunds_list(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/refunds", params=params, stripe_account=stripe_account)
