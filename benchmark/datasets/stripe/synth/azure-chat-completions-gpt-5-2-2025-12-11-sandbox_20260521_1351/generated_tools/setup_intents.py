from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_setup_intent(
    *,
    payment_method_types: Optional[list[str]] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_configuration: Optional[str] = None,
    attach_to_self: Optional[bool] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
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
    if usage is not None:
        params["usage"] = usage
    if confirm is not None:
        params["confirm"] = confirm
    if return_url is not None:
        params["return_url"] = return_url
    if automatic_payment_methods is not None:
        params["automatic_payment_methods"] = automatic_payment_methods
    if payment_method_options is not None:
        params["payment_method_options"] = payment_method_options
    if payment_method_data is not None:
        params["payment_method_data"] = payment_method_data
    if payment_method_configuration is not None:
        params["payment_method_configuration"] = payment_method_configuration
    if attach_to_self is not None:
        params["attach_to_self"] = attach_to_self

    return stripe_request("POST", "/v1/setup_intents", params=params, account=account, idempotency_key=idempotency_key)


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    expand: Optional[list[str]] = None,
    account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if client_secret is not None:
        params["client_secret"] = client_secret
    if expand is not None:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", params=params, account=account)


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    attach_to_self: Optional[bool] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_configuration: Optional[str] = None,
    excluded_payment_method_types: Optional[list[str]] = None,
    flow_directions: Optional[list[str]] = None,
    payment_method_types: Optional[list[str]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
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
    if attach_to_self is not None:
        params["attach_to_self"] = attach_to_self
    if payment_method_options is not None:
        params["payment_method_options"] = payment_method_options
    if payment_method_data is not None:
        params["payment_method_data"] = payment_method_data
    if payment_method_configuration is not None:
        params["payment_method_configuration"] = payment_method_configuration
    if excluded_payment_method_types is not None:
        params["excluded_payment_method_types"] = excluded_payment_method_types
    if flow_directions is not None:
        params["flow_directions"] = flow_directions
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types

    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if return_url is not None:
        params["return_url"] = return_url
    if use_stripe_sdk is not None:
        params["use_stripe_sdk"] = use_stripe_sdk
    if mandate_data is not None:
        params["mandate_data"] = mandate_data
    if payment_method_options is not None:
        params["payment_method_options"] = payment_method_options

    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def cancel_setup_intent(
    setup_intent_id: str,
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
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
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
    if payment_method is not None:
        params["payment_method"] = payment_method
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/setup_intents", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/setup_intents", params=params, account=account)
