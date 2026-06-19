from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/customers
# GET /v1/customers/{customer}
# POST /v1/customers/{customer}
# DELETE /v1/customers/{customer}
# GET /v1/customers


def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    payment_method: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "description": description,
        "phone": phone,
        "payment_method": payment_method,
        "address": address,
        "shipping": shipping,
        "tax": tax,
        "metadata": metadata,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_customer(customer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/customers/{customer_id}", stripe_account=stripe_account)


def update_customer(
    customer_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "DELETE",
        f"/v1/customers/{customer_id}",
        params=None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


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
    return stripe_request("GET", "/v1/customers", params=params, stripe_account=stripe_account)
