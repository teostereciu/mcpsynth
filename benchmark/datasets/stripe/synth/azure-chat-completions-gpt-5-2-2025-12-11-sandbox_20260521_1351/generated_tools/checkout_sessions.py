from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_checkout_session(
    mode: str,
    *,
    line_items: Optional[list[Dict[str, Any]]] = None,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    ui_mode: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    customer_update: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_collection: Optional[str] = None,
    locale: Optional[str] = None,
    expires_at: Optional[int] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    billing_address_collection: Optional[str] = None,
    submit_type: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"mode": mode}
    if line_items is not None:
        params["line_items"] = line_items
    if success_url is not None:
        params["success_url"] = success_url
    if cancel_url is not None:
        params["cancel_url"] = cancel_url
    if return_url is not None:
        params["return_url"] = return_url
    if ui_mode is not None:
        params["ui_mode"] = ui_mode
    if customer is not None:
        params["customer"] = customer
    if customer_email is not None:
        params["customer_email"] = customer_email
    if client_reference_id is not None:
        params["client_reference_id"] = client_reference_id
    if metadata is not None:
        params["metadata"] = metadata
    if allow_promotion_codes is not None:
        params["allow_promotion_codes"] = allow_promotion_codes
    if discounts is not None:
        params["discounts"] = discounts
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if customer_creation is not None:
        params["customer_creation"] = customer_creation
    if customer_update is not None:
        params["customer_update"] = customer_update
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if payment_method_collection is not None:
        params["payment_method_collection"] = payment_method_collection
    if locale is not None:
        params["locale"] = locale
    if expires_at is not None:
        params["expires_at"] = expires_at
    if shipping_address_collection is not None:
        params["shipping_address_collection"] = shipping_address_collection
    if shipping_options is not None:
        params["shipping_options"] = shipping_options
    if billing_address_collection is not None:
        params["billing_address_collection"] = billing_address_collection
    if submit_type is not None:
        params["submit_type"] = submit_type

    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(
    session_id: str,
    *,
    expand: Optional[list[str]] = None,
    account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}", params=params, account=account)


def expire_checkout_session(
    session_id: str,
    *,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        params={},
        account=account,
        idempotency_key=idempotency_key,
    )


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if subscription is not None:
        params["subscription"] = subscription
    if created is not None:
        params["created"] = created
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/checkout/sessions", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/checkout/sessions", params=params, account=account)
