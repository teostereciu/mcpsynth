from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


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
    metadata: Optional[Dict[str, str]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list[str]] = None,
    source: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
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
    if source is not None:
        params["source"] = source

    return stripe_request("POST", "/v1/customers", params=params, account=account, idempotency_key=idempotency_key)


def retrieve_customer(customer_id: str, *, expand: Optional[list[str]] = None, account: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/customers/{customer_id}", params=params, account=account)


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
    metadata: Optional[Dict[str, str]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    preferred_locales: Optional[list[str]] = None,
    default_source: Optional[str] = None,
    source: Optional[str] = None,
    tax_exempt: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
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
    if invoice_settings is not None:
        params["invoice_settings"] = invoice_settings
    if preferred_locales is not None:
        params["preferred_locales"] = preferred_locales
    if default_source is not None:
        params["default_source"] = default_source
    if source is not None:
        params["source"] = source
    if tax_exempt is not None:
        params["tax_exempt"] = tax_exempt

    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def delete_customer(customer_id: str, *, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}", params={}, account=account)


def list_customers(
    *,
    email: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if email is not None:
        params["email"] = email
    if created is not None:
        params["created"] = created
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/customers", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/customers", params=params, account=account)
