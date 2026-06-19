from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_coupon(
    *,
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
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
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/coupons",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_coupon(
    coupon_id: str,
    *,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"name": name, "metadata": metadata}
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/coupons/{coupon_id}",
        None,
        stripe_account=stripe_account,
    )
