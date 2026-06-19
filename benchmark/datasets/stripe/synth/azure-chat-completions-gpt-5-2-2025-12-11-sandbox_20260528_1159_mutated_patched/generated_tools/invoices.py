from typing import Any, Dict, Optional

from .http import stripe_request


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
    issuer: Optional[Dict[str, Any]] = None,
    on_behalf_of: Optional[str] = None,
    preview_mode: Optional[str] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "subscription": subscription,
        "automatic_tax": automatic_tax,
        "currency": currency,
        "customer_details": customer_details,
        "discounts": discounts,
        "invoice_items": invoice_items,
        "issuer": issuer,
        "on_behalf_of": on_behalf_of,
        "preview_mode": preview_mode,
        "schedule": schedule,
        "schedule_details": schedule_details,
        "subscription_details": subscription_details,
    }
    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
