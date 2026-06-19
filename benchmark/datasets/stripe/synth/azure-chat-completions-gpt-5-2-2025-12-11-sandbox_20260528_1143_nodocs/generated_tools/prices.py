from typing import Any, Dict, Optional

from .http import stripe_request


def prices_create(
    *,
    currency: str,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "nickname": nickname,
        "active": active,
        "metadata": metadata,
    }
    res, err = stripe_request(
        "POST",
        "/v1/prices",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or res  # type: ignore[return-value]


def prices_retrieve(*, price_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def prices_update(
    *,
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"active": active, "nickname": nickname, "metadata": metadata}
    res, err = stripe_request("POST", f"/v1/prices/{price_id}", data=data, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def prices_list(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    type: Optional[str] = None,
    recurring_interval: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "product": product,
        "active": active,
        "currency": currency,
        "type": type,
        "recurring[interval]": recurring_interval,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]
