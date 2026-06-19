from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


def create_coupon(
    *,
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    duration_in_months: Optional[int] = None,
    coupon_id: Optional[str] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    applies_to: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"duration": duration}
    if percent_off is not None:
        params["percent_off"] = percent_off
    if amount_off is not None:
        params["amount_off"] = amount_off
    if currency is not None:
        params["currency"] = currency
    if name is not None:
        params["name"] = name
    if metadata is not None:
        params["metadata"] = metadata
    if duration_in_months is not None:
        params["duration_in_months"] = duration_in_months
    if coupon_id is not None:
        params["id"] = coupon_id
    if max_redemptions is not None:
        params["max_redemptions"] = max_redemptions
    if redeem_by is not None:
        params["redeem_by"] = redeem_by
    if applies_to is not None:
        params["applies_to"] = applies_to
    if currency_options is not None:
        params["currency_options"] = currency_options

    return stripe_request_with_retries(
        "POST",
        "/v1/coupons",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_coupon(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/coupons/{coupon_id}",
        stripe_account=stripe_account,
    )


def update_coupon(
    coupon_id: str,
    *,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if metadata is not None:
        params["metadata"] = metadata
    if currency_options is not None:
        params["currency_options"] = currency_options

    return stripe_request_with_retries(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params=params,
        stripe_account=stripe_account,
    )


def delete_coupon(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "DELETE",
        f"/v1/coupons/{coupon_id}",
        stripe_account=stripe_account,
    )


def list_coupons(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/coupons",
        params=params,
        stripe_account=stripe_account,
    )
