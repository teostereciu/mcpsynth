from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def subscriptions_create(
    *,
    customer: str,
    items: List[Dict[str, Any]],
    currency: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    add_invoice_items: Optional[List[Dict[str, Any]]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer, "items": items}
    if currency is not None:
        data["currency"] = currency
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if payment_behavior is not None:
        data["payment_behavior"] = payment_behavior
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if trial_end is not None:
        data["trial_end"] = trial_end
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = cancel_at_period_end
    if proration_behavior is not None:
        data["proration_behavior"] = proration_behavior
    if payment_settings is not None:
        data["payment_settings"] = payment_settings
    if invoice_settings is not None:
        data["invoice_settings"] = invoice_settings
    if discounts is not None:
        data["discounts"] = discounts
    if add_invoice_items is not None:
        data["add_invoice_items"] = add_invoice_items
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/subscriptions",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def subscriptions_retrieve(*, subscription_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)


def subscriptions_update(
    *,
    subscription_id: str,
    items: Optional[List[Dict[str, Any]]] = None,
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
    pause_collection: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if items is not None:
        data["items"] = items
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = cancel_at_period_end
    if cancel_at is not None:
        data["cancel_at"] = cancel_at
    if proration_behavior is not None:
        data["proration_behavior"] = proration_behavior
    if payment_behavior is not None:
        data["payment_behavior"] = payment_behavior
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if trial_end is not None:
        data["trial_end"] = trial_end
    if pause_collection is not None:
        data["pause_collection"] = pause_collection
    if payment_settings is not None:
        data["payment_settings"] = payment_settings
    if invoice_settings is not None:
        data["invoice_settings"] = invoice_settings
    if discounts is not None:
        data["discounts"] = discounts
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def subscriptions_cancel(
    *,
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if invoice_now is not None:
        data["invoice_now"] = invoice_now
    if prorate is not None:
        data["prorate"] = prorate
    if extra:
        data.update(extra)

    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def subscriptions_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    price: Optional[str] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    current_period_end: Optional[Dict[str, Any]] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if customer is not None:
        query["customer"] = customer
    if status is not None:
        query["status"] = status
    if price is not None:
        query["price"] = price
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created
    if current_period_end is not None:
        query["current_period_end"] = current_period_end
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/subscriptions", params=query, stripe_account=stripe_account)
