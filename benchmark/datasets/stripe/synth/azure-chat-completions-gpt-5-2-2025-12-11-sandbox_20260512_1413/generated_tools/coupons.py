from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def coupons_create(
    *,
    duration: str = "once",
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    applies_to: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "name": name,
        "metadata": metadata,
        "duration_in_months": duration_in_months,
        "max_redemptions": max_redemptions,
        "redeem_by": redeem_by,
        "applies_to": applies_to,
    }
    return stripe_request("POST", "/v1/coupons", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def coupons_retrieve(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/coupons/{coupon_id}", None, stripe_account=stripe_account)


def coupons_update(
    coupon_id: str,
    *,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"name": name, "metadata": metadata, "currency_options": currency_options}
    return stripe_request("POST", f"/v1/coupons/{coupon_id}", params, stripe_account=stripe_account)


def coupons_delete(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}", None, stripe_account=stripe_account)


def coupons_list(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", "/v1/coupons", params, stripe_account=stripe_account)


def coupons_list_all(
    *,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    return stripe_list_all("/v1/coupons", {}, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
