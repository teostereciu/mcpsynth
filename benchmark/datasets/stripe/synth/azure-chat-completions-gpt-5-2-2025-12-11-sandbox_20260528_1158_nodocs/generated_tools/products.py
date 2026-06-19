from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def products_create(
    *,
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/products", params=params, stripe_account=stripe_account)


def products_retrieve(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/products/{product_id}", stripe_account=stripe_account)


def products_update(
    *,
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "name": name,
        "description": description,
        "active": active,
        "metadata": metadata,
    }
    return stripe_request("POST", f"/v1/products/{product_id}", params=params, stripe_account=stripe_account)


def products_delete(*, product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/products/{product_id}", stripe_account=stripe_account)


def products_list(
    *,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/products", params=params, stripe_account=stripe_account)
