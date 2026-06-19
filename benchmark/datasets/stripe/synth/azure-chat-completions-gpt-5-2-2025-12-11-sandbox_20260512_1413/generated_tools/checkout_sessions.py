from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def checkout_sessions_create(
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
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "mode": mode,
        "line_items": line_items,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "return_url": return_url,
        "ui_mode": ui_mode,
        "customer": customer,
        "customer_email": customer_email,
        "client_reference_id": client_reference_id,
        "metadata": metadata,
        "allow_promotion_codes": allow_promotion_codes,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "currency": currency,
        "payment_intent_data": payment_intent_data,
        "subscription_data": subscription_data,
        "invoice_creation": invoice_creation,
    }
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def checkout_sessions_retrieve(session_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}", None, stripe_account=stripe_account)


def checkout_sessions_expire(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def checkout_sessions_list(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/checkout/sessions", params, stripe_account=stripe_account)


def checkout_sessions_list_all(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "created": created,
    }
    return stripe_list_all("/v1/checkout/sessions", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
