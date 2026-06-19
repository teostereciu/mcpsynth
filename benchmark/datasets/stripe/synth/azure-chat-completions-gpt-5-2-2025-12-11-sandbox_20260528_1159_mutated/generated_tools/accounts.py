from typing import Any, Dict, Optional

from .http import stripe_request


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
    metadata: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    documents: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    groups: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
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
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
        "account_token": account_token,
        "business_profile": business_profile,
        "default_currency": default_currency,
        "documents": documents,
        "external_account": external_account,
        "groups": groups,
        "settings": settings,
    }
    return stripe_request(
        "POST",
        "/v1/accounts",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_account(
    account_id: str,
    *,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    email: Optional[str] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    documents: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    groups: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "email": email,
        "individual": individual,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
        "account_token": account_token,
        "business_profile": business_profile,
        "default_currency": default_currency,
        "documents": documents,
        "external_account": external_account,
        "groups": groups,
        "settings": settings,
    }
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_account(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/accounts/{account_id}",
        params=None,
        stripe_account=stripe_account,
    )
