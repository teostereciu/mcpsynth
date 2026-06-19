from typing import Any, Dict, Optional

from .stripe_client import stripe_request


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
    default_source: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    trial_end: Optional[object] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[object] = None,
    proration_behavior: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "items": items}
    if currency is not None:
        params["currency"] = currency
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if payment_behavior is not None:
        params["payment_behavior"] = payment_behavior
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if default_source is not None:
        params["default_source"] = default_source
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if discounts is not None:
        params["discounts"] = discounts
    if trial_end is not None:
        params["trial_end"] = trial_end
    if trial_period_days is not None:
        params["trial_period_days"] = trial_period_days
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end
    if cancel_at is not None:
        params["cancel_at"] = cancel_at
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if payment_settings is not None:
        params["payment_settings"] = payment_settings

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
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
    )


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[list[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[object] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if items is not None:
        params["items"] = items
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end
    if cancel_at is not None:
        params["cancel_at"] = cancel_at
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior
    if payment_behavior is not None:
        params["payment_behavior"] = payment_behavior
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if discounts is not None:
        params["discounts"] = discounts
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if payment_settings is not None:
        params["payment_settings"] = payment_settings

    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
    )


def cancel_subscription(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if invoice_now is not None:
        params["invoice_now"] = invoice_now
    if prorate is not None:
        params["prorate"] = prorate
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    collection_method: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if price is not None:
        params["price"] = price
    if status is not None:
        params["status"] = status
    if collection_method is not None:
        params["collection_method"] = collection_method
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request(
        "GET",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
    )
