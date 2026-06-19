from typing import Any, Dict, List, Optional

from .http_client import stripe_request_with_retries


def create_checkout_session(
    mode: str,
    *,
    line_items: Optional[List[Dict[str, Any]]] = None,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    ui_mode: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
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
        params["allow_promotion_codes"] = str(allow_promotion_codes).lower()
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
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types

    return stripe_request_with_retries(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(session_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        stripe_account=stripe_account,
    )


def update_checkout_session(
    session_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request_with_retries(
        "POST",
        f"/v1/checkout/sessions/{session_id}",
        params=params,
        stripe_account=stripe_account,
    )


def expire_checkout_session(session_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        stripe_account=stripe_account,
    )


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if subscription is not None:
        params["subscription"] = subscription
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
    )
