from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def checkout_sessions_create(
    *,
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: list,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    locale: Optional[str] = None,
    expires_at: Optional[int] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items": line_items,
        "customer": customer,
        "customer_email": customer_email,
        "client_reference_id": client_reference_id,
        "metadata": metadata,
        "allow_promotion_codes": allow_promotion_codes,
        "discounts": discounts,
        "subscription_data": subscription_data,
        "invoice_creation": invoice_creation,
        "payment_intent_data": payment_intent_data,
        "automatic_tax": automatic_tax,
        "locale": locale,
        "expires_at": expires_at,
    }
    res, err = stripe_post(
        "/v1/checkout/sessions",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def checkout_sessions_retrieve(*, session_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/checkout/sessions/{session_id}", stripe_account=stripe_account)
    return err or res


def checkout_sessions_list(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/checkout/sessions", params=params, stripe_account=stripe_account)
    return err or res
