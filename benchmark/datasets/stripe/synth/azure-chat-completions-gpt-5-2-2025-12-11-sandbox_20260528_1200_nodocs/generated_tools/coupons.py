from typing import Any, Dict, Optional

from .http import stripe_delete, stripe_get, stripe_post


def coupons_create(
    *,
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    id: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "id": id,
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "duration_in_months": duration_in_months,
        "max_redemptions": max_redemptions,
        "redeem_by": redeem_by,
        "name": name,
        "metadata": metadata,
    }
    res, err = stripe_post(
        "/v1/coupons",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def coupons_retrieve(*, coupon_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return err or res


def coupons_update(
    *,
    coupon_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {"name": name, "metadata": metadata}
    res, err = stripe_post(f"/v1/coupons/{coupon_id}", data=data, stripe_account=stripe_account)
    return err or res


def coupons_delete(*, coupon_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_delete(f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return err or res


def coupons_list(
    *,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    res, err = stripe_get("/v1/coupons", params=params, stripe_account=stripe_account)
    return err or res
