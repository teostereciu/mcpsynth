from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def promotion_codes_create(
    *,
    promotion: Dict[str, Any],
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"promotion": promotion}
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
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def promotion_codes_retrieve(
    *,
    promotion_code_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/promotion_codes/{promotion_code_id}",
        stripe_account=stripe_account,
    )


def promotion_codes_update(
    *,
    promotion_code_id: str,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if restrictions is not None:
        data["restrictions"] = restrictions
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def promotion_codes_list(
    *,
    limit: Optional[int] = 10,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if active is not None:
        query["active"] = active
    if code is not None:
        query["code"] = code
    if coupon is not None:
        query["coupon"] = coupon
    if customer is not None:
        query["customer"] = customer
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/promotion_codes", params=query, stripe_account=stripe_account)
