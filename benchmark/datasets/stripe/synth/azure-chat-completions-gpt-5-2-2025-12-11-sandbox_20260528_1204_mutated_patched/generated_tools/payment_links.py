from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_link(
    line_items: list[Dict[str, Any]],
    *,
    metadata: Optional[Dict[str, str]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    consent_collection: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    custom_fields: Optional[list[Dict[str, Any]]] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    name_collection: Optional[Dict[str, Any]] = None,
    optional_items: Optional[list[Dict[str, Any]]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links

    Doc: docs/payment-link.md (Create a payment link)
    """
    params: Dict[str, Any] = {
        "line_items": line_items,
        "metadata": metadata,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "consent_collection": consent_collection,
        "currency": currency,
        "metadata": custom_fields,
        "custom_text": custom_text,
        "customer_creation": customer_creation,
        "inactive_message": inactive_message,
        "invoice_creation": invoice_creation,
        "name_collection": name_collection,
        "optional_items": optional_items,
        "payment_intent_data": payment_intent_data,
        "payment_method_collection": payment_method_collection,
        "payment_method_types": payment_method_types,
        "phone_number_collection": phone_number_collection,
        "restrictions": restrictions,
        "shipping_address_collection": shipping_address_collection,
        "shipping_options": shipping_options,
        "submit_type": submit_type,
        "subscription_data": subscription_data,
        "tax_id_collection": tax_id_collection,
        "transfer_data": transfer_data,
    }
    return stripe_request(
        "POST",
        "/v1/payment_links",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    custom_fields: Optional[list[Dict[str, Any]]] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    name_collection: Optional[Dict[str, Any]] = None,
    optional_items: Optional[list[Dict[str, Any]]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_links/{payment_link_id}

    Doc: docs/payment-link.md (Update a payment link)
    """
    params: Dict[str, Any] = {
        "active": active,
        "line_items": line_items,
        "metadata": metadata,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "metadata": custom_fields,
        "custom_text": custom_text,
        "customer_creation": customer_creation,
        "inactive_message": inactive_message,
        "invoice_creation": invoice_creation,
        "name_collection": name_collection,
        "optional_items": optional_items,
        "payment_intent_data": payment_intent_data,
        "payment_method_collection": payment_method_collection,
        "payment_method_types": payment_method_types,
        "phone_number_collection": phone_number_collection,
        "restrictions": restrictions,
        "shipping_address_collection": shipping_address_collection,
        "submit_type": submit_type,
        "subscription_data": subscription_data,
        "tax_id_collection": tax_id_collection,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params,
        stripe_account=stripe_account,
    )


def retrieve_payment_link(
    payment_link_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{payment_link_id}

    Doc: docs/payment-link.md (Retrieve a payment link)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}",
        params,
        stripe_account=stripe_account,
    )


def list_payment_links(
    *,
    active: Optional[bool] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links

    Doc: docs/payment-link.md (List all payment links)
    """
    params: Dict[str, Any] = {
        "active": active,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
    }
    return stripe_request(
        "GET",
        "/v1/payment_links",
        params,
        stripe_account=stripe_account,
    )


def list_payment_link_line_items(
    payment_link_id: str,
    *,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_links/{payment_link_id}/line_items

    Doc: docs/payment-link.md (Retrieve a payment link's line items)
    """
    params: Dict[str, Any] = {
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
    }
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params,
        stripe_account=stripe_account,
    )
