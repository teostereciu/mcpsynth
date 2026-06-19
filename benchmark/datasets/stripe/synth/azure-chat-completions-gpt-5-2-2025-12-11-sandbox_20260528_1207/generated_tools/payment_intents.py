from typing import Any, Dict, Optional, List

from .http_client import stripe_request


def create_payment_intent(
    *,
    amount: int,
    currency: str,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    description: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    off_session: Optional[Any] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "currency": currency}
    if confirm is not None:
        params["confirm"] = confirm
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if payment_method is not None:
        params["payment_method"] = payment_method
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if description is not None:
        params["description"] = description
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if off_session is not None:
        params["off_session"] = off_session
    if automatic_payment_methods is not None:
        params["automatic_payment_methods"] = automatic_payment_methods
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/payment_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_intent(payment_intent_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", stripe_account=stripe_account)


def update_payment_intent(
    payment_intent_id: str,
    *,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    description: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
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
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if description is not None:
        params["description"] = description
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if shipping is not None:
        params["shipping"] = shipping
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix is not None:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}",
        params=params,
        stripe_account=stripe_account,
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
    mandate: Optional[str] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
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
    if mandate is not None:
        params["mandate"] = mandate
    if mandate_data is not None:
        params["mandate_data"] = mandate_data
    if payment_method_data is not None:
        params["payment_method_data"] = payment_method_data
    if shipping is not None:
        params["shipping"] = shipping
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/confirm",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def capture_payment_intent(
    payment_intent_id: str,
    *,
    amount_to_capture: Optional[int] = None,
    application_fee_amount: Optional[int] = None,
    final_capture: Optional[bool] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount_to_capture is not None:
        params["amount_to_capture"] = amount_to_capture
    if application_fee_amount is not None:
        params["application_fee_amount"] = application_fee_amount
    if final_capture is not None:
        params["final_capture"] = final_capture
    if transfer_data is not None:
        params["transfer_data"] = transfer_data
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/capture",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_payment_intent(
    payment_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if cancellation_reason is not None:
        params["cancellation_reason"] = cancellation_reason
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payment_intents/{payment_intent_id}/cancel",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_intents(
    *,
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer is not None:
        params["customer"] = customer
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if created is not None:
        params["created"] = created
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
