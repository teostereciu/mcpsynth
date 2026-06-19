from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def prices_create(
    *,
    unit_amount: int,
    currency: str,
    product: str,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "unit_amount": unit_amount,
        "currency": currency,
        "product": product,
        "recurring": recurring,
        "nickname": nickname,
        "active": active,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/prices", params=params, stripe_account=stripe_account)


def prices_retrieve(*, price_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/prices/{price_id}", stripe_account=stripe_account)


def prices_update(
    *,
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "nickname": nickname, "metadata": metadata}
    return stripe_request("POST", f"/v1/prices/{price_id}", params=params, stripe_account=stripe_account)


def prices_list(
    *,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "product": product,
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/prices", params=params, stripe_account=stripe_account)
