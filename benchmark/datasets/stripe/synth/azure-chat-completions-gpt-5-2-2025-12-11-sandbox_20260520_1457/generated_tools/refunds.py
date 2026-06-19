from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    instructions_email: Optional[str] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "instructions_email": instructions_email,
        "refund_application_fee": refund_application_fee,
        "reverse_transfer": reverse_transfer,
        "metadata": metadata,
    }
    status, payload = stripe_request(
        "POST", "/v1/refunds", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_refund(
    *,
    refund_id: str,
    metadata: Dict[str, str],
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    status, payload = stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params={"metadata": metadata},
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def retrieve_refund(*, refund_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/refunds/{refund_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_refunds(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/refunds", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
