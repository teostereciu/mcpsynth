from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def setup_intents_create(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[Any] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    attach_to_self: Optional[bool] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    use_stripe_sdk: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if description is not None:
        data["description"] = description
    if usage is not None:
        data["usage"] = usage
    if confirm is not None:
        data["confirm"] = confirm
    if return_url is not None:
        data["return_url"] = return_url
    if automatic_payment_methods is not None:
        data["automatic_payment_methods"] = automatic_payment_methods
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if payment_method_options is not None:
        data["payment_method_options"] = payment_method_options
    if payment_method_data is not None:
        data["payment_method_data"] = payment_method_data
    if metadata is not None:
        data["metadata"] = metadata
    if attach_to_self is not None:
        data["attach_to_self"] = attach_to_self
    if mandate_data is not None:
        data["mandate_data"] = mandate_data
    if use_stripe_sdk is not None:
        data["use_stripe_sdk"] = use_stripe_sdk
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/setup_intents",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def setup_intents_retrieve(
    *,
    setup_intent_id: str,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret} if client_secret else None
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )


def setup_intents_update(
    *,
    setup_intent_id: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[Any] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    attach_to_self: Optional[bool] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if payment_method_options is not None:
        data["payment_method_options"] = payment_method_options
    if payment_method_data is not None:
        data["payment_method_data"] = payment_method_data
    if attach_to_self is not None:
        data["attach_to_self"] = attach_to_self
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def setup_intents_confirm(
    *,
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if return_url is not None:
        data["return_url"] = return_url
    if use_stripe_sdk is not None:
        data["use_stripe_sdk"] = use_stripe_sdk
    if mandate_data is not None:
        data["mandate_data"] = mandate_data
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def setup_intents_cancel(
    *,
    setup_intent_id: str,
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
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def setup_intents_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
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
    if payment_method is not None:
        query["payment_method"] = payment_method
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/setup_intents", params=query, stripe_account=stripe_account)
