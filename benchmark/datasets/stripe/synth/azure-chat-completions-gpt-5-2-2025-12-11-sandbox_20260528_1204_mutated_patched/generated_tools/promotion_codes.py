from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes

    Doc: docs/promotion_codes.md (Create a promotion code)
    """
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
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(
    promotion_code_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes/{promotion_code_id}

    Doc: docs/promotion_codes.md (Retrieve a promotion code)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/promotion_codes/{promotion_code_id}",
        params,
        stripe_account=stripe_account,
    )


def update_promotion_code(
    promotion_code_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes/{promotion_code_id}

    Doc: docs/promotion_codes.md (Update a promotion code)
    """
    params: Dict[str, Any] = {
        "metadata": metadata,
        "active": active,
        "restrictions": restrictions,
    }
    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params,
        stripe_account=stripe_account,
    )


def list_promotion_codes(
    *,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes

    Doc: docs/promotion_codes.md (List all promotion codes)
    """
    params: Dict[str, Any] = {
        "active": active,
        "code": code,
        "coupon": coupon,
        "customer": customer,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/promotion_codes",
        params,
        stripe_account=stripe_account,
    )
