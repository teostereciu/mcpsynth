from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def setup_intents_create(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    payment_method_types: Optional[list] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "description": description,
        "metadata": metadata,
        "usage": usage,
        "confirm": confirm,
        "return_url": return_url,
        "payment_method_types": payment_method_types,
        "automatic_payment_methods": automatic_payment_methods,
    }
    return stripe_request("POST", "/v1/setup_intents", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def setup_intents_retrieve(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret} if client_secret else None
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", params, stripe_account=stripe_account)


def setup_intents_update(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "description": description,
        "metadata": metadata,
        "payment_method_types": payment_method_types,
        "automatic_payment_methods": automatic_payment_methods,
    }
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}", params, stripe_account=stripe_account)


def setup_intents_confirm(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"payment_method": payment_method, "return_url": return_url, "use_stripe_sdk": use_stripe_sdk}
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def setup_intents_cancel(
    setup_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def setup_intents_list(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "created": created,
        "payment_method": payment_method,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/setup_intents", params, stripe_account=stripe_account)


def setup_intents_list_all(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "created": created, "payment_method": payment_method}
    return stripe_list_all("/v1/setup_intents", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
