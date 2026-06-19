from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def invoices_create(
    *,
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if discounts is not None:
        data["discounts"] = discounts
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if footer is not None:
        data["footer"] = footer
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/invoices",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_retrieve(*, invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)


def invoices_update(
    *,
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if discounts is not None:
        data["discounts"] = discounts
    if default_payment_method is not None:
        data["default_payment_method"] = default_payment_method
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if footer is not None:
        data["footer"] = footer
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_finalize(
    *,
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_pay(
    *,
    invoice_id: str,
    payment_method: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if paid_out_of_band is not None:
        data["paid_out_of_band"] = paid_out_of_band
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_void(
    *,
    invoice_id: str,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data = extra or {}
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if customer is not None:
        query["customer"] = customer
    if subscription is not None:
        query["subscription"] = subscription
    if status is not None:
        query["status"] = status
    if created is not None:
        query["created"] = created
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/invoices", params=query, stripe_account=stripe_account)


def invoices_create_preview(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    schedule: Optional[str] = None,
    customer_details: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[List[Dict[str, Any]]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    preview_mode: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if subscription is not None:
        data["subscription"] = subscription
    if schedule is not None:
        data["schedule"] = schedule
    if customer_details is not None:
        data["customer_details"] = customer_details
    if subscription_details is not None:
        data["subscription_details"] = subscription_details
    if schedule_details is not None:
        data["schedule_details"] = schedule_details
    if invoice_items is not None:
        data["invoice_items"] = invoice_items
    if discounts is not None:
        data["discounts"] = discounts
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if currency is not None:
        data["currency"] = currency
    if preview_mode is not None:
        data["preview_mode"] = preview_mode
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        data=data,
        stripe_account=stripe_account,
    )
