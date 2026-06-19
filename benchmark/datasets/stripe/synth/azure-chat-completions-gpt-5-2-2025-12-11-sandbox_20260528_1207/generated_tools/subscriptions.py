from typing import Any, Dict, Optional, List

from .http_client import stripe_request


def create_subscription(
    *,
    customer: str,
    items: List[Dict[str, Any]],
    currency: Optional[str] = None,
    customer_account: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    add_invoice_items: Optional[List[Dict[str, Any]]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "items": items}
    if currency is not None:
        params["currency"] = currency
    if customer_account is not None:
        params["customer_account"] = customer_account
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if payment_behavior is not None:
        params["payment_behavior"] = payment_behavior
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
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if payment_settings is not None:
        params["payment_settings"] = payment_settings
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior
    if add_invoice_items is not None:
        params["add_invoice_items"] = add_invoice_items
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(subscription_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)


def update_subscription(
    subscription_id: str,
    *,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    items: Optional[List[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    trial_end: Optional[Any] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    pause_collection: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end
    if cancel_at is not None:
        params["cancel_at"] = cancel_at
    if items is not None:
        params["items"] = items
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior
    if payment_behavior is not None:
        params["payment_behavior"] = payment_behavior
    if trial_end is not None:
        params["trial_end"] = trial_end
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if discounts is not None:
        params["discounts"] = discounts
    if pause_collection is not None:
        params["pause_collection"] = pause_collection
    if payment_settings is not None:
        params["payment_settings"] = payment_settings
    if extra_params:
        params.update(extra_params)

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
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if invoice_now is not None:
        params["invoice_now"] = invoice_now
    if prorate is not None:
        params["prorate"] = prorate
    if extra_params:
        params.update(extra_params)

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
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    current_period_end: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer is not None:
        params["customer"] = customer
    if price is not None:
        params["price"] = price
    if status is not None:
        params["status"] = status
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if current_period_end is not None:
        params["current_period_end"] = current_period_end
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
