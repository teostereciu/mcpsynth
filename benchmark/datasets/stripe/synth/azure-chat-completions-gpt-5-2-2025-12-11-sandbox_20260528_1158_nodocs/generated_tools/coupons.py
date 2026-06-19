from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def coupons_create(
    *,
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration_in_months: Optional[int] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "duration_in_months": duration_in_months,
        "name": name,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/coupons", params=params, stripe_account=stripe_account)


def coupons_retrieve(*, coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)


def coupons_update(
    *,
    coupon_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"name": name, "metadata": metadata}
    return stripe_request("POST", f"/v1/coupons/{coupon_id}", params=params, stripe_account=stripe_account)


def coupons_delete(*, coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)


def coupons_list(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", "/v1/coupons", params=params, stripe_account=stripe_account)
