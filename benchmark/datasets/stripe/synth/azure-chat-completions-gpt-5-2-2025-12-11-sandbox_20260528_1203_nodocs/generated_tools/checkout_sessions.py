from typing import Any, Dict, Optional

from .http import stripe_request


def checkout_sessions_create(
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
    automatic_tax: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    expires_at: Optional[int] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    consent_collection: Optional[Dict[str, Any]] = None,
    locale: Optional[str] = None,
    ui_mode: Optional[str] = None,
    return_url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
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
        "automatic_tax": automatic_tax,
        "tax_id_collection": tax_id_collection,
        "billing_address_collection": billing_address_collection,
        "shipping_address_collection": shipping_address_collection,
        "expires_at": expires_at,
        "subscription_data": subscription_data,
        "payment_intent_data": payment_intent_data,
        "invoice_creation": invoice_creation,
        "consent_collection": consent_collection,
        "locale": locale,
        "ui_mode": ui_mode,
        "return_url": return_url,
    }
    data, err = stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def checkout_sessions_retrieve(session_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/checkout/sessions/{session_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def checkout_sessions_list(
    limit: int = 10,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/checkout/sessions", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
