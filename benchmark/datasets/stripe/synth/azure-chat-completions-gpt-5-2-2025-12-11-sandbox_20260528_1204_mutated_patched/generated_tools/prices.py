from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_price(
    currency: str,
    *,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    transform_quantity: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices

    Doc: docs/prices.md (Create a price)
    """
    params: Dict[str, Any] = {
        "currency": currency,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "product": product,
        "product_data": product_data,
        "recurring": recurring,
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "billing_scheme": billing_scheme,
        "custom_unit_amount": custom_unit_amount,
        "lookup_key": lookup_key,
        "currency_options": currency_options,
        "tiers": tiers,
        "tiers_mode": tiers_mode,
        "transfer_lookup_key": transfer_lookup_key,
        "transform_quantity": transform_quantity,
    }
    return stripe_request(
        "POST",
        "/v1/prices",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_price(
    price_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices/{price_id}

    Doc: docs/prices.md (Retrieve a price)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/prices/{price_id}",
        params,
        stripe_account=stripe_account,
    )


def update_price(
    price_id: str,
    *,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    currency_options: Optional[Dict[str, Any]] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices/{price_id}

    Doc: docs/prices.md (Update a price)
    """
    params: Dict[str, Any] = {
        "active": active,
        "nickname": nickname,
        "metadata": metadata,
        "tax_behavior": tax_behavior,
        "currency_options": currency_options,
        "lookup_key": lookup_key,
        "transfer_lookup_key": transfer_lookup_key,
    }
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params,
        stripe_account=stripe_account,
    )


def list_prices(
    *,
    active: Optional[bool] = None,
    currency: Optional[str] = None,
    product: Optional[str] = None,
    type: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices

    Doc: docs/prices.md (List all prices)
    """
    params: Dict[str, Any] = {
        "active": active,
        "currency": currency,
        "product": product,
        "type": type,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/prices",
        params,
        stripe_account=stripe_account,
    )
