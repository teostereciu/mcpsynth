from typing import Any, Dict, Optional

from .http import stripe_request


def create_payment_intent(
    amount: int,
    currency: str,
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    capture_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    confirmation_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
    }
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if capture_method is not None:
        data["capture_method"] = capture_method
    if confirm is not None:
        data["confirm"] = confirm
    if confirmation_method is not None:
        data["confirmation_method"] = confirmation_method
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if setup_future_usage is not None:
        data["setup_future_usage"] = setup_future_usage
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if transfer_data is not None:
        data["transfer_data"] = transfer_data
    if application_fee_amount is not None:
        data["application_fee_amount"] = application_fee_amount
    if on_behalf_of is not None:
        data["on_behalf_of"] = on_behalf_of

    res, err = stripe_request(
        "POST",
        "/v1/payment_intents",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_payment_intent(payment_intent_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request(
        "GET",
        f"/v1/payment_intents/{payment_intent_id}",
        stripe_account=stripe_account,
    )
    return res if err is None else err


def update_payment_intent(
    payment_intent_id: str,
    *,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    setup_future_usage: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount is not None:
        data["amount"] = amount
    if currency is not None:
        data["currency"] = currency
    if customer is not None:
        data["customer"] = customer
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if payment_method is not None:
        data["payment_method"] = payment_method
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if setup_future_usage is not None:
        data["setup_future_usage"] = setup_future_usage

    res, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        data=data,
        stripe_account=stripe_account,
    )
    return res if err is None else err


def confirm_payment_intent(
    payment_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    mandate: Optional[str] = None,
    off_session: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if return_url is not None:
        data["return_url"] = return_url
    if mandate is not None:
        data["mandate"] = mandate
    if off_session is not None:
        data["off_session"] = off_session

    res, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def capture_payment_intent(
    payment_intent_id: str,
    *,
    amount_to_capture: Optional[int] = None,
    application_fee_amount: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount_to_capture is not None:
        data["amount_to_capture"] = amount_to_capture
    if application_fee_amount is not None:
        data["application_fee_amount"] = application_fee_amount

    res, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def cancel_payment_intent(
    payment_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if cancellation_reason is not None:
        data["cancellation_reason"] = cancellation_reason

    res, err = stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        data=data,
        stripe_account=stripe_account,
    )
    return res if err is None else err


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if customer is not None:
        query["customer"] = customer
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created

    res, err = stripe_request(
        "GET",
        "/v1/payment_intents",
        query=query,
        stripe_account=stripe_account,
    )
    return res if err is None else err
