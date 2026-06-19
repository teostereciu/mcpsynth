from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    off_session: Optional[Any] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
    }
    if confirm is not None:
        params["confirm"] = confirm
    if customer is not None:
        params["customer"] = customer
    if payment_method is not None:
        params["payment_method"] = payment_method
    if description is not None:
        params["description"] = description
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if automatic_payment_methods is not None:
        params["automatic_payment_methods"] = automatic_payment_methods
    if metadata is not None:
        params["metadata"] = metadata
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix
    if off_session is not None:
        params["off_session"] = off_session

    return stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_intent(
    payment_intent_id: str,
    *,
    expand: Optional[list[str]] = None,
    account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", params=params, account=account)


def update_payment_intent(
    payment_intent_id: str,
    *,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if currency is not None:
        params["currency"] = currency
    if customer is not None:
        params["customer"] = customer
    if payment_method is not None:
        params["payment_method"] = payment_method
    if description is not None:
        params["description"] = description
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if metadata is not None:
        params["metadata"] = metadata
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def confirm_payment_intent(
    payment_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if return_url is not None:
        params["return_url"] = return_url
    if off_session is not None:
        params["off_session"] = off_session
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if payment_method_options is not None:
        params["payment_method_options"] = payment_method_options

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def capture_payment_intent(
    payment_intent_id: str,
    *,
    amount_to_capture: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount_to_capture is not None:
        params["amount_to_capture"] = amount_to_capture
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def cancel_payment_intent(
    payment_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if cancellation_reason is not None:
        params["cancellation_reason"] = cancellation_reason

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if created is not None:
        params["created"] = created
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/payment_intents", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/payment_intents", params=params, account=account)
