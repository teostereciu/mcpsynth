from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_promotion_code(
    promotion: Dict[str, Any],
    *,
    code: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"promotion": promotion}
    if code is not None:
        params["code"] = code
    if metadata is not None:
        params["metadata"] = metadata
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

    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(promotion_code_id: str, *, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", params={}, account=account)


def update_promotion_code(
    promotion_code_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = active
    if restrictions is not None:
        params["restrictions"] = restrictions

    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def list_promotion_codes(
    *,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if active is not None:
        params["active"] = active
    if code is not None:
        params["code"] = code
    if coupon is not None:
        params["coupon"] = coupon
    if customer is not None:
        params["customer"] = customer
    if created is not None:
        params["created"] = created
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/promotion_codes", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/promotion_codes", params=params, account=account)
