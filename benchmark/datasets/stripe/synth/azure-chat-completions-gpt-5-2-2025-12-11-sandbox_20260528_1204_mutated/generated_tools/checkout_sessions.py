from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    automatic_tax: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    currency: Optional[str] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    customer_update: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_collection: Optional[str] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    locale: Optional[str] = None,
    expires_at: Optional[int] = None,
    after_expiration: Optional[Dict[str, Any]] = None,
    consent_collection: Optional[Dict[str, Any]] = None,
    custom_fields: Optional[list[Dict[str, Any]]] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    submit_type: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions

    Doc: docs/checkout_sessions.md (Create a Checkout Session)
    """
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
        "automatic_tax": automatic_tax,
        "allow_promotion_codes": allow_promotion_codes,
        "discounts": discounts,
        "currency": currency,
        "payment_intent_data": payment_intent_data,
        "subscription_data": subscription_data,
        "invoice_creation": invoice_creation,
        "customer_creation": customer_creation,
        "customer_update": customer_update,
        "payment_method_types": payment_method_types,
        "payment_method_collection": payment_method_collection,
        "shipping_address_collection": shipping_address_collection,
        "shipping_options": shipping_options,
        "phone_number_collection": phone_number_collection,
        "tax_id_collection": tax_id_collection,
        "locale": locale,
        "expires_at": expires_at,
        "after_expiration": after_expiration,
        "consent_collection": consent_collection,
        "custom_fields": custom_fields,
        "custom_text": custom_text,
        "submit_type": submit_type,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(
    session_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions/{session_id}

    Doc: docs/checkout_sessions.md (Retrieve a Checkout Session)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        params,
        stripe_account=stripe_account,
    )


def expire_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions/{session_id}/expire

    Doc: docs/checkout_sessions.md (Expire a Checkout Session)
    """
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        None,
        stripe_account=stripe_account,
    )


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/checkout/sessions

    Doc: docs/checkout_sessions.md (List all Checkout Sessions)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "status": status,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/checkout/sessions",
        params,
        stripe_account=stripe_account,
    )
