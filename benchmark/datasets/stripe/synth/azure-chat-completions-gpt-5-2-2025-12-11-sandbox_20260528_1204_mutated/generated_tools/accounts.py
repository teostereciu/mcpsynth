from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_account(
    *,
    type: Optional[str] = None,
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    documents: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    groups: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts

    Doc: docs/accounts.md (Create an account)
    """
    params: Dict[str, Any] = {
        "type": type,
        "country": country,
        "email": email,
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "controller": controller,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
        "account_token": account_token,
        "business_profile": business_profile,
        "default_currency": default_currency,
        "documents": documents,
        "external_account": external_account,
        "groups": groups,
        "settings": settings,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/accounts",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_account(
    account_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/accounts/{account_id}

    Doc: docs/accounts.md (Retrieve an account)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/accounts/{account_id}",
        params,
        stripe_account=stripe_account,
    )


def update_account(
    account_id: str,
    *,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    documents: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    groups: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts/{account_id}

    Doc: docs/accounts.md (Update an account)
    """
    params: Dict[str, Any] = {
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "controller": controller,
        "email": email,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
        "business_profile": business_profile,
        "default_currency": default_currency,
        "documents": documents,
        "external_account": external_account,
        "groups": groups,
        "settings": settings,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params,
        stripe_account=stripe_account,
    )


def delete_account(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/accounts/{account_id}

    Doc: docs/accounts.md (Delete an account)
    """
    return stripe_request(
        "DELETE",
        f"/v1/accounts/{account_id}",
        None,
        stripe_account=stripe_account,
    )


def list_accounts(
    *,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/accounts

    Doc: docs/accounts.md (List all accounts)
    """
    params: Dict[str, Any] = {
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/accounts",
        params,
        stripe_account=stripe_account,
    )
