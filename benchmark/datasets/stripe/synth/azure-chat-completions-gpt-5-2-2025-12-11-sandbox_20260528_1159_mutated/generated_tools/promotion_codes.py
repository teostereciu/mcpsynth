from typing import Any, Dict, Optional

from .http import stripe_request


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
    params: Dict[str, Any] = {
        "promotion": promotion,
        "code": code,
        "metadata": metadata,
        "active": active,
        "customer": customer,
        "customer_account": customer_account,
        "expires_at": expires_at,
        "max_redemptions": max_redemptions,
        "restrictions": restrictions,
    }
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
    metadata: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata, "active": active, "restrictions": restrictions}
    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(
    promotion_code_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/promotion_codes/{promotion_code_id}",
        params=None,
        stripe_account=stripe_account,
    )
