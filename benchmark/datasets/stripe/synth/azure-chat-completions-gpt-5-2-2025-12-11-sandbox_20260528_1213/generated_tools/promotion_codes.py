from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_promotion_code(
    promotion: Dict[str, Any],
    *,
    code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes"""
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

    data, err = stripe_request(
        "POST",
        "/v1/promotion_codes",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def update_promotion_code(
    promotion_code_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes/{id}"""
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = active
    if restrictions is not None:
        params["restrictions"] = restrictions

    data, err = stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data if err is None else err


def retrieve_promotion_code(
    promotion_code_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes/{id}"""
    data, err = stripe_request(
        "GET",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=None,
        stripe_account=stripe_account,
    )
    return data if err is None else err
