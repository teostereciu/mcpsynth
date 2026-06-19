from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_invoice(
    customer: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    subscription: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
        "subscription": subscription,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
    }
    _, data = stripe_request(
        "POST",
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/invoices/{invoice_id}",
        stripe_account=stripe_account,
    )
    return data


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
        "discounts": discounts,
    }
    _, data = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def finalize_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"auto_advance": auto_advance}
    _, data = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def pay_invoice(
    invoice_id: str,
    *,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"payment_method": payment_method, "source": source}
    _, data = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def void_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def list_invoices(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
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
    _, data = stripe_request(
        "GET",
        "/v1/invoices",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def create_preview_invoice(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "subscription_details": subscription_details,
        "invoice_items": invoice_items,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
    }
    _, data = stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params=params,
        stripe_account=stripe_account,
    )
    return data
