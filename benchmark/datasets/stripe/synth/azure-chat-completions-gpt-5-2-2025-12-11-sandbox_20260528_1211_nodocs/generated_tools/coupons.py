from typing import Any, Dict, Optional

from .http import stripe_request


def create_coupon(
    *,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: str,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"duration": duration}
    if percent_off is not None:
        data["percent_off"] = percent_off
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency is not None:
        data["currency"] = currency
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if redeem_by is not None:
        data["redeem_by"] = redeem_by
    if name is not None:
        data["name"] = name
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request(
        "POST",
        "/v1/coupons",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_coupon(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_coupon(
    coupon_id: str,
    *,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/coupons/{coupon_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def delete_coupon(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)
    return res if err is None else err


def list_coupons(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/coupons", query=query, stripe_account=stripe_account)
    return res if err is None else err
