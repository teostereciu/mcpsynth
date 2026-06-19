from typing import Any, Dict, Optional, List

from .http_client import ok_or_error, stripe_request


def create_checkout_session(
    *,
    mode: str,
    line_items: Optional[List[Dict[str, Any]]] = None,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    ui_mode: Optional[str] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[List[Dict[str, Any]]] = None,
    expires_at: Optional[int] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "mode": mode,
        "line_items": line_items,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "return_url": return_url,
        "customer": customer,
        "customer_email": customer_email,
        "client_reference_id": client_reference_id,
        "metadata": metadata,
        "ui_mode": ui_mode,
        "allow_promotion_codes": allow_promotion_codes,
        "discounts": discounts,
        "automatic_tax": automatic_tax,
        "invoice_creation": invoice_creation,
        "payment_intent_data": payment_intent_data,
        "subscription_data": subscription_data,
        "shipping_address_collection": shipping_address_collection,
        "shipping_options": shipping_options,
        "expires_at": expires_at,
    }
    status, payload = stripe_request(
        "POST", "/v1/checkout/sessions", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_checkout_session(
    *,
    session_id: str,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"expand": expand}
    status, payload = stripe_request("GET", f"/v1/checkout/sessions/{session_id}", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_checkout_session(
    *,
    session_id: str,
    metadata: Optional[Dict[str, str]] = None,
    shipping_options: Optional[List[Dict[str, Any]]] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    allow_promotion_codes: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "metadata": metadata,
        "shipping_options": shipping_options,
        "discounts": discounts,
        "allow_promotion_codes": allow_promotion_codes,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def expire_checkout_session(
    *,
    session_id: str,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    status, payload = stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        params={},
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/checkout/sessions", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
