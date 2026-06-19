from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_promotion_code(
    promotion: Dict[str, Any],
    *,
    code: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes"""
    body: Dict[str, Any] = {"promotion": promotion}
    if code is not None:
        body["code"] = code
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/promotion_codes",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_promotion_code(
    promotion_code_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes/{promotion_code}"""
    return stripe_request(
        "POST",
        f"/v1/promotion_codes/{promotion_code_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_promotion_code(
    promotion_code_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes/{promotion_code}"""
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", {}, stripe_account=stripe_account)


def list_promotion_codes(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/promotion_codes"""
    return stripe_request("GET", "/v1/promotion_codes", params or {}, stripe_account=stripe_account)
