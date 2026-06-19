from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


def create_customer(
    *,
    name: Optional[str] = None,
    email: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    payment_method: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "name": name,
        "email": email,
        "description": description,
        "phone": phone,
        "payment_method": payment_method,
        "address": address,
        "shipping": shipping,
        "tax": tax,
        "metadata": metadata,
    }
    status, payload = stripe_request(
        "POST", "/v1/customers", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_customer(
    *,
    customer_id: str,
    name: Optional[str] = None,
    email: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    default_source: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "name": name,
        "email": email,
        "description": description,
        "phone": phone,
        "address": address,
        "shipping": shipping,
        "tax": tax,
        "metadata": metadata,
        "default_source": default_source,
        "invoice_settings": invoice_settings,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def retrieve_customer(*, customer_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_customers(
    *,
    email: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "email": email,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/customers", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
