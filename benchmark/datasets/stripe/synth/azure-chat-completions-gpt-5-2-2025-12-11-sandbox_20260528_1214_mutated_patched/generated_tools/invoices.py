from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/invoices.md

def create_invoice(
    customer: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "description": description,
        "metadata": metadata,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "payment_settings": payment_settings,
        "statement_descriptor": statement_descriptor,
        "footer": footer,
    }
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
    return stripe_request(
        "GET",
        f"/v1/invoices/{invoice_id}",
        params={"expand": expand},
        stripe_account=stripe_account,
    )


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "description": description,
        "metadata": metadata,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "payment_settings": payment_settings,
        "statement_descriptor": statement_descriptor,
        "footer": footer,
    }
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
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params={"auto_advance": auto_advance},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def pay_invoice(
    invoice_id: str,
    *,
    paid_out_of_band: Optional[bool] = None,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "paid_out_of_band": paid_out_of_band,
        "payment_method": payment_method,
        "source": source,
    }
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
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    customer_details: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "customer_details": customer_details,
        "subscription_details": subscription_details,
        "schedule": schedule,
        "schedule_details": schedule_details,
        "currency": currency,
        "discounts": discounts,
        "invoice_items": invoice_items,
        "automatic_tax": automatic_tax,
    }
    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
    )


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    collection_method: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    due_date: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "collection_method": collection_method,
        "created": created,
        "due_date": due_date,
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
