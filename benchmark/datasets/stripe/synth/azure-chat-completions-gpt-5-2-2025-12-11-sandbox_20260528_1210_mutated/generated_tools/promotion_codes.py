from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


def create_promotion_code(
    promotion: Dict[str, Any],
    *,
    code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"promotion": promotion}
    if code is not None:
        params["code"] = code
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = str(active).lower()
    if customer is not None:
        params["customer"] = customer
    if expires_at is not None:
        params["expires_at"] = expires_at
    if max_redemptions is not None:
        params["max_redemptions"] = max_redemptions
    if restrictions is not None:
        params["restrictions"] = restrictions

    return stripe_request_with_retries(
        "POST",
        "/v1/promotion_codes",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(promotion_code_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/promotion_codes/{promotion_code_id}",
        stripe_account=stripe_account,
    )


def update_promotion_code(
    promotion_code_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = str(active).lower()
    if restrictions is not None:
        params["restrictions"] = restrictions

    return stripe_request_with_retries(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_promotion_codes(
    *,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if code is not None:
        params["code"] = code
    if coupon is not None:
        params["coupon"] = coupon
    if customer is not None:
        params["customer"] = customer
    if active is not None:
        params["active"] = str(active).lower()
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/promotion_codes",
        params=params,
        stripe_account=stripe_account,
    )
