from typing import Any, Dict, Optional

from .http import stripe_request


def create_setup_intent(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    usage: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if usage is not None:
        data["usage"] = usage
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request(
        "POST",
        "/v1/setup_intents",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_setup_intent(setup_intent_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    if return_url is not None:
        data["return_url"] = return_url

    res, err = stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def cancel_setup_intent(setup_intent_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", data={}, stripe_account=stripe_account)
    return res if err is None else err


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if customer is not None:
        query["customer"] = customer
    if payment_method is not None:
        query["payment_method"] = payment_method
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/setup_intents", query=query, stripe_account=stripe_account)
    return res if err is None else err
