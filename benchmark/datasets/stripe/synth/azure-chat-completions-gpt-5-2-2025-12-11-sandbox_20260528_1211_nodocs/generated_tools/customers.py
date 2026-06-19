from typing import Any, Dict, Optional

from .http import stripe_request


def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if phone is not None:
        data["phone"] = phone
    if description is not None:
        data["description"] = description
    if payment_method is not None:
        data["payment_method"] = payment_method
    if invoice_settings is not None:
        data["invoice_settings"] = invoice_settings
    if address is not None:
        data["address"] = address
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request(
        "POST",
        "/v1/customers",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_customer(customer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if phone is not None:
        data["phone"] = phone
    if description is not None:
        data["description"] = description
    if invoice_settings is not None:
        data["invoice_settings"] = invoice_settings
    if address is not None:
        data["address"] = address
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/customers/{customer_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def delete_customer(customer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/customers/{customer_id}", stripe_account=stripe_account)
    return res if err is None else err


def list_customers(
    *,
    email: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if email is not None:
        query["email"] = email
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created

    res, err = stripe_request("GET", "/v1/customers", query=query, stripe_account=stripe_account)
    return res if err is None else err


def search_customers(
    query: str,
    *,
    limit: Optional[int] = None,
    page: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {"query": query}
    if limit is not None:
        q["limit"] = limit
    if page is not None:
        q["page"] = page

    res, err = stripe_request("GET", "/v1/customers/search", query=q, stripe_account=stripe_account)
    return res if err is None else err
