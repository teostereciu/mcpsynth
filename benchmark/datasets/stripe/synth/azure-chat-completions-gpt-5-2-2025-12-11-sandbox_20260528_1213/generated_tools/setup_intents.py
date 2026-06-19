from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_setup_intent(
    *,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    attach_to_self: Optional[bool] = None,
    payment_method_types: Optional[list] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents"""
    params: Dict[str, Any] = {}
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
    if payment_method is not None:
        params["payment_method"] = payment_method
    if usage is not None:
        params["usage"] = usage
    if attach_to_self is not None:
        params["attach_to_self"] = attach_to_self
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if payment_method_options is not None:
        params["payment_method_options"] = payment_method_options
    if return_url is not None:
        params["return_url"] = return_url
    if use_stripe_sdk is not None:
        params["use_stripe_sdk"] = use_stripe_sdk

    data, err = stripe_request(
        "POST",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    attach_to_self: Optional[bool] = None,
    excluded_payment_method_types: Optional[list] = None,
    flow_directions: Optional[list] = None,
    payment_method_configuration: Optional[str] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{id}"""
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
    if excluded_payment_method_types is not None:
        params["excluded_payment_method_types"] = excluded_payment_method_types
    if flow_directions is not None:
        params["flow_directions"] = flow_directions
    if payment_method_configuration is not None:
        params["payment_method_configuration"] = payment_method_configuration
    if payment_method_data is not None:
        params["payment_method_data"] = payment_method_data
    if payment_method_options is not None:
        params["payment_method_options"] = payment_method_options
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types

    data, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents/{id}"""
    params: Dict[str, Any] = {}
    if client_secret is not None:
        params["client_secret"] = client_secret

    data, err = stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params or None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
