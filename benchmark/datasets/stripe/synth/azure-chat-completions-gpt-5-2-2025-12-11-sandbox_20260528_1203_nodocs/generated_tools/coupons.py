from typing import Any, Dict, Optional

from .http import stripe_request


def coupons_create(
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    applies_to: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "duration_in_months": duration_in_months,
        "max_redemptions": max_redemptions,
        "redeem_by": redeem_by,
        "name": name,
        "metadata": metadata,
        "applies_to": applies_to,
    }
    data, err = stripe_request(
        "POST",
        "/v1/coupons",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def coupons_retrieve(coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def coupons_update(
    coupon_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"name": name, "metadata": metadata}
    data, err = stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def coupons_delete(coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("DELETE", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def coupons_list(
    limit: int = 10,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"limit": limit, "created": created, "starting_after": starting_after, "ending_before": ending_before}
    data, err = stripe_request("GET", "/v1/coupons", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
