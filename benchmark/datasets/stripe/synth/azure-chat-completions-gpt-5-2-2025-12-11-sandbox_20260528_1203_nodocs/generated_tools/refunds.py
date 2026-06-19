from typing import Any, Dict, Optional

from .http import stripe_request


def refunds_create(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
        "refund_application_fee": refund_application_fee,
        "reverse_transfer": reverse_transfer,
    }
    data, err = stripe_request(
        "POST",
        "/v1/refunds",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def refunds_retrieve(refund_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def refunds_update(
    refund_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"metadata": metadata}
    data, err = stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def refunds_list(
    limit: int = 10,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "charge": charge,
        "payment_intent": payment_intent,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/refunds", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
