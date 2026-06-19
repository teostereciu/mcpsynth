from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def promotion_codes_create(
    *,
    coupon: str,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    max_redemptions: Optional[int] = None,
    expires_at: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    customer: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "coupon": coupon,
        "code": code,
        "active": active,
        "max_redemptions": max_redemptions,
        "expires_at": expires_at,
        "restrictions": restrictions,
        "metadata": metadata,
        "customer": customer,
    }
    res, err = stripe_post(
        "/v1/promotion_codes",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def promotion_codes_retrieve(*, promotion_code_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)
    return err or res


def promotion_codes_update(
    *,
    promotion_code_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {"active": active, "metadata": metadata}
    res, err = stripe_post(f"/v1/promotion_codes/{promotion_code_id}", data=data, stripe_account=stripe_account)
    return err or res


def promotion_codes_list(
    *,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {
        "active": active,
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_get("/v1/promotion_codes", params=params, stripe_account=stripe_account)
    return err or res
