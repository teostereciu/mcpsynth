from typing import Any, Dict, Optional

from .http import stripe_request


def setup_intents_create(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "usage": usage,
        "confirm": confirm,
        "return_url": return_url,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        "/v1/setup_intents",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def setup_intents_retrieve(*, setup_intent_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def setup_intents_confirm(
    *,
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"payment_method": payment_method, "return_url": return_url}
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def setup_intents_cancel(
    *,
    setup_intent_id: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    result, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def setup_intents_list(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    result, err = stripe_request("GET", "/v1/setup_intents", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
