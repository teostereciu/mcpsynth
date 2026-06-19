from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def invoices_create(
    *,
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    subscription: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
        "subscription": subscription,
        "default_payment_method": default_payment_method,
    }
    res, err = stripe_post(
        "/v1/invoices",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def invoices_retrieve(*, invoice_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)
    return err or res


def invoices_update(
    *,
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_payment_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
        "default_payment_method": default_payment_method,
    }
    res, err = stripe_post(f"/v1/invoices/{invoice_id}", data=data, stripe_account=stripe_account)
    return err or res


def invoices_finalize(*, invoice_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None):
    res, err = stripe_post(
        f"/v1/invoices/{invoice_id}/finalize",
        data={},
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def invoices_pay(
    *,
    invoice_id: str,
    payment_method: Optional[str] = None,
    paid_out_of_band: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {"payment_method": payment_method, "paid_out_of_band": paid_out_of_band}
    res, err = stripe_post(
        f"/v1/invoices/{invoice_id}/pay",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def invoices_void(*, invoice_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None):
    res, err = stripe_post(
        f"/v1/invoices/{invoice_id}/void",
        data={},
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def invoices_list(
    *,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "customer": customer,
        "subscription": subscription,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    res, err = stripe_get("/v1/invoices", params=params, stripe_account=stripe_account)
    return err or res
