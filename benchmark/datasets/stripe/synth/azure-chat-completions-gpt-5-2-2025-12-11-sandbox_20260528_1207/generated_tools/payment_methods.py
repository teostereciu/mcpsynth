from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_method(
    *,
    type: str,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_redisplay: Optional[str] = None,
    type_details: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"type": type}
    if billing_details is not None:
        params["billing_details"] = billing_details
    if metadata is not None:
        params["metadata"] = metadata
    if allow_redisplay is not None:
        params["allow_redisplay"] = allow_redisplay
    # For type-specific fields, pass them under their type key (e.g. {"card": {...}})
    if type_details is not None:
        params[type] = type_details
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/payment_methods",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_method(payment_method_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_methods/{payment_method_id}", stripe_account=stripe_account)


def update_payment_method(
    payment_method_id: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    payto: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
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
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def attach_payment_method(
    payment_method_id: str,
    *,
    customer: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/attach",
        params={"customer": customer},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def detach_payment_method(
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/detach",
        params={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_methods_for_customer(
    customer_id: str,
    *,
    type: str = "card",
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"type": type, "limit": limit}
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods",
        params=params,
        stripe_account=stripe_account,
    )


def retrieve_customer_payment_method(
    customer_id: str,
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/customers/{customer_id}/payment_methods/{payment_method_id}",
        stripe_account=stripe_account,
    )
