from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_checkout_session(
    mode: str,
    *,
    line_items: Optional[list] = None,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    ui_mode: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[list] = None,
    allow_promotion_codes: Optional[bool] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions"""
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
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if discounts is not None:
        params["discounts"] = discounts
    if allow_promotion_codes is not None:
        params["allow_promotion_codes"] = allow_promotion_codes
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if shipping_address_collection is not None:
        params["shipping_address_collection"] = shipping_address_collection
    if shipping_options is not None:
        params["shipping_options"] = shipping_options

    data, err = stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions/{id}"""
    data, err = stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
