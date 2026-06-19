from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def payment_links_create(
    *,
    line_items: list,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    customer_creation: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "line_items": line_items,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "billing_address_collection": billing_address_collection,
        "customer_creation": customer_creation,
        "metadata": metadata,
        "restrictions": restrictions,
        "subscription_data": subscription_data,
        "payment_intent_data": payment_intent_data,
    }
    res, err = stripe_post(
        "/v1/payment_links",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def payment_links_retrieve(*, payment_link_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)
    return err or res


def payment_links_update(
    *,
    payment_link_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {"active": active, "metadata": metadata}
    res, err = stripe_post(f"/v1/payment_links/{payment_link_id}", data=data, stripe_account=stripe_account)
    return err or res


def payment_links_list(
    *,
    active: Optional[bool] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/payment_links", params=params, stripe_account=stripe_account)
    return err or res
