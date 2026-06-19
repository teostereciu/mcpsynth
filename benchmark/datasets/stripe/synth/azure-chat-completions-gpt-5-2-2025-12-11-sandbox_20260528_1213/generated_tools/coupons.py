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
    applies_to: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    duration_in_months: Optional[int] = None,
    coupon_id: Optional[str] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons"""
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
    if applies_to is not None:
        params["applies_to"] = applies_to
    if currency_options is not None:
        params["currency_options"] = currency_options
    if duration_in_months is not None:
        params["duration_in_months"] = duration_in_months
    if coupon_id is not None:
        params["id"] = coupon_id
    if max_redemptions is not None:
        params["max_redemptions"] = max_redemptions
    if redeem_by is not None:
        params["redeem_by"] = redeem_by

    if percent_off is None and amount_off is None:
        return {"error": "invalid_request", "message": "Must provide either percent_off or amount_off"}
    if amount_off is not None and currency is None and currency_options is None:
        return {"error": "invalid_request", "message": "currency is required when amount_off is provided (unless currency_options is used)"}

    data, err = stripe_request(
        "POST",
        "/v1/coupons",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_coupon(
    coupon_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    name: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons/{id}"""
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if name is not None:
        params["name"] = name
    if currency_options is not None:
        params["currency_options"] = currency_options

    data, err = stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/coupons/{id}"""
    data, err = stripe_request(
        "GET",
        f"/v1/coupons/{coupon_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
