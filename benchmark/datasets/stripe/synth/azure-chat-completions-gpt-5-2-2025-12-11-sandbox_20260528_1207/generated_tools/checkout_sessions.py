from typing import Any, Dict, Optional, List

from .http_client import stripe_request


def create_checkout_session(
    *,
    mode: str,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    ui_mode: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"mode": mode}
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
    if line_items is not None:
        params["line_items"] = line_items
    if metadata is not None:
        params["metadata"] = metadata
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if discounts is not None:
        params["discounts"] = discounts
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if allow_promotion_codes is not None:
        params["allow_promotion_codes"] = allow_promotion_codes
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(session_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}", stripe_account=stripe_account)


def update_checkout_session(
    session_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer is not None:
        params["customer"] = customer
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if subscription is not None:
        params["subscription"] = subscription
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/checkout/sessions", params=params, stripe_account=stripe_account)


def expire_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        params={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
