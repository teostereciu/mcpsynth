from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_invoice(
    customer: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "metadata": metadata,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "statement_descriptor": statement_descriptor,
        "footer": footer,
    }
    return stripe_request(
        "POST",
        "/v1/invoices",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
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
        params=params or None,
        stripe_account=stripe_account,
    )


def update_invoice(
    invoice_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    footer: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "description": description,
        "metadata": metadata,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "footer": footer,
    }
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
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"auto_advance": auto_advance}
    return stripe_request(
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
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"payment_method": payment_method, "paid_out_of_band": paid_out_of_band}
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        stripe_account=stripe_account,
    )


def void_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params=None,
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
        params=None,
        stripe_account=stripe_account,
    )


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
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
    currency: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "currency": currency,
        "discounts": discounts,
        "invoice_items": invoice_items,
        "subscription_details": subscription_details,
        "schedule": schedule,
        "schedule_details": schedule_details,
        "automatic_tax": automatic_tax,
    }
    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
    )
