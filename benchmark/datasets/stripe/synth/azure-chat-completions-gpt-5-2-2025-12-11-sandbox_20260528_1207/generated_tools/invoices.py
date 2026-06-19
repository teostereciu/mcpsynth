from typing import Any, Dict, Optional, List

from .http_client import stripe_request


def create_invoice(
    *,
    customer: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if discounts is not None:
        params["discounts"] = discounts
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)


def update_invoice(
    invoice_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if discounts is not None:
        params["discounts"] = discounts
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def finalize_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if extra_params:
        params.update(extra_params)

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
    paid_out_of_band: Optional[bool] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if paid_out_of_band is not None:
        params["paid_out_of_band"] = paid_out_of_band
    if extra_params:
        params.update(extra_params)

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
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer is not None:
        params["customer"] = customer
    if subscription is not None:
        params["subscription"] = subscription
    if status is not None:
        params["status"] = status
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/invoices", params=params, stripe_account=stripe_account)


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    customer_account: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[List[Dict[str, Any]]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    currency: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if subscription is not None:
        params["subscription"] = subscription
    if customer_account is not None:
        params["customer_account"] = customer_account
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
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
    if extra_params:
        params.update(extra_params)

    return stripe_request("POST", "/v1/invoices/create_preview", params=params, stripe_account=stripe_account)
