from typing import Any, Dict, Optional

from .http import stripe_request


def coupons_create(
    *,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: str,
    duration_in_months: Optional[int] = None,
    name: Optional[str] = None,
    id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    redeem_by: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "duration": duration,
        "duration_in_months": duration_in_months,
        "name": name,
        "id": id,
        "metadata": metadata,
        "redeem_by": redeem_by,
        "max_redemptions": max_redemptions,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        "/v1/coupons",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def coupons_retrieve(*, coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def coupons_update(
    *,
    coupon_id: str,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"metadata": metadata, "name": name}
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def coupons_delete(*, coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("DELETE", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def coupons_list(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    result, err = stripe_request("GET", "/v1/coupons", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
