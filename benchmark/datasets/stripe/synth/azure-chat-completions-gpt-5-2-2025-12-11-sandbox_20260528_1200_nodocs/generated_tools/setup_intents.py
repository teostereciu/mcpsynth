from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def setup_intents_create(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    usage: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    return_url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "confirm": confirm,
        "usage": usage,
        "description": description,
        "metadata": metadata,
        "payment_method_types": payment_method_types,
        "automatic_payment_methods": automatic_payment_methods,
        "return_url": return_url,
    }
    res, err = stripe_post(
        "/v1/setup_intents",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def setup_intents_retrieve(*, setup_intent_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/setup_intents/{setup_intent_id}", stripe_account=stripe_account)
    return err or res


def setup_intents_confirm(
    *,
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {"payment_method": payment_method, "return_url": return_url}
    res, err = stripe_post(
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def setup_intents_cancel(
    *,
    setup_intent_id: str,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    res, err = stripe_post(
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def setup_intents_list(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/setup_intents", params=params, stripe_account=stripe_account)
    return err or res
