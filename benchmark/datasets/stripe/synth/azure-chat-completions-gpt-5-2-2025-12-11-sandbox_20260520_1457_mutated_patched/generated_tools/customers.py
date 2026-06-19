from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "address": address,
        "shipping": shipping,
        "metadata": metadata,
        "payment_method": payment_method,
        "invoice_settings": invoice_settings,
    }
    _, data = stripe_request(
        "POST",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        stripe_account=stripe_account,
    )
    return data


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "address": address,
        "shipping": shipping,
        "metadata": metadata,
        "default_source": default_source,
        "invoice_settings": invoice_settings,
    }
    _, data = stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "DELETE",
        f"/v1/customers/{customer_id}",
        stripe_account=stripe_account,
    )
    return data


def list_customers(
    *,
    email: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    _, data = stripe_request(
        "GET",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
    )
    return data
