from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def promotion_codes_create(
    promotion: Dict[str, Any],
    *,
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "promotion": promotion,
        "code": code,
        "active": active,
        "customer": customer,
        "customer_account": customer_account,
        "expires_at": expires_at,
        "max_redemptions": max_redemptions,
        "restrictions": restrictions,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/promotion_codes", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def promotion_codes_retrieve(promotion_code_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", None, stripe_account=stripe_account)


def promotion_codes_update(
    promotion_code_id: str,
    *,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "restrictions": restrictions, "metadata": metadata}
    return stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", params, stripe_account=stripe_account)


def promotion_codes_list(
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
    params: Dict[str, Any] = {
        "active": active,
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/promotion_codes", params, stripe_account=stripe_account)


def promotion_codes_list_all(
    *,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "code": code, "coupon": coupon, "customer": customer}
    return stripe_list_all("/v1/promotion_codes", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
