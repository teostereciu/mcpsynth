from typing import Any, Dict, Optional, List

from .http_client import ok_or_error, stripe_request


def create_setup_intent(
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[List[str]] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "payment_method": payment_method,
        "usage": usage,
        "confirm": confirm,
        "return_url": return_url,
        "automatic_payment_methods": automatic_payment_methods,
        "payment_method_types": payment_method_types,
        "metadata": metadata,
    }
    status, payload = stripe_request(
        "POST", "/v1/setup_intents", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_setup_intent(
    *,
    setup_intent_id: str,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"client_secret": client_secret}
    status, payload = stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_setup_intent(
    *,
    setup_intent_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "payment_method": payment_method,
        "metadata": metadata,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def confirm_setup_intent(
    *,
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"payment_method": payment_method, "return_url": return_url, "use_stripe_sdk": use_stripe_sdk}
    status, payload = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def cancel_setup_intent(
    *,
    setup_intent_id: str,
    cancellation_reason: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"cancellation_reason": cancellation_reason}
    status, payload = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {
        "customer": customer,
        "payment_method": payment_method,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/setup_intents", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
