from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


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
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if type is not None:
        params["type"] = type
    if country is not None:
        params["country"] = country
    if email is not None:
        params["email"] = email
    if business_type is not None:
        params["business_type"] = business_type
    if capabilities is not None:
        params["capabilities"] = capabilities
    if company is not None:
        params["company"] = company
    if individual is not None:
        params["individual"] = individual
    if controller is not None:
        params["controller"] = controller
    if tos_acceptance is not None:
        params["tos_acceptance"] = tos_acceptance
    if metadata is not None:
        params["metadata"] = metadata
    if external_account is not None:
        params["external_account"] = external_account
    if default_currency is not None:
        params["default_currency"] = default_currency
    if business_profile is not None:
        params["business_profile"] = business_profile
    if settings is not None:
        params["settings"] = settings

    return stripe_request_with_retries(
        "POST",
        "/v1/accounts",
        params=params,
        idempotency_key=idempotency_key,
    )


def retrieve_account(account_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/accounts/{account_id}",
        stripe_account=stripe_account,
    )


def update_account(
    account_id: str,
    *,
    business_type: Optional[str] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if business_type is not None:
        params["business_type"] = business_type
    if company is not None:
        params["company"] = company
    if individual is not None:
        params["individual"] = individual
    if metadata is not None:
        params["metadata"] = metadata
    if tos_acceptance is not None:
        params["tos_acceptance"] = tos_acceptance
    if business_profile is not None:
        params["business_profile"] = business_profile
    if settings is not None:
        params["settings"] = settings

    return stripe_request_with_retries(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_accounts(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    return stripe_request_with_retries(
        "GET",
        "/v1/accounts",
        params=params,
    )
