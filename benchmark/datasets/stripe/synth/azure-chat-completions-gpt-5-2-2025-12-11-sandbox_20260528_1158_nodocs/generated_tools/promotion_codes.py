from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def promotion_codes_create(
    *,
    coupon: str,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    max_redemptions: Optional[int] = None,
    expires_at: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "coupon": coupon,
        "code": code,
        "active": active,
        "max_redemptions": max_redemptions,
        "expires_at": expires_at,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/promotion_codes", params=params, stripe_account=stripe_account)


def promotion_codes_retrieve(*, promotion_code_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)


def promotion_codes_update(
    *,
    promotion_code_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "metadata": metadata}
    return stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", params=params, stripe_account=stripe_account)


def promotion_codes_list(
    *,
    coupon: Optional[str] = None,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "coupon": coupon,
        "code": code,
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/promotion_codes", params=params, stripe_account=stripe_account)
