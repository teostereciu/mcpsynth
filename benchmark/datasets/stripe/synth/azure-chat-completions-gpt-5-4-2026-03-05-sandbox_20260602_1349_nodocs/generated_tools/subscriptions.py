from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_subscription(
    customer: str,
    price_id: str,
    quantity: Optional[int] = None,
    trial_period_days: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    params = {
        "customer": customer,
        "items[0][price]": price_id,
        "quantity": quantity,
        "trial_period_days": trial_period_days,
        "metadata": metadata,
    }
    if quantity is not None:
        params["items[0][quantity]"] = quantity
        params.pop("quantity", None)
    return stripe_request("POST", "/v1/subscriptions", params)


def retrieve_subscription(subscription_id: str) -> Any:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}")


def update_subscription(subscription_id: str, metadata: Optional[Dict[str, Any]] = None, cancel_at_period_end: Optional[bool] = None) -> Any:
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}", {"metadata": metadata, "cancel_at_period_end": cancel_at_period_end})


def list_subscriptions(customer: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/subscriptions", {"customer": customer, "status": status, "limit": limit})


def cancel_subscription(subscription_id: str, invoice_now: Optional[bool] = None, prorate: Optional[bool] = None) -> Any:
    return stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", {"invoice_now": invoice_now, "prorate": prorate})
