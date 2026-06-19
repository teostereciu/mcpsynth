from typing import Any, Dict, Optional

from .http import stripe_request


def setup_intents_create(
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "usage": usage,
        "confirm": confirm,
        "return_url": return_url,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
        "payment_method_types": payment_method_types,
        "mandate_data": mandate_data,
    }
    data, err = stripe_request(
        "POST",
        "/v1/setup_intents",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def setup_intents_retrieve(setup_intent_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def setup_intents_update(
    setup_intent_id: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "customer": customer,
        "payment_method": payment_method,
        "metadata": metadata,
        "payment_method_types": payment_method_types,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def setup_intents_confirm(
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"payment_method": payment_method, "return_url": return_url, "mandate_data": mandate_data}
    data, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def setup_intents_cancel(
    setup_intent_id: str,
    cancellation_reason: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"cancellation_reason": cancellation_reason}
    data, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def setup_intents_list(
    limit: int = 10,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "limit": limit,
        "customer": customer,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/setup_intents", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
