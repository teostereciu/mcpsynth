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
    tax: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers"""
    params: Dict[str, Any] = {}
    if email is not None:
        params["email"] = email
    if name is not None:
        params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if description is not None:
        params["description"] = description
    if address is not None:
        params["address"] = address
    if shipping is not None:
        params["shipping"] = shipping
    if tax is not None:
        params["tax"] = tax
    if payment_method is not None:
        params["payment_method"] = payment_method
    if metadata is not None:
        params["metadata"] = metadata
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if preferred_locales is not None:
        params["preferred_locales"] = preferred_locales

    data, err = stripe_request(
        "POST",
        "/v1/customers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_customer(
    customer_id: str,
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/customers/{customer}"""
    params: Dict[str, Any] = {}
    if email is not None:
        params["email"] = email
    if name is not None:
        params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if description is not None:
        params["description"] = description
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
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if preferred_locales is not None:
        params["preferred_locales"] = preferred_locales

    data, err = stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_customer(
    customer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer}"""
    data, err = stripe_request(
        "GET",
        f"/v1/customers/{customer_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
