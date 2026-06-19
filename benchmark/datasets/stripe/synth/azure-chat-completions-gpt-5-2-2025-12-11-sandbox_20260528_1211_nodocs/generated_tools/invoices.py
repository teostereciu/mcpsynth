from typing import Any, Dict, Optional

from .http import stripe_request


def create_invoice(
    customer: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    subscription: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if subscription is not None:
        data["subscription"] = subscription

    res, err = stripe_request(
        "POST",
        "/v1/invoices",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_invoice(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_invoice(
    invoice_id: str,
    *,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if collection_method is not None:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def finalize_invoice(invoice_id: str, *, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        data={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def pay_invoice(
    invoice_id: str,
    *,
    payment_method: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if paid_out_of_band is not None:
        data["paid_out_of_band"] = paid_out_of_band

    res, err = stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def void_invoice(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/void", data={}, stripe_account=stripe_account)
    return res if err is None else err


def mark_invoice_uncollectible(invoice_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request(
        "POST", f"/v1/invoices/{invoice_id}/mark_uncollectible", data={}, stripe_account=stripe_account
    )
    return res if err is None else err


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
    query: Dict[str, Any] = {}
    if customer is not None:
        query["customer"] = customer
    if subscription is not None:
        query["subscription"] = subscription
    if status is not None:
        query["status"] = status
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/invoices", query=query, stripe_account=stripe_account)
    return res if err is None else err
