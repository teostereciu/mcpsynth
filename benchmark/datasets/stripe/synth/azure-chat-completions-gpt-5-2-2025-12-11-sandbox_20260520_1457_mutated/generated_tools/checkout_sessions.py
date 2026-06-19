from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_checkout_session(
    mode: str,
    *,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    ui_mode: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "return_url": return_url,
        "customer": customer,
        "customer_email": customer_email,
        "client_reference_id": client_reference_id,
        "line_items": line_items,
        "metadata": metadata,
        "allow_promotion_codes": allow_promotion_codes,
        "discounts": discounts,
        "subscription_data": subscription_data,
        "payment_intent_data": payment_intent_data,
        "invoice_creation": invoice_creation,
        "automatic_tax": automatic_tax,
        "ui_mode": ui_mode,
    }
    _, data = stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_checkout_session(
    session_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"expand": expand} if expand else None
    _, data = stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def expire_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


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
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    _, data = stripe_request(
        "GET",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
    )
    return data
