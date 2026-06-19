from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_customer(
    *,
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "email": email,
        "phone": phone,
        "description": description,
        "address": address,
        "shipping": shipping,
        "metadata": metadata,
        "payment_method": payment_method,
    }
    return stripe_request(
        "POST",
        "/v1/customers",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_customer(
    customer_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        params=params or None,
        stripe_account=stripe_account,
    )


def update_customer(
    customer_id: str,
    *,
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "email": email,
        "phone": phone,
        "description": description,
        "address": address,
        "shipping": shipping,
        "metadata": metadata,
    }
    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        stripe_account=stripe_account,
    )


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "DELETE",
        f"/v1/customers/{customer_id}",
        params=None,
        stripe_account=stripe_account,
    )


def list_customers(
    *,
    email: Optional[str] = None,
    limit: Optional[int] = 10,
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
    return stripe_request(
        "GET",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
    )
