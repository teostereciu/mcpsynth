from typing import Any, Dict, Optional

from .http import stripe_request


def subscriptions_create(
    *,
    customer: str,
    items: list,
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "trial_period_days": trial_period_days,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        "/v1/subscriptions",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def subscriptions_retrieve(*, subscription_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def subscriptions_update(
    *,
    subscription_id: str,
    items: Optional[list] = None,
    cancel_at_period_end: Optional[bool] = None,
    default_payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    proration_behavior: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "items": items,
        "cancel_at_period_end": cancel_at_period_end,
        "default_payment_method": default_payment_method,
        "metadata": metadata,
        "proration_behavior": proration_behavior,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def subscriptions_cancel(
    *,
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    result, err = stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def subscriptions_list(
    *,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    price: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "status": status,
        "price": price,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    result, err = stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
