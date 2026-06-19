from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def coupons_create(
    *,
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    coupon_id: Optional[str] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    applies_to: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"duration": duration}
    if percent_off is not None:
        data["percent_off"] = percent_off
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency is not None:
        data["currency"] = currency
    if name is not None:
        data["name"] = name
    if coupon_id is not None:
        data["id"] = coupon_id
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if redeem_by is not None:
        data["redeem_by"] = redeem_by
    if applies_to is not None:
        data["applies_to"] = applies_to
    if currency_options is not None:
        data["currency_options"] = currency_options
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/coupons",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def coupons_retrieve(*, coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)


def coupons_update(
    *,
    coupon_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if metadata is not None:
        data["metadata"] = metadata
    if currency_options is not None:
        data["currency_options"] = currency_options
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/coupons/{coupon_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def coupons_delete(*, coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}", stripe_account=stripe_account)


def coupons_list(
    *,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/coupons", params=query, stripe_account=stripe_account)
