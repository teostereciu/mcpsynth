from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/accounts
# GET /v1/accounts/{account}
# POST /v1/accounts/{account}
# DELETE /v1/accounts/{account}
# GET /v1/accounts
# GET /v1/account (retrieve current account)


def create_account(
    *,
    type: Optional[str] = None,
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    controller: Optional[Dict[str, Any]] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "type": type,
        "country": country,
        "email": email,
        "business_type": business_type,
        "controller": controller,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/accounts",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_account(account_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account_id}", stripe_account=stripe_account)


def retrieve_current_account(*, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", "/v1/account", stripe_account=stripe_account)


def update_account(
    account_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def delete_account(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "DELETE",
        f"/v1/accounts/{account_id}",
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_accounts(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", "/v1/accounts", params=params, stripe_account=stripe_account)
