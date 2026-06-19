from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


def create_setup_intent(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[Any] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_method is not None:
        params["payment_method"] = payment_method
    if usage is not None:
        params["usage"] = usage
    if confirm is not None:
        params["confirm"] = str(confirm).lower()
    if return_url is not None:
        params["return_url"] = return_url
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if automatic_payment_methods is not None:
        params["automatic_payment_methods"] = automatic_payment_methods
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types

    return stripe_request_with_retries(
        "POST",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if client_secret is not None:
        params["client_secret"] = client_secret

    return stripe_request_with_retries(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_method is not None:
        params["payment_method"] = payment_method
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request_with_retries(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if return_url is not None:
        params["return_url"] = return_url
    if use_stripe_sdk is not None:
        params["use_stripe_sdk"] = str(use_stripe_sdk).lower()

    return stripe_request_with_retries(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_setup_intent(
    setup_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if cancellation_reason is not None:
        params["cancellation_reason"] = cancellation_reason

    return stripe_request_with_retries(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params=params,
        stripe_account=stripe_account,
    )


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_method is not None:
        params["payment_method"] = payment_method
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
    )
