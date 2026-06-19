from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_promotion_code(
    promotion: Dict[str, Any],
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes"""
    body: Dict[str, Any] = {"promotion": promotion}
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(
    promotion_code_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes/{id}"""
    return stripe_request(
        "GET",
        f"/v1/promotion_codes/{promotion_code_id}",
        None,
        stripe_account=stripe_account,
    )


def update_promotion_code(
    promotion_code_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes/{id}"""
    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_promotion_codes(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes"""
    return stripe_request("GET", "/v1/promotion_codes", params, stripe_account=stripe_account)
