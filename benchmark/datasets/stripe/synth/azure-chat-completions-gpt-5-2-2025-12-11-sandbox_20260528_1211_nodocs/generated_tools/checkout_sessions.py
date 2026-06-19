from typing import Any, Dict, Optional

from .http import stripe_request


def create_checkout_session(
    *,
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: Optional[list[Dict[str, Any]]] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    locale: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
    }
    if line_items is not None:
        data["line_items"] = line_items
    if customer is not None:
        data["customer"] = customer
    if customer_email is not None:
        data["customer_email"] = customer_email
    if client_reference_id is not None:
        data["client_reference_id"] = client_reference_id
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = allow_promotion_codes
    if discounts is not None:
        data["discounts"] = discounts
    if subscription_data is not None:
        data["subscription_data"] = subscription_data
    if payment_intent_data is not None:
        data["payment_intent_data"] = payment_intent_data
    if metadata is not None:
        data["metadata"] = metadata
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if locale is not None:
        data["locale"] = locale

    res, err = stripe_request(
        "POST",
        "/v1/checkout/sessions",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_checkout_session(session_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/checkout/sessions/{session_id}", stripe_account=stripe_account)
    return res if err is None else err


def list_checkout_sessions(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if customer is not None:
        query["customer"] = customer
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    if subscription is not None:
        query["subscription"] = subscription
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/checkout/sessions", query=query, stripe_account=stripe_account)
    return res if err is None else err
