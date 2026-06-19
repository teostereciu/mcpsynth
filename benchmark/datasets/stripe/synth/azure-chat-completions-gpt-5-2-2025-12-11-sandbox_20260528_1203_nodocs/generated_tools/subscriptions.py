from typing import Any, Dict, Optional

from .http import stripe_request


def subscriptions_create(
    customer: str,
    items: list,
    default_payment_method: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_period_days: Optional[int] = None,
    trial_end: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    proration_behavior: Optional[str] = None,
    cancel_at_period_end: Optional[bool] = None,
    backdate_start_date: Optional[int] = None,
    billing_cycle_anchor: Optional[int] = None,
    default_tax_rates: Optional[list] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_percent: Optional[float] = None,
    on_behalf_of: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "trial_period_days": trial_period_days,
        "trial_end": trial_end,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "proration_behavior": proration_behavior,
        "cancel_at_period_end": cancel_at_period_end,
        "backdate_start_date": backdate_start_date,
        "billing_cycle_anchor": billing_cycle_anchor,
        "default_tax_rates": default_tax_rates,
        "automatic_tax": automatic_tax,
        "transfer_data": transfer_data,
        "application_fee_percent": application_fee_percent,
        "on_behalf_of": on_behalf_of,
    }
    data, err = stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def subscriptions_retrieve(subscription_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def subscriptions_update(
    subscription_id: str,
    items: Optional[list] = None,
    default_payment_method: Optional[str] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    trial_end: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_tax_rates: Optional[list] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_percent: Optional[float] = None,
    on_behalf_of: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "items": items,
        "default_payment_method": default_payment_method,
        "cancel_at_period_end": cancel_at_period_end,
        "proration_behavior": proration_behavior,
        "payment_behavior": payment_behavior,
        "trial_end": trial_end,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
        "automatic_tax": automatic_tax,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_tax_rates": default_tax_rates,
        "transfer_data": transfer_data,
        "application_fee_percent": application_fee_percent,
        "on_behalf_of": on_behalf_of,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def subscriptions_cancel(
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"invoice_now": invoice_now, "prorate": prorate}
    data, err = stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def subscriptions_list(
    limit: int = 10,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    price: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "customer": customer,
        "status": status,
        "price": price,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
