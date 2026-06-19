from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


def create_price(
    *,
    currency: str,
    unit_amount: Optional[int] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    unit_amount_decimal: Optional[str] = None,
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "billing_scheme": billing_scheme,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
        "transform_quantity": transform_quantity,
        "unit_amount_decimal": unit_amount_decimal,
        "custom_unit_amount": custom_unit_amount,
        "currency_options": currency_options,
    }
    status, payload = stripe_request(
        "POST", "/v1/prices", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def update_price(
    *,
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "currency_options": currency_options,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
    }
    status, payload = stripe_request(
        "POST", f"/v1/prices/{price_id}", params=params, idempotency_key=idempotency_key, stripe_account=stripe_account
    )
    return ok_or_error(status, payload)


def retrieve_price(*, price_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def list_prices(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    type: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "product": product,
        "active": active,
        "currency": currency,
        "type": type,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    status, payload = stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
