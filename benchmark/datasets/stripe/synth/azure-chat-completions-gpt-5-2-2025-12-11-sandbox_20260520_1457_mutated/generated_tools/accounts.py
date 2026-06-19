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
    metadata: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    default_currency: Optional[str] = None,
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
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
        "external_account": external_account,
        "default_currency": default_currency,
        "settings": settings,
    }
    _, data = stripe_request(
        "POST",
        "/v1/accounts",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_account(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/accounts/{account_id}",
        stripe_account=stripe_account,
    )
    return data


def update_account(
    account_id: str,
    *,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "controller": controller,
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
        "settings": settings,
    }
    _, data = stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


def delete_account(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "DELETE",
        f"/v1/accounts/{account_id}",
        stripe_account=stripe_account,
    )
    return data


def list_accounts(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    _, data = stripe_request(
        "GET",
        "/v1/accounts",
        params=params,
        stripe_account=stripe_account,
    )
    return data
