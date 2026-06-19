from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/invoices
# GET /v1/invoices/{invoice}
# POST /v1/invoices/{invoice}
# DELETE /v1/invoices/{invoice}
# GET /v1/invoices
# POST /v1/invoices/{invoice}/finalize
# POST /v1/invoices/{invoice}/pay
# POST /v1/invoices/create_preview


def create_invoice(
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "metadata": metadata,
        "automatic_tax": automatic_tax,
    }
    params.update(kwargs)
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
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_draft_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "DELETE",
        f"/v1/invoices/{invoice_id}",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    return stripe_request("GET", "/v1/invoices", params=params, stripe_account=stripe_account)


def finalize_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"auto_advance": auto_advance}
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
    paid_out_of_band: Optional[bool] = None,
    payment_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"paid_out_of_band": paid_out_of_band, "payment_method": payment_method}
    params.update(kwargs)
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    schedule: Optional[str] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "schedule": schedule,
        "subscription_details": subscription_details,
        "schedule_details": schedule_details,
        "invoice_items": invoice_items,
        "automatic_tax": automatic_tax,
    }
    return stripe_request("POST", "/v1/invoices/create_preview", params=params, stripe_account=stripe_account)
