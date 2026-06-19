from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_coupon(
    duration: str,
    *,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    coupon_id: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "name": name,
        "metadata": metadata,
        "duration_in_months": duration_in_months,
        "max_redemptions": max_redemptions,
        "redeem_by": redeem_by,
        "id": coupon_id,
    }
    _, data = stripe_request(
        "POST",
        "/v1/coupons",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/coupons/{coupon_id}",
        stripe_account=stripe_account,
    )
    return data


def update_coupon(
    coupon_id: str,
    *,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"name": name, "metadata": metadata}
    _, data = stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def delete_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "DELETE",
        f"/v1/coupons/{coupon_id}",
        stripe_account=stripe_account,
    )
    return data


def list_coupons(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    _, data = stripe_request(
        "GET",
        "/v1/coupons",
        params=params,
        stripe_account=stripe_account,
    )
    return data
