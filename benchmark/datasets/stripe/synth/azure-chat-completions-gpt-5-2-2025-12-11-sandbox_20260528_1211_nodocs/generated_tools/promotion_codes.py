from typing import Any, Dict, Optional

from .http import stripe_request


def create_promotion_code(
    *,
    coupon: str,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"coupon": coupon}
    if code is not None:
        data["code"] = code
    if active is not None:
        data["active"] = active
    if customer is not None:
        data["customer"] = customer
    if expires_at is not None:
        data["expires_at"] = expires_at
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if restrictions is not None:
        data["restrictions"] = restrictions
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request(
        "POST",
        "/v1/promotion_codes",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_promotion_code(promotion_code_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_promotion_code(
    promotion_code_id: str,
    *,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if metadata is not None:
        data["metadata"] = metadata
    if restrictions is not None:
        data["restrictions"] = restrictions

    res, err = stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def list_promotion_codes(
    *,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if active is not None:
        query["active"] = active
    if code is not None:
        query["code"] = code
    if coupon is not None:
        query["coupon"] = coupon
    if customer is not None:
        query["customer"] = customer
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/promotion_codes", query=query, stripe_account=stripe_account)
    return res if err is None else err
