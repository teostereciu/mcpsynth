from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/payment-link.md

def create_payment_link(
    line_items: list[Dict[str, Any]],
    *,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "line_items": line_items,
        "metadata": metadata,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "currency": currency,
        "customer_creation": customer_creation,
        "inactive_message": inactive_message,
        "invoice_creation": invoice_creation,
        "payment_intent_data": payment_intent_data,
        "payment_method_types": payment_method_types,
        "shipping_address_collection": shipping_address_collection,
        "shipping_options": shipping_options,
        "submit_type": submit_type,
        "subscription_data": subscription_data,
        "tax_id_collection": tax_id_collection,
    }
    return stripe_request(
        "POST",
        "/v1/payment_links",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_link(
    payment_link_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}",
        params={"expand": expand},
        stripe_account=stripe_account,
    )


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    inactive_message: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "line_items": line_items,
        "metadata": metadata,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "currency": currency,
        "customer_creation": customer_creation,
        "inactive_message": inactive_message,
        "invoice_creation": invoice_creation,
        "payment_intent_data": payment_intent_data,
        "payment_method_types": payment_method_types,
        "shipping_address_collection": shipping_address_collection,
        "shipping_options": shipping_options,
        "submit_type": submit_type,
        "subscription_data": subscription_data,
        "tax_id_collection": tax_id_collection,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_links(
    *,
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        "/v1/payment_links",
        params=params,
        stripe_account=stripe_account,
    )


def retrieve_payment_link_line_items(
    payment_link_id: str,
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params=params,
        stripe_account=stripe_account,
    )
