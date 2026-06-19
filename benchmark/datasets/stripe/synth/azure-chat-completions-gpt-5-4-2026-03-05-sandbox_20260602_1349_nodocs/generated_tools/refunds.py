from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/refunds",
        {"charge": charge, "payment_intent": payment_intent, "amount": amount, "reason": reason, "metadata": metadata},
    )


def retrieve_refund(refund_id: str) -> Any:
    return stripe_request("GET", f"/v1/refunds/{refund_id}")


def update_refund(refund_id: str, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", f"/v1/refunds/{refund_id}", {"metadata": metadata})


def list_refunds(charge: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/refunds", {"charge": charge, "payment_intent": payment_intent, "limit": limit})


def cancel_refund(refund_id: str) -> Any:
    return stripe_request("POST", f"/v1/refunds/{refund_id}/cancel")
