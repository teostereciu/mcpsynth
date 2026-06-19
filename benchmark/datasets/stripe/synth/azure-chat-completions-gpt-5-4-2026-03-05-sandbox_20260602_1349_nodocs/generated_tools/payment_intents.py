from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/payment_intents",
        {
            "amount": amount,
            "currency": currency,
            "customer": customer,
            "payment_method": payment_method,
            "confirm": confirm,
            "description": description,
            "metadata": metadata,
        },
    )


def retrieve_payment_intent(payment_intent_id: str) -> Any:
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")


def update_payment_intent(
    payment_intent_id: str,
    amount: Optional[int] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        {"amount": amount, "customer": customer, "description": description, "metadata": metadata},
    )


def confirm_payment_intent(payment_intent_id: str, payment_method: Optional[str] = None) -> Any:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", {"payment_method": payment_method})


def cancel_payment_intent(payment_intent_id: str, cancellation_reason: Optional[str] = None) -> Any:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", {"cancellation_reason": cancellation_reason})


def list_payment_intents(customer: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/payment_intents", {"customer": customer, "limit": limit})
