from typing import Any, Dict, List, Optional

from .http_client import stripe_request_with_retries


def create_subscription(
    customer: str,
    items: List[Dict[str, Any]],
    *,
    currency: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
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
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    if trial_end is not None:
        params["trial_end"] = trial_end
    if trial_period_days is not None:
        params["trial_period_days"] = trial_period_days
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax

    return stripe_request_with_retries(
        "POST",
        "/v1/subscriptions",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_subscription(subscription_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        stripe_account=stripe_account,
    )


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[List[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
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
        params["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    if proration_behavior is not None:
        params["proration_behavior"] = proration_behavior

    return stripe_request_with_retries(
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
        params["invoice_now"] = str(invoice_now).lower()
    if prorate is not None:
        params["prorate"] = str(prorate).lower()

    return stripe_request_with_retries(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if status is not None:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
    )
