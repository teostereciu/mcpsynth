from typing import Any, Dict, Optional

from .http import stripe_request


def invoices_create(
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    discounts: Optional[list] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    on_behalf_of: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "default_tax_rates": default_tax_rates,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "on_behalf_of": on_behalf_of,
        "transfer_data": transfer_data,
        "application_fee_amount": application_fee_amount,
    }
    data, err = stripe_request(
        "POST",
        "/v1/invoices",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def invoices_retrieve(invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def invoices_update(
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    discounts: Optional[list] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "default_tax_rates": default_tax_rates,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def invoices_finalize(invoice_id: str, auto_advance: Optional[bool] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    params = {"auto_advance": auto_advance}
    data, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def invoices_pay(
    invoice_id: str,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"payment_method": payment_method, "source": source, "paid_out_of_band": paid_out_of_band}
    data, err = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data or err  # type: ignore[return-value]


def invoices_void(invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/void", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def invoices_mark_uncollectible(invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/mark_uncollectible", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def invoices_list(
    limit: int = 10,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/invoices", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
