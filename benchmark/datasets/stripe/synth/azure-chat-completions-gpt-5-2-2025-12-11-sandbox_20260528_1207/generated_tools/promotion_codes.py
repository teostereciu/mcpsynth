from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_promotion_code(
    *,
    promotion: Dict[str, Any],
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"promotion": promotion}
    if code is not None:
        params["code"] = code
    if active is not None:
        params["active"] = active
    if customer is not None:
        params["customer"] = customer
    if customer_account is not None:
        params["customer_account"] = customer_account
    if expires_at is not None:
        params["expires_at"] = expires_at
    if max_redemptions is not None:
        params["max_redemptions"] = max_redemptions
    if restrictions is not None:
        params["restrictions"] = restrictions
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_promotion_code(
    promotion_code_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = active
    if restrictions is not None:
        params["restrictions"] = restrictions
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(promotion_code_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)


def list_promotion_codes(
    *,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if code is not None:
        params["code"] = code
    if coupon is not None:
        params["coupon"] = coupon
    if customer is not None:
        params["customer"] = customer
    if active is not None:
        params["active"] = active
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/promotion_codes", params=params, stripe_account=stripe_account)
