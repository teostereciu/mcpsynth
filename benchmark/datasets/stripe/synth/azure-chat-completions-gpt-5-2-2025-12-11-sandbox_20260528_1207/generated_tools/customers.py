from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if email is not None:
        params["email"] = email
    if description is not None:
        params["description"] = description
    if phone is not None:
        params["phone"] = phone
    if payment_method is not None:
        params["payment_method"] = payment_method
    if address is not None:
        params["address"] = address
    if shipping is not None:
        params["shipping"] = shipping
    if tax is not None:
        params["tax"] = tax
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_customer(
    customer_id: str,
    *,
    name: Optional[str] = None,
    email: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if email is not None:
        params["email"] = email
    if description is not None:
        params["description"] = description
    if phone is not None:
        params["phone"] = phone
    if address is not None:
        params["address"] = address
    if shipping is not None:
        params["shipping"] = shipping
    if tax is not None:
        params["tax"] = tax
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        stripe_account=stripe_account,
    )


def list_customers(
    *,
    email: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if email is not None:
        params["email"] = email
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "GET",
        "/v1/customers",
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
        stripe_account=stripe_account,
    )
