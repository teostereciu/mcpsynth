from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


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
    applies_to: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    coupon_id: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
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
        "applies_to": applies_to,
        "currency_options": currency_options,
        "id": coupon_id,
    }
    status, payload = stripe_request(
        "POST", "/v1/coupons", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_coupon(
    *,
    coupon_id: str,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"metadata": metadata, "name": name, "currency_options": currency_options}
    status, payload = stripe_request(
        "POST", f"/v1/coupons/{coupon_id}", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_coupon(*, coupon_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_coupons(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    status, payload = stripe_request("GET", "/v1/coupons", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)


def delete_coupon(
    *,
    coupon_id: str,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    status, payload = stripe_request(
        "DELETE", f"/v1/coupons/{coupon_id}", params={}, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)
