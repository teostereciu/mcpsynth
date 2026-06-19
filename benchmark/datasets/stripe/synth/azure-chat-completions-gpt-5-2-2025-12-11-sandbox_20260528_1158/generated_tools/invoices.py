from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_invoice(
    customer: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer}
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
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if default_source is not None:
        params["default_source"] = default_source
    if discounts is not None:
        params["discounts"] = discounts
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if footer is not None:
        params["footer"] = footer

    return stripe_request(
        "POST",
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(
    invoice_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/invoices/{invoice_id}",
        params=params,
        stripe_account=stripe_account,
    )


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
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
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if default_source is not None:
        params["default_source"] = default_source
    if discounts is not None:
        params["discounts"] = discounts
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if footer is not None:
        params["footer"] = footer

    return stripe_request(
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
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def pay_invoice(
    invoice_id: str,
    *,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if source is not None:
        params["source"] = source
    if paid_out_of_band is not None:
        params["paid_out_of_band"] = paid_out_of_band
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def void_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params={},
        stripe_account=stripe_account,
    )


def delete_draft_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "DELETE",
        f"/v1/invoices/{invoice_id}",
        stripe_account=stripe_account,
    )


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
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
    if subscription is not None:
        params["subscription"] = subscription
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
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
    )


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    schedule: Optional[str] = None,
    customer_details: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if subscription is not None:
        params["subscription"] = subscription
    if schedule is not None:
        params["schedule"] = schedule
    if customer_details is not None:
        params["customer_details"] = customer_details
    if subscription_details is not None:
        params["subscription_details"] = subscription_details
    if schedule_details is not None:
        params["schedule_details"] = schedule_details
    if invoice_items is not None:
        params["invoice_items"] = invoice_items
    if discounts is not None:
        params["discounts"] = discounts
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if currency is not None:
        params["currency"] = currency

    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
    )
