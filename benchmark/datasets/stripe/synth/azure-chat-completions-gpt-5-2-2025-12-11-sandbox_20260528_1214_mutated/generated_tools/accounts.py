from typing import Any, Dict, Optional

from .http import stripe_request


# Docs: docs/accounts.md

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
    metadata: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    external_account: Optional[str] = None,
    settings: Optional[Dict[str, Any]] = None,
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
        "business_profile": business_profile,
        "default_currency": default_currency,
        "external_account": external_account,
        "settings": settings,
    }
    return stripe_request("POST", "/v1/accounts", params=params, idempotency_key=idempotency_key)


def retrieve_account(
    account_id: str,
    *,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account_id}", params={"expand": expand})


def update_account(
    account_id: str,
    *,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    external_account: Optional[str] = None,
    settings: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "email": email,
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
        "business_profile": business_profile,
        "default_currency": default_currency,
        "external_account": external_account,
        "settings": settings,
    }
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params,
        idempotency_key=idempotency_key,
    )


def delete_account(
    account_id: str,
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/accounts/{account_id}", params=None)


def list_accounts(
    *,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/accounts", params=params)
