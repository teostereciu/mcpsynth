from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_account(
    *,
    params: Dict[str, Any],
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts"""
    return stripe_request("POST", "/v1/accounts", params, idempotency_key=idempotency_key)


def retrieve_account(
    account_id: str,
) -> Dict[str, Any]:
    """GET /v1/accounts/{id}"""
    return stripe_request("GET", f"/v1/accounts/{account_id}", None)


def update_account(
    account_id: str,
    *,
    params: Dict[str, Any],
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts/{id}"""
    return stripe_request("POST", f"/v1/accounts/{account_id}", params, idempotency_key=idempotency_key)


def delete_account(
    account_id: str,
) -> Dict[str, Any]:
    """DELETE /v1/accounts/{id}"""
    return stripe_request("DELETE", f"/v1/accounts/{account_id}", None)


def list_accounts(
    *,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """GET /v1/accounts"""
    return stripe_request("GET", "/v1/accounts", params)
