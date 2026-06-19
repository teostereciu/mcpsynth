from typing import Any, Dict, Optional

from .http import stripe_delete, stripe_get, stripe_post


def subscriptions_create(
    *,
    customer: str,
    items: list,
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    trial_end: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    payment_behavior: Optional[str] = None,
    proration_behavior: Optional[str] = None,
    cancel_at_period_end: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "trial_period_days": trial_period_days,
        "trial_end": trial_end,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "payment_behavior": payment_behavior,
        "proration_behavior": proration_behavior,
        "cancel_at_period_end": cancel_at_period_end,
    }
    res, err = stripe_post(
        "/v1/subscriptions",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def subscriptions_retrieve(*, subscription_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)
    return err or res


def subscriptions_update(
    *,
    subscription_id: str,
    items: Optional[list] = None,
    default_payment_method: Optional[str] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "items": items,
        "default_payment_method": default_payment_method,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "cancel_at_period_end": cancel_at_period_end,
        "proration_behavior": proration_behavior,
        "payment_behavior": payment_behavior,
    }
    res, err = stripe_post(f"/v1/subscriptions/{subscription_id}", data=data, stripe_account=stripe_account)
    return err or res


def subscriptions_cancel(
    *,
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    res, err = stripe_delete(
        f"/v1/subscriptions/{subscription_id}",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def subscriptions_list(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "customer": customer,
        "price": price,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/subscriptions", params=params, stripe_account=stripe_account)
    return err or res
