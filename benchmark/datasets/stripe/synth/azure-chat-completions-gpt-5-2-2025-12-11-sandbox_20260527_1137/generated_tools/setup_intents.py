from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_setup_intent(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents"""
    return stripe_request(
        "POST",
        "/v1/setup_intents",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{seti}"""
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents/{seti}"""
    params: Dict[str, Any] = _maybe_expand({}, expand)
    if client_secret:
        params["client_secret"] = client_secret
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
    )


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{seti}/confirm"""
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_setup_intent(
    setup_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{seti}/cancel"""
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_setup_intents(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents"""
    return stripe_request("GET", "/v1/setup_intents", params or {}, stripe_account=stripe_account)
