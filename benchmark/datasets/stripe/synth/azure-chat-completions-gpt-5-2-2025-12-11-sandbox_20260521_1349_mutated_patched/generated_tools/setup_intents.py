from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_setup_intent(
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents"""
    return stripe_request(
        "POST",
        "/v1/setup_intents",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents/{id}"""
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{id}"""
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{id}/confirm"""
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_setup_intent(
    setup_intent_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{id}/cancel"""
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_setup_intents(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents"""
    return stripe_request("GET", "/v1/setup_intents", params, stripe_account=stripe_account)
