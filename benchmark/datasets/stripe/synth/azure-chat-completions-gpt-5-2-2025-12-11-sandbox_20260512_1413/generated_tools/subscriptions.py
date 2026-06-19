from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def subscriptions_create(
    customer: str,
    items: list,
    *,
    currency: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    discounts: Optional[list] = None,
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
        "trial_end": trial_end,
        "trial_period_days": trial_period_days,
        "automatic_tax": automatic_tax,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "discounts": discounts,
    }
    return stripe_request("POST", "/v1/subscriptions", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def subscriptions_retrieve(subscription_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", None, stripe_account=stripe_account)


def subscriptions_update(
    subscription_id: str,
    *,
    items: Optional[list] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    discounts: Optional[list] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "items": items,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "cancel_at_period_end": cancel_at_period_end,
        "cancel_at": cancel_at,
        "proration_behavior": proration_behavior,
        "payment_behavior": payment_behavior,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "trial_end": trial_end,
        "automatic_tax": automatic_tax,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "discounts": discounts,
    }
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}", params, stripe_account=stripe_account)


def subscriptions_cancel(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def subscriptions_list(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
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
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/subscriptions", params, stripe_account=stripe_account)


def subscriptions_list_all(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "price": price, "status": status, "created": created}
    return stripe_list_all("/v1/subscriptions", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
