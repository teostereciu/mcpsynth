from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_subscription(
    customer: str,
    items: list,
    *,
    currency: Optional[str] = None,
    customer_account: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    discounts: Optional[list] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    off_session: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    trial_settings: Optional[Dict[str, Any]] = None,
    cancel_at: Optional[Any] = None,
    cancel_at_period_end: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions"""
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
    }
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
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if default_source is not None:
        params["default_source"] = default_source
    if default_tax_rates is not None:
        params["default_tax_rates"] = default_tax_rates
    if discounts is not None:
        params["discounts"] = discounts
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if off_session is not None:
        params["off_session"] = off_session
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior
    if trial_end is not None:
        params["trial_end"] = trial_end
    if trial_period_days is not None:
        params["trial_period_days"] = trial_period_days
    if trial_settings is not None:
        params["trial_settings"] = trial_settings
    if cancel_at is not None:
        params["cancel_at"] = cancel_at
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end

    data, err = stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[list] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at: Optional[Any] = None,
    cancel_at_period_end: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    discounts: Optional[list] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    off_session: Optional[bool] = None,
    payment_behavior: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    trial_end: Optional[Any] = None,
    trial_settings: Optional[Dict[str, Any]] = None,
    pause_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions/{id}"""
    params: Dict[str, Any] = {}
    if items is not None:
        params["items"] = items
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if cancel_at is not None:
        params["cancel_at"] = cancel_at
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if default_source is not None:
        params["default_source"] = default_source
    if default_tax_rates is not None:
        params["default_tax_rates"] = default_tax_rates
    if discounts is not None:
        params[[... ELLIPSIZATION ...]"invoice_settings"] = invoice_settings
    if off_session is not None:
        params["off_session"] = off_session
    if payment_behavior is not None:
        params["payment_behavior"] = payment_behavior
    if payment_settings is not None:
        params["payment_settings"] = payment_settings
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior
    if trial_end is not None:
        params["trial_end"] = trial_end
    if trial_settings is not None:
        params["trial_settings"] = trial_settings
    if pause_collection is not None:
        params["pause_collection"] = pause_collection

    data, err = stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_subscription(
    subscription_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions/{id}"""
    data, err = stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
