from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def invoices_create(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
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
    }
    return stripe_request("POST", "/v1/invoices", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def invoices_retrieve(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoices/{invoice_id}", None, stripe_account=stripe_account)


def invoices_update(
    invoice_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[list] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "description": description,
        "metadata": metadata,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
    }
    return stripe_request("POST", f"/v1/invoices/{invoice_id}", params, stripe_account=stripe_account)


def invoices_finalize(invoice_id: str, *, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_pay(
    invoice_id: str,
    *,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"payment_method": payment_method, "source": source, "paid_out_of_band": paid_out_of_band}
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_void(invoice_id: str, *, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoices_list(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/invoices", params, stripe_account=stripe_account)


def invoices_list_all(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "subscription": subscription, "status": status, "created": created}
    return stripe_list_all("/v1/invoices", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)


def invoices_create_preview(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    subscription: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    discounts: Optional[list] = None,
    invoice_items: Optional[list] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "subscription": subscription,
        "automatic_tax": automatic_tax,
        "currency": currency,
        "discounts": discounts,
        "invoice_items": invoice_items,
        "subscription_details": subscription_details,
        "schedule": schedule,
        "schedule_details": schedule_details,
    }
    return stripe_request("POST", "/v1/invoices/create_preview", params, stripe_account=stripe_account)
