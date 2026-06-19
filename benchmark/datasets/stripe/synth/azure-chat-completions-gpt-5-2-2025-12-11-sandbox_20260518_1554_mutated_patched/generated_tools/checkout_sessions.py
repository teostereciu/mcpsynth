from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_checkout_session(
    mode: str,
    *,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    ui_mode: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    currency: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_collection: Optional[str] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    expires_at: Optional[int] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "return_url": return_url,
        "ui_mode": ui_mode,
        "customer": customer,
        "customer_email": customer_email,
        "client_reference_id": client_reference_id,
        "line_items": line_items,
        "currency": currency,
        "metadata": metadata,
        "allow_promotion_codes": allow_promotion_codes,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "invoice_creation": invoice_creation,
        "payment_intent_data": payment_intent_data,
        "subscription_data": subscription_data,
        "payment_method_types": payment_method_types,
        "payment_method_collection": payment_method_collection,
        "shipping_address_collection": shipping_address_collection,
        "shipping_options": shipping_options,
        "expires_at": expires_at,
    }
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_checkout_session(
    session_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        params=params or None,
        stripe_account=stripe_account,
    )


def expire_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        params=None,
        stripe_account=stripe_account,
    )


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
    )
