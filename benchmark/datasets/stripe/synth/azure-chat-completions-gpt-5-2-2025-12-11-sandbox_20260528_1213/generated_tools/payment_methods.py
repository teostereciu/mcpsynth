from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_method(
    type: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_methods"""
    params: Dict[str, Any] = {"type": type}
    if billing_details is not None:
        params["billing_details"] = billing_details
    if metadata is not None:
        params["metadata"] = metadata
    if allow_redisplay is not None:
        params["allow_redisplay"] = allow_redisplay
    # Pass type-specific details as a dict under the type key, e.g. {"card": {...}}
    if details is not None:
        params.update(details)

    data, err = stripe_request(
        "POST",
        "/v1/payment_methods",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_payment_method(
    payment_method_id: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    payto: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_methods/{id}"""
    params: Dict[str, Any] = {}
    if billing_details is not None:
        params["billing_details"] = billing_details
    if metadata is not None:
        params["metadata"] = metadata
    if allow_redisplay is not None:
        params["allow_redisplay"] = allow_redisplay
    if card is not None:
        params["card"] = card
    if us_bank_account is not None:
        params["us_bank_account"] = us_bank_account
    if payto is not None:
        params["payto"] = payto

    data, err = stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_customer_payment_method(
    customer_id: str,
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer}/payment_methods/{payment_method}"""
    data, err = stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
