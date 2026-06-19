from typing import Any, Dict, Optional

from .http import stripe_request


def customers_create(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
        "address": address,
        "shipping": shipping,
        "payment_method": payment_method,
        "invoice_settings": invoice_settings,
    }
    res, err = stripe_request(
        "POST",
        "/v1/customers",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or res  # type: ignore[return-value]


def customers_retrieve(*, customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def customers_update(
    *,
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
        "address": address,
        "shipping": shipping,
        "invoice_settings": invoice_settings,
    }
    res, err = stripe_request("POST", f"/v1/customers/{customer_id}", data=data, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def customers_delete(*, customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def customers_list(
    *,
    email: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_request("GET", "/v1/customers", params=params, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]
