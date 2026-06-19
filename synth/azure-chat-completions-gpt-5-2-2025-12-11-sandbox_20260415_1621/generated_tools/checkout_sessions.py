from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def checkout_sessions_create(
    *,
    mode: str,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    ui_mode: Optional[str] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[List[str]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[List[Dict[str, Any]]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    locale: Optional[str] = None,
    expires_at: Optional[int] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"mode": mode}
    if success_url is not None:
        data["success_url"] = success_url
    if cancel_url is not None:
        data["cancel_url"] = cancel_url
    if return_url is not None:
        data["return_url"] = return_url
    if customer is not None:
        data["customer"] = customer
    if customer_email is not None:
        data["customer_email"] = customer_email
    if client_reference_id is not None:
        data["client_reference_id"] = client_reference_id
    if line_items is not None:
        data["line_items"] = line_items
    if metadata is not None:
        data["metadata"] = metadata
    if ui_mode is not None:
        data["ui_mode"] = ui_mode
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = allow_promotion_codes
    if discounts is not None:
        data["discounts"] = discounts
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if invoice_creation is not None:
        data["invoice_creation"] = invoice_creation
    if payment_intent_data is not None:
        data["payment_intent_data"] = payment_intent_data
    if subscription_data is not None:
        data["subscription_data"] = subscription_data
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if shipping_address_collection is not None:
        data["shipping_address_collection"] = shipping_address_collection
    if shipping_options is not None:
        data["shipping_options"] = shipping_options
    if tax_id_collection is not None:
        data["tax_id_collection"] = tax_id_collection
    if locale is not None:
        data["locale"] = locale
    if expires_at is not None:
        data["expires_at"] = expires_at
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/checkout/sessions",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def checkout_sessions_retrieve(
    *,
    session_id: str,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/checkout/sessions/{session_id}",
        params=params if params else None,
        stripe_account=stripe_account,
    )


def checkout_sessions_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
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
    if payment_intent is not None:
        query["payment_intent"] = payment_intent
    if subscription is not None:
        query["subscription"] = subscription
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/checkout/sessions", params=query, stripe_account=stripe_account)


def checkout_sessions_expire(
    *,
    session_id: str,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/checkout/sessions/{session_id}/expire",
        data=extra or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
