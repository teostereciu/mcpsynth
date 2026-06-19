from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_invoice(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    on_behalf_of: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices

    Doc: docs/invoices.md (Create an invoice)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "description": description,
        "metadata": metadata,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "on_behalf_of": on_behalf_of,
        "transfer_data": transfer_data,
        "statement_descriptor": statement_descriptor,
        "footer": footer,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/invoices",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(
    invoice_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices/{invoice_id}

    Doc: docs/invoices.md (Retrieve an invoice)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/invoices/{invoice_id}",
        params,
        stripe_account=stripe_account,
    )


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    footer: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice_id}

    Doc: docs/invoices.md (Update an invoice)
    """
    params: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "description": description,
        "metadata": metadata,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "footer": footer,
        "statement_descriptor": statement_descriptor,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params,
        stripe_account=stripe_account,
    )


def finalize_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice_id}/finalize

    Doc: docs/invoices.md (Finalize an invoice)
    """
    params: Dict[str, Any] = {"auto_advance": auto_advance, "expand": expand}
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params,
        stripe_account=stripe_account,
    )


def pay_invoice(
    invoice_id: str,
    *,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice_id}/pay

    Doc: docs/invoices.md (Pay an invoice)
    """
    params: Dict[str, Any] = {
        "payment_method": payment_method,
        "source": source,
        "paid_out_of_band": paid_out_of_band,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def void_invoice(
    invoice_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice_id}/void

    Doc: docs/invoices.md (Void an invoice)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params,
        stripe_account=stripe_account,
    )


def delete_draft_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/invoices/{invoice_id}

    Doc: docs/invoices.md (Delete a draft invoice)
    """
    return stripe_request(
        "DELETE",
        f"/v1/invoices/{invoice_id}",
        None,
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
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices

    Doc: docs/invoices.md (List all invoices)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "collection_method": collection_method,
        "created": created,
        "due_date": due_date,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/invoices",
        params,
        stripe_account=stripe_account,
    )


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    subscription: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    customer_details: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    on_behalf_of: Optional[str] = None,
    preview_mode: Optional[str] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/create_preview

    Doc: docs/invoices.md (Create a preview invoice)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "subscription": subscription,
        "automatic_tax": automatic_tax,
        "currency": currency,
        "customer_details": customer_details,
        "discounts": discounts,
        "invoice_items": invoice_items,
        "on_behalf_of": on_behalf_of,
        "preview_mode": preview_mode,
        "schedule": schedule,
        "schedule_details": schedule_details,
        "subscription_details": subscription_details,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params,
        stripe_account=stripe_account,
    )
