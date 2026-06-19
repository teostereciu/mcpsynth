from typing import Any, Dict, Optional, List

from .http_client import ok_or_error, stripe_request


def create_payment_link(
    *,
    line_items: List[Dict[str, Any]],
    metadata: Optional[Dict[str, str]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
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
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    application_fee_percent: Optional[float] = None,
    on_behalf_of: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "line_items": line_items,
        "metadata": metadata,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "currency": currency,
        "custom_fields": custom_fields,
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
        "application_fee_amount": application_fee_amount,
        "application_fee_percent": application_fee_percent,
        "on_behalf_of": on_behalf_of,
    }
    status, payload = stripe_request(
        "POST", "/v1/payment_links", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_payment_link(
    *,
    payment_link_id: str,
    active: Optional[bool] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
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
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "active": active,
        "line_items": line_items,
        "metadata": metadata,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "custom_fields": custom_fields,
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
    status, payload = stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def retrieve_payment_link(*, payment_link_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_payment_links(
    *,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"active": active, "limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    status, payload = stripe_request("GET", "/v1/payment_links", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)


def retrieve_payment_link_line_items(
    *,
    payment_link_id: str,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    status, payload = stripe_request(
        "GET", f"/v1/payment_links/{payment_link_id}/line_items", params=params, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)
