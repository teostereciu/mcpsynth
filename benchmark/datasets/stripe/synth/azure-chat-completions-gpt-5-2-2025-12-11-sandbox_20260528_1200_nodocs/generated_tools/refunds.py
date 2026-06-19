from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def refunds_create(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
        "refund_application_fee": refund_application_fee,
        "reverse_transfer": reverse_transfer,
    }
    res, err = stripe_post(
        "/v1/refunds",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def refunds_retrieve(*, refund_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/refunds/{refund_id}", stripe_account=stripe_account)
    return err or res


def refunds_update(
    *,
    refund_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {"metadata": metadata}
    res, err = stripe_post(f"/v1/refunds/{refund_id}", data=data, stripe_account=stripe_account)
    return err or res


def refunds_list(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    res, err = stripe_get("/v1/refunds", params=params, stripe_account=stripe_account)
    return err or res
