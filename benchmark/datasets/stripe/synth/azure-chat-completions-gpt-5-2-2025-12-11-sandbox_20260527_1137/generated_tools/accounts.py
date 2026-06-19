from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


def create_account(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts"""
    return stripe_request(
        "POST",
        "/v1/accounts",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_account(
    account_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/accounts/{account}"""
    return stripe_request(
        "GET",
        f"/v1/accounts/{account_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def update_account(
    account_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts/{account}"""
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_account(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/accounts/{account}"""
    return stripe_request(
        "DELETE",
        f"/v1/accounts/{account_id}",
        {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_accounts(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/accounts"""
    return stripe_request("GET", "/v1/accounts", params or {}, stripe_account=stripe_account)
