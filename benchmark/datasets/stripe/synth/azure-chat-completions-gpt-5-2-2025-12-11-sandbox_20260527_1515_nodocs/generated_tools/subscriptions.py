from typing import Any, Dict, Optional

from ._client import stripe_request


def subscriptions_create(
    *,
    customer: str,
    items: list[Dict[str, Any]],
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    trial_end: Optional[int] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    proration_behavior: Optional[str] = None,
    cancel_at_period_end: Optional[bool] = None,
    default_tax_rates: Optional[list[str]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "trial_period_days": trial_period_days,
        "trial_end": trial_end,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "proration_behavior": proration_behavior,
        "cancel_at_period_end": cancel_at_period_end,
        "default_tax_rates": default_tax_rates,
        "automatic_tax": automatic_tax,
    }
    data, err = stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or data  # type: ignore[return-value]


def subscriptions_retrieve(*, subscription_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def subscriptions_update(
    *,
    subscription_id: str,
    items: Optional[list[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    pause_collection: Optional[Dict[str, Any]] = None,
    trial_end: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "items": items,
        "default_payment_method": default_payment_method,
        "cancel_at_period_end": cancel_at_period_end,
        "proration_behavior": proration_behavior,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "pause_collection": pause_collection,
        "trial_end": trial_end,
    }
    data, err = stripe_request("POST", f"/v1/subscriptions/{subscription_id}", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def subscriptions_cancel(
    *,
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"invoice_now": invoice_now, "prorate": prorate}
    data, err = stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]


def subscriptions_list(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "price": price,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    data, err = stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
    return err or data  # type: ignore[return-value]
