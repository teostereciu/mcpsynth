from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    *,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "automatic_tax": automatic_tax,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/subscriptions",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_subscription(
    subscription_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    default_payment_method: Optional[str] = None,
    cancel_at_period_end: Optional[bool] = None,
    description: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "metadata": metadata,
        "default_payment_method": default_payment_method,
        "cancel_at_period_end": cancel_at_period_end,
        "description": description,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(
    subscription_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        None,
        stripe_account=stripe_account,
    )
