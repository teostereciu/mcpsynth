from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_price(
    currency: str,
    *,
    unit_amount: Optional[int] = None,
    product: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices"""
    body: Dict[str, Any] = {"currency": currency}
    if unit_amount is not None:
        body["unit_amount"] = unit_amount
    if product is not None:
        body["product"] = product
    if params:
        body.update(params)
    return stripe_request(
        "POST",
        "/v1/prices",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_price(
    price_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices/{id}"""
    return stripe_request("GET", f"/v1/prices/{price_id}", None, stripe_account=stripe_account)


def update_price(
    price_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices/{id}"""
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_prices(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices"""
    return stripe_request("GET", "/v1/prices", params, stripe_account=stripe_account)
