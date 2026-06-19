from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_setup_intent(customer: Optional[str] = None, payment_method: Optional[str] = None, confirm: Optional[bool] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/setup_intents", {"customer": customer, "payment_method": payment_method, "confirm": confirm, "metadata": metadata})


def retrieve_setup_intent(setup_intent_id: str) -> Any:
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")


def update_setup_intent(setup_intent_id: str, metadata: Optional[Dict[str, Any]] = None, description: Optional[str] = None) -> Any:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}", {"metadata": metadata, "description": description})


def confirm_setup_intent(setup_intent_id: str, payment_method: Optional[str] = None) -> Any:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", {"payment_method": payment_method})


def cancel_setup_intent(setup_intent_id: str, cancellation_reason: Optional[str] = None) -> Any:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", {"cancellation_reason": cancellation_reason})


def list_setup_intents(customer: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/setup_intents", {"customer": customer, "limit": limit})
