from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def customers_create(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/customers", params=params, stripe_account=stripe_account)


def customers_retrieve(*, customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/customers/{customer_id}", stripe_account=stripe_account)


def customers_update(
    *,
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
    }
    return stripe_request("POST", f"/v1/customers/{customer_id}", params=params, stripe_account=stripe_account)


def customers_delete(*, customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}", stripe_account=stripe_account)


def customers_list(
    *,
    email: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/customers", params=params, stripe_account=stripe_account)
