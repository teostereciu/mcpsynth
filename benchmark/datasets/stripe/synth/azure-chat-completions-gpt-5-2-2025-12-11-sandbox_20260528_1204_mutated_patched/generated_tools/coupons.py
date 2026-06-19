from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_coupon(
    duration: str,
    *,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    applies_to: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    duration_in_months: Optional[int] = None,
    coupon_id: Optional[str] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons

    Doc: docs/coupons.md (Create a coupon)
    """
    params: Dict[str, Any] = {
        "duration": duration,
        "percent_off": percent_off,
        "amount_off": amount_off,
        "currency": currency,
        "name": name,
        "metadata": metadata,
        "applies_to": applies_to,
        "currency_options": currency_options,
        "duration_in_months": duration_in_months,
        "id": coupon_id,
        "max_redemptions": max_redemptions,
        "redeem_by": redeem_by,
    }
    return stripe_request(
        "POST",
        "/v1/coupons",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_coupon(
    coupon_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/coupons/{coupon_id}

    Doc: docs/coupons.md (Retrieve a coupon)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/coupons/{coupon_id}",
        params,
        stripe_account=stripe_account,
    )


def update_coupon(
    coupon_id: str,
    *,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons/{coupon_id}

    Doc: docs/coupons.md (Update a coupon)
    """
    params: Dict[str, Any] = {
        "name": name,
        "metadata": metadata,
        "currency_options": currency_options,
    }
    return stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        params,
        stripe_account=stripe_account,
    )


def delete_coupon(
    coupon_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/coupons/{coupon_id}

    Doc: docs/coupons.md (Delete a coupon)
    """
    return stripe_request(
        "DELETE",
        f"/v1/coupons/{coupon_id}",
        None,
        stripe_account=stripe_account,
    )


def list_coupons(
    *,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/coupons

    Doc: docs/coupons.md (List all coupons)
    """
    params: Dict[str, Any] = {
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
    }
    return stripe_request(
        "GET",
        "/v1/coupons",
        params,
        stripe_account=stripe_account,
    )
