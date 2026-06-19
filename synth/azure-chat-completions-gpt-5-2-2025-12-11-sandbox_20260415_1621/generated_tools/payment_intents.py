from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def payment_intents_create(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    confirm: Optional[bool] = None,
    off_session: Optional[Any] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if confirm is not None:
        data["confirm"] = confirm
    if off_session is not None:
        data["off_session"] = off_session
    if setup_future_usage is not None:
        data["setup_future_usage"] = setup_future_usage
    if automatic_payment_methods is not None:
        data["automatic_payment_methods"] = automatic_payment_methods
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/payment_intents",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_retrieve(
    *,
    payment_intent_id: str,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret} if client_secret else None
    return stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )


def payment_intents_update(
    *,
    payment_intent_id: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount is not None:
        data["amount"] = amount
    if currency is not None:
        data["currency"] = currency
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        data["setup_future_usage"] = setup_future_usage
    if automatic_payment_methods is not None:
        data["automatic_payment_methods"] = automatic_payment_methods
    if shipping is not None:
        data["shipping"] = shipping
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_confirm(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
    error_on_requires_action: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if return_url is not None:
        data["return_url"] = return_url
    if off_session is not None:
        data["off_session"] = off_session
    if error_on_requires_action is not None:
        data["error_on_requires_action"] = error_on_requires_action
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_capture(
    *,
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount_to_capture is not None:
        data["amount_to_capture"] = amount_to_capture
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_cancel(
    *,
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if cancellation_reason is not None:
        data["cancellation_reason"] = cancellation_reason
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_intents_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if customer is not None:
        query["customer"] = customer
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/payment_intents", params=query, stripe_account=stripe_account)
