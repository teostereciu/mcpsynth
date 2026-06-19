from typing import Any, Dict, Optional

from .stripe_client import stripe_request


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
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if email is not None:
        params["email"] = email
    if name is not None:
        params["name"] = name
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

    return stripe_request("POST", "/v1/customers", params=params)


def retrieve_customer(
    customer_id: str,
    *,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/customers/{customer_id}", params=params)


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if email is not None:
        params["email"] = email
    if name is not None:
        params["name"] = name
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

    return stripe_request("POST", f"/v1/customers/{customer_id}", params=params)


def delete_customer(customer_id: str) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}")


def list_customers(
    *,
    email: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
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

    return stripe_request("GET", "/v1/customers", params=params)
