from typing import Any, Dict, Optional

from .http import stripe_delete, stripe_get, stripe_post


def customers_create(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
        "invoice_settings": invoice_settings,
        "address": address,
        "shipping": shipping,
    }
    res, err = stripe_post(
        "/v1/customers",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def customers_retrieve(*, customer_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return err or res


def customers_update(
    *,
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
        "default_source": default_source,
        "invoice_settings": invoice_settings,
        "address": address,
        "shipping": shipping,
    }
    res, err = stripe_post(f"/v1/customers/{customer_id}", data=data, stripe_account=stripe_account)
    return err or res


def customers_delete(*, customer_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_delete(f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return err or res


def customers_list(
    *,
    email: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "email": email,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    res, err = stripe_get("/v1/customers", params=params, stripe_account=stripe_account)
    return err or res
