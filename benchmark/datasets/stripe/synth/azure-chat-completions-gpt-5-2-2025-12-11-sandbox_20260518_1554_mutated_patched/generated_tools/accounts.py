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
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    external_account: Optional[str] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    default_currency: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "type": type,
        "country": country,
        "email": email,
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "controller": controller,
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
        "external_account": external_account,
        "business_profile": business_profile,
        "settings": settings,
        "account_token": account_token,
        "default_currency": default_currency,
    }
    return stripe_request(
        "POST",
        "/v1/accounts",
        params=params,
        idempotency_key=idempotency_key,
    )


def retrieve_account(
    account_id: str,
    *,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request("GET", f"/v1/accounts/{account_id}", params=params or None)


def update_account(
    account_id: str,
    *,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
        "business_profile": business_profile,
        "settings": settings,
    }
    return stripe_request("POST", f"/v1/accounts/{account_id}", params=params)


def delete_account(
    account_id: str,
) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/accounts/{account_id}")


def list_accounts(
    *,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/accounts", params=params)
