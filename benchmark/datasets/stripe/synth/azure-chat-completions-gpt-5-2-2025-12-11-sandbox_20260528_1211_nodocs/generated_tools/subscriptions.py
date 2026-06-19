from typing import Any, Dict, Optional

from .http import stripe_request


def create_subscription(
    customer: str,
    *,
    items: list[Dict[str, Any]],
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    trial_end: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    proration_behavior: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer, "items": items}
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    if trial_end is not None:
        data["trial_end"] = trial_end
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = cancel_at_period_end
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if coupon is not None:
        data["coupon"] = coupon
    if promotion_code is not None:
        data["promotion_code"] = promotion_code
    if metadata is not None:
        data["metadata"] = metadata
    if payment_behavior is not None:
        data["payment_behavior"] = payment_behavior
    if proration_behavior is not None:
        data["proration_behavior"] = proration_behavior

    res, err = stripe_request(
        "POST",
        "/v1/subscriptions",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_subscription(subscription_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[list[Dict[str, Any]]] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if items is not None:
        data["items"] = items
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = cancel_at_period_end
    if proration_behavior is not None:
        data["proration_behavior"] = proration_behavior
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if metadata is not None:
        data["metadata"] = metadata
    if coupon is not None:
        data["coupon"] = coupon
    if promotion_code is not None:
        data["promotion_code"] = promotion_code

    res, err = stripe_request("POST", f"/v1/subscriptions/{subscription_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def cancel_subscription(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if invoice_now is not None:
        data["invoice_now"] = invoice_now
    if prorate is not None:
        data["prorate"] = prorate

    res, err = stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    price: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if customer is not None:
        query["customer"] = customer
    if status is not None:
        query["status"] = status
    if price is not None:
        query["price"] = price
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/subscriptions", query=query, stripe_account=stripe_account)
    return res if err is None else err
