from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    subscription: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    customer_details: Optional[Dict[str, Any]] = None,
    discounts: Optional[list] = None,
    invoice_items: Optional[list] = None,
    preview_mode: Optional[str] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/create_preview"""
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if subscription is not None:
        params["subscription"] = subscription
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if currency is not None:
        params["currency"] = currency
    if customer_details is not None:
        params["customer_details"] = customer_details
    if discounts is not None:
        params["discounts"] = discounts
    if invoice_items is not None:
        params["invoice_items"] = invoice_items
    if preview_mode is not None:
        params["preview_mode"] = preview_mode
    if schedule is not None:
        params["schedule"] = schedule
    if schedule_details is not None:
        params["schedule_details"] = schedule_details
    if subscription_details is not None:
        params["subscription_details"] = subscription_details

    data, err = stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
    )
    return data if err is None else err


def create_invoice(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    subscription: Optional[str] = None,
    discounts: Optional[list] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices"""
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if subscription is not None:
        params["subscription"] = subscription
    if discounts is not None:
        params["discounts"] = discounts
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if default_source is not None:
        params["default_source"] = default_source
    if payment_settings is not None:
        params["payment_settings"] = payment_settings

    data, err = stripe_request(
        "POST",
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    discounts: Optional[list] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{id}"""
    params: Dict[str, Any] = {}
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if discounts is not None:
        params["discounts"] = discounts
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if default_source is not None:
        params["default_source"] = default_source
    if payment_settings is not None:
        params["payment_settings"] = payment_settings

    data, err = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err
