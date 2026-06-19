from typing import Any, Dict, Optional, List

from .http_client import ok_or_error, stripe_request


def create_subscription(
    *,
    customer: str,
    items: List[Dict[str, Any]],
    currency: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    add_invoice_items: Optional[List[Dict[str, Any]]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    off_session: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "currency": currency,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "automatic_tax": automatic_tax,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "trial_end": trial_end,
        "trial_period_days": trial_period_days,
        "cancel_at_period_end": cancel_at_period_end,
        "proration_behavior": proration_behavior,
        "add_invoice_items": add_invoice_items,
        "discounts": discounts,
        "invoice_settings": invoice_settings,
        "payment_settings": payment_settings,
        "off_session": off_session,
    }
    status, payload = stripe_request(
        "POST", "/v1/subscriptions", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_subscription(*, subscription_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_subscription(
    *,
    subscription_id: str,
    items: Optional[List[Dict[str, Any]]] = None,
    cancel_at_period_end: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    default_payment_method: Optional[str] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    trial_end: Optional[Any] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    pause_collection: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "items": items,
        "cancel_at_period_end": cancel_at_period_end,
        "description": description,
        "metadata": metadata,
        "default_payment_method": default_payment_method,
        "proration_behavior": proration_behavior,
        "payment_behavior": payment_behavior,
        "trial_end": trial_end,
        "automatic_tax": automatic_tax,
        "discounts": discounts,
        "invoice_settings": invoice_settings,
        "payment_settings": payment_settings,
        "pause_collection": pause_collection,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def cancel_subscription(
    *,
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    status, payload = stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    price: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "status": status,
        "price": price,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status_code, payload = stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
    return ok_or_error(status_code, payload)
