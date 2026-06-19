from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    off_session: Optional[Any] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents"""
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
    }
    if automatic_payment_methods is not None:
        params["automatic_payment_methods"] = automatic_payment_methods
    if confirm is not None:
        params["confirm"] = confirm
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if off_session is not None:
        params["off_session"] = off_session
    if payment_method is not None:
        params["payment_method"] = payment_method
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix

    data, err = stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_payment_intent(
    payment_intent_id: str,
    *,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}"""
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if currency is not None:
        params["currency"] = currency
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if payment_method is not None:
        params["payment_method"] = payment_method
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix

    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_payment_intent(
    payment_intent_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_intents/{intent}"""
    data, err = stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
