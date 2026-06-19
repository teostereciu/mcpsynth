from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_invoice_preview(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "automatic_tax": automatic_tax,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params,
        stripe_account=stripe_account,
    )


def create_invoice(
    customer: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    days_until_due: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "description": description,
        "metadata": metadata,
        "days_until_due": days_until_due,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/invoices",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "description": description,
        "metadata": metadata,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/invoices/{invoice_id}",
        None,
        stripe_account=stripe_account,
    )
