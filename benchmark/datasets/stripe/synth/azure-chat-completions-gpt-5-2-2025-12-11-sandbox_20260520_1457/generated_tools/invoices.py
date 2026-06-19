from typing import Any, Dict, Optional, List

from .http_client import ok_or_error, stripe_request


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    customer_account: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[List[Dict[str, Any]]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    preview_mode: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "customer_account": customer_account,
        "automatic_tax": automatic_tax,
        "currency": currency,
        "subscription_details": subscription_details,
        "schedule": schedule,
        "schedule_details": schedule_details,
        "invoice_items": invoice_items,
        "discounts": discounts,
        "preview_mode": preview_mode,
    }
    status, payload = stripe_request("POST", "/v1/invoices/create_preview", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)


def create_invoice(
    *,
    customer: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    on_behalf_of: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
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
    }
    status, payload = stripe_request(
        "POST", "/v1/invoices", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_invoice(*, invoice_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_invoice(
    *,
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "description": description,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
        "footer": footer,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
    }
    status, payload = stripe_request(
        "POST", f"/v1/invoices/{invoice_id}", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def finalize_invoice(
    *,
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"auto_advance": auto_advance}
    status, payload = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def pay_invoice(
    *,
    invoice_id: str,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"payment_method": payment_method, "source": source, "paid_out_of_band": paid_out_of_band}
    status, payload = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def void_invoice(
    *,
    invoice_id: str,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    status, payload = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params={},
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status_code, payload = stripe_request("GET", "/v1/invoices", params=params, stripe_account=stripe_account)
    return ok_or_error(status_code, payload)
