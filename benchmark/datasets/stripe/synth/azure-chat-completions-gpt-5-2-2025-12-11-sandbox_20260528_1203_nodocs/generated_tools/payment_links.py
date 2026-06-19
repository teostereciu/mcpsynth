from typing import Any, Dict, Optional

from .http import stripe_request


def payment_links_create(
    line_items: list,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    customer_creation: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    application_fee_amount: Optional[int] = None,
    on_behalf_of: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "line_items": line_items,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "customer_creation": customer_creation,
        "metadata": metadata,
        "restrictions": restrictions,
        "shipping_address_collection": shipping_address_collection,
        "subscription_data": subscription_data,
        "tax_id_collection": tax_id_collection,
        "transfer_data": transfer_data,
        "application_fee_amount": application_fee_amount,
        "on_behalf_of": on_behalf_of,
    }
    data, err = stripe_request(
        "POST",
        "/v1/payment_links",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def payment_links_retrieve(payment_link_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def payment_links_update(
    payment_link_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "active": active,
        "metadata": metadata,
        "after_completion": after_completion,
        "restrictions": restrictions,
    }
    data, err = stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def payment_links_list(
    limit: int = 10,
    active: Optional[bool] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"limit": limit, "active": active, "starting_after": starting_after, "ending_before": ending_before}
    data, err = stripe_request("GET", "/v1/payment_links", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
