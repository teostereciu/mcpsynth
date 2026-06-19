from typing import Any, Dict, List, Optional

from .http_client import stripe_request_with_retries


def create_invoice(
    customer: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer}
    if auto_advance is not None:
        params["auto_advance"] = str(auto_advance).lower()
    if collection_method is not None:
        params["collection_method"] = collection_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax

    return stripe_request_with_retries(
        "POST",
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/invoices/{invoice_id}",
        stripe_account=stripe_account,
    )


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if auto_advance is not None:
        params["auto_advance"] = str(auto_advance).lower()
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request_with_retries(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params=params,
        stripe_account=stripe_account,
    )


def finalize_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if auto_advance is not None:
        params["auto_advance"] = str(auto_advance).lower()

    return stripe_request_with_retries(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params=params,
        stripe_account=stripe_account,
    )


def pay_invoice(
    invoice_id: str,
    *,
    payment_method: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if paid_out_of_band is not None:
        params["paid_out_of_band"] = str(paid_out_of_band).lower()

    return stripe_request_with_retries(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def void_invoice(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        stripe_account=stripe_account,
    )


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if subscription is not None:
        params["subscription"] = subscription
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
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
    )


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    customer_account: Optional[str] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[List[Dict[str, Any]]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    currency: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if subscription is not None:
        params["subscription"] = subscription
    if subscription_details is not None:
        params["subscription_details"] = subscription_details
    if schedule is not None:
        params["schedule"] = schedule
    if schedule_details is not None:
        params["schedule_details"] = schedule_details
    if invoice_items is not None:
        params["invoice_items"] = invoice_items
    if discounts is not None:
        params["discounts"] = discounts
    if currency is not None:
        params["currency"] = currency
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax

    return stripe_request_with_retries(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
    )
