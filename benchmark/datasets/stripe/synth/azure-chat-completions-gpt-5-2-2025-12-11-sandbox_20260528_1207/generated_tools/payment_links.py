from typing import Any, Dict, Optional, List

from .http_client import stripe_request


def create_payment_link(
    *,
    line_items: List[Dict[str, Any]],
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[List[Dict[str, Any]]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"line_items": line_items}
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = active
    if after_completion is not None:
        params["after_completion"] = after_completion
    if allow_promotion_codes is not None:
        params["allow_promotion_codes"] = allow_promotion_codes
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if billing_address_collection is not None:
        params["billing_address_collection"] = billing_address_collection
    if currency is not None:
        params["currency"] = currency
    if customer_creation is not None:
        params["customer_creation"] = customer_creation
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if shipping_options is not None:
        params["shipping_options"] = shipping_options
    if restrictions is not None:
        params["restrictions"] = restrictions
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/payment_links",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = active
    if line_items is not None:
        params["line_items"] = line_items
    if metadata is not None:
        params["metadata"] = metadata
    if after_completion is not None:
        params["after_completion"] = after_completion
    if allow_promotion_codes is not None:
        params["allow_promotion_codes"] = allow_promotion_codes
    if automatic_tax is not None:
        params["automatic_tax"] = automatic_tax
    if billing_address_collection is not None:
        params["billing_address_collection"] = billing_address_collection
    if customer_creation is not None:
        params["customer_creation"] = customer_creation
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if restrictions is not None:
        params["restrictions"] = restrictions
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_link(payment_link_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)


def list_payment_links(
    *,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if active is not None:
        params["active"] = active
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/payment_links", params=params, stripe_account=stripe_account)


def list_payment_link_line_items(
    payment_link_id: str,
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params=params,
        stripe_account=stripe_account,
    )
