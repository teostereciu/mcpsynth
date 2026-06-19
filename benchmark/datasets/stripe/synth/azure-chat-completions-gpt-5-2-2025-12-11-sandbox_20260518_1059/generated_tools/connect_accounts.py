from typing import Any, Dict, Optional

from .http_client import stripe_request


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
    metadata: Optional[Dict[str, str]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
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
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/accounts",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_account(
    account_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    email: Optional[str] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "metadata": metadata,
        "email": email,
        "company": company,
        "individual": individual,
        "business_profile": business_profile,
        "settings": settings,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params,
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
        None,
        stripe_account=stripe_account,
    )
