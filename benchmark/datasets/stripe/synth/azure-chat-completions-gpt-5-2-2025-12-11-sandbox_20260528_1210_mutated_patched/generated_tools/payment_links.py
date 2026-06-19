from typing import Any, Dict, List, Optional

from .http_client import stripe_request_with_retries


def create_payment_link(
    line_items: List[Dict[str, Any]],
    *,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[List[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[List[Dict[str, Any]]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"line_items": line_items}
    if metadata is not None:
        params["metadata"] = metadata
    if after_completion is not None:
        params["after_completion"] = after_completion
    if allow_promotion_codes is not None:
        params["allow_promotion_codes"] = str(allow_promotion_codes).lower()
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
    if payment_method_collection is not None:
        params["payment_method_collection"] = payment_method_collection
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if phone_number_collection is not None:
        params["phone_number_collection"] = phone_number_collection
    if shipping_address_collection is not None:
        params["shipping_address_collection"] = shipping_address_collection
    if shipping_options is not None:
        params["shipping_options"] = shipping_options
    if submit_type is not None:
        params["submit_type"] = submit_type
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if tax_id_collection is not None:
        params["tax_id_collection"] = tax_id_collection

    return stripe_request_with_retries(
        "POST",
        "/v1/payment_links",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_link(payment_link_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/payment_links/{payment_link_id}",
        stripe_account=stripe_account,
    )


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = str(active).lower()
    if line_items is not None:
        params["line_items"] = line_items
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request_with_retries(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_payment_links(
    *,
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = str(active).lower()
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/payment_links",
        params=params,
        stripe_account=stripe_account,
    )


def list_payment_link_line_items(
    payment_link_id: str,
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params=params,
        stripe_account=stripe_account,
    )
