from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_link(
    line_items: list,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    consent_collection: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    custom_fields: Optional[list] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    name_collection: Optional[Dict[str, Any]] = None,
    optional_items: Optional[list] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[list] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links"""
    params: Dict[str, Any] = {"line_items": line_items}
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
    if consent_collection is not None:
        params["consent_collection"] = consent_collection
    if currency is not None:
        params["currency"] = currency
    if custom_fields is not None:
        params["custom_fields"] = custom_fields
    if custom_text is not None:
        params["custom_text"] = custom_text
    if customer_creation is not None:
        params["customer_creation"] = customer_creation
    if inactive_message is not None:
        params["inactive_message"] = inactive_message
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if name_collection is not None:
        params["name_collection"] = name_collection
    if optional_items is not None:
        params["optional_items"] = optional_items
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if payment_method_collection is not None:
        params["payment_method_collection"] = payment_method_collection
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if phone_number_collection is not None:
        params["phone_number_collection"] = phone_number_collection
    if restrictions is not None:
        params["restrictions"] = restrictions
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

    data, err = stripe_request(
        "POST",
        "/v1/payment_links",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    line_items: Optional[list] = None,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    custom_fields: Optional[list] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    name_collection: Optional[Dict[str, Any]] = None,
    optional_items: Optional[list] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[list] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links/{id}"""
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
    if custom_fields is not None:
        params["custom_fields"] = custom_fields
    if custom_text is not None:
        params["custom_text"] = custom_text
    if customer_creation is not None:
        params["customer_creation"] = customer_creation
    if inactive_message is not None:
        params["inactive_message"] = inactive_message
    if invoice_creation is not None:
        params["invoice_creation"] = invoice_creation
    if name_collection is not None:
        params["name_collection"] = name_collection
    if optional_items is not None:
        params["optional_items"] = optional_items
    if payment_intent_data is not None:
        params["payment_intent_data"] = payment_intent_data
    if payment_method_collection is not None:
        params["payment_method_collection"] = payment_method_collection
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if phone_number_collection is not None:
        params["phone_number_collection"] = phone_number_collection
    if restrictions is not None:
        params["restrictions"] = restrictions
    if shipping_address_collection is not None:
        params["shipping_address_collection"] = shipping_address_collection
    if submit_type is not None:
        params["submit_type"] = submit_type
    if subscription_data is not None:
        params["subscription_data"] = subscription_data
    if tax_id_collection is not None:
        params["tax_id_collection"] = tax_id_collection

    data, err = stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_payment_link_line_items(
    payment_link_id: str,
    *,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{id}/line_items"""
    params: Dict[str, Any] = {}
    if ending_before is not None:
        params["ending_before"] = ending_before
    if starting_after is not None:
        params["starting_after"] = starting_after
    if limit is not None:
        params["limit"] = limit

    data, err = stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params=params,
        stripe_account=stripe_account,
    )
    return data if err is None else err
