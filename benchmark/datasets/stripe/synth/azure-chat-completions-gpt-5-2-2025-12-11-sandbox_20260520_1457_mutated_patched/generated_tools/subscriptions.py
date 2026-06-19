from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    *,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "trial_end": trial_end,
        "trial_period_days": trial_period_days,
        "cancel_at_period_end": cancel_at_period_end,
        "automatic_tax": automatic_tax,
        "coupon": coupon,
        "promotion_code": promotion_code,
    }
    _, data = stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_subscription(
    subscription_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        stripe_account=stripe_account,
    )
    return data


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[list[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "items": items,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "cancel_at_period_end": cancel_at_period_end,
        "proration_behavior": proration_behavior,
        "coupon": coupon,
        "promotion_code": promotion_code,
    }
    _, data = stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def cancel_subscription(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"invoice_now": invoice_now, "prorate": prorate}
    _, data = stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "price": price,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    _, data = stripe_request(
        "GET",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
    )
    return data
