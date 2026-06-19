from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    instructions_email: Optional[str] = None,
    origin: Optional[str] = None,
    refund_application_fee: Optional[bool] = None,
    reverse_transfer: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds

    Doc: docs/refunds.md (Create a refund)
    """
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
        "instructions_email": instructions_email,
        "origin": origin,
        "refund_application_fee": refund_application_fee,
        "reverse_transfer": reverse_transfer,
    }
    return stripe_request(
        "POST",
        "/v1/refunds",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_refund(
    refund_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds/{refund_id}

    Doc: docs/refunds.md (Retrieve a refund)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/refunds/{refund_id}",
        params,
        stripe_account=stripe_account,
    )


def update_refund(
    refund_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds/{refund_id}

    Doc: docs/refunds.md (Update a refund)
    """
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/refunds/{refund_id}",
        params,
        stripe_account=stripe_account,
    )


def list_refunds(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/refunds

    Doc: docs/refunds.md (List all refunds)
    """
    params: Dict[str, Any] = {
        "charge": charge,
        "payment_intent": payment_intent,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/refunds",
        params,
        stripe_account=stripe_account,
    )
