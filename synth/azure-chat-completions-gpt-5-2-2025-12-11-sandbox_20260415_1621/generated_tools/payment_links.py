from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def payment_links_create(
    *,
    line_items: List[Dict[str, Any]],
    metadata: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    consent_collection: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    custom_fields: Optional[List[Dict[str, Any]]] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    name_collection: Optional[Dict[str, Any]] = None,
    optional_items: Optional[List[Dict[str, Any]]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[List[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[List[Dict[str, Any]]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"line_items": line_items}
    if metadata is not None:
        data["metadata"] = metadata
    if active is not None:
        data["active"] = active
    if after_completion is not None:
        data["after_completion"] = after_completion
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = allow_promotion_codes
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if billing_address_collection is not None:
        data["billing_address_collection"] = billing_address_collection
    if consent_collection is not None:
        data["consent_collection"] = consent_collection
    if currency is not None:
        data["currency"] = currency
    if custom_fields is not None:
        data["custom_fields"] = custom_fields
    if custom_text is not None:
        data["custom_text"] = custom_text
    if customer_creation is not None:
        data["customer_creation"] = customer_creation
    if inactive_message is not None:
        data["inactive_message"] = inactive_message
    if invoice_creation is not None:
        data["invoice_creation"] = invoice_creation
    if name_collection is not None:
        data["name_collection"] = name_collection
    if optional_items is not None:
        data["optional_items"] = optional_items
    if payment_intent_data is not None:
        data["payment_intent_data"] = payment_intent_data
    if payment_method_collection is not None:
        data["payment_method_collection"] = payment_method_collection
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if phone_number_collection is not None:
        data["phone_number_collection"] = phone_number_collection
    if restrictions is not None:
        data["restrictions"] = restrictions
    if shipping_address_collection is not None:
        data["shipping_address_collection"] = shipping_address_collection
    if shipping_options is not None:
        data["shipping_options"] = shipping_options
    if submit_type is not None:
        data["submit_type"] = submit_type
    if subscription_data is not None:
        data["subscription_data"] = subscription_data
    if tax_id_collection is not None:
        data["tax_id_collection"] = tax_id_collection
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/payment_links",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_links_retrieve(*, payment_link_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)


def payment_links_update(
    *,
    payment_link_id: str,
    active: Optional[bool] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    custom_fields: Optional[List[Dict[str, Any]]] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    name_collection: Optional[Dict[str, Any]] = None,
    optional_items: Optional[List[Dict[str, Any]]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[List[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if line_items is not None:
        data["line_items"] = line_items
    if metadata is not None:
        data["metadata"] = metadata
    if after_completion is not None:
        data["after_completion"] = after_completion
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = allow_promotion_codes
    if automatic_tax is not None:
        data["automatic_tax"] = automatic_tax
    if billing_address_collection is not None:
        data["billing_address_collection"] = billing_address_collection
    if custom_fields is not None:
        data["custom_fields"] = custom_fields
    if custom_text is not None:
        data["custom_text"] = custom_text
    if customer_creation is not None:
        data["customer_creation"] = customer_creation
    if inactive_message is not None:
        data["inactive_message"] = inactive_message
    if invoice_creation is not None:
        data["invoice_creation"] = invoice_creation
    if name_collection is not None:
        data["name_collection"] = name_collection
    if optional_items is not None:
        data["optional_items"] = optional_items
    if payment_intent_data is not None:
        data["payment_intent_data"] = payment_intent_data
    if payment_method_collection is not None:
        data["payment_method_collection"] = payment_method_collection
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if phone_number_collection is not None:
        data["phone_number_collection"] = phone_number_collection
    if restrictions is not None:
        data["restrictions"] = restrictions
    if shipping_address_collection is not None:
        data["shipping_address_collection"] = shipping_address_collection
    if submit_type is not None:
        data["submit_type"] = submit_type
    if subscription_data is not None:
        data["subscription_data"] = subscription_data
    if tax_id_collection is not None:
        data["tax_id_collection"] = tax_id_collection
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def payment_links_list(
    *,
    limit: Optional[int] = 10,
    active: Optional[bool] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if active is not None:
        query["active"] = active
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/payment_links", params=query, stripe_account=stripe_account)


def payment_links_list_line_items(
    *,
    payment_link_id: str,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params=query if query else None,
        stripe_account=stripe_account,
    )
