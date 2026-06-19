from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/subscriptions.md

def create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    *,
    currency: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    off_session: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "currency": currency,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "cancel_at_period_end": cancel_at_period_end,
        "cancel_at": cancel_at,
        "trial_end": trial_end,
        "trial_period_days": trial_period_days,
        "automatic_tax": automatic_tax,
        "discounts": discounts,
        "invoice_settings": invoice_settings,
        "payment_settings": payment_settings,
        "proration_behavior": proration_behavior,
        "off_session": off_session,
    }
    return stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(
    subscription_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        params={"expand": expand},
        stripe_account=stripe_account,
    )


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[list[Dict[str, Any]]] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    trial_end: Optional[Any] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "items": items,
        "cancel_at_period_end": cancel_at_period_end,
        "cancel_at": cancel_at,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "proration_behavior": proration_behavior,
        "payment_behavior": payment_behavior,
        "discounts": discounts,
        "trial_end": trial_end,
        "invoice_settings": invoice_settings,
        "payment_settings": payment_settings,
        "automatic_tax": automatic_tax,
    }
    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_subscription(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"invoice_now": invoice_now, "prorate": prorate}
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    collection_method: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "price": price,
        "status": status,
        "collection_method": collection_method,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
    )
