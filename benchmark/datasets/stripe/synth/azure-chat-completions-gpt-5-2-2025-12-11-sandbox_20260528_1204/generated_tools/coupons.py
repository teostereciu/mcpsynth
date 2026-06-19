from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/coupons
# GET /v1/coupons/{coupon}
# POST /v1/coupons/{coupon}
# DELETE /v1/coupons/{coupon}
# GET /v1/coupons


def create_coupon(
    *,
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "name": name,
        "metadata": metadata,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/coupons",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_coupon(coupon_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)


def update_coupon(
    coupon_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata, "name": name}
    params.update(kwargs)
    return stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "DELETE",
        f"/v1/coupons/{coupon_id}",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_coupons(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", "/v1/coupons", params=params, stripe_account=stripe_account)
