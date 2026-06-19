from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
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
    if metadata is not None:
        params["metadata"] = metadata
    if automatic_payment_methods is not None:
        params["automatic_payment_methods"] = automatic_payment_methods
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix

    data, err = stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or data


def retrieve_payment_intent(
    payment_intent_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data, err = stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        stripe_account=stripe_account,
    )
    return err or data


def update_payment_intent(
    payment_intent_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    payment_method: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if payment_method is not None:
        params["payment_method"] = payment_method

    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return err or data


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    data, err = stripe_request(
        "GET",
        "/v1/payment_intents",
        params=params,
        stripe_account=stripe_account,
    )
    return err or data


def confirm_payment_intent(
    payment_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if return_url is not None:
        params["return_url"] = return_url

    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or data


def capture_payment_intent(
    payment_intent_id: str,
    *,
    amount_to_capture: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount_to_capture is not None:
        params["amount_to_capture"] = amount_to_capture

    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or data


def cancel_payment_intent(
    payment_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if cancellation_reason is not None:
        params["cancellation_reason"] = cancellation_reason

    data, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params=params,
        stripe_account=stripe_account,
    )
    return err or data
