from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


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
    metadata: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
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

    return stripe_request_with_retries(
        "POST",
        "/v1/customers",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/customers/{customer_id}",
        stripe_account=stripe_account,
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
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    stripe_account: Optional[str] = None,
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
    if default_source is not None:
        params["default_source"] = default_source

    return stripe_request_with_retries(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        stripe_account=stripe_account,
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
    params: Dict[str, Any] = {}
    if email is not None:
        params["email"] = email
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if created is not None:
        params["created"] = created

    return stripe_request_with_retries(
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
    return stripe_request_with_retries(
        "DELETE",
        f"/v1/customers/{customer_id}",
        stripe_account=stripe_account,
    )
