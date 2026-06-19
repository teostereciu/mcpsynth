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
    metadata: Optional[Dict[str, str]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    ui_mode: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
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
        "automatic_tax": automatic_tax,
        "ui_mode": ui_mode,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_checkout_session(
    session_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_checkout_session(
    session_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        None,
        stripe_account=stripe_account,
    )
