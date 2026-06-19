from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/promotion_codes
# GET /v1/promotion_codes/{promotion_code}
# POST /v1/promotion_codes/{promotion_code}
# GET /v1/promotion_codes


def create_promotion_code(
    promotion: Dict[str, Any],
    *,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "promotion": promotion,
        "code": code,
        "active": active,
        "customer": customer,
        "expires_at": expires_at,
        "max_redemptions": max_redemptions,
        "restrictions": restrictions,
        "metadata": metadata,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(promotion_code_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)


def update_promotion_code(
    promotion_code_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
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
    params: Dict[str, Any] = {
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/promotion_codes", params=params, stripe_account=stripe_account)
