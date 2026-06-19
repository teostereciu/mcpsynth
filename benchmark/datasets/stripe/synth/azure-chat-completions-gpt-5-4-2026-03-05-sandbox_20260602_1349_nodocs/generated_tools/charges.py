from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_charge(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    source: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/charges",
        {
            "amount": amount,
            "currency": currency,
            "customer": customer,
            "source": source,
            "description": description,
            "metadata": metadata,
        },
    )


def retrieve_charge(charge_id: str) -> Any:
    return stripe_request("GET", f"/v1/charges/{charge_id}")


def update_charge(charge_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", f"/v1/charges/{charge_id}", {"description": description, "metadata": metadata})


def list_charges(customer: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/charges", {"customer": customer, "payment_intent": payment_intent, "limit": limit})


def capture_charge(charge_id: str, amount: Optional[int] = None) -> Any:
    return stripe_request("POST", f"/v1/charges/{charge_id}/capture", {"amount": amount})
