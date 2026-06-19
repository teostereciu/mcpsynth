from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/checkout/sessions
# GET /v1/checkout/sessions/{session}
# GET /v1/checkout/sessions
# POST /v1/checkout/sessions/{session}/expire


def create_checkout_session(
    mode: str,
    *,
    line_items: Optional[list[Dict[str, Any]]] = None,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    allow_promotion_codes: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    ui_mode: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "mode": mode,
        "line_items": line_items,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "return_url": return_url,
        "customer": customer,
        "customer_email": customer_email,
        "client_reference_id": client_reference_id,
        "allow_promotion_codes": allow_promotion_codes,
        "metadata": metadata,
        "automatic_tax": automatic_tax,
        "ui_mode": ui_mode,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(session_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}", stripe_account=stripe_account)


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
