from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    **extra_params: Any,
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
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_promotion_code(
    promotion_code_id: str,
    *,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        {"active": active, "restrictions": restrictions, "metadata": metadata},
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
        None,
        stripe_account=stripe_account,
    )
