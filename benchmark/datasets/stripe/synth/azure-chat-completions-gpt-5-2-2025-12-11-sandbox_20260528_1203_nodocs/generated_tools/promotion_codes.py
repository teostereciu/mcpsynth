from typing import Any, Dict, Optional

from .http import stripe_request


def promotion_codes_create(
    coupon: str,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "coupon": coupon,
        "code": code,
        "active": active,
        "customer": customer,
        "expires_at": expires_at,
        "max_redemptions": max_redemptions,
        "metadata": metadata,
        "restrictions": restrictions,
    }
    data, err = stripe_request(
        "POST",
        "/v1/promotion_codes",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def promotion_codes_retrieve(promotion_code_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def promotion_codes_update(
    promotion_code_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"active": active, "metadata": metadata, "restrictions": restrictions}
    data, err = stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def promotion_codes_list(
    limit: int = 10,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "limit": limit,
        "active": active,
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "created": created,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    data, err = stripe_request("GET", "/v1/promotion_codes", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
