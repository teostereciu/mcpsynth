from typing import Any, Dict, Optional

from .http import stripe_request


def promotion_codes_create(
    *,
    coupon: str,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    max_redemptions: Optional[int] = None,
    expires_at: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "coupon": coupon,
        "code": code,
        "active": active,
        "max_redemptions": max_redemptions,
        "expires_at": expires_at,
        "metadata": metadata,
        "restrictions": restrictions,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        "/v1/promotion_codes",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def promotion_codes_retrieve(*, promotion_code_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def promotion_codes_update(
    *,
    promotion_code_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"active": active, "metadata": metadata}
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def promotion_codes_list(
    *,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    result, err = stripe_request("GET", "/v1/promotion_codes", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
