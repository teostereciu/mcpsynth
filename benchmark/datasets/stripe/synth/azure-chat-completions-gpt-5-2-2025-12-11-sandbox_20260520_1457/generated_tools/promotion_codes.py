from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


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
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
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
    status, payload = stripe_request(
        "POST", "/v1/promotion_codes", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_promotion_code(
    *,
    promotion_code_id: str,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"metadata": metadata, "active": active, "restrictions": restrictions}
    status, payload = stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def retrieve_promotion_code(*, promotion_code_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_promotion_codes(
    *,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/promotion_codes", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
