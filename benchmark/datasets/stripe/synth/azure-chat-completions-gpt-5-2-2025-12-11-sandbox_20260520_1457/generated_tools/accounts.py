from typing import Any, Dict, Optional

from .http_client import ok_or_error, stripe_request


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
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    external_account: Optional[str] = None,
    settings: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Any:
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
        "account_token": account_token,
    }
    status, payload = stripe_request("POST", "/v1/accounts", params=params, idempotency_key=idempotency_key)
    return ok_or_error(status, payload)


def retrieve_account(*, account_id: str, stripe_account: Optional[str] = None) -> Any:
    status, payload = stripe_request("GET", f"/v1/accounts/{account_id}", stripe_account=stripe_account)
    return ok_or_error(status, payload)


def update_account(
    *,
    account_id: str,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    settings: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "controller": controller,
        "tos_acceptance": tos_acceptance,
        "metadata": metadata,
        "business_profile": business_profile,
        "default_currency": default_currency,
        "settings": settings,
    }
    status, payload = stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return ok_or_error(status, payload)


def list_accounts(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Any:
    params = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    status, payload = stripe_request("GET", "/v1/accounts", params=params, stripe_account=stripe_account)
    return ok_or_error(status, payload)
