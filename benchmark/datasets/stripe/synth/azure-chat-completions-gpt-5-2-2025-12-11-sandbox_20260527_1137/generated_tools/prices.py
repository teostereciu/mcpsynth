from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_price(
    currency: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices"""
    body = {"currency": currency}
    body.update(params or {})
    return stripe_request(
        "POST",
        "/v1/prices",
        body,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_price(
    price_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/prices/{price}"""
    return stripe_request(
        "POST",
        f"/v1/prices/{price_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_price(
    price_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices/{price}"""
    return stripe_request(
        "GET",
        f"/v1/prices/{price_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def list_prices(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices"""
    return stripe_request("GET", "/v1/prices", params or {}, stripe_account=stripe_account)


def search_prices(
    query: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/prices/search"""
    p = {"query": query}
    p.update(params or {})
    return stripe_request("GET", "/v1/prices/search", p, stripe_account=stripe_account)
