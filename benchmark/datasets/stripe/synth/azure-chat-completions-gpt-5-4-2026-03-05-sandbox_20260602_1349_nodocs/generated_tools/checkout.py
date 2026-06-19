from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_checkout_session(
    mode: str,
    success_url: str,
    cancel_url: str,
    price_id: str,
    quantity: int = 1,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        {
            "mode": mode,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "customer": customer,
            "customer_email": customer_email,
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": quantity,
            "metadata": metadata,
        },
    )


def retrieve_checkout_session(session_id: str) -> Any:
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}")


def list_checkout_sessions(customer: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/checkout/sessions", {"customer": customer, "payment_intent": payment_intent, "limit": limit})


def expire_checkout_session(session_id: str) -> Any:
    return stripe_request("POST", f"/v1/checkout/sessions/{session_id}/expire")


def create_payment_link(price_id: str, quantity: int = 1, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/payment_links", {"line_items[0][price]": price_id, "line_items[0][quantity]": quantity, "metadata": metadata})


def retrieve_payment_link(payment_link_id: str) -> Any:
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}")


def list_payment_links(active: Optional[bool] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/payment_links", {"active": active, "limit": limit})


def update_payment_link(payment_link_id: str, active: Optional[bool] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", f"/v1/payment_links/{payment_link_id}", {"active": active, "metadata": metadata})
