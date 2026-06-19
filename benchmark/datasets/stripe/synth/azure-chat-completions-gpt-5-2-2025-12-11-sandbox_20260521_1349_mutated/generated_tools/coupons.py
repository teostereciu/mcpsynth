from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_coupon(
    duration: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons"""
    body = {"duration": duration}
    body.update(params)
    return stripe_request(
        "POST",
        "/v1/coupons",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/coupons/{id}"""
    return stripe_request("GET", f"/v1/coupons/{coupon_id}", None, stripe_account=stripe_account)


def update_coupon(
    coupon_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons/{id}"""
    return stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/coupons/{id}"""
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}", None, stripe_account=stripe_account)


def list_coupons(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/coupons"""
    return stripe_request("GET", "/v1/coupons", params, stripe_account=stripe_account)
